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

    ESTADO_CHOICES = (("RIO BRANCO - AC", "Acre"), ("MACEIO - AL", "Alagoas"), ("MACAPA - AP", "Amapá"), ("MANAUS - AM", "Amazonas"),
    ("SALVADOR - BA", "Bahia"), ("FORTALEZA - CE", "Ceará"), ("BRASILIA - DF", "Distrito Federal"),
    ("VITORIA - ES", "Espírito Santo"),
    ("GOIANIA - GO", "Goiás"), ("SAO LUIS - MA", "Maranhão"), ("BELO HORIZONTE - MG", "Minas Gerais"),
    ("CAMPO GRANDE - MS", "Mato Grosso do Sul"),
    ("CUIABA - MT", "Mato Grosso"), ("BELEM - PA", "Pará"), ("JOAO PESSOA - PB", "Paraíba"),
    ("RECIFE - PE", "Pernambuco"), ("TERESINA - PI", "Piauí"),
    ("CURITIBA - PR", "Paraná"), ("RIO DE JANEIRO - RJ", "Rio de Janeiro"), ("NATAL - RN", "Rio Grande do Norte"),
    ("PORTO VELHO - RO", "Rondônia"),
    ("BOA VISTA - RR", "Roraima"), ("PORTO ALEGRE - RS", "Rio Grande do Sul"), ("FLORIANOPOLIS - SC", "Santa Catarina"),
    ("ARACAJU - SE", "Sergipe"),
    ("SAO PAULO - SP", "São Paulo"), ("PALMAS - TO", "Tocantins"))

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

    ESTADO_CHOICES = ( ("RIO BRANCO - AC", "Acre"), ("MACEIO - AL", "Alagoas"), ("MACAPA - AP", "Amapá"), ("MANAUS - AM", "Amazonas"),
    ("SALVADOR - BA", "Bahia"), ("FORTALEZA - CE", "Ceará"), ("BRASILIA - DF", "Distrito Federal"),
    ("VITORIA - ES", "Espírito Santo"),
    ("GOIANIA - GO", "Goiás"), ("SAO LUIS - MA", "Maranhão"), ("BELO HORIZONTE - MG", "Minas Gerais"),
    ("CAMPO GRANDE - MS", "Mato Grosso do Sul"),
    ("CUIABA - MT", "Mato Grosso"), ("BELEM - PA", "Pará"), ("JOAO PESSOA - PB", "Paraíba"),
    ("RECIFE - PE", "Pernambuco"), ("TERESINA - PI", "Piauí"),
    ("CURITIBA - PR", "Paraná"), ("RIO DE JANEIRO - RJ", "Rio de Janeiro"), ("NATAL - RN", "Rio Grande do Norte"),
    ("PORTO VELHO - RO", "Rondônia"),
    ("BOA VISTA - RR", "Roraima"), ("PORTO ALEGRE - RS", "Rio Grande do Sul"), ("FLORIANOPOLIS - SC", "Santa Catarina"),
    ("ARACAJU - SE", "Sergipe"),
    ("SAO PAULO - SP", "São Paulo"), ("PALMAS - TO", "Tocantins"))

    pais = models.CharField(max_length=50, null=False, verbose_name="País", default="Brasil")
    estado = models.CharField(max_length=50, null=False, verbose_name="Estado", choices=ESTADO_CHOICES)
    instituicao = models.ForeignKey(Instituicao, verbose_name="Instituição")
    modalidade = models.CharField(max_length=50, null=False, verbose_name="Modalidade")
    programa = models.ForeignKey(Programa, verbose_name="Programa")
    vigencia = models.DateField(null=False, verbose_name="Vigência")
    descricao = models.CharField(max_length=150, null=False, verbose_name="Descrição")
    pesquisador = models.ForeignKey(Pesquisador, verbose_name="Pesquisador")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Bolsas"
        verbose_name = "Bolsa"

class Projeto(models.Model):

    ESTADO_CHOICES = (("RIO BRANCO - AC", "Acre"), ("MACEIO - AL", "Alagoas"), ("MACAPA - AP", "Amapá"), ("MANAUS - AM", "Amazonas"),
    ("SALVADOR - BA", "Bahia"), ("FORTALEZA - CE", "Ceará"), ("BRASILIA - DF", "Distrito Federal"),
    ("VITORIA - ES", "Espírito Santo"),
    ("GOIANIA - GO", "Goiás"), ("SAO LUIS - MA", "Maranhão"), ("BELO HORIZONTE - MG", "Minas Gerais"),
    ("CAMPO GRANDE - MS", "Mato Grosso do Sul"),
    ("CUIABA - MT", "Mato Grosso"), ("BELEM - PA", "Pará"), ("JOAO PESSOA - PB", "Paraíba"),
    ("RECIFE - PE", "Pernambuco"), ("TERESINA - PI", "Piauí"),
    ("CURITIBA - PR", "Paraná"), ("RIO DE JANEIRO - RJ", "Rio de Janeiro"), ("NATAL - RN", "Rio Grande do Norte"),
    ("PORTO VELHO - RO", "Rondônia"),
    ("BOA VISTA - RR", "Roraima"), ("PORTO ALEGRE - RS", "Rio Grande do Sul"), ("FLORIANOPOLIS - SC", "Santa Catarina"),
    ("ARACAJU - SE", "Sergipe"),
    ("SAO PAULO - SP", "São Paulo"), ("PALMAS - TO", "Tocantins"))

    pais = models.CharField(max_length=50, null=False, verbose_name="País", default="Brasil")
    estado = models.CharField(max_length=50, null=False, verbose_name="Estado", choices=ESTADO_CHOICES)
    instituicao = models.ForeignKey(Instituicao, verbose_name="Instituição")
    titulo = models.CharField(max_length=200, null=False, verbose_name="Título")
    resumo = models.CharField(max_length=500, null=False, verbose_name="Resumo")
    vigencia = models.DateField(null=False, verbose_name="Vigência")
    valor = models.CharField(max_length=50, verbose_name="Valor")
    programa = models.ForeignKey(Programa, verbose_name="Programa")
    pesquisador = models.ForeignKey(Pesquisador, verbose_name="Pesquisador")

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
    #instituicao = models.ForeignKey(Instituicao, verbose_name="Instituição")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Publicações"
        verbose_name = "Publicação"
        ordering = ['titulo']

class Evento(models.Model):

    ESTADO_CHOICES = (("RIO BRANCO - AC", "Acre"), ("MACEIO - AL", "Alagoas"), ("MACAPA - AP", "Amapá"), ("MANAUS - AM", "Amazonas"),
        ("SALVADOR - BA", "Bahia"), ("FORTALEZA - CE", "Ceará"), ("BRASILIA - DF", "Distrito Federal"),
        ("VITORIA - ES", "Espírito Santo"),
        ("GOIANIA - GO", "Goiás"), ("SAO LUIS - MA", "Maranhão"), ("BELO HORIZONTE - MG", "Minas Gerais"),
        ("CAMPO GRANDE - MS", "Mato Grosso do Sul"),
        ("CUIABA - MT", "Mato Grosso"), ("BELEM - PA", "Pará"), ("JOAO PESSOA - PB", "Paraíba"),
        ("RECIFE - PE", "Pernambuco"), ("TERESINA - PI", "Piauí"),
        ("CURITIBA - PR", "Paraná"), ("RIO DE JANEIRO - RJ", "Rio de Janeiro"), ("NATAL - RN", "Rio Grande do Norte"),
        ("PORTO VELHO - RO", "Rondônia"),
        ("BOA VISTA - RR", "Roraima"), ("PORTO ALEGRE - RS", "Rio Grande do Sul"),
        ("FLORIANOPOLIS - SC", "Santa Catarina"),
        ("ARACAJU - SE", "Sergipe"),
        ("SAO PAULO - SP", "São Paulo"), ("PALMAS - TO", "Tocantins"))

    TIPO_CHOICES = (("participacao", "Participação de Eventos"), ("organizacao", "Organização de Eventos"))

    titulo = models.CharField(max_length=200, null=False, verbose_name="Título")
    tipo = models.CharField(max_length=100, null=False, verbose_name="Tipo de Aplicação", choices=TIPO_CHOICES)
    area = models.CharField(max_length=200, null=False, verbose_name="Area do Conhecimento")
    pais = models.CharField(max_length=50, null=False, verbose_name="País", default="Brasil")
    estado = models.CharField(max_length=50, null=False, verbose_name="Estado", choices=ESTADO_CHOICES)
    data = models.DateField(null=False, verbose_name="Vigência")
    pesquisador = models.ForeignKey(Pesquisador, verbose_name="Pesquisador")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Eventos"
        verbose_name = "Evento"
