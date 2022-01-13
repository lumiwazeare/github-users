from flask import Blueprint


user_app = Blueprint("user_app", __name__, template_folder="templates")


@user_app.route("/")
def home():
    return "hello there"
