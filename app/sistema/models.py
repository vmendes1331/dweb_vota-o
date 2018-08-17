from django.db import models

class Lei(models.Model):
    
    nome = models.CharField(max_length=255, null=False, blank=True, verbose_name='Nome')
    usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='usuarios', verbose_name='Usuários')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'lei'
        verbose_name_plural = 'leis'

class Proposta(models.Model):

    Favor = "Favor"
    Contra = "Contra"
    VOTO = (
        (Favor, "Favor"), 
        (Contra, "Contra")
        )

    #user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, null=False, verbose_name='Usuário')
    nome = models.CharField(max_length=255, verbose_name='Lei')
    comentario = models.CharField(max_length=255, null=True, blank=True, verbose_name='Comentário')
    usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='usuario', verbose_name='Usuário')
    voto = models.CharField(max_length=6, choices=VOTO, default=Favor, verbose_name='Voto')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'proposta'
        verbose_name_plural = 'propostas'