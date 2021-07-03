import os
from flask import Flask,render_template

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path,
        'flaskApp.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def f():
        return render_template('index.html')
    
    from . import db
    db.init_app(app)

    from . import mood
    app.register_blueprint(mood.bp)

    from . import search
    app.register_blueprint(search.bp)
    
    return app

