# Generated by Django 3.1 on 2021-01-07 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('gif', models.ImageField(upload_to='portfolio')),
            ],
        ),
        migrations.RemoveField(
            model_name='habilidade',
            name='nivel',
        ),
    ]
