# Construção de formulários com Django

![Lincença do projeto](	https://img.shields.io/github/license/robsonleal/pedroreceitas)
![Bagde status desenvolvimento](https://img.shields.io/static/v1?label=status&message=CONCLUÍDO&color=green)

## Índice

* [Título](#Título)
* [Badges](#badges)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Acesso ao Projeto](#acesso-ao-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)

## Descrição do Projeto

Projeto com formulário que simulam a compra de uma passagem aérea;

O projeto foi criado com as funcionalidades do Django, sem escrever código HTML para criar os formulários.

## Funcionalidades e Demonstração da Aplicação
- `Funcionalidade 1`: Envio de dados com método POST e captura em outra página;
- `Funcionalidade 2`: Utilização de extendes ,include e laços de repetição no arquivo html para diminuir o tamanho dos arquivos e repetições de códigos;
- `Funcionalidade 3`: Exibição de mensagens de erro caso o usuário insira dados inválidos;
- `Funcionalidade 4`: Uso do date picker para exibir formulários personalizados com calendário;

Página de compra da passagem:
![Screenshot_20220206_113436](https://user-images.githubusercontent.com/27708175/152686047-d515bf62-94f0-4b8c-926b-5085ea58c6fc.png)

Página exibindo erro de preenchimento ao usuário:
![Screenshot_20220206_113558](https://user-images.githubusercontent.com/27708175/152686053-a0f93d10-bef4-4d73-9d9b-60dd5bac0dd3.png)

Página de captura das informações enviadas ao formulário:
![Screenshot_20220206_113656](https://user-images.githubusercontent.com/27708175/152686056-8f2d2f8c-032a-4ac7-87b8-c6e8aa3d6780.png)

## Acesso ao Projeto

```console
git clone git@github.com:robsonleal/django-formaularios.git
cd django-formularios
python -m venv ./venv
source /<caminho_até_o_projeto>/venv/bin/activate
pip install 'requirements.txt'
python manage.py runserver
```
- Abrir o endereço localhost:8000 no navegador de sua preferência

## Tecnologias utilizadas
`Django 4`
`Python 3`
