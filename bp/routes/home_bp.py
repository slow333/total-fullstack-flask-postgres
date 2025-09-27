from flask import Blueprint, render_template as render # type: ignore

bp = Blueprint('home_bp', __name__, url_prefix='/home')

@bp.route('/ide-set')
def home_ide():
  return render('home/ide-set.html')

@bp.route('/project1')
def home_project1():
  return render('home/project_v1.html')

@bp.route('/project2')
def home_project2():
  return render('home/project_v2.html')

@bp.route('/linux')
def home_linux():
  return render('home/linux.html')

@bp.route('/windows')
def home_windows():
  return render('home/windows.html')

@bp.route('/git')
def home_git():
  return render('home/git.html')

