# README-CANDIDATO

## Seção 1: Instruções para rodar

### Pré-requisitos
- **Docker** e **Docker Compose** instalados.
- O projeto foi desenvolvido mirando **Python 3.13**.

### Variáveis de Ambiente
O projeto está configurado para alternar automaticamente entre desenvolvimento local (SQLite) e containerizado (PostgreSQL).
Ao rodar via Docker, as variáveis são injetadas automaticamente pelo `docker-compose.yml`:
- `DB_ENGINE`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.

### Como rodar o projeto (Recomendado via Docker)
A maneira mais simples de iniciar a aplicação e o banco de dados é utilizando o Docker Compose.

1. Clone o repositório e abra a pasta do projeto:
   ```bash
   git clone https://github.com/dnxbatista/simple-resource-api/tree/Feature/daniel
   cd simple-resource-api\store_api\
   ```

2. Suba os containers (API + Banco):
    ```bash
    docker-compose up --build
    ```
    O comando irá automaticamente criar as migrações, aplicá-las e iniciar o servidor.

3. Acesse a documentação da API:
- http://localhost:8000/api/docs/

### Como rodar manualmente (Sem Docker)
Caso prefira rodar localmente com SQLite:

1. Crie e ative um ambiente virtual:
```bash
python -m venv venv
.\venv\Scripts\activate
```

2. Instale as dependencias
```bash
pip install -r requirements.txt
```

3. Execute as migrações e rode o servidor:
```bash
python manage.py migrate
python manage.py runserver
```
---
## Seção 2: Decisões de design
### Desafios e Soluções
A principal decisão arquitetural foi garantir que o ambiente de desenvolvimento fosse agnóstico ao sistema operacional.

<b>Dificuldade:</b> Configurar a comunicação correta entre o container da aplicação Django e o container do PostgreSQL, garantindo que o banco estivesse pronto antes da API iniciar.

<b>Solução:</b> Implementação de um docker-compose.yml robusto e adaptação do settings.py para ler configurações de banco via variáveis de ambiente (os.environ). Foi adicionado um script no comando de inicialização do Docker para rodar as migrações automaticamente a cada deploy.

### O que não foi possível fazer (Limitações do Timebox)
Devido à restrição de tempo e foco na solidez da infraestrutura Docker/PostgreSQL, a funcionalidade de upload de arquivos para nuvem (AWS S3) não foi implementada nesta versão.

### Como eu faria com mais tempo:
1. Utilizaria as bibliotecas boto3 e django-storages.

2. Configuraria um bucket S3 com políticas de IAM restritas.

3. Adicionaria as credenciais via .env (python-decouple) para não expor segredos no código.

4. Alteraria o DEFAULT_FILE_STORAGE no Django para apontar para o S3.

5. Além disso, adicionaria autenticação via JWT (Simple JWT) para proteger os endpoints de escrita (POST/PUT/DELETE).

---
## Seção 3: Link para Deploy (ou Docker)
O projeto não está hospedado em nuvem pública no momento, mas está pronto para execução imediata via Docker.

Para testar agora mesmo em sua máquina:
```bash
docker-compose up
```
A API estará disponível em http://localhost:8000.

---
## Seção Final: Recomendações
Sobre o desafio proposto, o escopo é excelente para avaliar conhecimentos fundamentais de Backend.

### Sugestões de melhoria para o projeto:
1. Testes Automatizados: Aumentar a cobertura de testes para incluir casos de borda (ex: tentar criar produto com preço negativo).

2. Paginação: Implementar paginação customizada nos ViewSets para lidar com grandes volumes de produtos.

3. Filtros Avançados: Utilizar django-filter para permitir filtrar produtos por faixas de preço (min_price, max_price).