from flask import (
    Blueprint, request, render_template as render, 
    redirect, flash, session, url_for, g # type: ignore
    )
from db import get_flaskdb as get_db # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET','POST'])
def register_users():
    if request.method == 'GET':
        return render('myapp/auth/register.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        error = None

        db = get_db()
        with db.cursor() as cur:
            cur.execute(
            'SELECT id FROM users WHERE username = %s;',(username,)
            )
            user = cur.fetchone()
        if user is not None:
            flash('User {} is already registered.'.format(username))
            return render('myapp/auth/register.html')
        
        if confirm_password != password:
            flash('Passwords do not match.')
            return render('myapp/auth/register.html')
        if error is None:
            with db.cursor() as cur:
                cur.execute(
                'INSERT INTO users (username, email, password) VALUES (%s, %s, %s);',
                (username, email, generate_password_hash(password))
                )
            db.commit()
            return redirect('/auth/login')
        flash(error)

@bp.route('/login', methods=['GET','POST'])
def login_users():
    if request.method == 'GET':
        return render('myapp/auth/login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        error = None
        user = None
        db = get_db()
        with db.cursor() as cur:
            cur.execute('SELECT * FROM users WHERE username = %s ;', (username,))
            user = cur.fetchone()
        if user is None:
            flash('Incorrect username.')
            return render('/auth/login')
        elif not check_password_hash(user[2], password):
            flash('Incorrect password.')
            return redirect('/auth/login')
        
        if error is None:
            session.clear()
            session['user_id'] = user[0]
            return redirect('/apps/')
        return flash(error)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        db = get_db()
        with db.cursor() as cur:
            cur.execute('SELECT * FROM users WHERE id = %s;', (user_id,))
            g.user = cur.fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/apps/')

def login_required(view):
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect('/auth/login')
        return view(**kwargs)
    return wrapped_view