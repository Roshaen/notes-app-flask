from flask import Blueprint


auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return '<p>This is login Page</p>'


@auth.route("/logout")
def logout():
    return '<p>This is logout page</p>'

@auth.route("/sign-up")
def sign_up():
    return '<p>This is signup page</p>'