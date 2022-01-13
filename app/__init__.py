from flask import Flask
from app.user_route import user_app
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(user_app)
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
