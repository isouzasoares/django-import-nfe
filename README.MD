# django-import-nfe
Importação de xmls de notas fiscais eletrônicas de um diretório para uma base de dados.
=============

### Instalação do projeto:
```
pip install -r requirements.txt
python manage.py syncdb
python manage.py migrate --all
python manage.py runserver
``` 

## Importar Nfes
```
Para importar os dados dos xmls das notas para o sistema, basta rodar o seguinte comando
 python manage.py addnfe '/home/user/dir_xmls_nfes'
``` 

## Implementações a serem feitas
'''
  Modelagem de endereços com vinculos para clientes e fornecedores
  Adição de relatórios
'''
