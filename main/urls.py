from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='match'),
    path('pricing/', views.PlanView.as_view(), name='plan'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', TemplateView.as_view(template_name="main/services.html"), name='services'),
    path('faq/', TemplateView.as_view(template_name='main/faq.html'), name='faq'),
]