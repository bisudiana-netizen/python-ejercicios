from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/', views.noticias, name='noticias'),
    path('formulario/', views.formulario, name='formulario'),
    path('<int:id>/', views.detalle_entrada, name= 'detalle_entrada'),
]