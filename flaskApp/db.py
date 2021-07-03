import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
import pandas as pd

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    already_there = False
    with current_app.open_resource('schema.sql') as f:
        try:
            db.executescript(f.read().decode('utf8'))
        except sqlite3.OperationalError as e:
            already_there=True
            print(e)
    if not already_there:
        for x in ['songs', 'artists', 'song_artist', 'popity']:
            with current_app.open_resource(f'csv_files/{x}.csv') as f:
                pd.read_csv(f).to_sql(x,db,if_exists = "append",
                index=False)



@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('database started...')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
