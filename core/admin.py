from django.contrib import admin
from core.models import Evento

# Register your models here.

# classe para definir quais campos mostrar de titulo
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ( 'usuario', 'data_evento', )

# registrando a tabela no banco de dados
admin.site.register(Evento, EventoAdmin)