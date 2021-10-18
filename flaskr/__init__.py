import os, logging

from flask import Flask, render_template
from flask_wtf import CSRFProtect

def create_app(test_config=None):
    csrf = CSRFProtect()

    app = Flask(__name__)
    app.config.from_object('config')
    csrf.init_app(app)

    @app.route('/')
    def index():
        return render_template('pages/index.html')

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    from . import todos
    app.register_blueprint(todos.bp)

    return app