from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='main/index.html'

class PlanView(TemplateView):
    template_name ='main/pricing.html'

class AboutView(TemplateView):
    template_name = 'main/about.html'






