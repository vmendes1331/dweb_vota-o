from django.urls import path

from . import views

app_name = 'sistema'

urlpatterns = [

    # Pripostas
    path('proposta/', views.PropostaCreateView.as_view(), name='proposta-create'),
    path('comentario', views.ComentarioCreateView.as_view(), name='comentario-create'),
    path('comentarios', views.ComentarioListView.as_view(), name='comentario-list'),
    path('voto', views.VotoCreateView.as_view(), name='voto-create'),
    path('', views.IndexView.as_view(), name='index'),
    #path('books/create/', views.UsuarioCreateView.as_view(), name='user-create'),
    #path('books/<pk>/', views.BookView.as_view(), name='book-detail'),
    #path('books/<pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
]