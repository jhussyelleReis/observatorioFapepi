from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.observatorio_default, name='observatorio_default'),
    url(r'^bolsa/listar/(?P<categoria>[\w\-]+)/$', views.listar_bolsas, name='listar_bolsas'),
    url(r'^bolsa/mapa/bolsas/$', views.mapa_bolsas, name='mapa_bolsas'),
    url(r'^evento/participacao/listar/(?P<categoria>[\w\-]+)/$', views.listar_participacao_eventos, name='listar_participacao_eventos'),
    url(r'^evento/mapa/eventos/participacao/$', views.mapa_participacao_eventos, name='mapa_participacao_eventos'),
    url(r'^evento/organizacao/listar/(?P<categoria>[\w\-]+)/$', views.listar_organizacao_eventos, name='listar_organizacao_eventos'),
    url(r'^evento/mapa/eventos/organizacao/$', views.mapa_organizacao_eventos, name='mapa_organizacao_eventos'),
    url(r'^projeto/listar/(?P<categoria>[\w\-]+)/$', views.listar_projetos, name='listar_projetos'),
    url(r'^projeto/mapa/projetos/$', views.mapa_projetos, name='mapa_projetos'),
    url(r'^publicacao/listar/(?P<categoria>[\w\-]+)/$', views.listar_publicacoes, name='listar_publicacoes'),
    url(r'^publicacao/mapa/publicacoes/$', views.mapa_publicoes, name='mapa_publicacoes'),

]

