from __future__ import unicode_literals

from django.db import models

import uuid

from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission

class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

class Proposta(models.Model):
    
    nome = models.CharField(max_length=255, verbose_name='Lei')
    descricao = models.TextField(null=False, blank=True, verbose_name='Descrição')
    usuario = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='propostas', verbose_name='UUIDUser')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'proposta'
        verbose_name_plural = 'propostas'

class Lei(models.Model):
    
    nome = models.ForeignKey(Proposta, on_delete=models.CASCADE, related_name='leis', verbose_name='Nome')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'lei'
        verbose_name_plural = 'leis'

class Comentario(models.Model):

    usuario = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='comentarios', verbose_name='UUIDUser')
    comentario = models.CharField(max_length=255, null=False, blank=False, verbose_name='Comentário')
    proposta = models.ForeignKey(Proposta,on_delete=models.CASCADE, related_name='comentarios', verbose_name='Proposta')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')

    def __str__(self):
        return self.comentario

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'

class Voto(models.Model):

    Favor = "Favor"
    Contra = "Contra"
    VOTO = (
        (Favor, "Favor"), 
        (Contra, "Contra")
        )

    usuario = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, related_name='votos', verbose_name='UUIDUser')
    voto = models.CharField(max_length=6, choices=VOTO, default=Favor, verbose_name='Voto')
    proposta = models.ForeignKey(Proposta,on_delete=models.CASCADE, related_name='votos', verbose_name='Proposta')

    def __str__(self):
        return self.voto

    class Meta:
        verbose_name = 'voto'
        verbose_name_plural = 'votos'