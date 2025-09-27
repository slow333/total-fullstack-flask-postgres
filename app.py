from flask import Flask, render_template as render, jsonify # type: ignore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_super_secret_key_here'

@app.route("/")
@app.route("/home/")
def index():
  return render("home.html")
# ==============================
# contents pages
# ==============================
from bp.routes.home_bp import bp as home_bp
app.register_blueprint(home_bp)

from bp.routes.python_bp import bp as python_bp
app.register_blueprint(python_bp)

from bp.routes.database_bp import bp as db_bp
app.register_blueprint(db_bp)

from bp.routes.spring_bp import bp as spring_bp
app.register_blueprint(spring_bp)

from bp.routes.js_bp import bp as js_bp
app.register_blueprint(js_bp)

from bp.routes.java_bp import bp as java_bp
app.register_blueprint(java_bp)

from bp.routes.dom_bp import bp as dom_bp
app.register_blueprint(dom_bp)
# ==============================
# auth 관련 페이지
# ==============================
from bp.myapp.auth import bp as auth
app.register_blueprint(auth)

from bp.myapp.myapp_bp import bp as myapp_bp
app.register_blueprint(myapp_bp)

from bp.myapp.topic_bp import bp as topic_bp
app.register_blueprint(topic_bp)

from bp.myapp.users_db_bp import bp as users_db_bp
app.register_blueprint(users_db_bp)

from bp.myapp.blog_db_auth_bp import bp as blog_db_auth_bp
app.register_blueprint(blog_db_auth_bp)

from bp.myapp.todo_db_auth_bp import bp as todo_db_auth_bp
app.register_blueprint(todo_db_auth_bp)

from bp.myapp.rest_api_book_bp import book_bp as rest_api_book_bp
app.register_blueprint(rest_api_book_bp)
# ==============================
# 공통 적용 사항
# ==============================
@app.after_request
def after_request(response):
  response.headers["Access-Control-Allow-Origin"] = "*"
  response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
  response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
  response.headers["Access-Control-Allow-Credentials"] = "true"
  return response

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)