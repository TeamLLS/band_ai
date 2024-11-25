from flask import Blueprint, request, jsonify
from app.models.budget import Budget
from app.models.tensorflow_model import model  # TensorFlow 모델 불러오기

bp = Blueprint('budget', __name__)

@bp.route('/predict_budget', methods=['POST'])
def predict_budget():
    """
    예산 부족 여부를 예측하는 엔드포인트
    """
    data = request.get_json()
    try:
        # 요청 데이터에서 'current_usage'와 'target_budget' 값 추출
        current_usage = data.get('current_usage')
        target_budget = data.get('target_budget')

        if current_usage is None or target_budget is None:
            return jsonify({"error": "Invalid input data"}), 400

        # TensorFlow 모델을 사용해 부족 확률 예측
        predictions = model.predict([[current_usage, target_budget]])
        return jsonify({"shortage_probability": float(predictions[0][0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
