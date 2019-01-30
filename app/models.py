from django.db import models


class Pesquisador(models.Model):
    SEXO_CHOICES = (("feminino", "Feminino"), ("masculino", "Masculino"))

    nome = models.CharField(max_length=100, null=False, verbose_name="Nome")
    cpf = models.CharField(max_length=50, null=False)
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    telefone = models.CharField(max_length=20, null=False)
    area_pesquisa = models.CharField(max_length=150, null=False, verbose_name="Área de Pesquisa")

    # foto?

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Pesquisadores"
        verbose_name = "Pesquisador"
        ordering = ['nome']

class Programa(models.Model):
    nome = models.CharField(max_length=150, null=False, verbose_name="Nome")
    descricao = models.CharField(null=False, max_length=150, verbose_name="Descrição")

    # só?

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Programas"
        verbose_name = "Programa"
        ordering = ['nome']

class Instituicao(models.Model):

    ESTADO_CHOICES = (
    ("RIOBRANCO-AC", "Acre"), ("MACEIO-AL", "Alagoas"), ("MACAPA-AP", "Amapá"), ("MANAUS-AM", "Amazonas"),
    ("SALVADOR-BA", "Bahia"), ("FORTALEZA-CE", "Ceará"), ("BRASILIA-DF", "Distrito Federal"),
    ("VITORIA-ES", "Espírito Santo"),
    ("GOIANIA-GO", "Goiás"), ("SAOLUIS-MA", "Maranhão"), ("BELOHORIZONTE-MG", "Minas Gerais"),
    ("CAMPOGRANDE-MS", "Mato Grosso do Sul"),
    ("CUIABA-MT", "Mato Grosso"), ("BELEM-PA", "Pará"), ("JOAOPESSOA-PB", "Paraíba"),
    ("RECIFE-PE", "Pernambuco"), ("TERESINA-PI", "Piauí"),
    ("CURITIBA-PR", "Paraná"), ("RIODEJANEIRO-RJ", "Rio de Janeiro"), ("NATAL-RN", "Rio Grande do Norte"),
    ("PORTOVELHO-RO", "Rondônia"),
    ("BOAVISTA-RR", "Roraima"), ("PORTOALEGRE-RS", "Rio Grande do Sul"), ("FLORIANOPOLIS-SC", "Santa Catarina"),
    ("ARACAJU-SE", "Sergipe"),
    ("SAOPAULO-SP", "São Paulo"), ("PALMAS-TO", "Tocantins"))

    pais = models.CharField(max_length=50, null=False, verbose_name="País", default="Brasil")
    estado = models.CharField(max_length=50, null=False, verbose_name="Estado", choices=ESTADO_CHOICES)
    nome = models.CharField(null=False, max_length=50, verbose_name="Nome")
    endereco = models.CharField(null=False, max_length=50, verbose_name="Endereço")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Instituições"
        verbose_name = "Instituição"
        ordering = ['nome']

class Edital(models.Model):

    TIPO_CHOICES = (("bolsa", "Bolsa"), ("participacao", "Participação em Eventos"),
                    ("organizacao", "Organização de Eventos"), ("projeto", "Projeto"),
                    ("publicacao", "Publicação"))
    ANO_CHOICES = (("2018", "2018"), ("2017", "2017"),("2016", "2016"), ("2015", "2015"),("2014", "1014"),
                   ("2013", "2013"), ("2012", "2012"), ("2011", "2011"))

    titulo = models.CharField(max_length=200, null=False, verbose_name="Título")
    tipo = models.CharField(max_length=100, null=False, verbose_name="Tipo de Aplicação", choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=200, null=False, verbose_name="Descrição")
    ano = models.CharField(max_length=200, null=False, verbose_name="Ano", choices=ANO_CHOICES)
    vigencia = models.DateField(null=False, verbose_name="Vigência")
    programa = models.ForeignKey(Programa, verbose_name="Programa")
    recurso = models.DecimalField(max_digits=19, decimal_places=10, null=False, verbose_name="Valor Global do Edital", default=0)
    #faixa = models.ForeignKey(Faixa, verbose_name="Faixas")


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Editais"
        verbose_name = "Edital"

class Faixa(models.Model):

    nome = models.CharField(max_length=200, null=False, verbose_name="Nome")
    valor = models.DecimalField(max_digits=19, decimal_places=10, null=False, verbose_name="Valor", default=0)
    quantidade = models.IntegerField(null=False, verbose_name="Quantidade", default=0)
    edital = models.ForeignKey(Edital, verbose_name="Faixas")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Faixas de Financiamento"
        verbose_name = "Faixa"

class Bolsa(models.Model):
  #  PAISES_CHOICES = (("afeganistao", "Afeganistão"), ("africa_do_sul", "África do Sul"), ("albania", "Albânia"),
   #                   ("alemanha", "Alemanha"), ("andorra", "Andorra"), ("angola", "Angola"),
    #                  ("antiga_barbuda", "Antiga e Barbuda"), ("arabia", "Arábia Saudita"), ("argelia", "Argélia"),
     #                 ("argentina", "Argentina"), ("arménia", "Arménia"), ("australia", "Austrália"),
      #                ("austria", "Áustria"), ("azer", "Azerbaijão"), ("angola", "Bahamas"),
       #               ("bangladexe", "Bangladexe"), ("barbados", "Barbados"), ("barem", "Barém"),
        #              ("belgica", "Bélgica"), ("belize", "Belize"), ("benim", "Benim"),
         #             ("bielorrussia", "Bielorrússia"), ("bolivia", "Bolívia"), ("bosnia", "Bósnia e Herzegovina"),
          #            ("botsuana", "Botsuana"), ("brasil", "Brasil"), ("brunei", "Brunei"),
           #           ("bulgaria", "Bulgária"), ("burquina", "Burquina Faso"), ("burundi", "Burúndi"),
            #          ("butao", "Butão"), ("cabo_verde", "Cabo Verde"), ("camaraes", "Camarões"),
             #         ("camboja", "Camboja"), ("canada", "Canadá"), ("catar", "Catar"),
              #        ("cazaquistao", "Cazaquistão"), ("chade", "Chade"), ("chile", "Chile"),
               #       ("china", "China"), ("chipre", "Chipre"), ("colombia", "Colômbia"),
               #       ("comores", "Comores"), ("congo", "Congo-Brazzaville"), ("coreia_norte", "Coreia do Norte"),
            #          ("coreia_sul", "Coreia do Sul"), ("cosvo", "Cosovo"), ("costa_marfim", "Costa do Marfim"),
          #            ("costa_rica", "Costa Rica"), ("croacia", "Croácia"), ("cuaite", "Cuaite"),
           #           ("cuba", "Cuba"), ("dinamarca", "Dinamarca"), ("dominca", "Dominica"),
            #          ("egito", "Egito"), ("emirados", "Emirados Árabes Unidos"), ("equador", "Equador"),
             #         ("eritreia", "Eritreia"), ("eslovaquia", "Eslováquia"), ("eslovenia", "Eslovénia"),
           #           ("espanha", "Espanha"), ("palestina", "Estado da Palestina"), ("eua", "Estados Unidos"),
           #           ("estonia", "Estónia"), ("etiopia", "Etiópia"), ("fiji", "Fiji"),
            #          ("filipinas", "Filipinas"), ("finlandia", "Finlândia"), ("franca", "França"),
             #         ("gabao", "Gabão"), ("gambia", "Gâmbia"), ("gana", "Gana"),
              #        ("georgia", "Geórgia"), ("granada", "Granada"), ("grecia", "Grécia"),
               #       ("guine_e", "Guiné Equatorial"), ("guine_b", "Guiné-Bissau"), ("haiti", "Haiti"),
                #      ("holanda", "Holanda"),
             #         ("honduras", "Honduras"), ("hungria", "Hungria"), ("iemen", "Iémen"),
              #        ("ilhas", "Ilhas Marechal"), ("india", "Índia"), ("indonésia", "Indonésia"),
               #       ("irao", "Irão"), ("iraque", "Iraque"), ("irlanda", "Irlanda"),
                #      ("islandia", "Islândia"), ("israel", "Israel"), ("italia", "Itália"),
           #           ("jamaica", "Jamaica"), ("japao", "Japão"), ("jibuti", "Jibuti"),
            #          ("jordania", "Jordânia"), ("laus", "Laus"), ("lesoto", "Lesoto"),
             #         ("letonia", "Letónia"), ("libano", "Líbano"), ("liberia", "Libéria"),
              #        ("libia", "Líbia"), ("listenstaine", "Listenstaine"), ("lituania", "Lituânia"),
               #       ("luxemburgo", "Luxemburgo"), ("macedonia", "Macedónia"), ("madagascar", "Madagáscar"),
                #      ("malasia", "Malásia"), ("malaui", "Maláui"), ("maldivas", "Maldivas"),
                 #     ("mali", "Mali"), ("malta", "Malta"), ("marrocos", "Marrocos"),
                  #    ("mauricia", "Maurícia"), ("mauritania", "Mauritânia"), ("mexico", "México"),
     #                 ("mianmar", "Mianmar"), ("micronesia", "Micronésia"), ("mocambique", "Moçambique"),
      #                ("moldavia", "Moldávia"), ("monaco", "Mónaco"), ("mongolia", "Mongólia"),
       #               ("montenegro", "Montenegro"), ("namibia", "Namíbia"), ("nauru", "Nauru"),
        #              ("nepal", "Nepal"), ("nicaragua", "Nicarágua"), ("niger", "Níger"),
         #             ("nigeria", "Nigéria"), ("noruega", "Noruega"), ("nova_zelandia", "Nova Zelândia"),
          #            ("oma", "Omã"), ("paises_baixos", "Países Baixos"), ("palau", "Palau"),
           #           ("panama", "Panamá"), ("nova_guine", "Papua Nova Guiné"), ("paquistao", "Paquistão"),
            #          ("paraguai", "Paraguai"), ("peru", "Peru"), ("polonia", "Polónia"),
             #         ("portugal", "Portugal"), ("quenia", "Quénia"), ("quirguistao", "Quirguistão"),
              #        ("quiribati", "Quiribáti"), ("reino_unido", "Reino Unido"),
               #       ("republica_ca", "República Centro-Africana"),
                #      ("republica_checa", "República Checa"), ("republica_dc", "República Democrática do Congo"),
                 #     ("republica_d", "República Dominicana"),
            #          ("romenia", "Roménia"), ("ruanda", "Ruanda"), ("russia", "Rússia"),
             #         ("salomao", "Salomão"), ("salvador", "Salvador"), ("samoa", "Samoa"),
              #        ("santa_lucia", "Santa Lúcia"), ("sao_cristovao", "São Cristóvão e Neves"),
               #       ("sao_marinho", "São Marinho"),
                #      ("sao_tome", "São Tomé e Príncipe"), ("sao_vicente", "São Vicente e Granadinas"),
                 #     ("seicheles", "Seicheles"),
                  #    ("senegal", "Senegal"), ("serra", "Serra Leoa"), ("servia", "Sérvia"), ("singapura", "Singapura"),
                   #   ("siria", "Síria"), ("angola", "Somália"), ("sri_Lanca", "Sri Lanca"),
                    #  ("suazilandia", "Suazilândia"),
                     # ("sudao", "Sudão"), ("sudao_sul", "Sudão do Sul"), ("suecia", "Suécia"), ("suica", "Suíça"),
        #              ("suriname", "Suriname"), ("tailandia", "Tailândia"), ("taiua", "Taiuã"),
         #             ("tajiquistao", "Tajiquistão"), ("tanzania", "Tanzânia"), ("timor_leste", "Timor-Leste"),
          #            ("togo", "Togo"), ("tonga", "Tonga"), ("trindade_tobago", "Trindade e Tobago"),
           #           ("tunisia", "Tunísia"), ("turcomenistao", "Turcomenistão"), ("turquia", "Turquia"),
            #          ("tuvalu", "Tuvalu"), ("ucrania", "Ucrânia"), ("uganda", "Uganda"),
             #         ("uruguai", "Uruguai"), ("usbequistao", "Usbequistão"), ("vanuatu", "Vanuatu"),
              #        ("vaticano", "Vaticano"), ("venezuela", "Venezuela"), ("vietname", "Vietname"),
               #       ("zambia", "Zâmbia"), ("zimbabue", "Zimbábue"))#

    ESTADO_CHOICES = ( ("RIOBRANCO-AC", "Acre"), ("MACEIO-AL", "Alagoas"), ("MACAPA-AP", "Amapá"), ("MANAUS-AM", "Amazonas"),
    ("SALVADOR-BA", "Bahia"), ("FORTALEZA-CE", "Ceará"), ("BRASILIA-DF", "Distrito Federal"),
    ("VITORIA-ES", "Espírito Santo"),
    ("GOIANIA-GO", "Goiás"), ("SAOLUIS-MA", "Maranhão"), ("BELOHORIZONTE-MG", "Minas Gerais"),
    ("CAMPOGRANDE-MS", "Mato Grosso do Sul"),
    ("CUIABA-MT", "Mato Grosso"), ("BELEM-PA", "Pará"), ("JOAOPESSOA-PB", "Paraíba"),
    ("RECIFE-PE", "Pernambuco"), ("TERESINA-PI", "Piauí"),
    ("CURITIBA-PR", "Paraná"), ("RIODEJANEIRO-RJ", "Rio de Janeiro"), ("NATAL-RN", "Rio Grande do Norte"),
    ("PORTOVELHO-RO", "Rondônia"),
    ("BOAVISTA-RR", "Roraima"), ("PORTOALEGRE-RS", "Rio Grande do Sul"), ("FLORIANOPOLIS-SC", "Santa Catarina"),
    ("ARACAJU-SE", "Sergipe"),
    ("SAOPAULO-SP", "São Paulo"), ("PALMAS-TO", "Tocantins"))

    pais = models.CharField(max_length=50, null=False, verbose_name="País", default="Brasil")
    estado = models.CharField(max_length=50, null=False, verbose_name="Estado", choices=ESTADO_CHOICES)
    instituicao = models.ForeignKey(Instituicao, verbose_name="Instituição")
    modalidade = models.CharField(max_length=50, null=False, verbose_name="Modalidade")
    programa = models.ForeignKey(Programa, verbose_name="Programa")
    vigencia = models.DateField(null=False, verbose_name="Vigência")
    descricao = models.CharField(max_length=150, null=False, verbose_name="Descrição")
    pesquisador = models.ForeignKey(Pesquisador, verbose_name="Pesquisador")
    edital = models.ForeignKey(Edital, verbose_name="Edital")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Bolsas"
        verbose_name = "Bolsa"

class Projeto(models.Model):

    ESTADO_CHOICES = (
    ("RIOBRANCO-AC", "Acre"), ("MACEIO-AL", "Alagoas"), ("MACAPA-AP", "Amapá"), ("MANAUS-AM", "Amazonas"),
    ("SALVADOR-BA", "Bahia"), ("FORTALEZA-CE", "Ceará"), ("BRASILIA-DF", "Distrito Federal"),
    ("VITORIA-ES", "Espírito Santo"),
    ("GOIANIA-GO", "Goiás"), ("SAOLUIS-MA", "Maranhão"), ("BELOHORIZONTE-MG", "Minas Gerais"),
    ("CAMPOGRANDE-MS", "Mato Grosso do Sul"),
    ("CUIABA-MT", "Mato Grosso"), ("BELEM-PA", "Pará"), ("JOAOPESSOA-PB", "Paraíba"),
    ("RECIFE-PE", "Pernambuco"), ("TERESINA-PI", "Piauí"),
    ("CURITIBA-PR", "Paraná"), ("RIODEJANEIRO-RJ", "Rio de Janeiro"), ("NATAL-RN", "Rio Grande do Norte"),
    ("PORTOVELHO-RO", "Rondônia"),
    ("BOAVISTA-RR", "Roraima"), ("PORTOALEGRE-RS", "Rio Grande do Sul"), ("FLORIANOPOLIS-SC", "Santa Catarina"),
    ("ARACAJU-SE", "Sergipe"),
    ("SAOPAULO-SP", "São Paulo"), ("PALMAS-TO", "Tocantins"))

    pais = models.CharField(max_length=50, null=False, verbose_name="País", default="Brasil")
    estado = models.CharField(max_length=50, null=False, verbose_name="Estado", choices=ESTADO_CHOICES)
    instituicao = models.ForeignKey(Instituicao, verbose_name="Instituição")
    titulo = models.CharField(max_length=200, null=False, verbose_name="Título")
    resumo = models.CharField(max_length=500, null=False, verbose_name="Resumo")
    vigencia = models.DateField(null=False, verbose_name="Vigência")
    valor = models.CharField(max_length=50, verbose_name="Valor")
    programa = models.ForeignKey(Programa, verbose_name="Programa")
    pesquisador = models.ForeignKey(Pesquisador, verbose_name="Pesquisador")
    edital = models.ForeignKey(Edital, verbose_name="Edital")


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Projetos"
        verbose_name = "Projeto"
        ordering = ['titulo']

class Publicacao(models.Model):
    MODALIDADE_CHOICES = (("artigo", "Artigo Científico"), ("livro", "Livro Impresso"), ("ebook", "E-book"))


    titulo = models.CharField(max_length=200, null=False, verbose_name="Título")
    modalidade = models.CharField(max_length=100, null=False, choices=MODALIDADE_CHOICES, verbose_name="Modalidade")
    area = models.CharField(max_length=200, null=False, verbose_name="Area do Conhecimento")
    pesquisador = models.ForeignKey(Pesquisador, verbose_name="Pesquisador")
    instituicao = models.ForeignKey(Instituicao, verbose_name="Instituição")
    edital = models.ForeignKey(Edital, verbose_name="Edital")


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Publicações"
        verbose_name = "Publicação"
        ordering = ['titulo']

class Evento(models.Model):

  #  ESTADO_CHOICES = (
  #  ("RIOBRANCO-AC", "Acre"), ("MACEIO-AL", "Alagoas"), ("MACAPA-AP", "Amapá"), ("MANAUS-AM", "Amazonas"),
  #  ("SALVADOR-BA", "Bahia"), ("FORTALEZA-CE", "Ceará"), ("BRASILIA-DF", "Distrito Federal"),
  #  ("VITORIA-ES", "Espírito Santo"),
  #  ("GOIANIA-GO", "Goiás"), ("SAOLUIS-MA", "Maranhão"), ("BELOHORIZONTE-MG", "Minas Gerais"),
  #  ("CAMPOGRANDE-MS", "Mato Grosso do Sul"),
  #  ("CUIABA-MT", "Mato Grosso"), ("BELEM-PA", "Pará"), ("JOAOPESSOA-PB", "Paraíba"),
  #  ("RECIFE-PE", "Pernambuco"), ("TERESINA-PI", "Piauí"),
  #  ("CURITIBA-PR", "Paraná"), ("RIODEJANEIRO-RJ", "Rio de Janeiro"), ("NATAL-RN", "Rio Grande do Norte"),
  #  ("PORTOVELHO-RO", "Rondônia"),
  #  ("BOAVISTA-RR", "Roraima"), ("PORTOALEGRE-RS", "Rio Grande do Sul"), ("FLORIANOPOLIS-SC", "Santa Catarina"),
  #  ("ARACAJU-SE", "Sergipe"),
  #  ("SAOPAULO-SP", "São Paulo"), ("PALMAS-TO", "Tocantins"))


    ESTADO_CHOICES = (
      ("ACAUA-PI", "Acauã"),("AGRICOLANDIA-PI", "Agricolandia"),("AGUABRANCA-PI", "Água Branca"),
      ("ALAGOINHADOPIAUI-PI", "Alagoinha do Piauí"), ("ALEGRETEDOPIAUI-PI", "Alegrete do Piauí"), ("ALTOLONGA-PI", "Alto Longá"),
      ("ALTOS-PI", "Altos"), ("ALVORADADOGURGUEIA-PI", "Alvorada do Gurguéia"), ("AMARANTE-PI", "Amarante"),
      ("ANGICALDOPIAUI-PI", "Angical do Piauí"), ("ANISIODEABREU-PI", "Anisio de Abreu"), ("ANTONIOALMEIDA-PI", "Antônio Almeida"),
      ("AROAZES-PI", "Aroazes"), ("ARRAIAL-PI", "Arraial"), ("ASSUNCAODOPIAUI-PI", "Assunção do Piauí"),
      ("AVELINOLOPES-PI", "Avelino Lopes"), ("BAIXAGRANDEDORIBEIRO-PI", "Baixa Grande do Ribeiro"), ("BARRAD'ALCANTARA-PI", "Barra D'Alcantara"),
      ("BARRAS-PI", "Barras"), ("BARREIRAS DO PIAUI - PI", "Barreiras do Piauí"), ("BARRODURO-PI", "Barro Duro"),
      ("BATALHA-PI", "Batalha"), ("BELAVISTADOPIAUI-PI", "Bela Vista do Piauí"), ("BELEMDOPIAUI-PI", "Belém do Piauí"),
      ("BENEDITINOS-PI", "Beneditinos"), ("BERTOLINIA-PI", "Bertolinia"), ("BETANIADOPIAUI-PI","Betânia do Piauí"),
      ("BOAHORA-PI", "Boa Hora"), ("BOCAINA-PI", "Bocaína"), ("BOMJESUS-PI", "Bom Jesus"),
      ("BOMPRINCIPIODOPIAUI-PI", "Bom Princípio do Piauí"), ("BONFIMDOPIAUI-PI", "Bonfim do Piauí"), ("BOQUEIRAODOPIAUI-PI", "Boqueirão do Piauí"),
      ("BRASILEIRA-PI", "Brasileira"), ("BREJODOPIAUI-PI", "Brejo do Piauí"), ("BURITIDOSLOPES-PI", "Buriti dos Lopes"),
      ("BURITIDOSMONTES-PI", "Buriti dos Montes"), ("CABECEIRASDOPIAUI-PI", "Cabeceiras do Piauí"), ("CAJAZEIRASDOPIAUI-PI", "Cajazeoras do Piauí"),
      ("CAJUEIRODAPRAIA-PI", "Cajueiro da Praia"), ("CALDEIRAOGRANDEDOPIAUI-PI", "Caldeirão Grande do Piauí"), ("CAMPINASDOPIAUI-PI", "Campinas do Piauí"),
      ("CAMPOALEGREDOFIDALGO-PI", "Campo Alegre do Fidalgo"), ("CAMPOGRANDEDOPIAUI-PI", "Campo Grande do Piauí"), ("CAMPOLARGODOPIAUI-PI", "Campo Largo do Piauí"),
      ("CAMPOMAIOR-PI", "Campo Maior"), ("CANAVIEIRA-PI", "Canavieira"), ("CANTODOBURITI-PI", "Canto do Buriti"),
      ("CAPITAODECAMPOS-PI", "Capitão de Campos"), ("CAPITAOGERVASIOOLIVEIRA-PI", "Capitão Gervásio Oliveira"), ("CARACOL-PI", "Caracol"),
      ("CARAUBASDOPIAUI-PI", "Caraubas do Piauí"), ("CARIDADEDOPIAUI-PI", "Caridade do Piauí"), ("CASTELODOPIAUI-PI","Castelo do Piauí"),
      ("CAXINGO-PI", "Caxingó"), ("COCAL-PI", "Cocal"), ("COCALDETELHA-PI", "Cocal de Telha"), ("COCALDOSALVES-PI", "Cocal dos Alves"),
      ("COIVARAS-PI", "Coivaras"), ("COLONIADOGURGUEIA-PI", "Colônia do Gurguéia"), ("COLONIADOPIAUI-PI", "Colônia do Piauí"),
      ("CONCEICAODOCANINDE-PI", "Conceição do Canidé"), ("CORONELJOSEDIAS-PI", "Coronel José Dias"), ("CORRENTE - PI", "Corrente"),
      ("CRISTALANDIADOPIAUI-PI", "Cristalandia do Piauí"), ("CRISTINOCASTRO-PI", "Cristino Castro"), ("CURIMATA-PI", "Curimata"),
      ("CURRAIS-PI", "Currais"), ("CURRALNOVODOPIAUI-PI", "Curral Novo do Piauí"), ("CURRALINHOS-PI", "Curralinhos"),
      ("DEMERVALLOBAO-PI", "Demerval Lobão"), ("DIRCEUARCOVERDE-PI", "Dirceu Arcoverde"), ("DOMEXPEDITOLOPES-PI", "Dom Expedito Lopes"),
      ("DOMINOCENCIO-PI", "Domino Cencio"), ("DOMINGOS MOURAO-PI", "Domingos Mourão"), ("ELESBAOVELOSO-PI", "Elesbão Veloso"),
      ("ELISEUMARTINS-PI", "Eliseu Martins"), ("ESPERANTINA-PI", "Esperantina"), ("FARTURADOPIAUI-PI", "Fartura do Piauí"),
      ("FLORESDOPIAUI-PI", "Flores do Piauí"), ("FLORESTADOPIAUI-PI", "Floresta do Piauí"), ("FLORIANO-PI", "Floriano"),
      ("FRANCINOPOLIS-PI", "Francinopolis"), ("FRANCISCOAYRES-PI", "Francisco Ayres"), ("FRANCISCOMACEDO-PI", "Francisco Macedo"),
      ("FRANCISCOSANTOS-PI", "Francisco Santos"), ("FRONTEIRAS-PI","Fronteiras"), ("GEMINIANO-PI", "Germiniano"),
      ("GILBUES-PI", "Gilbues"), ("GUADALUPE-PI", "Guadalupe"), ("GUARIBAS-PI", "Guaribas"),
      ("HUGONAPOLEAO-PI", "Hugo Napoleão"), ("ILHAGRANDE-PI", "Ilha Grande"),("INHUMA-PI", "Inhuma"),
      ("IPIRANGADOPIAUI-PI", "Ipiranga do Piauí"), ("ISAIASCOELHO-PI", "Isaías Coelho"), ("ITAINOPOLIS-PI", "Itainopolis"),
      ("ITAUEIRA-PI", "Itaueira"), ("JACOBINADOPIAUI-PI", "Jacobina do Piauí"), ("JAICOS-PI", "Jaicós"),
      ("JARDIMDOMULATO-PI", "Jardim do Mulato"), ("JATOBADOPIAUI-PI", "Jatoba do Piauí"), ("JERUMENHA-PI", "Jerumenha"),
      ("JOAOCOSTA-PI", "João Costa"), ("JOAQUIMPIRES- PI", "Joaquim Pires"), ("JOCAMARQUES-PI", "Joca Marques"),
      ("JOSEDEFREITAS-PI", "José de Freitas"), ("JUAZEIRODOPIAUI-PI", "Juazeiro do Piauí"), ("JULIOBORGES-PI", "Julio Borges"),
      ("JUREMA-PI", "Jurema"), ("LAGOAALEGRE-PI", "Lagoa Alegre"), ("LAGOADESAOFRANCISCO-PI", "Lagoa de São Francisco"),
      ("LAGOADOBARRODOPIAUI-PI", "Lagoa do Barro do Piauí"), ("LAGOADOPIAUI-PI", "Lagoa do Piauí"), ("LAGOADOSITIO-PI", "Lagoa do Sítio"),
      ("LAGOINHADOPIAUI-PI", "Lagoinha do Piauí"), ("LANDRISALES-PI", "Landri Sales"), ("LUISCORREIA-PI", "Luis Correia"),
      ("LUZILANDIA-PI", "Luzilandia"), ("MADEIRO-PI", "Madeiro"), ("MANOELEMIDIO-PI", "Manoel Emídio"),
      ("MARCOLANDIA-PI", "Marcolandia"), ("MARCOSPARENTE-PI", "Marcos Parente"), ("MASSAPEDOPIAUI-PI", "Massapê do Piauí"),
      ("MATIASOLIMPIO-PI", "Matias Olimpio"), ("MIGUELALVES-PI", "Miguel Alves"), ("MIGUELLEAO-PI", "Miguel Leão"),
      ("MILTONBRANDAO-PI", "Milton Brandão"), ("MONSENHORGIL-PI", "Monsenhor Gil"), ("MONSENHORHIPOLITO-PI", "Monsenhor Hipólito"),
      ("MONTEALEGREDOPIAUI-PI", "Monte Alegre do Piauí"), ("MORROCABECANOTEMPO-PI", "Morro Cabeça no Tempo"), ("MORRODOCHAPEUDOPIAUI-PI", "Morro do Chapeu do Piauí"),
      ("MURICIDOSPORTELAS-PI", "Murici dos Portelas"), ("NAZAREDOPIAUI-PI", "Nazaré do Piauí"), ("NOSSASENHORADENAZARE-PI", "Nossa Senhora de Nazaré"),
      ("NOSSASENHORADOSREMEDIOS-PI", "Nossa Senhora dos Remédios"), ("NOVOORIENTEDOPIAUI-PI", "Novo Oriente do Piauí"), ("NOVOSANTOANTONIO-PI", "Novo Antônio"),
      ("OEIRAS-PI", "Oeiras"), ("OLHOD'AGUADOPIAUI-PI", "Olho D'Agua do Piauí"), ("PAESLANDIM-PI", "Pães Landim"),
      ("PAJEUDOPIAUI-PI", "Pajeu do Piauí"), ("PALMEIRADOPIAUI-PI", "Palmeira do Piauí"), ("PALMEIRAIS-PI", "Palmeirais"),
      ("PAQUETA-PI", "Paquetá"), ("PARNAGUA-PI", "Parnaguá"), ("PARNAIBA-PI", "Parnaíba"),
      ("PASSAGEMFRANCADOPIAUI-PI", "Passagem Franca do Piauí"), ("PATOSDOPIAUI-PI", "Patos do Piauí"), ("PAULISTANA-PI", "Paulistana"),
      ("PAVUSSU-PI", "Pavussu"), ("PEDROII-PI", "Pedro II"), ("PEDROLAURENTINO-PI", "Pedro Laurentino"),
      ("PETRONIOPORTELA-PI", "Petronio Portela"), ("PICOS-PI", "Picos"), ("PIMENTEIRAS-PI", "Pimenteiras"),
      ("PIOIX-PI", "Pio IX"), ("PIRACURUCA-PI", "Piracuruca"), ("PIRIPIRI-PI", "Piripiri"),
      ("PORTO-PI", "Porto"), ("PORTOALEGREDOPIAUI-PI", "Porto Alegre do Piauí"), ("PRATADOPIAUI-PI", "Prata do Piauí"),
      ("QUEIMADANOVA-PI", "Queimada Nova"), ("REDENCAODOGURGUEIA-PI", "Redenção do Gurguéia"), ("REGENERACAO-PI", "Regeneração"),
      ("RIACHOFRIO-PI", "Riacho Frio"), ("RIBEIRADOPIAUI-PI", "Ribeira do Piauí"), ("RIBEIROGONCALVES-PI", "Ribeiro Gonçalves"),
      ("RIOGRANDEDOPIAUI-PI", "Rio Grande do Piauí"), ("SANTACRUZDOPIAUI-PI", "Santa Cruz do Piauí"), ("SANTACRUZDOSMILAGRES-PI", "Santa Cruz dos Milagres"),
      ("SANTAFILOMENA-PI", "Santa Filomena"), ("SANTALUZ-PI", "Santa Luz"), ("SANTAROSADOPIAUI-PI", "Santa Rosa do Piauí"),
      ("SANTANADOPIAUI-PI", "Santana do Piauí"), ("SANTOANTONIODELISBOA-PI", "Santo Antônio de Lisboa"), ("SANTOANTONIODOSMILAGRES-PI", "Santo Antonio dos Milagres"),
      ("SANTOINACIODOPIAUI-PI", "Santo Inácio do Piauí"), ("SAOBRAZDOPIAUI-PI", "São Braz do Piauí"), ("SAOFELIXDOPIAUI-PI", "São Feliz do Piauí"),
      ("SAOFRANCISCODEASSISDOPIAUI-PI", "São Francisco de Assis do Piauí"), ("SAOFRANCISCODOPIAUI-PI", "São Francisco do Piauí"), ("SAOGONCALODOGURGUEIA-PI", "São Gonçalo do Gurguéia"),
      ("SAOGONCALODOPIAUI-PI", "São Gonçalo do Piauí"), ("SAOJOAODACANABRAVA-PI", "São João da Canabrava"), ("SAOJOAODAFRONTEIRA-PI", "São João da Fronteira"),
      ("SAOJOAODASERRA-PI", "São João da Serra"), ("SAOJOAODAVARJOTA-PI", "São João da Varjota"), ("SAOJOAODOARRAIAL-PI", "São João do Arraial"),
      ("SAOJOAODOPIAUI-PI", "São João do Piauí"), ("SAOJOSEDODIVINO-PI", "São José do Divino"), ("SAOJOSEDOPEIXE-PI", "São José do Peixe"),
      ("SAOJOSEDOPIAUI-PI", "São José do Piauí"), ("SAOJULIAO-PI", "São Julião"), ("SAOLOURENCODOPIAUI-PI", "São Lourenço do Piauí"),
      ("SAOLUISDOPIAUI-PI", "São Luís do Piauí"), ("SAOMIGUELDABAIXAGRANDE-PI", "São Miguel da Baixa Grande"), ("SAOMIGUELDOFIDALGO-PI", "São Miguel do Figalgo"),
      ("SAOMIGUELDOTAPUIO-PI", "São Miguel do Tapuio"), ("SAOPEDRODOPIAUI-PI", "São Pedro do Piauí"), ("SAORAIMUNDONONATO-PI", "São Raimundo Nonato"),
      ("SEBASTIAOBARROS-PI", "Sebastião Barros"), ("SEBASTIAOLEAL-PI", "Sebastião Leal"), ("SIGEFREDOPACHECO-PI", "Sigefredo Pacheco"),
      ("SIMOES-PI", "Simões"), ("SIMPLICIOMENDES-PI", "Simplicio Mendes"), ("SOCORRODOPIAUI-PI", "Socorro do Piauí"),
      ("SUSSUAPARA-PI", "Sussuapara"), ("TAMBORILDOPIAUI-PI", "Tamboril do Piauí"), ("TANQUEDOPIAUI-PI", "Tanque do Piauí"),
      ("TERESINA-PI", "Teresina"), ("UNIAO-PI", "União"), ("URUCUI-PI", "Uruçui"),
      ("VALENCADOPIAUI-PI", "Valença do Piauí"), ("VARZEABRANCA-PI", "Varzea Branca"), ("VARZEAGRANDE-PI", "Varzea Grande"),
      ("VERAMENDES-PI", "Vera Mendes"), ("VILANOVADOPIAUI-PI", "Vila Nova do Piauí"), ("WALLFERRAZ-PI", "Wall Ferraz"))

    TIPO_CHOICES = (("participacao", "Participação de Eventos"), ("organizacao", "Organização de Eventos"))

    titulo = models.CharField(max_length=200, null=False, verbose_name="Título")
    tipo = models.CharField(max_length=100, null=False, verbose_name="Tipo de Aplicação", choices=TIPO_CHOICES)
    area = models.CharField(max_length=200, null=False, verbose_name="Area do Conhecimento")
    pais = models.CharField(max_length=50, null=False, verbose_name="País", default="Brasil")
    estado = models.CharField(max_length=200, null=False, verbose_name="Estado", choices=ESTADO_CHOICES)
    data = models.DateField(null=False, verbose_name="Vigência")
    pesquisador = models.ForeignKey(Pesquisador, verbose_name="Pesquisador")
    edital = models.ForeignKey(Edital, verbose_name="Edital")


    def __str__(self):
      return self.titulo

    class Meta:
      verbose_name_plural = "Eventos"
      verbose_name = "Evento"

