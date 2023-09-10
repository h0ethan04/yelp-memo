from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Yelp
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# import for hashing
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ Handles a request to login, given an email and password"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', catgory='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Invalid email', category='error')

    return render_template('login.html', user=current_user)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """ Handles request to sign up for an account, given an email,
        password and first name"""
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # print(email, first_name, password1, password2)
        
        if User.query.filter_by(email=email).first():
            flash('Email is already attached to an account', category='error')
        elif len(email) < 4:
            flash('Email must be longer than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be longer than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7 or len(password1) > 20:
            flash('Password must be at least 7 characters and at most 20 characters.', category='error')
        else:
            # add user to db
            new_user = User(email=email, 
                            first_name=first_name, 
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)
