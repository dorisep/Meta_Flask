from flask_app.main import render_template 

@bp.route('/')
def index():
    return render_template('index.html')