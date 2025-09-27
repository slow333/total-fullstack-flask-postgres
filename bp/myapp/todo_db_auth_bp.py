from flask import (
  Blueprint, request, redirect, g,
  render_template as render, flash) # type: ignore
from db import get_flaskdb as get_db # type: ignore
from bp.myapp.auth import login_required # type: ignore

bp = Blueprint("todo_db_auth_bp", __name__, url_prefix="/apps/todos")

@bp.route("/")
def users_():
  page = request.args.get("page", 1, type=int)
  per_page = 6  # 한 페이지에 5명씩
  offset = (page - 1) * per_page

  db = get_db()

  with db.cursor() as cursor:
    cursor.execute('SELECT b.id as id, b.title, b.content, b.done, b.created, b.fdate, '
                   ' b.author_id, u.id AS user_id '
                   ' FROM todo b '
                   ' INNER JOIN users u ON b.author_id = u.id '
                   ' ORDER BY b.id DESC LIMIT %s OFFSET %s;', (per_page, offset))
    todo_page = cursor.fetchall()

  with db.cursor() as cur:
    cur.execute('SELECT COUNT(*) FROM todo;')
    total = cur.fetchone()[0]

  # 페이지네이션: 현재 페이지 기준으로 최대 5개 페이지만 표시
  total_pages = (total // per_page) + (1 if total % per_page else 0)
  todo_page_len = len(todo_page)

  start_page = max(1, page - 2)
  end_page = min(total_pages, start_page + 4)
  if end_page - start_page < 4:
    start_page = max(1, end_page - 4)
  
  return render("myapp/todo/todo_home.html", 
                todos=todo_page, page=page, total_pages=total_pages, 
                start_page=start_page, end_page=end_page, 
                todo_page_len=todo_page_len)

@bp.route("/create", methods=["GET", "POST"])
@login_required
def create_todo():
  if request.method == "POST":
    title = request.form["title"]
    content = request.form["content"]
    done = request.form.get("done")
    fdate = request.form.get("fdate")

    error=None
    if not title or not content:
      error = "타이틀과 컨텐트는 필수입니다."
    if done is None:
      done = 'false'
    if fdate is None or fdate == '':
      fdate = None
    if error is not None:
      flash(error)
      return render("myapp/todo/create_todo.html")
    else:
      db = get_db()
      with db.cursor() as cursor:
        cursor.execute('INSERT INTO todo (title, content, done, fdate, author_id) '
                       ' VALUES (%s, %s, %s, %s, %s);', 
                       (title, content, done,fdate , g.user['id']))
        db.commit()
      return redirect("/apps/todos/")
  return render("myapp/todo/create_todo.html")


@bp.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_todo(id):
  db = get_db()
  if request.method == "POST":
    title = request.form["title"]
    content = request.form["content"]
    done = request.form.get("done")
    fdate = request.form.get("fdate")

    error=None
    if not title or not content:
      error = "타이틀과 컨텐트는 필수입니다."
    if done is None:
      done = 'false'
    if fdate is None or fdate == '':
      fdate = None
    if error is not None:
      flash(error)
      return render("myapp/todo/update_todo.html")
    if error is None:
      with db.cursor() as cursor:
        cursor.execute('UPDATE todo SET title = %s, content = %s, done = %s, fdate = %s '
                       'WHERE id = %s;', 
                      (title, content, done, fdate, id))
        db.commit()
    return redirect("/apps/todos/")
  elif request.method == "GET":
    with db.cursor() as cur:
      cur.execute('SELECT * FROM todo WHERE id = %s;', (id,))
      todo = cur.fetchone()
    return render("myapp/todo/edit_todo.html", todo=todo)
  return None

@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def delete_todo(id):
  db = get_db()
  if request.method == "POST":
    with db.cursor() as cursor:
      cursor.execute('DELETE FROM todo WHERE id = %s;', (id,))
      db.commit()
    return redirect("/apps/todos/")
  elif request.method == "GET":
    with db.cursor() as cur:
      cur.execute("SELECT * FROM todo WHERE id = %s;", (id,))
      todo = cur.fetchone()
    return render("myapp/todo/delete_todo.html", todo=todo)
  return None

