from datetime import date

from . import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    created = db.Column(db.Date, default=date.today)
    done = db.Column(db.Boolean, default=False)
