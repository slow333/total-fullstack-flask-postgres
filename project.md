# 사용 라이브러리
1. python venv 구성
- 우선 python version을 시스템 환경 변수에서 원하는 버전으로 변경
- C:\Program Files\Python36\ // 맨 위로 설정
- C:\Program Files\Python36\Scripts // 맨 위로 설정
- python -m venv .venv
- source .venv/Script/activate // bash shell
- .venv\Script\activate // windows shell
- deactivate // 모두 공통
2. pip list
```
Package            Version
------------------ -------
click              8.0.4
colorama           0.4.5
dataclasses        0.8
Flask              0.12.5
importlib-metadata 4.8.3
itsdangerous       2.0.1
Jinja2             3.0.3
MarkupSafe         2.0.1
pip                18.1
psycopg2-binary    2.9.6
setuptools         40.6.2
SQLAlchemy         1.3.2
typing-extensions  4.1.1
Werkzeug           0.16.1
zipp               3.6.0
```
3. web framework: flask
- backend를 구현
- pip install flask==0.12.5

4. html render : jinja2
- frontend를 같이 구현
- flask 설치하면 같이 설치됨

5. database : psycopg2
- 순수한 sql로 구현하기 위한 db연결, query library
- pip install --only-binary :all: psycopg2-binary

# 전체 내용을 python web으로 구현
  - login 기능 구현
  - 회사에서 구현한 오래된 버젼으로 구현

# 전체 내용을 처음부터 다시 구현함...
  - 우선 flask를 먼저 더 공부

# 기존의 전체 내용을 fullsack으로 구현

# etc config
```
window는 cmd 파일 생성
 // run_flask.cmd
@echo off
cd b:/python/flask_app
set FLASK_APP=pybo
set FLASK_DEBUG=true
b:/python/venvs/flask_app/Scripts/activate  
// stop_flask.cmd
@echo off
cd b:/python/flask_app
b:/python/venvs/flask_app/Scripts/deactivate.bat  
```

1. Python 설치 
1. 다운로드:
Python.org에서 3.6.8 버전의 Python 설치 파일을 다운로드
2. 설치:
설치 과정에서 "Add Python to PATH" 옵션을 반드시 선택하여 환경 변수를 등록합니다.

2. 가상 환경(Virtual Environment) 생성 
가상 환경 생성: 개발하려는 프로젝트 폴더를 만들고
    python -m venv .venv
가상 환경 활성화: 생성된 가상 환경을 활성화
    .venv\Scripts\activate
(프롬프트 앞에 .venv가 붙으면 활성화된 것입니다.) 
Flask 설치
    pip install Flask

데이터베이스 라이브러리 설치
pip install --only-binary :all: psycopg2-binary
(앞에 option이 없으면 c++ 14 설치하라는 애러 나옮)

db 연동 라이브러리 설치
pip install sqlalchemy

4. VS Code와 같은 IDE 설정 

echo "# python-flask-db-window" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:slow333/python-flask-db-window.git
git push -u origin main

# ===================================
# 상위 버젼의 python, flask 등을 사용했을 때 구성
# ===================================
### python version에 따라 pip에서 설치되는 flask version, sqlalchemy, psycopg2 버전이 다름

### python 13 버젼 기준
```
Package           Version
----------------- -------
blinker           1.9.0
click             8.2.1
colorama          0.4.6
Flask             3.1.2
greenlet          3.2.4
itsdangerous      2.2.0
Jinja2            3.1.6
MarkupSafe        3.0.2
pip               25.2
psycopg2-binary   2.9.10
SQLAlchemy        2.0.43
typing_extensions 4.15.0
Werkzeug          3.1.3
```
이 버전에서 flask --app flaskr run --debug 가능함<br>
__init__.py 설정도 상위 python version에서 가능함
```
flaskr/__init__.py
import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```
### run app : flask --app flaskr run --debug

### database 연결 설정(psycopg2)
```
flaskr/db.py
from flask import current_app, g

DATABASE = 'postgresql://postgres:1111@localhost/flaskr'

def get_db():
  if 'db' not in g:
    g.db = psycopg2.connect(DATABASE, cursor_factory=psycopg2.extras.DictCursor)
  return g.db

def close_db(e=None):
  """Close the database connection."""
  db = g.pop('db', None)

  if db is not None:
    db.close()

def init_db():
  db = get_db()

  with current_app.open_resource('schema.sql') as f:
    # psycopg2 requires a cursor to execute commands
    with db.cursor() as cur:
      cur.execute(f.read().decode('utf8'))
  # Commit the changes to make them persistent
  db.commit()

@click.command('init-db')
def init_db_command():
  """Clear the existing data and create new tables."""
  init_db()
  click.echo('Initialized the PostgreSQL database.')

def init_app(app):
  """Register database functions with the Flask app."""
  app.teardown_appcontext(close_db)
  app.cli.add_command(init_db_command)
```
### __init__.py 설정
```
    from . import db
    db.init_app(app)
```
### g is a special object that is unique for each request. It is used to store data that might be accessed by multiple functions during the request. The connection is stored and reused instead of creating a new connection if get_db is called a second time in the same request.

### run : flask --app flaskr init-db

### psycopg2에서 query 객체를 dict처럼 사용 가능하나 (user['id'])
> 여기서는 with conn.cursor() as cur: cur.execute('sql')
### sqlalchemy에서는 qeury 객체를 dict 처럼 안되고 tuple처럼 해야함(user[0])
> 여기서는 with engine.connect() as conn: conn.execute('sql')
## flask 버전에 따라 프로젝트에서 db sesstion 연결하는 방식이 다름

## 주의 할점
### 공통으로 select 처럼 return 값이 있으면 with 에서 fetch를 수행해야 하고,
> sqlalchemy
```
session_db = get_db()
session_db.execute(
    text('INSERT INTO blog (title, body, author_id) VALUES (:title, :body, :author_id)'),
    {'title': title, 'body': body, 'author_id': g.user['id']}
)
session_db.commit()

session_db = get_db()
result = session_db.execute(text(
  'SELECT b.id, title, body, created, author_id, username'
  ' FROM blog b JOIN users u ON b.author_id = u.id'
  ' ORDER BY created DESC'
))
blogs = result.fetchall()
```
> psycopg2
```
db = get_db()
db.cursor().execute(
  'UPDATE blog SET title = %s, body = %s  WHERE id = %s',
  (title, body, id)
)
db.commit()

session_db = get_db()
result = session_db.execute(text(
  'SELECT b.id, title, body, created, author_id, username'
  ' FROM blog b JOIN users u ON b.author_id = u.id'
  ' ORDER BY created DESC'
))
blogs = result.fetchall()
return render_template('blog/index.html', blogs=blogs)
```
# set env run script
```
$ cat ~/.bashrc
alias start="source /b/python/flask-tutorial/.venv/Scripts/activate"
alias run="flask --app flaskr run --debug"
```

# flask_crud 
### To run the app, 
### bash: export FLASK_APP=pybo, export FLASK_DEBUG=true , flask run
### cmd : set FLASK_APP=pybo, set FLASK_DEBUG=true, flask run

# ===================================
# flask seesion 관리
# ===================================

# flask session 관리
- Flask는 웹 애플리케이션에서 사용자별 데이터를 저장하고 관리하기 위해 세션(Session) 기능을 제공합니다. Flask의 세션은 기본적으로 클라이언트의 브라우저에 저장되는 쿠키 기반(cookie-based) 방식입니다.

1. 세션의 작동 방식
- 세션 생성: 사용자가 웹사이트에 접속하면, Flask는 고유한 세션 ID를 가진 세션 객체를 생성합니다.
- 데이터 저장: 개발자는 이 세션 객체에 데이터를 딕셔너리처럼 저장할 수 있습니다 (예: session['username'] = 'Alice').
- 암호화된 쿠키: Flask는 이 데이터를 서버에 저장하지 않고, 서명된(signed) 쿠키 형태로 사용자에게 보냅니다. 이 쿠키는 SECRET_KEY로 암호화되어 있어 위변조가 불가능합니다.
- 다음 요청: 사용자가 다음 요청을 보낼 때, 브라우저는 이 쿠키를 다시 서버로 전송하고, Flask는 이를 복호화하여 세션 데이터를 불러옵니다.
- Flask는 웹 애플리케이션에서 사용자별 데이터를 저장하고 관리하기 위해 세션(Session) 기능을 제공합니다. Flask의 세션은 기본적으로 클라이언트의 브라우저에 저장되는 쿠키 기반(cookie-based) 방식입니다.

1. 세션의 작동 방식
- 세션 생성: 사용자가 웹사이트에 접속하면, Flask는 고유한 세션 ID를 가진 세션 객체를 생성합니다.
- 데이터 저장: 개발자는 이 세션 객체에 데이터를 딕셔너리처럼 저장할 수 있습니다 (예: session['username'] = 'Alice').
- 암호화된 쿠키: Flask는 이 데이터를 서버에 저장하지 않고, 서명된(signed) 쿠키 형태로 사용자에게 보냅니다. 이 쿠키는 SECRET_KEY로 암호화되어 있어 위변조가 불가능합니다.
- 다음 요청: 사용자가 다음 요청을 보낼 때, 브라우저는 이 쿠키를 다시 서버로 전송하고, Flask는 이를 복호화하여 세션 데이터를 불러옵니다.

2. 세션 사용을 위한 필수 설정: SECRET_KEY
- 세션 데이터를 안전하게 암호화하기 위해서는 반드시 SECRET_KEY를 설정해야 합니다. 이 키는 외부에 노출되지 않도록 안전하게 관리해야 합니다.
```
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_super_secret_key_here'
```
3. 세션 사용 예제
- 세션을 사용하려면 Flask의 session 객체를 임포트해야 합니다. session은 g 객체처럼 현재 요청의 컨텍스트에 바인딩된 프록시 객체입니다.
- 사용자 아이디를 세션에 저장하여 로그인 상태를 유지하는 예시입니다.
```
from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_super_secret_key_here'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # 로그인 성공 시, 세션에 사용자 정보 저장
        session['username'] = username
        return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/profile')
def profile():
    # 세션에 'username'이 있는지 확인하여 로그인 여부 체크
    if 'username' in session:
        return f"<h1>Hello, {session['username']}!</h1>"
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # 세션에서 사용자 정보 제거
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
```
4. 세션 설정 옵션
- app.config를 통해 세션의 동작을 제어할 수 있습니다.
- SESSION_COOKIE_NAME: 세션 쿠키의 이름 (기본값: 'session').
- SESSION_COOKIE_SECURE: True로 설정하면 HTTPS 연결에서만 쿠키를 전송합니다. 프로덕션 환경에서는 이 설정을 활성화하는 것이 좋습니다.
- PERMANENT_SESSION_LIFETIME: 세션의 유효 기간(초 단위)을 설정합니다. session.permanent = True로 설정해야 적용됩니다. 기본값은 31일입니다.
- SESSION_COOKIE_DOMAIN: 쿠키를 사용할 도메인을 지정합니다.
```
app.config['SESSION_COOKIE_SECURE'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 3600 # 1시간
```