# API festival

## Installation

Pre-requisites:

- Docker

Run `docker-compose up -d --build` in the app directory.

It binds the application server to `localhost:80` and redirect to the docs.

## Database

The database is bind on the port 5432

### Migration

To make a migration :

If alembic.ini doesn't exist :

```
$ docker-compose exec web alembic init -t async migrations
```

And edit alembic.ini with

```
sqlalchemy.url = postgresql+asyncpg://postgres:postgres@db:5432/foo
```

Modify the env.py with these informations :

- Add : `from sqlmodel import SQLModel`
- Import your models
- Remplace this : `target_metadata = SQLModel.metadata`


After that, generate the first migration :

```
$ docker-compose exec web alembic revision --autogenerate -m "init"
```

To apply the migration : 
```
$ docker-compose exec web alembic upgrade head
```