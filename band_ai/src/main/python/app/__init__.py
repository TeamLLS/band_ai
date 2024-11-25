from flask import Flask, Blueprint, jsonify, request
from app.models.user import User
from app import db
from app.routes.budget_routes import bp as budget_bp
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# TensorFlow 모델 초기화
def init_model():
    model = Sequential([
        Dense(16, activation='relu', input_shape=(2,)),
        Dense(8, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

model = init_model()

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return jsonify({"message": "Welcome to Band AI!"})

@bp.route('/simulate', methods=['POST'])
def simulate():
    params = request.json
    return jsonify({"status": "simulation started", "params": params})

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return jsonify(user_list)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "user": {"id": new_user.id, "name": new_user.name}})

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # 라우트 등록
    app.register_blueprint(budget_bp, url_prefix='/api/budget')

    # 예산 부족 예측 라우트 추가
    @app.route('/predict_budget', methods=['POST'])
    def predict_budget():
        data = request.get_json()
        current_usage = data.get('current_usage', 0)
        target_budget = data.get('target_budget', 0)
        predictions = model.predict([[current_usage, target_budget]])
        return jsonify({"shortage_probability": float(predictions[0])})

    return app
