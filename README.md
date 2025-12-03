# Desafio Backend - Catálogo de Produtos API

## 🔗 Links do Projeto (Deploy)

A aplicação está hospedada e rodando no **Render**.

  - 📘 **Documentação Interativa (Swagger UI):**
    [https://simple-resource-api.onrender.com/api/docs/](https://simple-resource-api.onrender.com/api/docs/)
    *(Utilize esta interface para testar todos os endpoints e realizar upload de imagens).*

  - 🛡️ **Painel Administrativo:**
    [https://simple-resource-api.onrender.com/admin/](https://simple-resource-api.onrender.com/admin/)
    *user:admin senha:admin12345*


> **Nota:** Como o deploy utiliza o plano gratuito, a primeira requisição pode levar cerca de 50 segundos para "acordar" o servidor. Agradeço a paciência.

---

## 🛠 Seção 1: Como Rodar Localmente

Como já falado, o projeto está em deploy, mas se quiser executar localmente: 
O projeto segue estritamente a abordagem **"Docker First"**. Não é necessário configurar ambiente virtual, instalar Python ou PostgreSQL na sua máquina. O ambiente é 100% isolado e reprodutível.

### Pré-requisitos

  - **Docker** e **Docker Compose** instalados.
    > *Caso não tenha, consulte o guia oficial: [Get Docker](https://docs.docker.com/get-docker/)*

### Passo a Passo

1.  **Subir a infraestrutura:**
    Na raiz do projeto, execute:

    ```bash
    sudo docker-compose up -d --build
    ```

2.  **Aplicar Migrações e Setup Inicial:**
    Execute os comandos dentro do container para criar as tabelas no banco:

    ```bash
    sudo docker-compose exec web python manage.py makemigrations
    sudo docker-compose exec web python manage.py migrate
    ```

3.  **Criar Superusuário (Admin):**

    ```bash
    sudo docker-compose exec web python manage.py createsuperuser
    ```

4.  **Acessar:**

      - API Docs: `http://127.0.0.1:8000/api/docs/`
      - Admin: `http://127.0.0.1:8000/admin/`

-----

## 🧠 Seção 2: Decisões de Design e Arquitetura

### 1\. Infraestrutura e Dockerização

Adotei uma arquitetura de microsserviços via `docker-compose`, isolando a aplicação (`web`) e o banco de dados (`db`).

  - **Benefício:** Elimina o clássico problema de "na minha máquina funciona". 

### 2\. Django Rest Framework & Otimizações

  - **ViewSets & Routers:** Utilizei `ModelViewSet` para garantir a padronização das rotas RESTful.
  - **Paginação Global:** Configurei `PageNumberPagination` para evitar sobrecarga no banco de dados e na rede ao listar grandes volumes de dados.
  - **Serializer Híbrido:** `ProductSerializer` exibe o nome da categoria na leitura, facilitando o consumo pelo Frontend, mas mantém a performance na escrita aceitando apenas o ID.

### 3\. Documentação Avançada (Swagger)

A documentação foi gerada com `drf-spectacular` e **customizada manualmente**.

  - **Problema Resolvido:** O Swagger padrão não renderiza corretamente o botão de upload de arquivos.
  - **Solução:** Forcei o parser `MultiPartParser` na View e estendi o schema (`@extend_schema`) definindo o campo de imagem como `binary`. Isso permite testar o upload visualmente direto na documentação.

### 4\. Estratégia de Armazenamento (Storage)

Optei por configurar o `MEDIA_ROOT` para armazenamento local em vez de S3 neste momento.

  - **Justificativa:** Priorizei a facilidade de avaliação. Configurar S3 exigiria expor chaves AWS ou obrigar o avaliador a configurar credenciais.
  - **Visão de Futuro:** O código está pronto para receber `django-storages` e `boto3` para migrar para S3 ou MinIO com poucas linhas de configuração.

-----

## ✅ Seção 3: Qualidade de Código e Testes

A aplicação conta com uma suíte de testes automatizados.

Para rodar os testes:

```bash
sudo docker-compose exec web python manage.py test api -v 2
```

**Cenários Cobertos:**

  - **POST (Upload):** Validação completa de envio `multipart/form-data` com geração de imagem em memória.
  - **GET (Listagem):** Verificação da estrutura JSON, paginação e presença dos campos customizados (`category_name`).
  - **PATCH/PUT:** Garantia de atualização parcial de dados.
  - **DELETE:** Verificação de integridade e limpeza do banco (`204 No Content`).

---

## Seção 4: Recomendações

Se houvesse mais tempo, estas seriam as próximas implementações:

1.  **Segurança:** Implementar autenticação via **JWT**. Atualmente o Admin exige login, mas a API está aberta para facilitar os testes manuais conforme o escopo. A melhoria seria proteger as rotas de escrita, mantendo apenas o GET público.
2.  **Filtros Avançados:** Adicionar filtros mais complexos (ex: filtrar produtos por faixa de preço).
3. **CI/CD:** Configuraria um workflow de Integração Contínua
   - **Testes Automatizados:** Execução automática da suíte de testes a cada push.
   - **Build Verification:** Teste de build da imagem Docker para garantir que novas dependências não quebrem o container.