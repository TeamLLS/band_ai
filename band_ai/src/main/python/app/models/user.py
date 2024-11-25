# app/models/user.py
from app import db

class User(db.Model):
    # 유저 고유 ID (Primary Key)
    id = db.Column(db.Integer, primary_key=True)

    # 유저 이름 (최대 50자, 필수 입력)
    # - 50자로 제한한 이유: 일반적으로 이름 길이가 짧음
    # - 데이터베이스 성능 최적화를 위해 문자열 길이 제한
    name = db.Column(db.String(50), nullable=False)

    # 유저 이메일 (최대 120자, 고유, 필수 입력)
    # - 120자는 이메일 주소의 일반적인 최대 길이
    # - 고유 제약 조건으로 중복 방지
    email = db.Column(db.String(120), unique=True, nullable=False)

    # 계정 생성일 (현재 시각 자동 설정)
    # - 유저 생성 시 타임스탬프 저장
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<User {self.name}>"
