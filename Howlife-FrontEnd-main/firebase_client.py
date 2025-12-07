import firebase_admin
from firebase_admin import credentials, firestore

# 앱이 중복 초기화되지 않도록 체크
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()
