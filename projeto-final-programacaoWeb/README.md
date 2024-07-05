# Projeto Final - Programação Web

Este é um projeto web desenvolvido com FastAPI, SQLAlchemy e Jinja2. Ele fornece uma API para gerenciar PCs, com endpoints para criar, listar e deletar PCs. Além disso, inclui autenticação básica com OAuth2 e senhas hash.

## 🚀 Instalação e Configuração

### 📋 Pré-requisitos

```
Python 3.7+
SQLite
Docker (opcional)
```

### 🔧 Instalação

1. Clone o repositório:
   ```
   git clone <   git clone <https://github.com/laceerdag/projeto-final-programacaoWeb.git>
   cd projeto-final-programacaoweb
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Configure o banco de dados (será criado automaticamente na primeira execução):
   
  O banco de dados SQLite é usado neste projeto. Ele será criado automaticamente na primeira execução do aplicativo.

## 📦 Implantação

### Localmente

Para executar o projeto localmente, utilize o comando:

```
uvicorn app.main:app --reload
```

### Usando Docker

Para executar o projeto usando Docker, utilize os seguintes comandos:

```
docker-compose up --build
```

## 🛠️ Construído com


* [FastAPI](https://fastapi.tiangolo.com/) - O framework web usado
* [SQLAlchemy](https://www.sqlalchemy.org/) - ORM para banco de dados
* [Jinja2](https://palletsprojects.com/p/jinja/) - Template engine
* [Uvicorn](https://www.uvicorn.org/) - Servidor ASGI
* [Docker](https://www.docker.com/) - Containerização

## 📌 Versão

Nós usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto). 


* **Gabriel Costa** - *Trabalho Inicial - back end* - [gabrielcosta](https://github.com/laceerdag)
* **Lucas** - *Front-end* - [Lucas](https://github.com/lucasrso?tab=overview&from=2024-06-01&to=2024-06-20)


## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 Agradecimentos

* Agradeço ao Professor Lucas por me fazer perder o sono 🫂;

---
⌨️ com ❤️ por [Gabriel](https://github.com/laceerdag)) 😊
