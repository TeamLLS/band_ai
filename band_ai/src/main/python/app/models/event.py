# app/models/event.py
from app import db

class Event(db.Model):
    # 이벤트 고유 ID (Primary Key)
    id = db.Column(db.Integer, primary_key=True)

    # 이벤트 이름 (최대 100자, 필수 입력)
    # - 100자는 이벤트 제목을 간결하게 표현하기에 충분
    name = db.Column(db.String(100), nullable=False)

    # 이벤트 날짜 (필수 입력)
    # - 특정 날짜를 기반으로 데이터 필터링 또는 분석 가능
    event_date = db.Column(db.DateTime, nullable=False)

    # 이벤트 생성자 ID (User 모델과의 관계)
    # - 유저와의 외래키 관계 설정
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Event {self.name}>"
