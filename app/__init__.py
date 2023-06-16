from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

from app.models.models import db, User
db.init_app(app)

with app.app_context():
    db.create_all()


from app.views.base import base_bp
from app.views.auth import auth_bp
app.register_blueprint(base_bp)
app.register_blueprint(auth_bp)


from app.utils.bcrypt import bcrypt
bcrypt.init_app(app)

from app.utils.sessions import sessions
sessions.init_app(app)

from app.utils.admin import admin
from flask_admin.contrib.sqla import ModelView
admin.init_app(app)
admin.add_view(ModelView(User, db.session))

from app.utils.migrate import migrate
migrate.init_app(app, db)
