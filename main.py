from flask import Flask
from extensions import db, login_manager
from core.services.employee_service import employee_bp
from core.services.auth_service import auth_bp
from config import Config
import psycopg2
import urllib.parse
from core.models.db_schemas import User

def create_app():
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY
    passw = urllib.parse.quote(Config.PASSWORD)
    db_uri = f"postgresql+psycopg2://{Config.USER}:{passw}@{Config.SQLALCHEMY_DATABASE_URI}:{Config.PORT}/{Config.EMPLOYEE_DB}"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to access this page."
    # Register Blueprints
    app.register_blueprint(employee_bp)
    app.register_blueprint(auth_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
