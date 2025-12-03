Variáveis de ambiente necessárias:
DJANGO_SECRET_KEY, DEBUG, DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME (e opcionalmente AWS_S3_CUSTOM_DOMAIN).

Como instalar dependências:
pip install -r requirements.txt (recomenda-se usar um ambiente virtual).

Como rodar o projeto:
docker-compose up --build

Maior dificuldade e como superou:
Encontrei dificuldades com AWS e Docker, principalmente para configurar corretamente o armazenamento em nuvem e os containers. Consegui superar pesquisando a documentação oficial, tutoriais e testando diferentes abordagens até fazer funcionar.

O que não teve tempo de fazer e como faria se tivesse mais tempo:
Faltou tempo para polir e configurar melhor o código, como refatorar algumas partes, adicionar validações mais completas e otimizar a integração com AWS. Se tivesse mais tempo, faria essas melhorias, deixando o projeto mais organizado e robusto.

Instrua como rodar via Docker:

Certifique-se de ter o Docker e o Docker Compose instalados.

Crie um arquivo .env com as variáveis de ambiente necessárias (DJANGO_SECRET_KEY, DB_NAME, DB_USER, DB_PASSWORD, etc.).

Execute o comando:

docker-compose up --build

Acesse o projeto em http://localhost:8000.

Dicas, melhorias e recomendações:
Faltou tempo para concluir completamente o código, mas gostei muito do desafio e senti que ele foi realmente desafiador.
Para melhorar, seria interessante polir algumas funcionalidades, ajustar configurações e adicionar validações mais completas.
Todo o conhecimento utilizado nesse desafio — Django, DRF, Docker, AWS, PostgreSQL — é muito aplicado no dia a dia de um desenvolvedor, então vale a pena praticar e aprofundar-se nessas tecnologias.