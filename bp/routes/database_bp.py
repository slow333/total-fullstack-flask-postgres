from flask import Blueprint, render_template as render # type: ignore

bp = Blueprint('database_bp', __name__, url_prefix='/database')

@bp.route('/')
def database_home():
  return render('database/database_index.html')
