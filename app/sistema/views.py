from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy

from . import models

from . import forms

class IndexView(TemplateView):

    template_name = 'dashboard.html'

class UserCreateView(CreateView):

    model = models.UUIDUser
    template_name = 'usuario/auth.html'
    success_url = reverse_lazy('sistema:proposta-create')
    form_class = forms.UserForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return super(UserCreateView, self).form_valid(form)

class PropostaView(DetailView):

    model = models.Proposta
    template_name = 'proposta/detail.html'

    def get_context_data(self, **kwargs):
        kwargs['comentario'] = models.Comentario.objects.filter(id=self.object.pk)

        return super(PropostaView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return models.Proposta.objects.all()

class PropostaCreateView(CreateView):

    model = models.Proposta
    template_name = 'proposta/create.html'
    success_url = reverse_lazy('sistema:proposta-create')
    fields = ['nome', 'descricao', 'usuario']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(PropostaCreateView, self).form_valid(form)

class ComentarioCreateView(CreateView):

    model = models.Comentario
    template_name = 'comentario/create.html'
    success_url = reverse_lazy('sistema:comentario-create')
    fields = ['usuario', 'comentario', 'proposta']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(ComentarioCreateView, self).form_valid(form)

class VotoCreateView(CreateView):

    model = models.Voto
    template_name = 'voto/create.html'
    success_url = reverse_lazy('sistema:voto-create')
    fields = ['usuario', 'voto', 'proposta']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(VotoCreateView, self).form_valid(form)

class ComentarioListView(ListView):

    model = models.Comentario
    template_name = 'comentario/list.html'

class PropostaListView(ListView):

    model = models.Proposta
    template_name = 'proposta/list.html'