from flask import (
  Blueprint, request, redirect, 
  render_template as render, flash) # type: ignore
from db import get_mydb as get_db # type: ignore

bp = Blueprint("crud_db", __name__, url_prefix="/apps/users")

@bp.route("/")
def users_():
  page = request.args.get("page", 1, type=int)
  per_page = 10  # 한 페이지에 5명씩
  offset = (page - 1) * per_page

  db = get_db()

  with db.cursor() as cursor:
    cursor.execute('SELECT * FROM users ORDER BY id DESC LIMIT %s OFFSET %s;', (per_page, offset))
    users_page = cursor.fetchall()
    print(users_page)

  with db.cursor() as cur:
    cur.execute('SELECT COUNT(*) FROM users;')
    total = cur.fetchone()[0]

  # 페이지네이션: 현재 페이지 기준으로 최대 5개 페이지만 표시
  total_pages = (total // per_page) + (1 if total % per_page else 0)
  users_page_len = len(users_page)

  start_page = max(1, page - 2)
  end_page = min(total_pages, start_page + 4)
  if end_page - start_page < 4:
    start_page = max(1, end_page - 4)

  return render("myapp/users/users_home.html", users=users_page, page=page, total_pages=total_pages, start_page=start_page, end_page=end_page, users_page_len=users_page_len)


@bp.route("/<int:id>")
def users_detail(id):
  db = get_db()
  with db.cursor() as cursor:
    cursor.execute('SELECT * FROM users WHERE id = %s;', (id,))
    user = cursor.fetchone()
  return render("myapp/users/users_detail.html", user=user)

@bp.route("/create", methods=["GET", "POST"])
def create_user():
  if request.method == "POST":
    fname = request.form["firstname"]
    lname = request.form["lastname"]
    email = request.form["email"]

    error=None
    if not fname or not lname:
      error = "이름은 필수입니다."
    if error is not None:
      flash(error)
      return render("myapp/users/create_user.html")
    else:
      db = get_db()
      with db.cursor() as cursor:
        cursor.execute('INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s);', 
                       (fname, lname, email))
        db.commit()
      return redirect("/apps/users/")
  return render("myapp/users/create_user.html")


@bp.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_user(id):
  db = get_db()
  if request.method == "POST":
    fname = request.form["firstname"]
    lname = request.form["lastname"]
    email = request.form["email"]
    with db.cursor() as cursor:
      cursor.execute('UPDATE users SET first_name = %s, last_name = %s, email = %s WHERE id = %s;', 
                     (fname, lname, email, id))
      db.commit()
    return redirect("/apps/users/")
  elif request.method == "GET":
    with db.cursor() as cur:
      cur.execute('SELECT * FROM users WHERE id = %s;', (id,))
      user = cur.fetchone()
    return render("myapp/users/edit_user.html", user=user)
  return None

@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def delete_user(id):
  db = get_db()
  if request.method == "POST":
    with db.cursor() as cursor:
      cursor.execute('DELETE FROM users WHERE id = %s;', (id,))
      db.commit()
    return redirect("/apps/users/")
  elif request.method == "GET":
    with db.cursor() as cur:
      cur.execute("SELECT * FROM users WHERE id = %s;", (id,))
      user = cur.fetchone()
    return render("myapp/users/delete_user.html", user=user)
  return None

