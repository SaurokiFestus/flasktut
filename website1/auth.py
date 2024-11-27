from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, login_user, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method== 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password!', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required #requires you to login to access this page
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup',  methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        firstname=request.form.get('firstname')
        password=request.form.get('password')
        password2=request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists', category='error')
        elif len(email)< 4:
            flash('Email must be greater than 4 char', category='error')
        elif len(firstname) <2:
            flash('Name is too short', category='error')
        elif password!= password2:
            flash('Passwords don\'t match', category='error')
        elif len(password) < 7:
            flash('Password is too short', category='error')
        else:
            new_user=User(email=email, first_name=firstname, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account successfully created', category='success')
            return redirect(url_for('views.home'))

    return render_template('signup.html', user=current_user)