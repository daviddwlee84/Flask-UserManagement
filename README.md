# Flask - User Management

## Getting Started

```powershell
pip install -r requirements.txt

python create_database.py
# https://www.sqlite.org/download.html => sqlite-tools-*
sqlite3 .\instance\db.sqlite
$ .tables
```

```powershell
flask --app project run --debug

# https://stackoverflow.com/questions/1420719/powershell-setting-an-environment-variable-for-a-single-command-only
```

## Resources

Tutorial

- [**How To Add Authentication to Your App with Flask-Login | DigitalOcean**](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)

Flask

- [Application Setup — Flask Documentation (2.3.x)](https://flask.palletsprojects.com/en/2.3.x/tutorial/factory/) - Application Factory

Python Database

- [sqlalchemy/sqlalchemy: The Database Toolkit for Python](https://github.com/sqlalchemy/sqlalchemy)
- [pallets-eco/flask-sqlalchemy: Adds SQLAlchemy support to Flask](https://github.com/pallets-eco/flask-sqlalchemy/)

Database Schema

- [Database schema for Django User Sessions - DrawSQL](https://drawsql.app/templates/django-user-sessions)
- [Database schema for Django Oauth Toolkit - DrawSQL](https://drawsql.app/templates/django-oauth-toolkit)
- [Database schema for Django Two Factor Auth - DrawSQL](https://drawsql.app/templates/django-two-factor-auth)

CSS Framework

- [Bulma: Free, open source, and modern CSS framework based on Flexbox](https://bulma.io/)
  - [jgthms/bulma: Modern CSS framework based on Flexbox](https://github.com/jgthms/bulma)

Others

- [Werkzeug — Werkzeug Documentation (2.3.x)](https://werkzeug.palletsprojects.com/en/2.3.x/)
