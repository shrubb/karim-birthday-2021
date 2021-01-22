from django.urls import path

from . import views

urlpatterns = [
    path('', views.login),
    path('<str:nickname>/', views.main),
    path('<str:nickname>/state-query/', views.state_query),
    path('<str:nickname>/submit-word/', views.submit_word),
    path('<str:nickname>/leaderboard/', views.leaderboard),
]
