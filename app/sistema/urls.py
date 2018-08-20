from __future__ import unicode_literals

from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views
from . import views as sistema

app_name = 'sistema'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),

    path('login/', auth_views.LoginView.as_view(template_name='usuario/auth.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', sistema.UserCreateView.as_view(template_name='usuario/create.html'), name='signup'),

    path('proposta/', views.PropostaCreateView.as_view(), name='proposta-create'),
    path('proposta/<pk>/', views.PropostaView.as_view(), name='proposta-detail'),
    path('propostas/', views.PropostaListView.as_view(), name='proposta-list'),

    path('comentario/', views.ComentarioCreateView.as_view(), name='comentario-create'),
    path('comentarios/', views.ComentarioListView.as_view(), name='comentario-list'),

    path('voto/', views.VotoCreateView.as_view(), name='voto-create')

    #path('books/create/', views.UsuarioCreateView.as_view(), name='user-create'),
    #path('books/<pk>/', views.BookView.as_view(), name='book-detail'),
    #path('books/<pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
]