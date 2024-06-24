import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase Configuration
cred = credentials.Certificate('unimentor-idgs91-firebase-adminsdk-aibea-e1018507fb.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://unimentor-idgs91-default-rtdb.firebaseio.com/'
})


unimentor_db = db.reference('/')
universidades = [unimentor_db.child('universidades').get()]
