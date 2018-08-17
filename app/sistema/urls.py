from django.urls import path

from . import views

app_name = 'sistema'

urlpatterns = [

    # Pripostas
    path('proposta/', views.PropostaView.as_view(), name='proposta-list'),
    #path('books/create/', views.UsuarioCreateView.as_view(), name='user-create'),
    #path('books/<pk>/', views.BookView.as_view(), name='book-detail'),
    #path('books/<pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
]