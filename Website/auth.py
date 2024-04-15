from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, User
auth=Blueprint('auth',__name__)

@auth.route('/login-signup', methods=['GET','POST'])
def login_signup():
    if request.method=='POST':
        form_type=request.form.get['form_type']
        if form_type=='login':
            username=request.form.get('userid')
            password=request.form.get('password')
            user=User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                flash('Logged in successfully',category='success')
                return redirect(url_for('dashboard.html')) 
            else:
                flash('Incorrect username or password',category='error')
        elif form_type=='register':
            username=request.form.get('userid')
            email=request.form.get('email')
            password=request.form.get('password')
            existing_user=User.query.filter_by(username=username).first()
            if existing_user:
                flash('User already exists',category='error')
            else:
                new_user=User(username=username,password=password)
                new_user.set_password(password)
                db.session.add(new_user)
                db.session.commit()
                flash('Account created successfully',category='success')
                return redirect(url_for('auth.login_signup'))
    return render_template('signup.html')                 
                 

@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login_signup'))
