from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.getData),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('superendpoint/', views.superEndpoint)
]
