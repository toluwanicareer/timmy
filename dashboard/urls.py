from django.conf.urls import url
from django.urls import path
from . import views

app_name='dash'

urlpatterns = [
    path('', views.MatchView.as_view(), name='match'),
    path('ajax_user/<int:pk>/', views.UserInfoView.as_view(), name='ajax_user'),
    path('ajax_evidence/', views.EvidenceList.as_view(), name='ajax_evidence'),
    path('ajax_action', views.MatchAction.as_view(), name='ajax_action'),
    path('upload_evidence/<int:pk>/', views.UploadEvidence.as_view(), name='upload_evidence'),
    path('request_match', views.RequestMatch.as_view(), name='request_match'),
    path('profile', views.ProfileUpdateView.as_view(), name='profile'),
    path('matchadmin', views.MatchAdmin.as_view(), name='match_admin'),

    ]