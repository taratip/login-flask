from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import LoginForm, PasswordForm, RegisterForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@app.route('/index')
@app.route('/index/<name>', methods=['GET', 'POST'])
def index(name=''):
    return render_template('index.html', name=name, page='index')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Credentials are incorrect')
            return redirect(url_for('login'))
        return redirect(url_for('password', email=user.email))

    return render_template('login.html', form=form, page='login')


@app.route('/password/<email>', methods=['GET', 'POST'])
def password(email=''):
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = PasswordForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=email).first()
        if user is None or not user.check_password(form.password.data):
            flash('Credentials are incorrect')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        flash('You are now logged in.')
        return redirect(url_for('index', name=user.name))

    return render_template('password.html', form=form, page='password', email=email)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you have successfully registered.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, page='register')


@app.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('index'))
