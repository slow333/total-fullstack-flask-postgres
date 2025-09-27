import psycopg2 # type: ignore
import psycopg2.extras
from flask import g
from flask import current_app # type: ignore

db_url_mydb = "postgresql://postgres:1111@localhost/mydb"
db_url_flaskdb = "postgresql://postgres:1111@localhost/flaskr"

def get_mydb():
  if 'mydb' not in g:
    g.mydb = psycopg2.connect(db_url_mydb, cursor_factory=psycopg2.extras.DictCursor)
  return g.mydb

def get_flaskdb():
  if 'flaskdb' not in g:
    g.flaskdb = psycopg2.connect(db_url_flaskdb, cursor_factory=psycopg2.extras.DictCursor)
  return g.flaskdb

def close_db(e=None):
  mydb = g.pop('mydb', None)
  if mydb is not None:
    mydb.close()
  flaskdb = g.pop('flaskdb', None)
  if flaskdb is not None:
    flaskdb.close()

def init_app(app):
  """Register database functions with the Flask app."""
  app.teardown_appcontext(close_db)