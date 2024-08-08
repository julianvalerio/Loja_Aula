from django.urls import path
from Loja_online import views

urlpatterns = [
    path('', views.index, name='index'),
    path("produtos/", views.listar_produtos, name="produtos"),
    
]