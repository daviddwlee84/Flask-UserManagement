from project import db, create_app, models

# Deprecated: we should use flask-migrate instead
# (because every time we change schema we should upgrade our database)
#
# $ flask db init
# $ flask db migrate
# $ flask db upgrade

# This script is only need to execute at the first time

# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#create-the-tables

with create_app().app_context():
    db.create_all()

# Legacy syntax (2.x syntax)
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy.create_all
# db.create_all(
#     app=create_app()
# )  # pass the create_app result so Flask-SQLAlchemy gets the configuration.
