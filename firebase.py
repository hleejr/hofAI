import random
import requests
import datetime as dt
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('FirebaseKey.json')
default_app = firebase_admin.initialize_app(cred)
fb = firestore.client()
