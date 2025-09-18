from flask import Blueprint, render_template as render # type: ignore

bp = Blueprint('python_bp', __name__, url_prefix='/python')

@bp.route('/')
def python_home():
  return render('python/python_index.html')

@bp.route('/core/datatype')
def python_datatype():
  return render('python/core/01_datatype.html')

@bp.route('/core/print-format')
def python_print_format():
  return render('python/core/02_print_format.html')

@bp.route('/core/loop')
def python_loop():
  return render('python/core/03_loop.html')

@bp.route('/core/def-file')
def python_def_file():
  return render('python/core/04_def_file.html')

@bp.route('/core/class-module')
def python_class_module():
  return render('python/core/05_class_module.html')

@bp.route('/core/try-except')
def python_try_except():
  return render('python/core/06_try_except.html')

@bp.route('/core/py-library')
def python_py_library():
  return render('python/core/07_py_library.html')

@bp.route('/core/closer-decorator')
def python_closer_decorator():
  return render('python/core/08_closer_decorator.html')

@bp.route('/core/regexp')
def python_regexp():
  return render('python/core/09_regexp.html')

@bp.route('/flask/install')
def flask_install():
  return render('python/flask/00_python_flask_install.html')

@bp.route('/flask/core-crud')
def flask_core_crud():
  return render('python/flask/core_crud.html')

@bp.route('/flask/db-setup')
def flask_db_setup():
  return render('python/flask/db_setup.html')