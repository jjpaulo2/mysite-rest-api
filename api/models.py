from django.db.models import ( Model, 
                               CharField, 
                               TextField, 
                               IntegerField, 
                               OneToOneField, 
                               ImageField,
                               CASCADE )

class Sobre(Model):
    nome = CharField(max_length=50)
    sobrenome = CharField(max_length=50)
    cidade = CharField(max_length=50)
    telefone = CharField(max_length=20)
    lattes = CharField(max_length=255)

class ParagrafoDescricao(Model):
    paragrafo = TextField(max_length=1000)

class RedeSocial(Model):
    nome = CharField(max_length=50)
    icone = CharField(max_length=20, verbose_name='Classe de ícone do FontAwesome')
    link = CharField(max_length=200)

class Experiencia(Model):
    empresa = CharField(max_length=100)
    cargo = CharField(max_length=100)
    inicio = CharField(max_length=50)
    fim = CharField(max_length=50)
    descricao = TextField(max_length=1000)

class Educacao(Model):
    instituicao = CharField(max_length=100)
    titulo = CharField(max_length=100)
    inicio = CharField(max_length=50)
    fim = CharField(max_length=50)

class ProjetoEducacao(Model):
    instituicao = OneToOneField(Educacao, on_delete=CASCADE)
    titulo = CharField(max_length=100)
    ano = IntegerField()
    descricao = CharField(max_length=500)

class Habilidade(Model):
    titulo = CharField(max_length=50)
    icone = CharField(max_length=20, verbose_name='Classe de ícone do DevIcon')
    descricao = TextField(default=None)

class Portfolio(Model):
    titulo = CharField(max_length=100)
    descricao = TextField()
    gif = ImageField(upload_to='portfolio')
