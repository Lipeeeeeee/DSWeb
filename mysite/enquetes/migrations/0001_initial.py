# Generated by Django 4.0.6 on 2024-03-11 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=256)),
                ('data_pub', models.DateTimeField(verbose_name='Data de publicação')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=256)),
                ('votos', models.IntegerField(default=0, verbose_name='Quantidade de votos')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquetes.pergunta')),
            ],
        ),
    ]
