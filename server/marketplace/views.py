import os
from flask import render_template, Blueprint, request, flash, redirect, url_for, current_app
from server.user.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required
from server import db, models, bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))
marketplace_blueprint = Blueprint('marketplace', __name__,)

@marketplace_blueprint.route("/marketplace", methods=['GET', 'POST'])
def marketplace():
    return render_template('marketplace/marketplace.html')
