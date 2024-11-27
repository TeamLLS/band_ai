from app import db

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    club_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    status = db.Column(db.String(50), nullable=False)  # 상태: OPENED, CLOSED, CANCELED
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    participant_num = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    closed_at = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Activity {self.name}>"