# project/server/main/views.py

import os
from flask import render_template, Blueprint, request, flash, redirect, url_for, current_app
from server.user.forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, login_required
from server import db, models, bcrypt
import flask_whooshalchemy

basedir = os.path.abspath(os.path.dirname(__file__))
account_blueprint = Blueprint('account', __name__,)

@login_required
@account_blueprint.route("/<username>", methods=['GET', 'POST'])
def main(username):
    return render_template('account/account.html', username = username)
