from flask import (
  Blueprint, request, redirect, render_template as render 
) # type: ignore

bp = Blueprint("main", __name__, url_prefix="/apps/topic")

nextId = 4
topics = [
    {"id": 1, "title": "Flask", "content": "Flask is a micro web framework for Python."},
    {"id": 2, "title": "Django", "content": "Django is a high-level Python web framework."},
    {"id": 3, "title": "FastAPI", "content": "FastAPI is a modern web framework for building APIs."}
]

def manage_topic_by_id(id, new_topic=None, delete=False):
  for topic in topics:
    if topic["id"] == id:
      if delete:
        del topics[topics.index(topic)]
        return None
      elif new_topic is not None:
        topic.update(new_topic)
        return topic
      return topic
  return None

@bp.route("/create", methods=["GET", "POST"])
def create_topic():
  if request.method == "POST":
    global nextId
    title = request.form["title"]
    content = request.form["content"]
    if not title or not content:
      return redirect("/app/topic/create")
    new_topic = {"id": nextId, "title": title, "content": content}
    topics.append(new_topic)
    url = "/app/topic/" + str(new_topic["id"])
    nextId += 1
    return redirect(url)
  elif request.method == "GET":
    return render("myapp/topic/create.html")

@bp.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_topic(id):
  if request.method == "POST":
    title = request.form["title"]
    content = request.form["content"]
    new_topic = {"id": id, "title": title, "content": content}
    manage_topic_by_id(id, new_topic)
    url = "/app/topic/" + str(new_topic["id"])
    return redirect(url)
  elif request.method == "GET":
    topic = manage_topic_by_id(id)
    return render("myapp/topic/edit.html", topic=topic)

@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def delete_topic(id):
  if request.method == "POST":
    manage_topic_by_id(id, delete=True)
    return redirect("/app/topic/")
  elif request.method == "GET":
    topic = manage_topic_by_id(id)
    return render("myapp/topic/delete.html", topic=topic)

@bp.route("/<int:id>")
def topic_detail(id):
  topic = manage_topic_by_id(id)
  return render("myapp/topic/read.html", topic=topic, topics=topics)

@bp.route("/")
def topic_home():
  return render("myapp/topic/topic_home.html", topics=topics)