# Desafio Simple Resource API - Wellington

## Seção 1: Instruções para rodar

Este projeto utiliza Python, Django e Django Rest Framework.

### Pré-requisitos
* Python 3.10+ instalado
* Git instalado

### Instalação

1. Clone o repositório e entre na pasta:
   ```bash
   git clone <SEU_LINK_DO_GITHUB_AQUI>
   cd simple-resource-api


2. Crie e ative o ambiente virtual:
# Windows
python -m venv venv
.\venv\Scripts\activate

 3. Instale as dependências:

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Instale as dependências:


pip install -r requirements.txt
Prepare o banco de dados:

4. Prepare o banco de dados:

python manage.py migrate
python manage.py createsuperuser # (Opcional: para acessar o admin)
Rode os testes automatizados (para validar a aplicação):

5. Rode os testes automatizados (para validar a aplicação):

python manage.py test
Inicie o servidor:

6. Inicie o servidor:

python manage.py runserver


🔗 Acesso
API (Swagger/Documentação): https://www.google.com/search?q=http://127.0.0.1:8000/api/docs/

Painel Admin: https://www.google.com/search?q=http://127.0.0.1:8000/admin/

API Root: https://www.google.com/search?q=http://127.0.0.1:8000/api/


Decisões Técnicas
Estrutura: Mantive a estrutura padrão do Django (store_api como config e api como app) para facilitar a leitura por outros desenvolvedores.

Modelagem: Utilizei DecimalField para o preço (precisão financeira) e on_delete=models.PROTECT na Categoria para garantir integridade referencial.

API: Utilizei ViewSets e Routers do DRF para garantir uma implementação RESTful padrão e produtiva.

Dificuldades e Superações
Como minha stack principal é Java, meu maior desafio foi a adaptação rápida à sintaxe e ao ecossistema do Python dentro do timebox.

Swagger (Superação): Consegui implementar a documentação automática (drf-spectacular) como bônus, facilitando o teste da API.

Deploy (Decisão): Tentei realizar o deploy no Render, mas encontrei dificuldades com a configuração do ambiente em Python num curto espaço de tempo. Optei estrategicamente por priorizar a qualidade do código local e a cobertura de testes (que estão 100% funcionais) em vez de entregar um deploy instável.

O que faria com mais tempo
Com mais tempo de estudo na linguagem Python, implementaria:

Docker: Para containerizar a aplicação e resolver as questões de ambiente.

Deploy: Finalizaria a configuração do Gunicorn/Postgres no Render.