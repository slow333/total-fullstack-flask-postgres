from flask import Blueprint, render_template as render # type: ignore

bp = Blueprint('dom_bp', __name__, url_prefix='/dom')

@bp.route('/')
def dom_home():
  return render('dom/dom-index.html')

# =========== DOM basic ======================
@bp.route('/01-document/')
@bp.route('/01-document/01-dom-search')
def dom_doc_search():
  return render('dom/01-document/01-dom-search.html')

@bp.route('/01-document/02-dom-query')
def dom_doc_query():
  return render('dom/01-document/02-dom-query.html')

@bp.route('/01-document/03-dom-attribute')
def dom_doc_attribute():
  return render('dom/01-document/03-dom-attribute.html')

@bp.route('/01-document/04-dom-change')
def dom_doc_change():
  return render('dom/01-document/04-dom-change.html')

@bp.route('/01-document/05-style-class')
def dom_doc_style_class():
  return render('dom/01-document/05-style-class.html')

@bp.route('/01-document/06-elem-size-scroll')
def dom_doc_elem_size_scroll():
  return render('dom/01-document/06-elem-size-scroll.html')

@bp.route('/01-document/07-browser-size')
def dom_doc_browser_size():
  return render('dom/01-document/07-browser-size.html')

@bp.route('/01-document/08-position')
def dom_doc_position():
  return render('dom/01-document/08-position.html')

# =========== DOM event ======================
@bp.route('/02-event/')
@bp.route('/02-event/01-browser-event')
def dom_event_browser_event():
  return render('dom/02-event/01-browser-event.html')

@bp.route('/02-event/02-event-bubbling')
def dom_event_bubbling():
  return render('dom/02-event/02-event-bubbling.html')

# =========== DOM UI event ======================
@bp.route('/03-UI-event/')
@bp.route('/03-UI-event/01-mouse-event')
def dom_ui_event_mouse_event():
  return render('dom/03-UI-event/01-mouse-event.html')

@bp.route('/03-UI-event/02-drag-drop-mouseevent')
def dom_ui_event_drag_drop_mouse_event():
  return render('dom/03-UI-event/02-drag-drop-mouseevent.html')

@bp.route('/03-UI-event//03-keydown-up')
def dom_ui_event_keydown_up():
  return render('dom/03-UI-event//03-keydown-up.html')

@bp.route('/03-UI-event/04-scroll')
def dom_ui_event_scroll():
  return render('dom/03-UI-event/04-scroll.html')

# =========== DOM form ======================
@bp.route('/04-form/')
@bp.route('/04-form/01-property-method')
def dom_form_property_method():
  return render('dom/04-form/01-property-method.html')

@bp.route('/04-form/02-focus-blur')
def dom_form_focus_blur():
  return render('dom/04-form/02-focus-blur.html')

@bp.route('/04-form/03-event-change-input')
def dom_form_event_change_input():
  return render('dom/04-form/03-event-change-input.html')

@bp.route('/04-form/04-submit')
def dom_form_submit():
  return render('dom/04-form/04-submit.html')

# =========== DOM css ======================
@bp.route('/05-html-css/')
@bp.route('/05-html-css/01-css-basic')
def dom_css_basic():
  return render('dom/05-html-css/01-css-basic.html')

@bp.route('/05-html-css/02-css-color')
def dom_css_color():
  return render('dom/05-html-css/02-css-color.html')

@bp.route('/05-html-css/03-align-flex-grid')
def dom_css_aligh_flex_grid():
  return render('dom/05-html-css/03-align-flex-grid.html')

@bp.route('/05-html-css/04-css-more')
def dom_css_more():
  return render('dom/05-html-css/04-css-more.html')

@bp.route('/05-html-css/05-media')
def dom_etc_media():
  return render('dom/05-html-css/05-media.html')
