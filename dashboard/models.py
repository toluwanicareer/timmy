from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
# Create your models here.

class Plan(models.Model):
    name=models.CharField(max_length=200)
    amount=models.IntegerField(default=250)
    day_length=models.IntegerField()





class Investment(models.Model):
    day_started=models.DateTimeField(auto_now_add=True)

    plan=models.ForeignKey(Plan, on_delete=models.CASCADE)
    owner=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    maturity_date=models.DateTimeField(null=True)
    status=models.CharField(max_length=200, default='Maturing')
    completed_date=models.DateTimeField(null=True)

    def mature_inv(self):

        self.maturity_date=timezone.now()
        self.save()
        self.status = 'Matured'
        Payment.objects.bulk_create([Payment(investment=self),
                                     Payment(investment=self),
                                     Payment(investment=self)])

    def admin_mature_env(self):
        self.save()
        self.status = 'Matured'
        Payment.objects.bulk_create([Payment(investment=self,),
                                     Payment(investment=self),
                                     Payment(investment=self)])


class Payment(models.Model):
    investment=models.ForeignKey(Investment, on_delete=models.CASCADE)
    status=models.CharField(max_length=200, default='Awaiting Match')
    created_date=models.DateTimeField(auto_now_add=True, null=True)
    completion_date=models.DateTimeField(null=True)

    def match(self):
        #self.status='Awaiting Payment'
        self.save()



class Match(models.Model):
    payer=models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='payer', blank=True)
    investment=models.ForeignKey(Investment, on_delete=models.CASCADE, related_name='investment', null=True, blank=True)
    plan=models.ForeignKey(Plan, on_delete=models.CASCADE, null=True, blank=True)
    receiver=models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='receiver', blank=True)
    bitcoin_value=models.DecimalField(decimal_places=8,max_digits=70, null=True, blank=True)

    status=models.CharField(max_length=200,default='Waiting For Match', choices=(('Expired','Expired'),
                                                     ('Completed' , 'Completed'),
                                                     ('Waiting For Match','Waiting For Match'),
                                                     ('Waiting For Payment','Waiting For Payment')))
    time_matched=models.DateTimeField(null=True, blank=True)
    time_completed=models.DateTimeField(null=True, blank=True)
    expiry_date=models.DateTimeField(default=timezone.now(), null=True, blank=True)
    grace=models.BooleanField(default=True)
    created_date=models.DateTimeField(null=True, auto_now_add=True, blank=True)
    pay=models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)

    def complete_match(self,inv, pay):
        self.time_match=timezone.now()
        self.receiver=inv.owner
        self.bitcoin_value=get_bitcoin_value()
        self.status='Waiting For you to pay'
        self.expiry_date=timezone.now()+timedelta(days=1)
        self.pay=pay
        self.investment=inv
        self.save()



class Evidence(models.Model):
    proof = models.ImageField()
    for_match=models.ForeignKey(Match, on_delete=models.CASCADE)

def get_bitcoin_value():
    return 0.02







