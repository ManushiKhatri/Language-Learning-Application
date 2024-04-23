import pyrebase

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

email='alu@gmail.com'
password='test1234'

user=auth.sign_in_with_email_and_password(email,password)
print(user)

#user=auth.sign_in_with_email_and_password(email,password)
