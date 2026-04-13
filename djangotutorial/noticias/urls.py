from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.artigo_list, name='artigo_list'),
    path('artigo/<int:pk>/', views.artigo_detail, name='artigo_detail'),
    path('artigo/<int:pk>/comentarios/', views.comentarios_view, name='comentarios'),
]