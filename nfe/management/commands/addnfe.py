# -*- coding: utf-8 -*-
import xmltodict
import os

from nfe.models import Client, Provider, Product, Order

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = '<name...>'
    help = u'Adiciona nfe a partir de um diretorio'

    def get_provider(self, doc):
        """
        """
        doc = doc['NFe']['infNFe']['emit']
        data = {}

        data['name'] = doc['xNome']
        if doc.get('CNPJ', ''):
            data['cnpj'] = doc['CNPJ']
        if doc.get('CPF', ''):
            data['cpf'] = doc['CPF']
        if doc.get('xFant', ''):
            data['name_fant'] = doc['xFant']
        if doc.get('IM', ''):
            data['im'] = doc['IM']
        if doc.get('CNAE', ''):
            data['cnae'] = doc['CNAE']
        if doc.get('IE', ''):
            data['ie'] = doc['IE']
        if doc.get('IEST', ''):
            data['iest'] = doc['IEST']
        if doc.get('CRT', ''):
            data['crt'] = doc['CRT']

        return data

    def get_client(self, doc):
        """
        """
        doc = doc['NFe']['infNFe']['dest']
        data = {}
        data['name'] = doc['xNome']
        if doc.get('CNPJ', ''):
            data['cnpj'] = doc['CNPJ']
        if doc.get('CPF', ''):
            data['cpf'] = doc['CPF']
        if doc.get('idEstrangeiro', ''):
            data['idestrangeiro'] = doc['idEstrangeiro']
        if doc.get('indIEDest', ''):
            data['indiedest'] = doc['indIEDest']
        if doc.get('IE_dest', ''):
            data['ie'] = doc['IE_dest']
        if doc.get('ISUF', ''):
            data['isuf'] = doc['ISUF']
        if doc.get('IM_dest', ''):
            data['im'] = doc['IM_dest']

        return data

    def handle(self, *args, **options):
        for filename in os.listdir(args[0]):
            with open(args[0] + filename) as fd:
                doc = xmltodict.parse(fd.read())
                prov = self.get_provider(doc)
                provider, new_provider = Provider.objects.get_or_create(
                    **prov)
                client = self.get_client(doc)
                client, new_client = Client.objects.get_or_create(
                    **client)
