# Generated by Django 5.1 on 2024-08-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financas', '0002_alter_balancete_options_alter_transacao_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='boleto',
            field=models.ImageField(blank=True, height_field='30', null=True, upload_to='', verbose_name='Foto do boleto da transação', width_field='10'),
        ),
    ]
