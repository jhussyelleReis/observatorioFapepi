from django.shortcuts import render
from .models import *
#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.core import paginator
import folium
import os
import pandas as pd
import sys

from html.parser import HTMLParser


def listar_bolsas_restri(request, estado, template_name="bolsas_list_restri.html"):
    bolsas = Bolsa.objects.filter(estado=estado)

    return render(request, template_name, {'bolsas': bolsas})

def mapa_bolsas(request, template_name="mapa_bolsas.html"):

    municipios = pd.read_excel('municipiosBrasil.xlsx', encoding='latin1')

    qs = Bolsa.objects.all()

    municipiosBanco = pd.DataFrame.from_records(qs.values('pais', 'estado', 'instituicao', 'modalidade', 'programa', 'vigencia', 'descricao', 'pesquisador'))

    dados = municipios.merge(municipiosBanco, left_on='Mun/UF', right_on='estado', how='inner')

    mapa = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)

    lat = dados['LATITUDE'][:500].values

    long = dados['LONGITUDE'][:500].values

    estados = dados['estado'][:500].values

    municipios = dados['Mun/UF'][:500].values

    for la, lo, es in zip(lat, long, estados):
        if((dados[dados.LATITUDE == la]) is not None ):
            totalDeBolsas = pd.value_counts(dados['LATITUDE'])

        folium.Marker(location=[la, lo], popup=(folium.Popup(es + '</br> Total de Bolsas: '+ str(totalDeBolsas[la]) + '</br><a href="http://127.0.0.1:8000/bolsa/listarrestri/'+es+'" target="_blank"> Pesquisadores </a>'))).add_to(mapa)

    mapa.save(os.path.join('app/templates',"mapa_bolsas.html"))

    with open("app/templates/mapa_bolsas.html", 'r') as f:
        texto = f.readlines()
    with open("app/templates/mapa_bolsas.html", 'w') as f:
        for i in texto:
            if (i.count("rawgit")):
                f.write('    <link rel="stylesheet" href="https://cdn.rawgit.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>' + '\n')
            else:
                f.write(i)

    return render(request, template_name)

def listar_bolsas(request, categoria, template_name="bolsas_list.html"):

    query = request.GET.get("busca", '')

    bolsas = Bolsa.objects.all()

    try:
        if query:
            pesquisador = Pesquisador.objects.get(nome__contains=query)
            bolsas = Bolsa.objects.filter(pesquisador_id=pesquisador.pk)
            mapa_bolsas(request, "mapa_bolsas.html")
        else:
            mapa_bolsas(request, "mapa_bolsas.html")
    except Exception :
        print(sys.exc_info()[0])

    eventosOrganizacao = Evento.objects.filter(tipo='organizacao')

    eventosParticipacao = Evento.objects.filter(tipo='participacao')

    projetos = Projeto.objects.all()

    publicacoes = Publicacao.objects.all()

    instituicoes = Instituicao.objects.all()

    programas = Programa.objects.all()

    return render(request, template_name, {'bolsas': bolsas, 'eventosOrganizacao': eventosOrganizacao,
                                           'eventosParticipacao': eventosParticipacao, 'projetos': projetos,
                                           'publicacoes': publicacoes, 'instituicoes':instituicoes, 'programas':programas})

def listar_participacao_evento_restri(request, estado, template_name="eventos_participacao_list_restri.html"):
    eventosParticipacao = Evento.objects.filter(tipo='participacao', estado=estado)

    return render(request, template_name, {'eventosParticipacao': eventosParticipacao})

def mapa_participacao_eventos(request, template_name="mapa_participacao_eventos.html"):

    municipios = pd.read_excel('municipiosBrasil.xlsx', encoding='latin1')

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
                      popup=(folium.Popup(es + '</br> Total de Eventos: '+ str(totalDeEventos[la]) + '</br><a href="http://127.0.0.1:8000/evento/participacao/listarrestri/'+es+'" target="_blank"> Pesquisadores </a>'))).add_to(mapa)
        #folium.Marker(location=[la, lo], popup='Localização do Evento').add_to(mapa)

    mapa.save(os.path.join('app/templates',"mapa_participacao_eventos.html"))

    with open("app/templates/mapa_participacao_eventos.html", 'r') as f:
        texto = f.readlines()
    with open("app/templates/mapa_participacao_eventos.html", 'w') as f:
        for i in texto:
            if (i.count("rawgit")):
                f.write('    <link rel="stylesheet" href="https://cdn.rawgit.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>' + '\n')
            else:
                f.write(i)


    return render(request, template_name)

def listar_participacao_eventos(request, categoria, template_name="eventos_participacao_list.html"):

    query = request.GET.get("busca", '')

    eventosParticipacao = Evento.objects.filter(tipo='participacao')

    try:
        if query:
            pesquisador = Pesquisador.objects.get(nome__contains=query)
            eventosParticipacao = Evento.objects.filter(pesquisador_id=pesquisador.pk)
            mapa_participacao_eventos(request, "mapa_participacao_eventos.html")
        else:
            mapa_participacao_eventos(request, "mapa_participacao_eventos.html")
    except Exception:
        print(sys.exc_info()[0])

    bolsas = Bolsa.objects.all()

    eventosOrganizacao = Evento.objects.filter(tipo='organizacao')

    projetos = Projeto.objects.all()

    publicacoes = Publicacao.objects.all()

    return render(request, template_name, {'bolsas': bolsas, 'eventosOrganizacao': eventosOrganizacao,
                                           'eventosParticipacao': eventosParticipacao, 'projetos': projetos,
                                           'publicacoes': publicacoes})

def listar_organizacao_evento_restri(request, estado, template_name="eventos_organizacao_list_restri.html"):
    eventosOrganizacao = Evento.objects.filter(tipo='organizacao', estado=estado)

    return render(request, template_name, {'eventosOrganizacao': eventosOrganizacao})

def mapa_organizacao_eventos(request, template_name="mapa_organizacao_eventos.html"):
    municipios = pd.read_excel('municipiosBrasil.xlsx', encoding='latin1')

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
                      popup=(folium.Popup(es + '</br> Total de Eventos: '+ str(totalDeEventos[la]) + '</br><a href="http://127.0.0.1:8000/evento/organizacao/listarrestri/'+es+'" target="_blank"> Pesquisadores </a>'))).add_to(mapa)
        #folium.Marker(location=[la, lo], popup='Localização do Evento').add_to(mapa)

    mapa.save(os.path.join('app/templates', "mapa_organizacao_eventos.html"))

    with open("app/templates/mapa_organizacao_eventos.html", 'r') as f:
        texto = f.readlines()
    with open("app/templates/mapa_organizacao_eventos.html", 'w') as f:
        for i in texto:
            if (i.count("rawgit")):
                f.write('    <link rel="stylesheet" href="https://cdn.rawgit.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>' + '\n')
            else:
                f.write(i)

    return render(request, template_name)

def listar_organizacao_eventos(request, categoria, template_name="eventos_organizacao_list.html"):

    query = request.GET.get("busca", '')

    eventosOrganizacao = Evento.objects.filter(tipo='organizacao')

    try:
        if query:
            pesquisador = Pesquisador.objects.get(nome__contains=query)
            eventosOrganizacao = Evento.objects.filter(pesquisador_id=pesquisador.pk)
            mapa_organizacao_eventos(request, "mapa_organizacao_eventos.html")
        else:
            mapa_organizacao_eventos(request, "mapa_organizacao_eventos.html")
    except Exception:
        print(sys.exc_info()[0])

    bolsas = Bolsa.objects.all()

    eventosParticipacao = Evento.objects.filter(tipo='participacao')

    projetos = Projeto.objects.all()

    publicacoes = Publicacao.objects.all()

    return render(request, template_name, {'bolsas': bolsas, 'eventosOrganizacao': eventosOrganizacao,
                                           'eventosParticipacao': eventosParticipacao, 'projetos': projetos,
                                           'publicacoes': publicacoes})

def listar_projetos_restri(request, estado, template_name="projetos_list_restri.html"):
    projetos = Projeto.objects.filter(estado=estado)

    return render(request, template_name, {'projetos': projetos})

def mapa_projetos(request, template_name="mapa_projetos.html"):
    municipios = pd.read_excel('municipiosBrasil.xlsx', encoding='latin1')

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
                      popup=(folium.Popup(es + '</br> Total de Projetos: '+ str(totalDeProjetos[la]) + '</br><a href="http://127.0.0.1:8000/projeto/listarrestri/'+es+'" target="_blank"> Pesquisadores </a>'))).add_to(
            mapa)
        #folium.Marker(location=[la, lo], popup='Total de Projetos: ').add_to(mapa)

    mapa.save(os.path.join('app/templates', "mapa_projetos.html"))

    with open("app/templates/mapa_projetos.html", 'r') as f:
        texto = f.readlines()
    with open("app/templates/mapa_projetos.html", 'w') as f:
        for i in texto:
            if (i.count("rawgit")):
                f.write('    <link rel="stylesheet" href="https://cdn.rawgit.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>' + '\n')
            else:
                f.write(i)

    return render(request, template_name)

def listar_projetos(request, categoria, template_name="projetos_list.html"):

    query = request.GET.get("busca", '')

    projetos = Projeto.objects.all()

    try:
        if query:
            pesquisador = Pesquisador.objects.get(nome__contains=query)
            projetos = Projeto.objects.filter(pesquisador_id=pesquisador.pk)
            mapa_projetos(request, "mapa_projetos.html")
        else:
            mapa_projetos(request, "mapa_projetos.html")
    except Exception:
        print(sys.exc_info()[0])

    bolsas = Bolsa.objects.all()

    eventosOrganizacao = Evento.objects.filter(tipo='organizacao')

    eventosParticipacao = Evento.objects.filter(tipo='participacao')

    publicacoes = Publicacao.objects.all()

    return render(request, template_name, {'bolsas': bolsas, 'eventosOrganizacao': eventosOrganizacao,
                                           'eventosParticipacao': eventosParticipacao, 'projetos': projetos,
                                           'publicacoes': publicacoes})

def listar_publicacoes_restri(request, estado, template_name="publicacoes_list_restri.html"):
    instituicoes = Instituicao.objects.filter(estado=estado)
    publicacoes = Publicacao.objects.filter(instituicao = instituicoes)

    return render(request, template_name, {'publicacoes': publicacoes})

def mapa_publicoes(request, template_name="mapa_publicacoes.html"):
    municipios = pd.read_excel('municipiosBrasil.xlsx', encoding='latin1')

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
                      popup=(folium.Popup(es + '</br> Total de Publicações: '+ str(totalDePublicacoes[la]) + '</br><a href="http://127.0.0.1:8000/publicacao/listarrestri/'+es+'" target="_blank"> Pesquisadores </a>'))).add_to(
            mapa)
        #folium.Marker(location=[la, lo], popup='Total de Projetos: ').add_to(mapa)

    mapa.save(os.path.join('app/templates', "mapa_publicacoes.html"))

    with open("app/templates/mapa_publicacoes.html", 'r') as f:
        texto = f.readlines()
    with open("app/templates/mapa_publicacoes.html", 'w') as f:
        for i in texto:
            if (i.count("rawgit")):
                f.write('    <link rel="stylesheet" href="https://cdn.rawgit.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>' + '\n')
            else:
                f.write(i)


    return render(request, template_name)

def listar_publicacoes(request, categoria, template_name="publicacoes_list.html"):

    query = request.GET.get("busca", '')

    publicacoes = Publicacao.objects.all()

    try:
        if query:
            pesquisador = Pesquisador.objects.get(nome__contains=query)
            publicacoes = Publicacao.objects.filter(pesquisador_id=pesquisador.pk)
            mapa_publicoes(request, "mapa_publicacoes.html")
        else:
            mapa_publicoes(request, "mapa_publicacoes.html")
    except Exception:
        print(sys.exc_info()[0])

    bolsas = Bolsa.objects.all()

    eventosOrganizacao = Evento.objects.filter(tipo='organizacao')

    eventosParticipacao = Evento.objects.filter(tipo='participacao')

    projetos = Projeto.objects.all()

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

    instituicoes = Instituicao.objects.all()

    programas = Programa.objects.all()

    return render(request, template_name, {'bolsas': bolsas, 'eventosOrganizacao': eventosOrganizacao,
                                           'eventosParticipacao': eventosParticipacao, 'projetos': projetos,
                                           'publicacoes': publicacoes, 'instituicoes': instituicoes,
                                           'programas': programas})
