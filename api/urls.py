from django.urls import path
from . import views

urlpatterns = [
    path('clubs/', views.ClubList.as_view()),
    path('clubs/<int:pk>/', views.ClubDetail.as_view()),

    path('tournaments/', views.TournamentList.as_view()),
    path('tournaments/<int:pk>/', views.TournamentDetail.as_view()),

    path('clubs/', views.ClubList.as_view()),
    path('clubs/<int:pk>/', views.ClubDetail.as_view()),

    path('verificationcodes/', views.VerificationCodeList.as_view()),
    path('verificationcodes/<int:pk>/', views.VerificationCodeDetail.as_view()),

    path('duels/', views.DuelList.as_view()),
    path('duels/<int:pk>/', views.DuelDetail.as_view()),
    
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),

    path('trees/', views.TreeList.as_view()),
    path('trees/<int:pk>/', views.TreeDetail.as_view()),

    path('participants/', views.ParticipantList.as_view()),
    path('participants/<int:pk>/', views.ParticipantDetail.as_view()),
    
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
