from django.urls import path
from . import views

urlpatterns = [
    path('participants/', views.ParticipantList.as_view()),
    path('clubs/', views.ClubList.as_view()),
    path('clubs/<int:pk>/', views.ClubDetail.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
]
