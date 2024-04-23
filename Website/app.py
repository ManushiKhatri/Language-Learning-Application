from flask import Flask, session, render_template, request, redirect
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

@app.route('/', methods=['GET','POST'])
def loginsignup():
    if ('user' in session):
        print("User already logged in")
        return render_template('dashboard.html')
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        try:
            print("entered", email, password)
            user=auth.sign_in_with_email_and_password(email,password)
            session['user']= email
        except:
            return 'Invalid Credentials. Please try again.'
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    print("Logged out")
    session.pop('user', None)
   
    return redirect('/')

if __name__=='__main__':
    app.run(port=1111)

