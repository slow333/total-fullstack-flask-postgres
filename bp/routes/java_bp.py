from flask import Blueprint, render_template as render # type: ignore

bp = Blueprint('java_bp', __name__, url_prefix='/java')

@bp.route('/')
def java_home():
  return render('java/java_index.html')

# =========== java basic ======================
@bp.route('/01-basic/')
@bp.route('/01-basic/01-data-type')
def java_basic_datatype():
  return render('java/01-basic/01-data-type.html')

@bp.route('/01-basic/02-if-for')
def java_basic_if_for():
  return render('java/01-basic/02-if-for.html')

@bp.route('/01-basic/03-array')
def java_basic_array():
  return render('java/01-basic/03-array.html')

@bp.route('/01-basic/04-stream')
def java_basic_stream():
  return render('java/01-basic/04-stream.html')

@bp.route('/01-basic/05-enum')
def java_basic_enum():
  return render('java/01-basic/05-enum.html')

# =========== java oop ======================
@bp.route('/02-oop/')
@bp.route('/02-oop/01-oop-intro')
def java_oop_intro():
  return render('java/02-oop/01-oop-intro.html')

@bp.route('/02-oop/02-oop-1')
def java_oop_1():
  return render('java/02-oop/02-oop-1.html')

# =========== java adv ======================
@bp.route('/03-adv/')
@bp.route('/03-adv/01-Object')
def java_adv_Object():
  return render('java/03-adv/01-Object.html')

@bp.route('/03-adv/02-String')
def java_adv_string():
  return render('java/03-adv/02-String.html')

@bp.route('/03-adv/03-StringBuffer')
def java_adv_string_buffer():
  return render('java/03-adv/03-StringBuffer.html')

@bp.route('/03-adv/04-Math')
def java_adv_math():
  return render('java/03-adv/04-Math.html')

@bp.route('/03-adv/05-LocalDateTime')
def java_adv_local_date_time():
  return render('java/03-adv/05-LocalDateTime.html')

@bp.route('/03-adv/06-Collection-fw1')
def java_adv_collection_1():
  return render('java/03-adv/06-Collection-fw1.html')

@bp.route('/03-adv/07-Collection-fw2')
def java_adv_collection_2():
  return render('java/03-adv/07-Collection-fw2.html')


