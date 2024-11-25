from flask import Blueprint, jsonify, request
from app.models.budget import Budget

bp = Blueprint('main', __name__)

@bp.route('/activities', methods=['GET'])
def get_activities():
    # 활동 리스트 API - 페이징 적용 및 추가 필드 처리
    page_no = int(request.args.get('pageNo', 1))
    page_size = int(request.args.get('pageSize', 10))
    activities = [
        {"id": 1, "name": "Activity A", "description": "Fun activity", "date": "2024-11-25", "contact_info": "123-456-7890"},
        {"id": 2, "name": "Activity B", "description": "Learning session", "date": "2024-11-26", "contact_info": "987-654-3210"}
    ]
    return jsonify({"list": activities[(page_no-1)*page_size:page_no*page_size]})

@bp.route('/participants', methods=['GET'])
def get_participants():
    # 참가자 리스트 조회 및 상태 처리
    participants = [
        {"id": 1, "name": "User A", "attend": True},
        {"id": 2, "name": "User B", "attend": False}
    ]
    return jsonify({"participants": participants})
