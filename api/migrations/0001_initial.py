# Generated by Django 3.1 on 2020-08-31 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Educacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('inicio', models.CharField(max_length=50)),
                ('fim', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('inicio', models.CharField(max_length=50)),
                ('fim', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('icone', models.CharField(max_length=20, verbose_name='Classe de ícone do DevIcon')),
                ('nivel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ParagrafoDescricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragrafo', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='RedeSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('icone', models.CharField(max_length=20, verbose_name='Classe de ícone do FontAwesome')),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
                ('lattes', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProjetoEducacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('descricao', models.CharField(max_length=500)),
                ('instituicao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.educacao')),
            ],
        ),
    ]
