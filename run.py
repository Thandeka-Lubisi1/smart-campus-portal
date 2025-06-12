from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Import and register blueprints
    from app.auth.routes import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app