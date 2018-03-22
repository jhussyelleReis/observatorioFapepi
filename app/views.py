from django.shortcuts import render
from .models import *
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.core import paginator
import folium
import os
import pandas as pd

def mapa_bolsas(request, template_name="mapa_bolsas.html"):

    municipios = pd.read_excel('municipiosBrasil.xls', encoding='latin1')

    qs = Bolsa.objects.all()

    municipiosBanco = pd.DataFrame.from_records(qs.values('pais', 'estado', 'instituicao', 'modalidade', 'programa', 'vigencia', 'descricao', 'pesquisador'))

    dados = municipios.merge(municipiosBanco, left_on='Mun/UF', right_on='estado', how='inner')

    mapa = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)

    lat = dados['LATITUDE'][:500].values

    long = dados['LONGITUDE'][:500].values

    estados = dados['estado'][:500].values

    for la, lo, es in zip(lat, long, estados):
        if((dados[dados.LATITUDE == la]) is not None ):
            totalDeBolsas = pd.value_counts(dados['LATITUDE'])
        folium.Marker(location=[la, lo], popup=(folium.Popup(es + '</br> Total de Bolsas: ' + str(totalDeBolsas[la]) + " ." ))).add_to(mapa)

    mapa.save(os.path.join('app/templates',"mapa_bolsas.html"))

    return render(request, template_name)

def listar_bolsas(request, categoria, template_name="bolsas_list.html"):

    mapa_bolsas(request, "mapa_bolsas.html")

    bolsas = Bolsa.objects.all()

    eventosOrganizacao = Evento.objects.filter(tipo='organizacao')

    eventosParticipacao = Evento.objects.filter(tipo='participacao')

    projetos = Projeto.objects.all()

    publicacoes = Publicacao.objects.all()

    return render(request, template_name, {'bolsas': bolsas, 'eventosOrganizacao': eventosOrganizacao,
                                           'eventosParticipacao': eventosParticipacao, 'projetos': projetos,
                                           'publicacoes': publicacoes})

def mapa_participacao_eventos(request, template_name="mapa_participacao_eventos.html"):

    municipios = pd.read_excel('municipiosBrasil.xls', encoding='latin1')

    qs = Evento.objects.all()

    municipiosBanco = pd.DataFrame.from_records(qs.values('titulo', 'tipo', 'area', 'pais', 'estado', 'data', 'pesquisador'))

    municipiosBanco = municipiosBanco[municipiosBanco.tipo == 'participacao']

    dados = municipios.merge(municipiosBanco, left_on='Mun/UF', right_on='estado', how='inner')

    mapa = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)

    lat = dados['LATITUDE'][:500].values

    long = dados['LONGITUDE'][:500].values

    estados = dados['estado'][:500].values

    for la, lo, es in zip(lat, long, estados):
        if ((dados[dados.LATITUDE == la]) is not None):
            totalDeEventos = pd.value_counts(dados['LATITUDE'])
        folium.Marker(location=[la, lo],
                      popup=(folium.Popup(es + '</br> Total de Eventos: ' + str(totalDeEventos[la]) + " ."))).add_to(mapa)
        #folium.Marker(location=[la, lo], popup='Localização do Evento').add_to(mapa)

    mapa.save(os.path.join('app/templates',"mapa_participacao_eventos.html"))

    return render(request, template_name)

def listar_participacao_eventos(request, categoria, template_name="eventos_participacao_list.html"):

    mapa_participacao_eventos(request, "mapa_participacao_eventos.html")

    bolsas = Bolsa.objects.all()

    eventosOrganizacao = Evento.objects.filter(tipo='organizacao')

    eventosParticipacao = Evento.objects.filter(tipo='participacao')

    projetos = Projeto.objects.all()

    publicacoes = Publicacao.objects.all()

    return render(request, template_name, {'bolsas': bolsas, 'eventosOrganizacao': eventosOrganizacao,
                                           'eventosParticipacao': eventosParticipacao, 'projetos': projetos,
                                           'publicacoes': publicacoes})

def mapa_organizacao_eventos(request, template_name="mapa_organizacao_eventos.html"):
    municipios = pd.read_excel('municipiosBrasil.xls', encoding='latin1')

    qs = Evento.objects.all()

    municipiosBanco = pd.DataFrame.from_records(
        qs.values('titulo', 'tipo', 'area', 'pais', 'estado', 'data', 'pesquisador'))

    municipiosBanco = municipiosBanco[municipiosBanco.tipo == 'organizacao']

    dados = municipios.merge(municipiosBanco, left_on='Mun/UF', right_on='estado', how='inner')

    mapa = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)

    lat = dados['LATITUDE'][:1000].values

    long = dados['LONGITUDE'][:1000].values

    estados = dados['estado'][:1000].values

    for la, lo, es in zip(lat, long, estados):
        if ((dados[dados.LATITUDE == la]) is not None):
            totalDeEventos = pd.value_counts(dados['LATITUDE'])
        folium.Marker(location=[la, lo],
                      popup=(folium.Popup(es + '</br> Total de Eventos: ' + str(totalDeEventos[la]) + " ."))).add_to(mapa)
        #folium.Marker(location=[la, lo], popup='Localização do Evento').add_to(mapa)

    mapa.save(os.path.join('app/templates', "mapa_organizacao_eventos.html"))

    return render(request, template_name)

def listar_organizacao_eventos(request, categoria, template_name="eventos_organizacao_list.html"):

    mapa_organizacao_eventos(request, "mapa_organizacao_eventos.html")

    bolsas = Bolsa.objects.all()

    eventosOrganizacao = Evento.objects.filter(tipo='organizacao')

    eventosParticipacao = Evento.objects.filter(tipo='participacao')

    projetos = Projeto.objects.all()

    publicacoes = Publicacao.objects.all()

    return render(request, template_name, {'bolsas': bolsas, 'eventosOrganizacao': eventosOrganizacao,
                                           'eventosParticipacao': eventosParticipacao, 'projetos': projetos,
                                           'publicacoes': publicacoes})

def mapa_projetos(request, template_name="mapa_projetos.html"):
    municipios = pd.read_excel('municipiosBrasil.xls', encoding='latin1')

    qs = Projeto.objects.all()

    municipiosBanco = pd.DataFrame.from_records(
        qs.values('pais', 'estado', 'instituicao', 'titulo', 'resumo', 'vigencia', 'valor','programa', 'pesquisador'))

    dados = municipios.merge(municipiosBanco, left_on='Mun/UF', right_on='estado', how='inner')

    mapa = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)

    lat = dados['LATITUDE'][:500].values

    long = dados['LONGITUDE'][:500].values

    estados = dados['estado'][:1000].values

    for la, lo, es in zip(lat, long, estados):
        if ((dados[dados.LATITUDE == la]) is not None):
            totalDeProjetos = pd.value_counts(dados['LATITUDE'])
        folium.Marker(location=[la, lo],
                      popup=(folium.Popup(es + '</br> Total de Eventos: ' + str(totalDeProjetos[la]) + " ."))).add_to(
            mapa)
        #folium.Marker(location=[la, lo], popup='Total de Projetos: ').add_to(mapa)

    mapa.save(os.path.join('app/templates', "mapa_projetos.html"))

    return render(request, template_name)

def listar_projetos(request, categoria, template_name="projetos_list.html"):

    mapa_projetos(request, "mapa_projetos.html")

    bolsas = Bolsa.objects.all()

    eventosOrganizacao = Evento.objects.filter(tipo='organizacao')

    eventosParticipacao = Evento.objects.filter(tipo='participacao')

    projetos = Projeto.objects.all()

    publicacoes = Publicacao.objects.all()

    return render(request, template_name, {'bolsas': bolsas, 'eventosOrganizacao': eventosOrganizacao,
                                           'eventosParticipacao': eventosParticipacao, 'projetos': projetos,
                                           'publicacoes': publicacoes})

def mapa_publicoes(request, template_name="mapa_publicacoes.html"):
    municipios = pd.read_excel('municipiosBrasil.xls', encoding='latin1')

    publicacoes = Publicacao.objects.all()

    publicacoesBanco = pd.DataFrame.from_records(
        publicacoes.values('titulo', 'modalidade', 'area', 'pesquisador', 'instituicao'))

    instituicoes = Instituicao.objects.all()

    instituicoesBanco = pd.DataFrame.from_records(
        instituicoes.values('id','pais', 'estado', 'nome', 'endereco'))

    pesquisa = publicacoesBanco.merge(instituicoesBanco, left_on='instituicao', right_on='id', how='inner')

    dados = municipios.merge(pesquisa, left_on='Mun/UF', right_on='estado', how='inner')

    mapa = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)

    lat = dados['LATITUDE'][:500].values

    long = dados['LONGITUDE'][:500].values

    estados = dados['estado'][:1000].values

    for la, lo, es in zip(lat, long, estados):
        if ((dados[dados.LATITUDE == la]) is not None):
            totalDePublicacoes = pd.value_counts(dados['LATITUDE'])
        folium.Marker(location=[la, lo],
                      popup=(folium.Popup(es + '</br> Total de Publicações: ' + str(totalDePublicacoes[la]) + " ."))).add_to(
            mapa)
        #folium.Marker(location=[la, lo], popup='Total de Projetos: ').add_to(mapa)

    mapa.save(os.path.join('app/templates', "mapa_publicacoes.html"))

    return render(request, template_name)

def listar_publicacoes(request, categoria, template_name="publicacoes_list.html"):

    mapa_projetos(request, "mapa_publicacoes.html")

    bolsas = Bolsa.objects.all()

    eventosOrganizacao = Evento.objects.filter(tipo='organizacao')

    eventosParticipacao = Evento.objects.filter(tipo='participacao')

    projetos = Projeto.objects.all()

    publicacoes = Publicacao.objects.all()

    return render(request, template_name, {'bolsas': bolsas, 'eventosOrganizacao': eventosOrganizacao,
                                           'eventosParticipacao': eventosParticipacao, 'projetos': projetos, 'publicacoes':publicacoes})

def observatorio_default(request, template_name="observatorio_default.html"):

    mapa_bolsas(request, "mapa_bolsas.html")

    bolsas = Bolsa.objects.all()

    eventosBanco = Evento.objects.all()

    eventosTratamento = pd.DataFrame.from_records(
        eventosBanco.values('titulo', 'tipo', 'area', 'pais', 'estado', 'data', 'pesquisador'))

    eventosOrganizacao = eventosTratamento[eventosTratamento.tipo == 'organizacao']

    eventosParticipacao = eventosTratamento[eventosTratamento.tipo == 'participacao']

    projetos = Projeto.objects.all()

    publicacoes = Publicacao.objects.all()

    return render(request, template_name, {'bolsas': bolsas, 'eventosOrganizacao': eventosOrganizacao,
                                           'eventosParticipacao': eventosParticipacao, 'projetos': projetos,
                                           'publicacoes': publicacoes})
