from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from .models import Match, Evidence, Investment, Payment, get_bitcoin_value, Plan
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404, HttpResponseRedirect
from datetime import timedelta
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
from .forms import UserForm,ProfileForm
from acc.models import Profile

# Create your views here.

class MatchView(LoginRequiredMixin, View):
    template_name='remiel_admin/match.html'

    def get(self, request, *args, **kwargs):
       active_receive_matches=Match.objects.filter(receiver=request.user).exclude(status='Completed')
       old_receive_matches=Match.objects.filter(receiver=request.user).filter(status='Completed')[:10]
       active_pay_matches=Match.objects.filter(payer=request.user).exclude(status='Completed')
       old_pay_matches=Match.objects.filter(payer=request.user).filter(status='Completed')[:10]
       active_inv=Investment.objects.exclude(status='Complete').filter(owner=request.user)


       context={'arm':active_receive_matches, 'orm':old_receive_matches,
                'apm':active_pay_matches,'opm':old_pay_matches,
                'ainv':active_inv
                }
       return render(request, self.template_name, context)

class UserInfoView(LoginRequiredMixin, DetailView):
    model=User
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context=super(UserInfoView, self).get_context_data(**kwargs)
        context['str_data']=render_to_string('remiel_admin/user_info.html', context)
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse({'html_data': context['str_data']})



class EvidenceList(LoginRequiredMixin, ListView):
    model=Evidence
    match_id=None
    context_object_name = 'evidences'

    def get(self, request, *args, **kwargs):
        self.match_id=request.GET.get('match_id')
        return super(EvidenceList,self).get(request,*args, **kwargs)

    def get_queryset(self):
        try:
            match=Match.objects.get(pk=self.match_id)

        except Match.DoesNotExist:
            return Http404()
        return Evidence.objects.filter(for_match=match)


    def render_to_response(self, context, **response_kwargs):
        html_data=render_to_string('remiel_admin/evidences.html', context)

        return JsonResponse({'html_data': html_data})

class MatchAction(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        action=request.GET.get('action')
        match_id=request.GET.get('match_id')
        try:
            match_obj=Match.objects.get(pk=match_id)
        except Match.DoesNotExist:
            return Http404()
        if action == 'Complete':
            match_obj.status='Completed'
            now=timezone.now()
            maturity_date = now+timedelta(days=7)
            inv = Investment(plan=match_obj.plan, status='Maturing',
                             owner=match_obj.payer,
                             maturity_date=maturity_date)
            match_obj.pay.status='Completed'
            match_obj.pay.save()
            related_inv=Payment.objects.exclude(status='Completed'
                                      ).filter(
                                           investment=match_obj.investment)
            if not related_inv.exists():
                match_obj.investment.status='Completed'
                match_obj.investment.save()

            inv.save()
            messages.success(request, "Payment Successful Approved")
        if action =='Extend':
            match_obj.expiry_date=match_obj.expiry_date+timedelta(hours=6)
            messages.success(request, "Payment deadline successfully extended")
            match_obj.grace=False



        match_obj.save()
        return JsonResponse({'status':True, 'redirect_url':'/office'})

class UploadEvidence(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        pk=kwargs.pop('pk')
        context=dict()
        try:
            context['match']=Match.objects.get(pk=pk)
        except:
            return Http404()
        return render(request, 'remiel_admin/fileupload.html', context)

    def post(self, request,*args,**kwargs):

        

        pk = kwargs.pop('pk')
        try:
            match=Match.objects.get(pk=pk)
        except Match.DoesNotExist:
            return Http404()
        evidence= Evidence(for_match=match, proof=request.FILES['file'])
        evidence.save()

        return JsonResponse({'status':True})

class RequestMatch(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        #waiting_match=Match.objects.filter(status='Waiting For Match')
        #if not waiting_match.exists():
        matches=Match.objects.filter(status='Waiting For Match').filter(payer=request.user)
        if matches.exists():
            messages.warning(request, 'Please complete your pending Matches')
            return HttpResponseRedirect('/office/')
        match=Match(payer=request.user)
        match.bitcoin_value=get_bitcoin_value()
        match.plan=Plan.objects.get(id=1)

        match.save()

        messages.success(request, 'Match Request Created')
        #else:
        #    messages.warning(request, 'Complete your Match request')
        return HttpResponseRedirect('/office/')

class ProfileUpdateView(LoginRequiredMixin, View):
    login_url = 'account/login'

    def get(self, request, *args, **kwargs):
        userform = UserForm(instance=self.request.user)
        profile = Profile.objects.get(user=self.request.user)
        profileform = ProfileForm(instance=profile)
        context = {'user': request.user, 'userform': userform, 'profileform': profileform}
        return render(self.request, 'remiel_admin/profile.html', context)

    def post(self, request, *args, **kwargs):
        try:
            userform = UserForm(data=self.request.POST, instance=self.request.user)
            profile = Profile.objects.get(user=self.request.user)
            profileform = ProfileForm(data=self.request.POST, instance=profile, files=request.FILES)
            userform.save()
            profileform.save()
            messages.success(request, 'Profile Updated Successfully')
        except:
            messages.warning(request, 'Invalid form input, please try again or send email to hello@dailynaija.com')

        return HttpResponseRedirect('/office/profile')


class MatchAdmin(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        if request.user.is_staff == True:
            inv=Investment(plan_id=1,owner=request.user,status='Complete')
            inv.save()
            inv.mature_inv()
            messages.success(request, 'Payment Request Created, Wait for the next match ')
        return HttpResponseRedirect('/office/')


def make_match():
    pays=Payment.objects.exclude(status='Completed').order_by('created_date')
    matches=Match.objects.filter(status='Waiting For Match').order_by('created_date')
    index=0
    for pay in pays:
        try:
            match=matches[index]
        except IndexError:
            break
        if pay.investment.owner != match.receiver:
            match.complete_match(pay.investment, pay)
        index+=1
        pay.match()






def chk_investment():
    invs=Investment.objects.filter(status='Maturing')
    for inv in invs:
        now=timezone.now()
        if inv.maturity_date < now:
            inv.mature_inv()











