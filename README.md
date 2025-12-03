# Desafio Simple Resource API - Wellington

## Seção 1: Instruções para rodar

Este projeto utiliza Python, Django e Django Rest Framework.

### Pré-requisitos
* Python 3.8+ instalado
* Git instalado

### Instalação

1. Clone o repositório e entre na pasta:
   ```bash
   git clone <SEU_LINK_DO_GITHUB_AQUI>
   cd simple-resource-api

2. Crie o ambiente virtual
   # Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

3. Instale as dependências:

pip install django djangorestframework

4. Prepare o banco de dados:

python manage.py migrate
python manage.py createsuperuser # (Opcional: para acessar o admin)

5. Rode os testes automatizados (para validar a aplicação):

python manage.py test

6. Inicie o servidor:

python manage.py runserver

Acesse a API em: https://www.google.com/search?q=http://127.0.0.1:8000/api/

PARABÉNS, WELLINGTON! 🏆

Aquele OK ali no final significa que você concluiu 100% dos Requisitos Essenciais do desafio.

✅ Banco de Dados criado e protegido.

✅ Admin configurado.

✅ API retornando os dados certos (com o nome da categoria).

✅ Testes automatizados passando.

Agora vamos para a Rubrica 3 (Processo e Comunicação). Para tirar nota máxima, você precisa entregar o código organizado e com a documentação que eles pediram.

Siga estes 3 passos finais para fechar com chave de ouro:

Passo 1: Salvar e Finalizar a Feature
Como os testes passaram, seu código está seguro. Vamos salvar na sua branch.

Bash

git add .
git commit -m "feat: finaliza serializers e garante testes passando"
Passo 2: Juntar tudo na Principal (Merge)
Lembra que criamos uma branch separada? Agora vamos levar tudo para a main para "entregar" o projeto.

Bash

git checkout main
git merge feature/desenvolvimento-api
(Se tudo der certo, o código vai aparecer na branch main).

Passo 3: O Documento Final (README)
O enunciado pede explicitamente para preencher o arquivo README-CANDIDATO. Isso vale 25% da nota!

Vou te dar um modelo pronto e profissional baseado no que fizemos.

Crie (ou abra) o arquivo README-CANDIDATO.md na raiz do projeto.

Cole este texto nele:

Markdown

# Desafio Simple Resource API - Wellington

## Seção 1: Instruções para rodar

Este projeto utiliza Python, Django e Django Rest Framework.

### Pré-requisitos
* Python 3.8+ instalado
* Git instalado

### Instalação

1. Clone o repositório e entre na pasta:
   ```bash
   git clone <SEU_LINK_DO_GITHUB_AQUI>
   cd simple-resource-api
Crie e ative o ambiente virtual:

Bash

# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

Bash

pip install django djangorestframework
Prepare o banco de dados:

Bash

python manage.py migrate
python manage.py createsuperuser # (Opcional: para acessar o admin)
Rode os testes automatizados (para validar a aplicação):

Bash

python manage.py test
Inicie o servidor:

Bash

python manage.py runserver
Acesse a API em: https://www.google.com/search?q=http://127.0.0.1:8000/api/

Seção 2: Decisões de design
Decisões Técnicas:

Estrutura: Mantive a estrutura padrão do Django (store_api como config e api como app) para facilitar a leitura por outros desenvolvedores Django.

Modelagem: Utilize DecimalField para o preço visando precisão financeira e on_delete=models.PROTECT na Categoria para garantir a integridade referencial, impedindo que produtos fiquem órfãos.

API: Utilizei ViewSets e Routers do DRF para garantir uma implementação RESTful padrão e produtiva, focando na qualidade da entrega dentro do tempo estipulado.

Dificuldades e Superações: A principal atenção foi na configuração correta das rotas para que os testes automatizados (reverse) funcionassem corretamente, exigindo a configuração explícita do basename no roteador.

O que faria com mais tempo: Devido ao timebox de 4 horas, priorizei a qualidade dos Requisitos Essenciais (Testes e Código Limpo). Com mais tempo, implementaria:

Docker: Para facilitar ainda mais o setup.

Swagger: Para documentação visual da API.

Autenticação: JWT para proteger as rotas de escrita.

