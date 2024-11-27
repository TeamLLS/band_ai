from app import db

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    member_id = db.Column(db.Integer, nullable=False)
    member_name = db.Column(db.String(255))
    status = db.Column(db.String(50), nullable=False)  # 참가 상태: ATTEND, NOT_ATTEND, ADDITIONAL_ATTEND

    def __repr__(self):
        return f"<Participant {self.username}>"
