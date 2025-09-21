from flask import Blueprint, render_template as render # type: ignore

bp = Blueprint('spring_bp', __name__, url_prefix='/spring')

# ============= setting java backend ====================
@bp.route('/00-setting/sbb-index')
@bp.route('/00-setting/')
@bp.route('/')
def spring_sbb_index():
  return render('spring/00-setting/sbb-index.html')

@bp.route('/00-setting/01-about-spring-boot')
def spring_01_about_spring_boot():
  return render('spring/00-setting/01-about-spring-boot.html')

@bp.route('/00-setting/02-sts-setting')
def spring_sts_setting():
  return render('spring/00-setting/02-sts-setting.html')

@bp.route('/00-setting/03-cors-setting')
def spring_core_setting():
  return render('spring/00-setting/03-cors-setting.html')

@bp.route('/00-setting/04-intellij-setting')
def spring_intellij_setting():
  return render('spring/00-setting/04-intellij-setting.html')

@bp.route('/00-setting/99-cors-config-oldversion')
def spring_core_config_oldversion():
  return render('spring/00-setting/99-cors-config-oldversion.html')

# ============= Sring basic ====================
@bp.route('/01-basics/00-project-architecture')
@bp.route('/01-basics/')
def spring_basic_project_arghitecture():
  return render('spring/01-basics/00-project-architecture.html')

@bp.route('/01-basics/01-Controller')
def spring_basic_controller():
  return render('spring/01-basics/01-Controller.html')

@bp.route('/01-basics/02-JPA-db')
def spring_basic_jpa_db():
  return render('spring/01-basics/02-JPA-db.html')

@bp.route('/01-basics/03-entity-db-mapping')
def spring_basic_entity_db_mapping():
  return render('spring/01-basics/03-entity-db-mapping.html')

@bp.route('/01-basics/04-repository-basic')
def spring_basic_repository_basic():
  return render('spring/01-basics/04-repository-basic.html')

@bp.route('/01-basics/05-repository-crud')
def spring_basic_repository_crud():
  return render('spring/01-basics/05-repository-crud.html')

@bp.route('/01-basics/06-domain-categorize')
def spring_basic_domain_categorize():
  return render('spring/01-basics/06-domain-categorize.html')

@bp.route('/01-basics/07-templates')
def spring_basic_templates():
  return render('spring/01-basics/07-templates.html')

# ============= Sring board ====================
@bp.route('/02-board-basic-page/01-question-list')
@bp.route('/02-board-basic-page/')
def spring_board_question_list():
  return render('spring/02-board-basic-page/01-question-list.html')

@bp.route('/02-board-basic-page/02-service-intro')
def spring_board_service_intro():
  return render('spring/02-board-basic-page/02-service-intro.html')

@bp.route('/02-board-basic-page/03-question-detail')
def spring_board_question_detail():
  return render('spring/02-board-basic-page/03-question-detail.html')

@bp.route('/02-board-basic-page/04-thymeleaf-style')
def spring_board_thymeleaf_style():
  return render('spring/02-board-basic-page/04-thymeleaf-style.html')

@bp.route('/02-board-basic-page/05-question-create')
def spring_board_question_create():
  return render('spring/02-board-basic-page/05-question-create.html')

@bp.route('/02-board-basic-page/06-validation')
def spring_board_validation():
  return render('spring/02-board-basic-page/06-validation.html')

# ============= Sring board advance ====================
@bp.route('/03-board-advanced/01-nav-bar')
@bp.route('/03-board-advanced/')
def spring_board_adv_nav_bar():
  return render('spring/03-board-advanced/01-nav-bar.html')

@bp.route('/03-board-advanced/02-paging')
def spring_board_adv_paging():
  return render('spring/03-board-advanced/02-paging.html')

@bp.route('/03-board-advanced/03-board-detail')
def spring_board_adv_board_detail():
  return render('spring/03-board-advanced/03-board-detail.html')

@bp.route('/03-board-advanced/04-spring-security')
def spring_board_adv_spring_security():
  return render('spring/03-board-advanced/04-spring-security.html')

@bp.route('/03-board-advanced/05-user-subscribe')
def spring_board_adv_user_subscribe():
  return render('spring/03-board-advanced/05-user-subscribe.html')

@bp.route('/03-board-advanced/06-login-logout')
def spring_board_adv_login_logout():
  return render('spring/03-board-advanced/06-login-logout.html')

# ============= Sring board 수정 삭제 ====================
@bp.route('/04-board-more/01-add-author')
@bp.route('/04-board-more/')
def spring_board_more_add_author():
  return render('spring/04-board-more/01-add-author.html')

@bp.route('/04-board-more/02-edit-delete')
def spring_board_more_edit_delete():
  return render('spring/04-board-more/02-edit-delete.html')

@bp.route('/04-board-more/03-like')
def spring_board_more_like():
  return render('spring/04-board-more/03-like.html')

@bp.route('/04-board-more/04-anchor')
def spring_board_more_anchor():
  return render('spring/04-board-more/04-anchor.html')

@bp.route('/04-board-more/05-markdown')
def spring_board_more_markdown():
  return render('spring/04-board-more/05-markdown.html')

@bp.route('/04-board-more/06-search')
def spring_board_more_search():
  return render('spring/04-board-more/06-search.html')

# ============= Sring board etc ====================
@bp.route('/05-board-etc/01-additional-functions')
@bp.route('/05-board-etc/')
def spring_board_etc_additional_functions():
  return render('spring/05-board-etc/01-additional-functions.html')

@bp.route('/05-board-etc/00-rest-spring-27-setting')
def spring_board_etc_sp27_settings():
  return render('spring/05-board-etc/00-rest-spring-27-setting.html')

@bp.route('/05-board-etc/01-project-basic')
def spring_board_etc_project_basic():
  return render('spring/05-board-etc/01-project-basic.html')

# ============= Sring board JSP ====================
@bp.route('/06-JSP/01-settings')
@bp.route('/06-JSP/')
def spring_jsp_settings():
  return render('spring/06-JSP/01-settings.html')

@bp.route('/06-JSP/02-start-jsp')
def spring_jsp_start_jsp():
  return render('spring/06-JSP/02-start-jsp.html')

@bp.route('/06-JSP/03-method-scriptlit')
def spring_jsp_method_scriptlit():
  return render('spring/06-JSP/03-method-scriptlit.html')