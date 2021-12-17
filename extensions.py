from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
bootstrap = Bootstrap()
migrate = Migrate()
login_manager = LoginManager()

