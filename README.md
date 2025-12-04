***

# Simple Resource API

API REST para gerenciamento de recursos/produtos, desenvolvida em Django e Django REST Framework, com suporte a Docker e documentação via Swagger.

***

## 1. Como rodar o projeto

### Variáveis de ambiente

Para desenvolvimento local, o projeto funciona com valores padrão, mas é recomendado configurar um arquivo `.env` na raiz:

```bash
# .env (desenvolvimento)
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
ALLOWED_HOSTS=localhost,127.0.0.1
```

Em produção, é fundamental definir uma `SECRET_KEY` segura e usar `DEBUG=False`, além de ajustar `ALLOWED_HOSTS` para o domínio correto.

### Instalação de dependências

#### Opção A: Com Docker (recomendado)

Todas as dependências já estão descritas no `Dockerfile` e orquestradas via `docker-compose`.

```bash
# Build dos containers
docker-compose build
```

#### Opção B: Manualmente (sem Docker)

```bash
# 1. Criar e ativar ambiente virtual
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

# 2. Instalar dependências
pip install -r requirements.txt
```

### Executando o projeto

#### Com Docker Compose (fluxo principal)

```bash
# 1. Subir os containers
docker-compose up -d

# 2. Executar migrações (caso não rodem automaticamente)
docker-compose exec web python manage.py migrate

# 3. Criar superusuário (opcional, para acessar o admin)
docker-compose exec web python manage.py createsuperuser
```

Acessos padrão:

- API base: http://localhost:8000/api/  
- Documentação Swagger: http://localhost:8000/api/docs/  
- Django Admin: http://localhost:8000/admin/  

Para parar os serviços:

```bash
docker-compose down
```

#### Sem Docker

```bash
# 1. Aplicar migrações
python manage.py migrate

# 2. Rodar o servidor de desenvolvimento
python manage.py runserver

# 3. Acessar em: http://localhost:8000
```

***

## 2. Decisões de design

### Dificuldades e soluções

A principal dificuldade foi implementar o bônus de upload de imagens para AWS S3 dentro do timebox de 4 horas.
O campo `ImageField` foi adicionado ao modelo `Product`, mas a configuração completa com S3 exigiu ajustes adicionais de credenciais, permissões e variáveis de ambiente além do escopo de tempo.

Diante disso, a decisão foi:

- Garantir uma implementação funcional localmente (armazenamento de mídia no filesystem).
- Manter a estrutura preparada para, em produção, apenas configurar as credenciais AWS e ajustar o backend de storage, seguindo boas práticas de separação entre código e configuração.

### O que faria com mais tempo

Com mais tempo, seriam priorizadas as seguintes melhorias na API:

- Paginação otimizada (por exemplo, cursor-based pagination) para grandes volumes de dados.
- Filtros avançados com `django-filter` (categoria, faixa de preço, nome, disponibilidade etc.).
- Cache com Redis para endpoints mais acessados, reduzindo carga no banco.
- Rate limiting para proteção contra abuso e melhoria de segurança/robustez da API.

***

## 3. Deploy / Execução com Docker (Bônus)

### Repositório

- Código-fonte: https://github.com/coder-marllon/simple-resource-api.git

### Método 1: Docker Compose

```bash
# 1. Clonar o repositório
git clone https://github.com/coder-marllon/simple-resource-api.git
cd simple-resource-api

# 2. Construir e subir os containers
docker-compose up --build

# 3. (Opcional) Rodar em segundo plano
docker-compose up -d --build
```

Acessos:

- API + Swagger: http://localhost:8000/api/docs/  
- Django Admin: http://localhost:8000/admin/  

### Método 2: Apenas Docker (sem docker-compose)

```bash
# 1. Construir a imagem
docker build -t simple-resource-api .

# 2. Executar o container
docker run -p 8000:8000 \
  -v $(pwd)/db.sqlite3:/app/db.sqlite3 \
  -v $(pwd)/media:/app/media \
  -e DEBUG=1 \
  simple-resource-api

# 3. Em outro terminal, aplicar migrações
docker exec -it <container_id> python manage.py migrate
```

***

## 4. Recomendações e melhorias

Algumas melhorias planejadas para evoluir o desafio:

- Adicionar paginação às listagens da API, evitando respostas muito grandes.
- Implementar filtros por categoria, faixa de preço e nome, facilitando buscas mais específicas.
- Incluir autenticação e permissões para diferenciar operações públicas e restritas.
- Adicionar testes automatizados (unitários e de integração) para garantir a qualidade da API.

O desafio é bem estruturado e permite demonstrar conhecimentos em Django, DRF, Docker e boas práticas de APIs REST, sendo uma ótima base para evolução do projeto.