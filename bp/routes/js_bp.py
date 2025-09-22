from flask import Blueprint, render_template as render # type: ignore

bp = Blueprint('js_bp', __name__, url_prefix='/javascript')

# ============= javascript basic ====================
@bp.route('/02-basic/')
@bp.route('/02-basic/01-basic')
@bp.route('/')
def js_basic_index():
  return render('javascript/02-basic/01-basic.html')

@bp.route('/02-basic/02-data-type')
def js_basic_data_type():
  return render('javascript/02-basic/02-data-type.html')

@bp.route('/02-basic/03-basic-object')
def js_basic_basic_object():
  return render('javascript/02-basic/03-basic-object.html')

@bp.route('/02-basic/04-type-transform')
def js_basic_type_transform():
  return render('javascript/02-basic/04-type-transform.html')

@bp.route('/02-basic/05-handle-string')
def js_basic_handle_string():
  return render('javascript/02-basic/05-handle-string.html')

@bp.route('/02-basic/06-handle-array')
def js_basic_handle_array():
  return render('javascript/02-basic/06-handle-array.html')

@bp.route('/02-basic/07-iterable')
def js_basic_iterable():
  return render('javascript/02-basic/07-iterable.html')

@bp.route('/02-basic/08-map-set')
def js_basic_map_set():
  return render('javascript/02-basic/08-map-set.html')

@bp.route('/02-basic/09-destructuring-assignment')
def js_basic_destructuring_assignment():
  return render('javascript/02-basic/09-destructuring-assignment.html')

@bp.route('/02-basic/10-date')
def js_basic_date():
  return render('javascript/02-basic/10-date.html')

@bp.route('/02-basic/11-json')
def js_basic_json():
  return render('javascript/02-basic/11-json.html')

# ============= javascript advance ====================
@bp.route('/03-adv/')
@bp.route('/03-adv/01-recursion-stack')
def js_adv_index():
  return render('javascript/03-adv/01-recursion-stack.html')

@bp.route('/03-adv/02-rest-param-spread-syntax')
def js_adv_rest_param_spread_syntax():
  return render('javascript/03-adv/02-rest-param-spread-syntax.html')

@bp.route('/03-adv/03-lexical')
def js_adv_lexical():
  return render('javascript/03-adv/03-lexical.html')

@bp.route('/03-adv/04-setTimeout-Interval')
def js_adv_setTimeout_Interval():
  return render('javascript/03-adv/04-setTimeout-Interval.html')

@bp.route('/03-adv/05-call-apply')
def js_adv_call_apply():
  return render('javascript/03-adv/05-call-apply.html')

@bp.route('/03-adv/06-bind')
def js_adv_bind():
  return render('javascript/03-adv/06-bind.html')

@bp.route('/03-adv/07-arrow-func')
def js_adv_arrow_func():
  return render('javascript/03-adv/07-arrow-func.html')

@bp.route('/03-adv/08-try-catch')
def js_adv_try_catch():
  return render('javascript/03-adv/08-try-catch.html')

# ============= javascript 콜백/프라미스 ====================
@bp.route('/04-callback/')
@bp.route('/04-callback/01-callback')
def js_callback_index():
  return render('javascript/04-callback/01-callback.html')

@bp.route('/04-callback/02-promise')
def js_callback_promise():
  return render('javascript/04-callback/02-promise.html')

@bp.route('/04-callback/03-promise-chaining')
def js_callback_promise_chaining():
  return render('javascript/04-callback/03-promise-chaining.html')

@bp.route('/04-callback/04-promise-api')
def js_callback_promise_api():
  return render('javascript/04-callback/04-promise-api.html')

@bp.route('/04-callback/05-async-await')
def js_callback_async_await():
  return render('javascript/04-callback/05-async-await.html')

# ============= javascript Generator/module... ====================
@bp.route('/05-yield-module-etc/')
@bp.route('/05-yield-module-etc/01-generator')
def js_yield_module_etc_index():
  return render('javascript/05-yield-module-etc/01-generator.html')

@bp.route('/05-yield-module-etc/02-async-generator')
def js_yield_module_etc_async_generator():
  return render('javascript/05-yield-module-etc/02-async-generator.html')

@bp.route('/05-yield-module-etc/03-module')
def js_yield_module_etc_module():
  return render('javascript/05-yield-module-etc/03-module.html')

@bp.route('/05-yield-module-etc/04-proxy')
def js_yield_module_etc_proxy():
  return render('javascript/05-yield-module-etc/04-proxy.html')

@bp.route('/05-yield-module-etc/05-currying')
def js_yield_module_etc_curry():
  return render('javascript/05-yield-module-etc/05-currying.html')

@bp.route('/05-yield-module-etc/06-bigint')
def js_yield_module_etc_bigint():
  return render('javascript/05-yield-module-etc/06-bigint.html')


# ============= javascript Generator/module... ====================
@bp.route('/06-object/')
@bp.route('/06-object/01-js-object-intro')
def js_object_index():
  return render('javascript/06-object/01-js-object-intro.html')

@bp.route('/06-object/02-js-object-prototype')
def js_object_js_object_prototype():
  return render('javascript/06-object/02-js-object-prototype.html')

@bp.route('/06-object/03-js-inheritance')
def js_object_js_inheritance():
  return render('javascript/06-object/03-js-inheritance.html')

@bp.route('/06-object/04-js-json')
def js_object_js_json():
  return render('javascript/06-object/04-js-json.html')

@bp.route('/06-object/04-js-json2')
def js_object_js_json2():
  return render('javascript/06-object/04-js-json2.html')

# ============= javascript Async ====================
@bp.route('/07-async/')
@bp.route('/07-async/01-js-async-intro')
def js_async_index():
  return render('javascript/07-async/01-js-async-intro.html')

@bp.route('/07-async/02-js-async-eventHandler')
def js_async_js_async_eventHandler():
  return render('javascript/07-async/02-js-async-eventHandler.html')

@bp.route('/07-async/03-js-promises')
def js_async_js_promises():
  return render('javascript/07-async/03-js-promises.html')

@bp.route('/07-async/04-js-promises-ex')
def js_async_js_promises_ex():
  return render('javascript/07-async/04-js-promises-ex.html')

@bp.route('/07-async/05-promises-multiple')
def js_async_promises_multiple():
  return render('javascript/07-async/05-promises-multiple.html')

@bp.route('/07-async/06-js-custom-promises')
def js_async_js_custom_promises():
  return render('javascript/07-async/06-js-custom-promises.html')

@bp.route('/07-async/07-js-promise-api')
def js_async_js_promise_api():
  return render('javascript/07-async/07-js-promise-api.html')

@bp.route('/07-async/08-js-worker')
def js_async_js_worker():
  return render('javascript/07-async/08-js-worker.html')

# ============= javascript nework req. ====================
@bp.route('/08-net-req/')
@bp.route('/08-net-req/01-fetch')
def js_net_req_index():
  return render('javascript/08-net-req/01-fetch.html')

@bp.route('/08-net-req/02-formData-fetch')
def js_net_req_formData_fetch():
  return render('javascript/08-net-req/02-formData-fetch.html')

@bp.route('/08-net-req/03-fetch-Abort')
def js_net_req_fetch_Abort():
  return render('javascript/08-net-req/03-fetch-Abort.html')

@bp.route('/08-net-req/04-cors')
def js_net_req_cors():
  return render('javascript/08-net-req/04-cors.html')

@bp.route('/08-net-req/05-url-object')
def js_net_req_url_object():
  return render('javascript/08-net-req/05-url-object.html')

@bp.route('/08-net-req/06-XMLHttpRequest')
def js_net_req_XMLHttpRequest():
  return render('javascript/08-net-req/06-XMLHttpRequest.html')

@bp.route('/08-net-req/07-WebSocket')
def js_net_req_WebSocket():
  return render('javascript/08-net-req/07-WebSocket.html')