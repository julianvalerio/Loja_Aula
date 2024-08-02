from django.urls import path
from Loja_online import views

urlpatterns = [
    path('', views.index, name='index'),
]