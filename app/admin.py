from django.contrib import admin
from .models import *

class BolsaAdmin(admin.ModelAdmin):
    model = Bolsa
    list_display = ('pesquisador','programa','pais')
    list_filter = ['pesquisador','programa','pais','vigencia']
    search_fields = ['estado']

class PesquisadorAdmin(admin.ModelAdmin):
    model = Pesquisador
    list_display = ('nome', 'area_pesquisa')
    list_filter = ['sexo']
    search_fields = ['nome']

class InstituicaoAdmin(admin.ModelAdmin):
    model = Instituicao
    list_display = ('nome', 'endereco')
    search_fields = ['nome']

class ProgramaAdmin(admin.ModelAdmin):
    model = Programa
    list_display = ('nome','descricao')
    search_fields = ['nome']

class ProjetoAdmin(admin.ModelAdmin):
    model = Projeto
    list_display = ('titulo', 'pesquisador', 'vigencia')
    list_filter = ['titulo', 'pesquisador', 'programa', 'vigencia']
    search_fields = ['titulo']

class PublicacaoAdmin(admin.ModelAdmin):
    model = Publicacao
    list_display = ('titulo', 'pesquisador', 'modalidade')
    list_filter = ['titulo', 'pesquisador', 'modalidade']
    search_fields = ['titulo']

class EventoAdmin(admin.ModelAdmin):
    model = Evento
    list_display = ('titulo', 'pesquisador', 'pais', 'estado')
    list_filter = ['titulo', 'pesquisador', 'estado']
    search_fields = ['titulo']

admin.site.register(Bolsa, BolsaAdmin)
admin.site.register(Pesquisador, PesquisadorAdmin)
admin.site.register(Programa, ProgramaAdmin)
admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Evento, EventoAdmin)