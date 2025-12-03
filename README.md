README-CANDIDATO: E-Commerce API (Django REST Framework)
Este documento detalha o desenvolvimento da API de E-Commerce (Produtos e Categorias) em Django REST Framework, focando nas decisões de engenharia, instruções de uso e pontos de melhoria, conforme as instruções do desafio.

Seção 1: Instruções para Rodar
O projeto usa Python 3.8+ e SQLite. Não são necessárias variáveis de ambiente específicas para rodar localmente.

Instalação de Dependências
Primeiro, clone o repositório e crie/ative um ambiente virtual:

Bash

# Exemplo
# git clone URL_DO_REPO
# cd nome_do_projeto
python -m venv venv
source venv/bin/activate 
Instale o Django e o Django REST Framework:

Bash

pip install django djangorestframework
Como Rodar o Projeto
Aplicação de Migrações:

Bash

python manage.py migrate
Inicialização do Servidor:

Bash

python manage.py runserver
A API estará acessível em: http://127.0.0.1:8000/api/

Seção 2: Decisões de Design
Qual foi a maior dificuldade que você encontrou e como superou?
A principal dificuldade foi ao me deparar com algumas funções as quais não tinha familiaridade.
Para superar esse desafio fiz uso da documentação do django e python, sinto que fiz um bom trabalho levando em conta as dificuldades.

O que você não teve tempo de fazer (dentro do timebox) e como você faria se tivesse mais tempo?
O recurso que não foi implementado é a Autenticação e Permissões (Segurança) e as funcionalidades bônus.

Como Faria: Implementaria Django Simple JWT para gerenciar a autenticação via tokens. Em seguida, definiria classes de permissão no views.py (ex: permission_classes = [IsAdminUser]) para garantir que apenas usuários autenticados e administradores possam realizar operações de modificação (POST, PUT, DELETE).


