from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from . import models, forms

class PropostaCreateView(CreateView):

    model = models.Proposta
    template_name = 'proposta/create.html'
    success_url = reverse_lazy('sistema:proposta-list')
    fields = ['nome', 'comentario', 'voto']