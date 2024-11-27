from flask import Blueprint, jsonify, request
from simulation.simulation_example import run_simulation

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


@bp.route('/simulate', methods=['POST'])
def simulate():
    try:
        # 요청 데이터 수신
        params = request.json
        if not params:
            return jsonify({"error": "Request body is required"}), 400

        # 파라미터 검증
        duration = params.get('duration')
        num_members = params.get('num_members')

        if not isinstance(duration, int) or duration <= 0:
            return jsonify({"error": "Invalid 'duration'. Must be a positive integer."}), 400
        if not isinstance(num_members, int) or num_members <= 0:
            return jsonify({"error": "Invalid 'num_members'. Must be a positive integer."}), 400

        # 시뮬레이션 실행
        result = run_simulation(duration, num_members)

        # 성공적으로 결과 반환
        return jsonify({"status": "success", "data": result}), 200
    except Exception as e:
        # 예외 발생 시 처리
        return jsonify({"error": str(e)}), 500
