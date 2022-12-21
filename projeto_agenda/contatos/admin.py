from django.contrib import admin

# Register your models here.
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','telefone','email','date_create','categoria','mostrar')
    list_display_links = ('id','nome','sobrenome')
    list_per_page = 10
    search_fields = ('nome','sobrenome','telefone')
    list_editable = ('telefone','mostrar')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)