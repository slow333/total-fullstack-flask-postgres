from flask import Blueprint, request, redirect, render_template as render # type: ignore
from db import get_mydb as get_db # type: ignore

users_db_bp = Blueprint("crud_db", __name__, url_prefix="/apps/users")

@users_db_bp.route("/")
def users_all():
    page = int(request.args.get("page", 1))
    per_page = 5  # 한 페이지에 5명씩
    offset = (page - 1) * per_page

    db = get_db()

    with db.cursor() as cursor:
      cursor.execute('SELECT * FROM users;')
      users_page = cursor.fetchall()

    with db.cursor() as cur:
      # 전체 사용자 수 구하기
      cur.execute('SELECT COUNT(*) FROM users;')
      total = cur.fetchone()[0]

    users_list = getUsersList(users_page)

    # 페이지네이션: 현재 페이지 기준으로 최대 5개 페이지만 표시
    total_pages = (total // per_page) + (1 if total % per_page else 0)
    start_page = max(1, page - 2)
    end_page = min(total_pages, start_page + 4)
    if end_page - start_page < 4:
      start_page = max(1, end_page - 4)
    page_links = ''
    for i in range(start_page, end_page + 1):
      if i == page:
        page_links += f'<strong style="color: red;font-size:1.4rem;">{i}</strong> '
      else:
        page_links += f'<a href="/users/all?page={i}" style="color: blue;font-size:1.4rem;">{i}</a> '
    next_page = getPage(page + 1, "Next") if len(users_page) == per_page else ''
    prev_page = getPage(page - 1, "Prev") if page > 1 else ''
    first_page = getPage(1, "First") if page > 1 else ''
    last_page = getPage(total_pages, "Last") if page < total_pages else ''
    pagination = f'''<div>
      {first_page} {prev_page}
      {page_links}
      {next_page} {last_page}
      </div>'''

    new_users_list = f'''
    <h1>전체 사용자 목록</h1>
    <div class="links-list">
      <a href="/users/create">Create User</a>
      <a href="/users/">HOME</a>
    </div>
    {users_list}
    {pagination}
    '''
    return body("users DB", new_users_list)

def getPage(goto=1, label=""):
  return f'''<button class="nav-button">
        <a href="/users/all?page={goto}">
        {label}</a></button>
  '''

@users_db_bp.route("/<int:id>")
def users_detail(id):
  sel_user = select([users]).where(users.c.id == id)
  user = ''
  with engine.connect() as conn:
    user = conn.execute(sel_user).fetchone()
  user_detail = getUsersDetail(user)
  return body("users DB", user_detail)

@users_db_bp.route("/create", methods=["GET", "POST"])
def create_user():
  if request.method == "POST":
    fname = request.form["first_name"]
    lname = request.form["last_name"]
    email = request.form["email"]
    if not fname or not lname:
      return redirect("/users/create")
    stmt = insert(users).values(first_name=fname, last_name=lname, email=email)
    with engine.connect() as conn: conn.execute(stmt)
    return redirect("/users/all")
  elif request.method == "GET":
    return body("Create User", createUserForm())
  return None


@users_db_bp.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_user(id):
  if request.method == "POST":
    fname = request.form["first_name"]
    lname = request.form["last_name"]
    email = request.form["email"]
    stmt = update(users).where(users.c.id == id).values(first_name=fname, last_name=lname, email=email)
    with engine.connect() as conn: conn.execute(stmt)
    return redirect("/users/all")
  elif request.method == "GET":
    user = select([users]).where(users.c.id == id)
    with engine.connect() as conn:
      user = conn.execute(user).fetchone()
    return body("Edit User", editUserForm(user))
  return None

@users_db_bp.route("/<int:id>/delete", methods=["GET", "POST"])
def delete_user(id):
  if request.method == "POST":
    stmt = delete(users).where(users.c.id == id)
    with engine.connect() as conn: conn.execute(stmt)
    return redirect("/users/all")
  elif request.method == "GET":
    sel_user = select([users]).where(users.c.id == id)
    with engine.connect() as conn:
      user = conn.execute(sel_user).fetchone()
    return body("Delete User", deleteUserForm(user))
  return None

def getUsersList(users):
  user_list = ''
  for user in users:
    user_list += f"<div>{user['firstname']} {user['lastname']} {user['email']}</div>"
  return user_list