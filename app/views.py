from django.shortcuts import render
from .models import *
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.core import paginator
import folium
import os
import pandas as pd

def listar_bolsas(request, template_name="bolsas_list.html"):

    #testeDeCommit

    return render(request, template_name)


def mapa(request, template_name="mapa.html"):

    municipios = pd.read_excel('municipiosBrasil.xls', encoding='latin1')

    qs = Bolsa.objects.all()

    municipiosBanco = pd.DataFrame.from_records(qs.values('pais', 'estado', 'instituicao', 'modalidade', 'programa', 'vigencia', 'descricao', 'pesquisador'))

    dados = municipios.merge(municipiosBanco, left_on='Mun/UF', right_on='estado', how='inner')

    mapa = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)

    lat = dados['LATITUDE'][:500].values

    long = dados['LONGITUDE'][:500].values

    for la, lo in zip(lat, long):
        folium.Marker(location=[la, lo], popup='Localização da Bolsa').add_to(mapa)

    mapa.save(os.path.join('app/templates',"mapa.html"))

    return render(request, template_name)
