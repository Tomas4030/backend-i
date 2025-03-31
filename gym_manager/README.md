# Gym App - Django Project

Este projeto Django é uma aplicação para gestão de treinos e planos personalizados de ginásio. Permite que os utilizadores se registrem, façam login, atualizem seus perfis e recebam planos de treino adaptados aos seus objetivos.

## Tecnologias Utilizadas

- **Django**: Framework web para o desenvolvimento do backend.
- **Docker**: Contêineres para facilitar a configuração e execução do ambiente de desenvolvimento.
- **Poetry**: Gerenciador de dependências e ambientes Python.
- **PostgreSQL** (opcional): Pode ser configurado como banco de dados.

## Funcionalidades

- **Autenticação de Utilizadores**: Permite login, logout e criação de novos utilizadores.
- **Gestão de Perfis**: Os utilizadores podem criar e atualizar seu perfil com informações como peso, altura, objetivos e dias de treino.
- **Plano de Treino Personalizado**: Geração automática de um plano de treino baseado nos objetivos do utilizador.
- **Interface de Utilizador**: Páginas para login, cadastro e atualização do perfil.

## Pré-Requisitos

Antes de iniciar, certifique-se de ter os seguintes itens instalados na sua máquina:

- **Docker**: Para rodar a aplicação dentro de contêineres.
- **Poetry**: Para gerenciar as dependências do projeto Python.

## Instalação e Configuração

### 1. Clonar o Repositório

Clone o repositório para a sua máquina local:

git clone https://github.com/Tomas4030/backend-i.git


### 2. Configuração do Ambiente

Após clonar o repositório, execute os seguintes passos:

1. **Iniciar os contêineres do Docker**:

    Para rodar a aplicação no Docker, utilize o comando:

    ```bash
    make start
    ```

    Isso irá executar automaticamente os seguintes comandos:

    ```bash
    docker-compose up --build --force-recreate
    poetry run python manage.py migrate
    ```

    O comando `docker-compose up --build --force-recreate` irá iniciar os contêineres e o banco de dados, e o comando `poetry run python manage.py migrate` irá aplicar as migrações no banco de dados.

2. **Criar um Superuser** (Admin):

    Para criar um superuser para o painel administrativo do Django, execute:

    ```bash
    make createsuperuser
    ```

3. **Coletar arquivos estáticos**:

    Caso o admin não tenha estilos aplicados, utilize o seguinte comando para coletar os arquivos estáticos:

    ```bash
    make compose.collectstatic
    ```

4. **Executar os Testes**:

    Para rodar os testes automatizados do projeto, utilize o comando:

    ```bash
    make pytest
    ```

### 3. Acessando a Aplicação

Depois de configurar o ambiente e iniciar os contêineres, você pode acessar a aplicação localmente através de:

- **URL de acesso**: `http://localhost:8000`

Você pode acessar a página de login e cadastro, ou acessar o painel administrativo do Django com o superusuário que você criou.

### 4. Configuração Opcional do Banco de Dados

Este projeto utiliza o **PostgreSQL** como banco de dados, mas também é possível configurar outros bancos. Caso queira configurar o **PostgreSQL**:

1. No arquivo `.env`, defina as variáveis de ambiente do banco de dados:

    ```bash
    API=(https://wger.de/pt/user/api-key) -> Ir a este site para criar a api
    POSTGRES_USERNAME=
    POSTGRES_PASSWORD=
    POSTGRES_HOST=
    POSTGRES_PORT=
    POSTGRES_DB=
    ```
