import os
from flask import render_template, Blueprint, request, flash, redirect, url_for, current_app
from flask_login import login_user, logout_user, login_required
from server import db, models, bcrypt

basedir = os.path.abspath(os.path.dirname(__file__))
demo_blueprint = Blueprint('demo', __name__,)


@demo_blueprint.route("/demo", methods=['GET', 'POST'])
def demo():
    return render_template('demo/demo.html')
