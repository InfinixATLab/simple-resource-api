# Simple Resource API – Matheus Camargo

## Seção 1: Instruções para rodar

**Variáveis de ambiente**
- `DJANGO_SECRET_KEY` (opcional): mantive um valor de desenvolvimento no `settings.py` para facilitar a avaliação, mas recomendo definir este segredo via variáveis de ambiente ao rodar em produção.
- `DEBUG` (opcional, default `True`): defina como `False` em ambientes públicos.

**Instalação de dependências**
1. Crie um ambiente virtual: `python -m venv venv` e ative-o.
   - Linux/macOS: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
2. Instale dependências: `pip install -r requirements.txt`.
3. Aplique migrações: `python manage.py migrate`.
4. (Opcional) Crie um superusuário para acessar o Django Admin: `python manage.py createsuperuser`.

**Como rodar o projeto**
1. Execute os testes para garantir que tudo está funcionando: `python manage.py test`.
2. Inicie o servidor: `python manage.py runserver`.
3. Endpoints úteis:
   - **Swagger UI (Documentação)**: `http://127.0.0.1:8000/` (Redirecionamento automático da raiz)
   - Redoc: `http://127.0.0.1:8000/redoc/`
   - API Categories: `http://127.0.0.1:8000/api/categories/`
   - API Products: `http://127.0.0.1:8000/api/products/`

## Seção 2: Decisões de design
- **Pré-desafio**: o primeiro passo foi reservar um tempo para ler a documentação oficial (Django Core e DRF) e me guiar por ela antes mesmo de iniciar o código.

- **Adaptação de stack**: vindo de uma base sólida em Java/Spring Boot, meu desafio foi traduzir conceitos de arquitetura para o "jeito Django" dentro do timebox. Foquei em construir o essencial com `ModelViewSets` e `Routers` para manter o código limpo e idiomático (Pythonico), preservando boas práticas de orientação a objetos.

- **Estratégia de estudo**: para otimizar o tempo, evitei consultas aleatórias. Escrevi snippets no VS Code para models/serializers/views, servindo como “templates”, e alimentei um Notion com anotações curtas. Para complementar esse estudo teórico, consumi conteúdos práticos de referência, replicando implementações para acelerar com a sintaxe e os padrões do Django.

- **Serializador de Product**: a exigência de retornar o nome da categoria demandou uma pesquisa específica na documentação. Resolvi de forma otimizada com `category_name = serializers.CharField(source='category.name', read_only=True)`, reaproveitando o relacionamento já carregado pelo ORM.

- **O que não deu tempo**: o maior desafio foi o gerenciamento de tempo para os bônus de infraestrutura. Se tivesse mais horas, incluiria um `ImageField`, configuraria `django-storages` + `boto3` (AWS S3) e subiria um `docker-compose` com web e PostgreSQL, lendo variáveis de um `.env`.

## Seção 3: Link para Deploy (Bônus)
Não publiquei em um serviço externo. O projeto está configurado para rodar localmente via `runserver`, com todas as dependências listadas no `requirements.txt`.

## Seção final: Recomendações futuras
- **Segurança:** Implementar autenticação (JWT ou OAuth2) para proteger as rotas de escrita (POST/PUT/DELETE).
- **Infraestrutura:** Criar um `Dockerfile` e `docker-compose.yml` para facilitar o setup do ambiente.
- **Testes:** Expandir a suíte de testes para cobrir cenários de erro e validações de borda.

## Referências e Material de Estudo
Durante o desenvolvimento, utilizei as seguintes referências oficiais:
- **Django Core:** https://docs.djangoproject.com/
- **Django REST Framework:** https://www.django-rest-framework.org/