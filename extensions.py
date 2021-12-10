from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = "/"
login_manager.login_message = 'Please login first!'
login_manager.refresh_view = "/"
login_manager.needs_refresh_message = 'Refresh for login!'
