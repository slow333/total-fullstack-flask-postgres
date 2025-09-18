from flask import Flask, render_template as render, jsonify # type: ignore

app = Flask(__name__)

@app.route("/")
def index():
  return render("home.html")

from bp.routes.python_bp import bp as python_bp
app.register_blueprint(python_bp)

from bp.routes.database_bp import bp as db_bp
app.register_blueprint(db_bp)


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