import os
from flask import render_template, Blueprint, request, flash, redirect, url_for, current_app, jsonify
import json
from server.user.forms import LoginForm, RegisterForm, ArtistApplication
from flask_login import login_user, logout_user, login_required
from server import db, models, bcrypt
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict

basedir = os.path.abspath(os.path.dirname(__file__))
user_blueprint = Blueprint('user', __name__,)

@user_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        try:
            user = models.User.objects.get(username=form.username.data)
        except:
            user = None
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('You are logged in. Welcome!', 'success')
            return redirect(url_for('main.landing'))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('user/login.html', form=form)
    return render_template('user/login.html', form = form)

@user_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = models.User(
            username = form.username.data,
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password.data,
                current_app.config.get('BCRYPT_LOG_ROUNDS')).decode('utf-8'),
            admin = False
        )

        user.save()

        login_user(user)
        flash('You are logged in. Welcome to Gallery!', 'success')
        return redirect(url_for('main.landing'))

    return render_template('user/register.html', form = form)

@user_blueprint.route("/artistinfo", methods=['GET', 'POST'])
def artist_info():
    form = ArtistApplication(request.form)
    if form.validate_on_submit():
        photo = request.files['background_photo']
        photo.save(current_app.config.get('IMAGE_BUCKET_PATH') + photo.filename)

    return render_template('user/artist_info.html', form=form)

@user_blueprint.route("/thankyou", methods=['GET'])
def artist_thanks():
    pass

#TODO: Find alternative for calling Token build
@user_blueprint.route("/build", methods=['GET'])
def build():
    with open("build/contracts/ArtToken.json") as json_data:
        d = json.load(json_data)
        json_data.close()

    return jsonify(d)

@login_required
@user_blueprint.route("/account/<username>", methods=['GET', 'POST'])
def account(username):
    return render_template('user/account.html', username = username)

@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out. Bye!', 'success')
    return redirect(url_for('main.landing'))
