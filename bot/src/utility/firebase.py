import firebase_admin
from firebase_admin import credentials, firestore

path_to_json = "./firebase.json"
appCredentials = credentials.Certificate(path_to_json)
firebase_admin.initialize_app(appCredentials)

db = firestore.client()
