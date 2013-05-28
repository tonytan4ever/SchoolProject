from flask_assets import Bundle

common_css = Bundle(
    'vendor/bootstrap/css/bootstrap.css',
    Bundle(
        'css/style.css',
        'js/dojo/dijit/themes/claro/claro.css',
    ),
    output='public/css/common.css')

common_dojo_js = Bundle(
    'js/dojo/dojo/dojo.js',
    output='js/dojo/dojo/dojo_compressed.js')

common_bootstrap_js = Bundle(
    'vendor/bootstrap/js/dojo_config.js',                         
    'vendor/bootstrap/js/bootstrap.main.js',
    output='public/js/common_bootstrap.js')