from django.contrib import admin
from .models import *

admin.site.register(UUIDUser)
admin.site.register(Proposta)
admin.site.register(Lei)
admin.site.register(Comentario)
admin.site.register(Voto)
