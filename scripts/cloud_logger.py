import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, timedelta


cred = credentials.Certificate("firebase_key.json")

firebase_admin.initialize_app(cred)

db = firestore.client()


def log_event(object_name, distance, risk):

    # Convert UTC to IST
    ist_time = datetime.utcnow() + timedelta(hours=5, minutes=30)

    data = {

        "object": object_name,
        "distance": distance,
        "risk": risk,
        "time": ist_time

    }

    db.collection("braking_events").add(data)