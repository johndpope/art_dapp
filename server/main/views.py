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

@main_blueprint.route("/marketplace", methods=['GET', 'POST'])
def marketplace():
    return render_template('main/marketplace.html')

@main_blueprint.route("/faq", methods=['GET', 'POST'])
def faq():
    return render_template('main/faq.html')

@main_blueprint.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('main/about.html')

@main_blueprint.route("/join", methods=['GET', 'POST'])
def join():
    return render_template('main/join.html')
