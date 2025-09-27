from flask import (
  Blueprint, request, redirect, g,
  render_template as render, flash) # type: ignore
from db import get_flaskdb as get_db # type: ignore

bp = Blueprint("blog_db_auth_bp", __name__, url_prefix="/apps/blogs")

@bp.route("/")
def users_():
  page = request.args.get("page", 1, type=int)
  per_page = 10  # 한 페이지에 5명씩
  offset = (page - 1) * per_page

  db = get_db()

  with db.cursor() as cursor:
    cursor.execute('SELECT b.id as id, b.title, b.content, b.comment, '
                   ' b.author_id, u.id AS user_id FROM blog b '
                   'INNER JOIN users u ON b.author_id = u.id '
                   'ORDER BY b.id DESC LIMIT %s OFFSET %s;', (per_page, offset))
    blog_page = cursor.fetchall()

  with db.cursor() as cur:
    cur.execute('SELECT COUNT(*) FROM blog;')
    total = cur.fetchone()[0]

  # 페이지네이션: 현재 페이지 기준으로 최대 5개 페이지만 표시
  total_pages = (total // per_page) + (1 if total % per_page else 0)
  blog_page_len = len(blog_page)

  start_page = max(1, page - 2)
  end_page = min(total_pages, start_page + 4)
  if end_page - start_page < 4:
    start_page = max(1, end_page - 4)
  
  return render("myapp/blog/blog_home.html", blogs=blog_page, page=page, total_pages=total_pages, start_page=start_page, end_page=end_page, blog_page_len=blog_page_len)


@bp.route("/create", methods=["GET", "POST"])
def create_blog():
  if request.method == "POST":
    title = request.form["title"]
    content = request.form["content"]
    comment = request.form["comment"]

    error=None
    if not title or not content:
      error = "타이틀과 컨텐트는 필수입니다."
    if error is not None:
      flash(error)
      return render("myapp/blog/create_blog.html")
    else:
      db = get_db()
      with db.cursor() as cursor:
        cursor.execute('INSERT INTO blog (title, content, comment, author_id) VALUES (%s, %s, %s, %s);', 
                       (title, content, comment, g.user['id']))
        db.commit()
      return redirect("/apps/blogs/")
  return render("myapp/blog/create_blog.html")


@bp.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_blog(id):
  db = get_db()
  if request.method == "POST":
    title = request.form["title"]
    content = request.form["content"]
    comment = request.form["comment"]
    with db.cursor() as cursor:
      cursor.execute('UPDATE blog SET title = %s, content = %s, comment = %s WHERE id = %s;', 
                     (title, content, comment, id))
      db.commit()
    return redirect("/apps/blogs/")
  elif request.method == "GET":
    with db.cursor() as cur:
      cur.execute('SELECT * FROM blog WHERE id = %s;', (id,))
      blog = cur.fetchone()
    return render("myapp/blog/edit_blog.html", blog=blog)
  return None

@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def delete_blog(id):
  db = get_db()
  if request.method == "POST":
    with db.cursor() as cursor:
      cursor.execute('DELETE FROM blog WHERE id = %s;', (id,))
      db.commit()
    return redirect("/apps/blogs/")
  elif request.method == "GET":
    with db.cursor() as cur:
      cur.execute("SELECT * FROM blog WHERE id = %s;", (id,))
      blog = cur.fetchone()
    return render("myapp/blog/delete_blog.html", blog=blog)
  return None

