from django.db.models import ( Model, 
                               CharField, 
                               TextField, 
                               IntegerField, 
                               OneToOneField,
                               ForeignKey,
                               ImageField,
                               CASCADE )

class Sobre(Model):
    nome = CharField(max_length=50)
    sobrenome = CharField(max_length=50)
    cidade = CharField(max_length=50)
    telefone = CharField(max_length=20)
    lattes = CharField(max_length=255)

    def __str__(self):
        return f'Sobre {self.nome}'

    class Meta:
        verbose_name = 'informação'
        verbose_name_plural = 'sobre mim'

class ParagrafoDescricao(Model):
    paragrafo = TextField(max_length=1000)

    def __str__(self):
        return f'{self.paragrafo[0:20]}...'

    class Meta:
        verbose_name = 'paragrafo de descrição'
        verbose_name_plural = 'paragrafos de descrição'

class RedeSocial(Model):
    nome = CharField(max_length=50)
    icone = CharField(max_length=20, verbose_name='Classe de ícone do FontAwesome')
    link = CharField(max_length=200)

    def __str__(self):
        return f'{self.nome}: {self.link}'

    class Meta:
        verbose_name = 'rede social'
        verbose_name_plural = 'Redes sociais'

class Experiencia(Model):
    empresa = CharField(max_length=100)
    cargo = CharField(max_length=100)
    inicio = CharField(max_length=50)
    fim = CharField(max_length=50)
    descricao = TextField(max_length=1000)

    def __str__(self):
        return f'({self.inicio}-{self.fim}) {self.empresa} - {self.cargo}'

    class Meta:
        verbose_name = 'experiência profissional'
        verbose_name_plural = 'experiências'

class Educacao(Model):
    instituicao = CharField(max_length=100)
    titulo = CharField(max_length=100)
    inicio = CharField(max_length=50)
    fim = CharField(max_length=50)

    def __str__(self):
        return f'({self.inicio}-{self.fim}) {self.instituicao} - {self.titulo}'

    class Meta:
        verbose_name = 'educação'
        verbose_name_plural = 'formações'

class ProjetoEducacao(Model):
    instituicao = ForeignKey(Educacao, on_delete=CASCADE)
    titulo = CharField(max_length=100)
    ano = IntegerField()
    descricao = CharField(max_length=500)

    def __str__(self):
        return f'({self.ano}) {self.titulo} - {self.instituicao}'

    class Meta:
        verbose_name = 'projeto realizado durante formação'
        verbose_name_plural = 'projetos'

class Habilidade(Model):
    titulo = CharField(max_length=50)
    icone = CharField(max_length=20, verbose_name='Classe de ícone do DevIcon')
    descricao = TextField(default=None)

    def __str__(self):
        return f'{self.titulo}: {self.descricao[0:10]}...'

    class Meta:
        verbose_name = 'habilidade/tecnologia'
        verbose_name_plural = 'habilidades'

class Portfolio(Model):
    titulo = CharField(max_length=100)
    descricao = TextField()
    gif = ImageField(upload_to='portfolio')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'trabalho'
        verbose_name_plural = 'portfólio'
