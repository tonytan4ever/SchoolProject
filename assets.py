from flask_assets import Bundle

common_css = Bundle(
    'vendor/bootstrap/css/bootstrap.css',
    Bundle(
        'css/style.css',
        'js/dojo/dijit/themes/claro/claro.css',
    ),
    output='public/css/common.css')


common_ui_control_js = Bundle(
    'public/js/ui/login_form.js',                         
    output='public/js/ui_controls.js')

common_bootstrap_js = Bundle(
    'vendor/bootstrap/js/dojo_config.js',                         
    'vendor/bootstrap/js/bootstrap.main.js',
    output='public/js/common_bootstrap.js')