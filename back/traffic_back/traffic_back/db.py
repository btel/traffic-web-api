import psycopg2
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(current_app.config['DATABASE_URL'])
        g.db.autocommit = True
        pass

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('static/schema.sql') as f:
        with db.cursor() as cursor:
            cursor.execute(f.read())

@click.command('init-db')
@with_appcontext
def init_db_command():
    "create new db tables"
    init_db()
    click.echo("Initialized the DB")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

