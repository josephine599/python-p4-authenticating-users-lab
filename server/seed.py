#!/usr/bin/env python3

from app import app
from models import db, User

with app.app_context():
    db.session.query(User).delete()

    users = [
        User(username="jane"),
        User(username="john"),
        User(username="alex")
    ]

    db.session.add_all(users)
    db.session.commit()

    print("🌱 Database seeded")
