from flask import session, Response, render_template, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource
from models.user import UserModel
from models.forms import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, logout_user, AnonymousUserMixin

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return UserModel.find_by_id(int(user_id))

class Anonymous(AnonymousUserMixin):
  def __init__(self):
    self.email = 'Guest'

login_manager.anonymous_user = Anonymous


class UserRegister(Resource):

    def get(self):
        form = RegisterForm()
        return Response(render_template('user/register.html', form=form))  ## passing signup form to signup template

    def post(self):
        form = RegisterForm()
        if form.validate_on_submit():
            if UserModel.find_by_email(form.email.data) or UserModel.find_by_username(form.username.data):
                flash(f'User already exist', 'alert alert-danger')
                return Response(render_template('user/register.html', form=form))

            hashed_password = generate_password_hash(form.password.data,
                                                     method='sha256')  ## password get hashed for security purposes
            new_user = UserModel(email=form.email.data, username=form.username.data, password=hashed_password)
            new_user.save_to_db()
            login_user(new_user)
            return redirect("/")

        return Response(render_template('user/register.html', form=form))  ## passing signup form to signup template


class UserLogin(Resource):

    def get(self):
        form = LoginForm()

        # alert alert-success
        return Response(render_template('user/login.html', form=form))  ## passing login form to login template

    def post(self):
        form = LoginForm()

        if form.validate_on_submit():  ## if form was submitted....
            user = UserModel.find_by_email(email=form.email.data)
            if user:
                if check_password_hash(user.password, form.password.data):
                    session['current_user'] = user.email
                    flash(f'You have successfully logged in as {user.email}', 'alert alert-success')
                    login_user(user)
                    return redirect("/")
            else:
                flash(u'Invalid Email or Password provided', 'alert alert-danger')

        return Response(render_template('user/login.html', form=form))


class UserLogout(Resource):

    def get(self):
        logout_user()
        return redirect("login")
