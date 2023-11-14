from datetime import datetime
from app.utils.database import db


class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_filename = db.Column(db.String(255), nullable=True)
    cgm_data = db.Column(db.Float, nullable=True)  # Continuous Glucose Monitoring data
    insulin_level = db.Column(db.Float, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
