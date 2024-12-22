from flask_sqlalchemy import SQLAlchemy
from database_setup import MAX_NAME_LENGTH, gen_short_uuid

db = SQLAlchemy()

class UserView (db.Model):
    id = db.Column(db.String(13), primary_key=True, default=gen_short_uuid)
    user = db.Column(db.String(MAX_NAME_LENGTH))
    user_description = db.Column(db.String(100), default="pole veel lisatud")
    target_id = db.Column(db.String(13), db.ForeignKey('user_view.id'))
    target = db.relationship('UserView',
                           uselist=False,
                           remote_side=[id],
                           foreign_keys=[target_id])