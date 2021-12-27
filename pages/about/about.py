from flask import blueprints, render_template

about = blueprints ('about', __name__, static_folder = 'static',
                    static_url_path = '/about', template_folder='templates')

@about.routh('/about')
def about_func():
    return render_template('about.html')