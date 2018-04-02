import os
from flask import render_template, Blueprint, request, flash, redirect, url_for, current_app
from server.user.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required
from server import db, models, bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))
main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route("/", methods=['GET', 'POST'])
def landing():
    return render_template('main/landing.html')
