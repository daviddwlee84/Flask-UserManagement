# Flask - User Management

## Getting Started

```powershell
pip install -r requirements.txt

python create_database.py

# https://www.sqlite.org/download.html => sqlite-tools-*
sqlite3 .\instance\db.sqlite
sqlite> .tables
user
sqlite> .schema user
CREATE TABLE user (
        id INTEGER NOT NULL,
        email VARCHAR(100),
        password VARCHAR(100),
        name VARCHAR(1000),
        PRIMARY KEY (id),
        UNIQUE (email)
);
```

```powershell
flask --app project run --debug

# https://stackoverflow.com/questions/1420719/powershell-setting-an-environment-variable-for-a-single-command-only
```

## Database

- [Flask-UserManagement | DrawSQL](https://drawsql.app/teams/trader/diagrams/flask-usermanagement)

## Todo

- [ ] Dockerize
- [ ] PostgreSQL
- [ ] HTTPS

## Resources

Tutorial

- [**How To Add Authentication to Your App with Flask-Login | DigitalOcean**](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)

Flask

- [Application Setup — Flask Documentation (2.3.x)](https://flask.palletsprojects.com/en/2.3.x/tutorial/factory/) - Application Factory

Python Database

- [sqlalchemy/sqlalchemy: The Database Toolkit for Python](https://github.com/sqlalchemy/sqlalchemy)
  - [The Type Hierarchy — SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/core/type_basics.html#generic-camelcase-types)
- [pallets-eco/flask-sqlalchemy: Adds SQLAlchemy support to Flask](https://github.com/pallets-eco/flask-sqlalchemy/)

Database Schema

- [Database schema for Django User Sessions - DrawSQL](https://drawsql.app/templates/django-user-sessions)
- [Database schema for Django Oauth Toolkit - DrawSQL](https://drawsql.app/templates/django-oauth-toolkit)
- [Database schema for Django Two Factor Auth - DrawSQL](https://drawsql.app/templates/django-two-factor-auth)

Database

- SQLite
  - [SQLite Download Page](https://www.sqlite.org/download.html)
  - [Command Line Shell For SQLite](https://www.sqlite.org/cli.html)

CSS Framework

- [Bulma: Free, open source, and modern CSS framework based on Flexbox](https://bulma.io/)
  - [jgthms/bulma: Modern CSS framework based on Flexbox](https://github.com/jgthms/bulma)

Others

- [Werkzeug — Werkzeug Documentation (2.3.x)](https://werkzeug.palletsprojects.com/en/2.3.x/)
