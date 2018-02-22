from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^bolsa/listar/$', views.listar_bolsas, name='listar_bolsas'),
    url(r'^bolsa/mapa/$', views.mapa, name='mapa'),
]

