from flask import Flask
from app.user_route import construct_user_blueprint
from app.user_api_route import construct_user_api_blueprint
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.user_service import UserService


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# quick user model declaration
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    avatar_url = db.Column(db.String(512))
    type = db.Column(db.String(40))
    URL = db.Column(db.String(512))

    def __repr__(self) -> str:
        return "<UserModel {}>".format(self.username)


# register user services
userService = UserService(UserModel)
app.register_blueprint(construct_user_blueprint(db, userService))
app.register_blueprint(construct_user_api_blueprint(db, userService))
