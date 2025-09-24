from flask import Blueprint, render_template as render, url_for, redirect, g # type: ignore
import psycopg2 # type: ignore
from db import get_flaskdb as get_db # type: ignore

bp = Blueprint('myapp_bp', __name__, url_prefix='/apps')

@bp.route('/')
def myapp_home():
    # db = get_db()
    # if g.user is None:
    #     return redirect(url_for('auth.login'))
    # else:
    #   user_id = g.user['id']
    #   with db.cursor() as cursor:
    #       cursor.execute('SELECT * FROM users where id =%s;', (user_id,))
    #       user = cursor.fetchall()
    return render('myapp/myapp_home.html')
