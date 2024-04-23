from flask import Flask, session, render_template, request, redirect, flash
import pyrebase

app=Flask(__name__)

config = {
  'apiKey': "AIzaSyBaE61l8fXoU4t9fjMBdX0QDYMO4f8LMfg",
  'authDomain': "daichamaicha-c5831.firebaseapp.com",
  'projectId': "daichamaicha-c5831",
  'storageBucket': "daichamaicha-c5831.appspot.com",
  'messagingSenderId': "522793105803",
  'appId': "1:522793105803:web:25708fb8a0dc4e225b978e",
  'measurementId': "G-EPRSBW6051",
  'databaseURL': '' 
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key ='daichamaicha'

#login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
            return redirect('/dashboard')
        except Exception as e:
            flash('Login failed: ' + str(e), 'error')
            return redirect('/')
    return render_template('./templates/signup.html')

#register route
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            auth.create_user_with_email_and_password(email, password)
            return redirect('/login')
        except Exception as e:
            flash('Registration failed: ' + str(e), 'error')
            return redirect('/')
    return redirect('/')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('./templates/dashboard.html')
    else:
        return redirect('/')

# Routes for beginner and intermediate levels for each category
@app.route('/gbeginner')
def gbeginner():
    return render_template('./templates/gbeginner_quiz.html')

@app.route('/gintermediate')
def gintermediate():
    return render_template('./templates/gintermediate_quiz.html')
    
@app.route('/sbeginner')
def sbeginner():
    return render_template('./templates/sbeginner_quiz.html')

@app.route('/sintermediate')
def sintermediate():
    return render_template('./templates/sintermediate.html')

@app.route('/tbeginner')
def tbeginner():
    return render_template('./templates/tbeginner.html')

@app.route('/tintermediate')
def tintermediate():
    return render_template('./templates/tintermediate.html')

@app.route('/wbeginner')
def wbeginner():
    return render_template('./templates/wbeginner.html')

@app.route('/wintermediate')
def wintermediate():
    return render_template('./templates/wintermediate.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('./templates/signup.html')

# Main entry point of the Flask application
if __name__ == '__main__':
    app.run(port=1111)

