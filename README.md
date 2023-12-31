# Flask - User Management

## Getting Started

### Local Machine

```powershell
pip install -r requirements.txt
```

- Set PostgreSQL username & password in `db.env`
- Start PostgreSQL server

```powershell
flask --app project db init
flask --app project db migrate
flask --app project db upgrade
```

> ```powershell
> python create_database.py
> ```
>
> ```powershell
> # https://www.sqlite.org/download.html => sqlite-tools-*
> sqlite3 .\instance\db.sqlite
> sqlite> .tables
> user
> sqlite> .schema user
> CREATE TABLE user (
>         id INTEGER NOT NULL,
>         email VARCHAR(100),
>         password VARCHAR(100),
>         name VARCHAR(1000),
>         PRIMARY KEY (id),
>         UNIQUE (email)
> );
> ```

```powershell
flask --app project run --debug

# https://stackoverflow.com/questions/1420719/powershell-setting-an-environment-variable-for-a-single-command-only
```

When you upgrade any of your database schema

```sh
flask --app project db migrate
flask --app project db upgrade
```

This will create new `migrations/version` and automatically upgrade your database

### Docker Compose

```powershell
docker compose up --build
```

Initialize PostgreSQL

```powershell
$ docker exec -it flask-usermanagement-app-1 /bin/sh
flask --app project db init
flask --app project db migrate
flask --app project db upgrade
```

- Adminer: http://localhost:8080/
  - System: `PostgreSQL`
  - Server: `pgsql`
  - Username: `postgres`
  - Password: `example`
- App: http://localhost:5000/

## Database

- [Flask-UserManagement | DrawSQL](https://drawsql.app/teams/trader/diagrams/flask-usermanagement)

## Todo

- [X] Dockerize
- [X] PostgreSQL
  - [**Using SQLAlchemy with Flask and PostgreSQL**](https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/)
    - [ro6ley/cars_in_a_flask: A simple API built using Flask and SQLAlchemy.](https://github.com/ro6ley/cars_in_a_flask)
  - [docker-library/postgres: Docker Official Image packaging for Postgres](https://github.com/docker-library/postgres)
  - [Container Password](https://github.com/docker-library/postgres/issues/111#issuecomment-293053904)
  - [**flask + postgres + sqlalchemy migrations dockerized intro - DEV Community**](https://dev.to/yactouat/flask-postgres-sqlalchemy-migrations-dockerized-intro-2f8p)
- [ ] HTTPS
- [ ] Replace password plain hash `All plain hashes are deprecated and will not be supported in Werkzeug 3.0.`

## Resources

Tutorial

- [**How To Add Authentication to Your App with Flask-Login | DigitalOcean**](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)

Flask

- [Application Setup — Flask Documentation (2.3.x)](https://flask.palletsprojects.com/en/2.3.x/tutorial/factory/) - Application Factory

Python Database

- [sqlalchemy/sqlalchemy: The Database Toolkit for Python](https://github.com/sqlalchemy/sqlalchemy)
  - [The Type Hierarchy — SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/core/type_basics.html#generic-camelcase-types)
- [pallets-eco/flask-sqlalchemy: Adds SQLAlchemy support to Flask](https://github.com/pallets-eco/flask-sqlalchemy/)
- [miguelgrinberg/Flask-Migrate: SQLAlchemy database migrations for Flask applications using Alembic](https://github.com/miguelgrinberg/flask-migrate)
  - [Flask-Migrate — Flask-Migrate documentation](https://flask-migrate.readthedocs.io/en/latest/)
  - [Welcome to Alembic’s documentation! — Alembic 1.11.1 documentation](https://alembic.sqlalchemy.org/en/latest/)

Database Schema

- [Database schema for Django User Sessions - DrawSQL](https://drawsql.app/templates/django-user-sessions)
- [Database schema for Django Oauth Toolkit - DrawSQL](https://drawsql.app/templates/django-oauth-toolkit)
- [Database schema for Django Two Factor Auth - DrawSQL](https://drawsql.app/templates/django-two-factor-auth)

Database

- PostgreSQL
  - [PostgreSQL — SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html)
  - [How to Interact with Databases using SQLAlchemy with PostgreSQL - CoderPad](https://coderpad.io/blog/development/sqlalchemy-with-postgresql/)
  - [postgres - Official Image | Docker Hub](https://hub.docker.com/_/postgres)
- SQLite
  - [SQLite Download Page](https://www.sqlite.org/download.html)
  - [Command Line Shell For SQLite](https://www.sqlite.org/cli.html)
- [adminer - Official Image | Docker Hub](https://hub.docker.com/_/adminer/)
- [Multiple Databases with Binds — Flask-SQLAlchemy Documentation (2.x)](https://flask-sqlalchemy.palletsprojects.com/en/2.x/binds/)

CSS Framework

- [Bulma: Free, open source, and modern CSS framework based on Flexbox](https://bulma.io/)
  - [jgthms/bulma: Modern CSS framework based on Flexbox](https://github.com/jgthms/bulma)

Docker

- [Ways to set environment variables in Compose | Docker Documentation](https://docs.docker.com/compose/environment-variables/set-environment-variables/)
- [Services top-level element | Docker Documentation](https://docs.docker.com/compose/compose-file/05-services/#env_file)

Others

- [Werkzeug — Werkzeug Documentation (2.3.x)](https://werkzeug.palletsprojects.com/en/2.3.x/)
