# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.


@python_2_unicode_compatible
class Provider(models.Model):

    cnpj = models.CharField(null=True, blank=True, max_length=40,
                            db_index=True)
    cpf = models.CharField(null=True, blank=True, max_length=40,
                           db_index=True)
    name = models.CharField(max_length=500)
    name_fant = models.CharField(null=True, blank=True, max_length=500)
    im = models.CharField(max_length=100, null=True, blank=True)
    cnae = models.CharField(max_length=100, null=True, blank=True)
    ie = models.CharField(max_length=100, null=True, blank=True)
    iest = models.CharField(max_length=100, null=True, blank=True)
    crt = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Client(models.Model):

    INDIEDESTCHOICES = (
        (1, u'Contribuinte ICMS'),
        (2, u'Contribuinte isento de Inscrição no cadastro de Contribuintes do'
            u'ICMS'),
        (9, u'Não Contribuinte, que pode ou não possuir Inscrição Estadual no'
            u'Cadastro de Contribuintes do ICMS'),)

    cnpj = models.CharField(null=True, blank=True, max_length=40,
                            db_index=True)
    cpf = models.CharField(null=True, blank=True, max_length=40,
                           db_index=True)
    idestrangeiro = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=500)
    indiedest = models.CharField(choices=INDIEDESTCHOICES, max_length=1,
                                 blank=True, null=True)
    ie = models.CharField(max_length=100, null=True, blank=True)
    isuf = models.CharField(max_length=100, null=True, blank=True)
    im = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Product(models.Model):

    cod = models.IntegerField()
    name = models.CharField(max_length=500)
    ncm = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Order(models.Model):

    INDPAGCHOICES = (
        (0, u'Pagamento à vista'),
        (1, u'Pagamento à prazo'),
        (2, u'Outros'),)

    TPNFCHOICES = (
        (0, u'Saída'),
        (1, u'Entrada'),)

    TPIMPCHOICES = (
        (1, u'Retrato'),
        (2, u'Paisagem'),
        (3, u'Simplificado'),
        (4, u'DANFE NFC-e'),
        (5, u'DANFE NFC-e em mensagem eletrônica'),)

    TPEMISCHOICES = (
        (1, u'Normal'),
        (2, u'Contingência FS'),
        (3, u'Contingência SCAN '),
        (4, u'Contingência DPEC '),
        (5, u'Contingência FS-DA'),
        (6, u'Contingência SVC-AN'),
        (7, u'Contingência SVC-RS'),
        (9, u'Contingência off-line da NFC-e'),)

    FINNFECHOICES = (
        (1, u'NF-e normal'),
        (2, u'NF-e complementar'),
        (3, u'NF-e de ajuste'),
        (4, u'Devolução/Retorno'),)

    TPAMBCHOICES = (
        (1, u'Homologação'),
        (2, u'Produção'),)

    IDDESTCHOICES = (
        (1, u'Operação interna;'),
        (2, u'Operação interestadual'),
        (3, u'Operação com exterior'),)

    INDFINALCHOICES = (
        (0, u'Não'),
        (1, u'Consumidor Final'),)

    INDPRESCHOICES = (
        (0, u'Não se aplica'),
        (1, u'Operação presencial'),
        (2, u'Operação não presencial, pela Internet'),
        (3, u'Operação não presencial, Teleatendimento'),
        (4, u'NFC-e em operação com entrega a domicílio'),
        (9, u'Operação não presencial, outros'),)

    uf_cod = models.IntegerField()
    cnf = models.IntegerField()
    natop = models.CharField(max_length=100, null=True, blank=True)
    indpag = models.CharField(choices=INDPAGCHOICES, max_length=1)
    mod = models.CharField(max_length=3)
    serie = models.IntegerField()
    nnf = models.IntegerField()
    dhemi = models.DateField()
    fusohorario = models.CharField(max_length=5, blank=True, null=True)
    dhsaient = models.DateField()
    hsaient = models.TimeField()
    tpnf = models.CharField(choices=TPNFCHOICES, max_length=1)
    iddest = models.CharField(choices=IDDESTCHOICES, max_length=1,
                              blank=True, null=True)
    cmunfg = models.IntegerField()
    tpimp = models.CharField(choices=TPIMPCHOICES, max_length=2)
    tpemis = models.CharField(choices=TPEMISCHOICES, max_length=2)
    finnfe = models.CharField(choices=FINNFECHOICES, max_length=2)
    indfinal = models.CharField(choices=INDFINALCHOICES, max_length=1,
                                blank=True, null=True)
    indpres = models.CharField(choices=INDPRESCHOICES, max_length=1,
                               blank=True, null=True)
    dhcont = models.DateTimeField(blank=True, null=True)
    xjust = models.CharField(blank=True, null=True, max_length=500)
    emailarquivos = models.CharField(blank=True, null=True, max_length=500)
    tpamb = models.CharField(choices=TPAMBCHOICES, max_length=1)

    def __str__(self):
        return self.cnf
