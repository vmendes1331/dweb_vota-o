from django.db import models

class Proposta(models.Model):
    
    nome = models.CharField(max_length=255, verbose_name='Lei')
    descricao = models.TextField(null=False, blank=True, verbose_name='Descrição')
    usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='propostas', verbose_name='Usuário')

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

    usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='comentarios', verbose_name='Usuário')
    comentario = models.CharField(max_length=255, null=False, blank=False, verbose_name='Comentário')
    proposta = models.ForeignKey(Proposta,on_delete=models.CASCADE, related_name='comentarios', verbose_name='Proposta')

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

    usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='votos', verbose_name='Usuário')
    voto = models.CharField(max_length=6, choices=VOTO, default=Favor, verbose_name='Voto')
    proposta = models.ForeignKey(Proposta,on_delete=models.CASCADE, related_name='votos', verbose_name='Proposta')

    def __str__(self):
        return self.voto

    class Meta:
        verbose_name = 'voto'
        verbose_name_plural = 'votos'