# README - Candidato

## Seção 1: Instruções para rodar

### Variáveis de ambiente

Nenhuma variável de ambiente é necessária para rodar o projeto em desenvolvimento. O projeto utiliza SQLite como banco de dados padrão, que não requer configuração adicional.

### Instalação de dependências

```bash
# Navegue até a pasta do projeto
cd store_api

# Instale as dependências
pip install -r ../requirements.txt
```

### Como rodar o projeto

```bash
# Navegue até a pasta store_api
cd store_api

# Execute as migrações
python manage.py migrate

# Crie um superusuário (opcional, para acessar o admin)
python manage.py createsuperuser

# Inicie o servidor de desenvolvimento
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000/`

### Endpoints disponíveis

- **API Categories**: `http://127.0.0.1:8000/api/categories/`
- **API Products**: `http://127.0.0.1:8000/api/products/`
- **Admin**: `http://127.0.0.1:8000/admin/`
- **Busca de produtos**: `http://127.0.0.1:8000/api/products/search/?name=nome_do_produto`

---

## Seção 2: Decisões de design

### Maior dificuldade encontrada

A maior dificuldade foi implementar um sistema robusto de tratamento de erros personalizado. Para resolver isso, criei uma estrutura de exceções customizadas (`DuplicateResourceException`) e um handler global (`custom_exception_handler`) que formata as respostas de erro de forma consistente em toda a API. Isso permite que a API retorne mensagens claras e padronizadas, facilitando o consumo pelos clientes.

### Decisões técnicas implementadas

- **Validação de duplicatas**: Implementei validação no método `create` de ambos os ViewSets (Category e Product) para prevenir criação de recursos com nomes duplicados, retornando HTTP 409 (Conflict) com mensagem clara.

- **Paginação**: Configurei paginação padrão (10 itens por página) para melhorar performance em listagens grandes.

- **Busca de produtos**: Adicionei endpoint customizado `/api/products/search/` para busca por nome (case-insensitive).

- **Tratamento de exceções**: Sistema centralizado de tratamento de erros com respostas formatadas.

### O que não teve tempo de fazer

**Testes unitários**: Não implementei os testes solicitados (criação e listagem de produtos) pois ainda não me sinto com conhecimento sólido em testes com APITestCase do DRF.

Se tivesse mais tempo, estudaria a documentação oficial do DRF sobre testes e implementaria testes para:

- Criação de produto com dados válidos
- Criação de produto com nome duplicado (deve retornar 409)
- Listagem de produtos com paginação
- Busca de produtos por nome
- Validação de campos obrigatórios

---

## Seção 3: Link para Deploy (Bônus)

Não foi implementado deploy ou Docker. O projeto está configurado apenas para desenvolvimento local com SQLite.

---

## Seção final: Recomendações

### Melhorias que poderiam ser implementadas

1. **Testes automatizados**: Implementar suite completa de testes unitários e de integração para garantir qualidade e facilitar refatorações futuras.

2. **Validação no serializer**: Mover a validação de duplicatas para o serializer usando `validate_name()`, seguindo melhor as práticas do DRF.

3. **Documentação da API**: Implementar Swagger/OpenAPI para documentação automática dos endpoints.

4. **Banco de dados em produção**: Configurar PostgreSQL para produção, mantendo SQLite apenas para desenvolvimento.

5. **Índices no banco**: Adicionar índices nos campos `name` das tabelas Category e Product para melhorar performance das buscas.

6. **Autenticação**: Adicionar autenticação (JWT ou Token) se a API for exposta publicamente.
