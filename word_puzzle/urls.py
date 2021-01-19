from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('<str:nickname>/', views.main, name='main'),
    path('<str:nickname>/state-query/', views.state_query, name='state query')
]
