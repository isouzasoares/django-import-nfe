# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(blank=True, db_index=True, max_length=40, null=True)),
                ('cpf', models.CharField(blank=True, db_index=True, max_length=40, null=True)),
                ('idestrangeiro', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=500)),
                ('indiedest', models.CharField(blank=True, choices=[(1, 'Contribuinte ICMS'), (2, 'Contribuinte isento de Inscri\xe7\xe3o no cadastro de Contribuintes doICMS'), (9, 'N\xe3o Contribuinte, que pode ou n\xe3o possuir Inscri\xe7\xe3o Estadual noCadastro de Contribuintes do ICMS')], max_length=1, null=True)),
                ('ie', models.CharField(blank=True, max_length=100, null=True)),
                ('isuf', models.CharField(blank=True, max_length=100, null=True)),
                ('im', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf_cod', models.IntegerField()),
                ('cnf', models.IntegerField()),
                ('natop', models.CharField(blank=True, max_length=100, null=True)),
                ('indpag', models.CharField(choices=[(0, 'Pagamento \xe0 vista'), (1, 'Pagamento \xe0 prazo'), (2, 'Outros')], max_length=1)),
                ('mod', models.CharField(max_length=3)),
                ('serie', models.IntegerField()),
                ('nnf', models.IntegerField()),
                ('dhemi', models.DateField()),
                ('fusohorario', models.CharField(blank=True, max_length=5, null=True)),
                ('dhsaient', models.DateField()),
                ('hsaient', models.TimeField()),
                ('tpnf', models.CharField(choices=[(0, 'Sa\xedda'), (1, 'Entrada')], max_length=1)),
                ('iddest', models.CharField(blank=True, choices=[(1, 'Opera\xe7\xe3o interna;'), (2, 'Opera\xe7\xe3o interestadual'), (3, 'Opera\xe7\xe3o com exterior')], max_length=1, null=True)),
                ('cmunfg', models.IntegerField()),
                ('tpimp', models.CharField(choices=[(1, 'Retrato'), (2, 'Paisagem'), (3, 'Simplificado'), (4, 'DANFE NFC-e'), (5, 'DANFE NFC-e em mensagem eletr\xf4nica')], max_length=2)),
                ('tpemis', models.CharField(choices=[(1, 'Normal'), (2, 'Conting\xeancia FS'), (3, 'Conting\xeancia SCAN '), (4, 'Conting\xeancia DPEC '), (5, 'Conting\xeancia FS-DA'), (6, 'Conting\xeancia SVC-AN'), (7, 'Conting\xeancia SVC-RS'), (9, 'Conting\xeancia off-line da NFC-e')], max_length=2)),
                ('finnfe', models.CharField(choices=[(1, 'NF-e normal'), (2, 'NF-e complementar'), (3, 'NF-e de ajuste'), (4, 'Devolu\xe7\xe3o/Retorno')], max_length=2)),
                ('indfinal', models.CharField(blank=True, choices=[(0, 'N\xe3o'), (1, 'Consumidor Final')], max_length=1, null=True)),
                ('indpres', models.CharField(blank=True, choices=[(0, 'N\xe3o se aplica'), (1, 'Opera\xe7\xe3o presencial'), (2, 'Opera\xe7\xe3o n\xe3o presencial, pela Internet'), (3, 'Opera\xe7\xe3o n\xe3o presencial, Teleatendimento'), (4, 'NFC-e em opera\xe7\xe3o com entrega a domic\xedlio'), (9, 'Opera\xe7\xe3o n\xe3o presencial, outros')], max_length=1, null=True)),
                ('dhcont', models.DateTimeField(blank=True, null=True)),
                ('xjust', models.CharField(blank=True, max_length=500, null=True)),
                ('emailarquivos', models.CharField(blank=True, max_length=500, null=True)),
                ('tpamb', models.CharField(choices=[(1, 'Homologa\xe7\xe3o'), (2, 'Produ\xe7\xe3o')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.IntegerField()),
                ('name', models.CharField(max_length=500)),
                ('ncm', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(blank=True, db_index=True, max_length=40, null=True)),
                ('cpf', models.CharField(blank=True, db_index=True, max_length=40, null=True)),
                ('name', models.CharField(max_length=500)),
                ('name_fant', models.CharField(blank=True, max_length=500, null=True)),
                ('im', models.CharField(blank=True, max_length=100, null=True)),
                ('cnae', models.CharField(blank=True, max_length=100, null=True)),
                ('ie', models.CharField(blank=True, max_length=100, null=True)),
                ('iest', models.CharField(blank=True, max_length=100, null=True)),
                ('crt', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
