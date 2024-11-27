from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import logging

# Database initialization
db = SQLAlchemy()

# TensorFlow model initialization
def init_model():
    model = Sequential([
        Dense(16, activation='relu', input_shape=(2,)),
        Dense(8, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

model = init_model()

# Seed data for initial database population
def seed_data():
    """Insert initial data into the database."""

    # Add activities
    activity1 = Activity(name="Activity A", description="Description A", status="opened", participant_num=10)
    activity2 = Activity(name="Activity B", description="Description B", status="closed", participant_num=5)

    db.session.add_all([activity1, activity2])

    # Add participants
    participant1 = Participant(activity_id=1, member_id=1, username="user1", member_name="User One", status="attend")
    participant2 = Participant(activity_id=1, member_id=2, username="user2", member_name="User Two", status="not_attend")
    db.session.add_all([participant1, participant2])

    db.session.commit()

# Flask application factory

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # Config 적용
    db.init_app(app)

    # Database initialization and seeding
    with app.app_context():
        db.create_all()
        seed_data()

    logging.basicConfig(level=logging.INFO)

    # Register Blueprints
    from app.routes.main_routes import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/api')

    # Error handlers
    @app.errorhandler(400)
    def handle_bad_request(e):
        return jsonify({"error": "Bad request"}), 400

    @app.errorhandler(500)
    def handle_internal_error(e):
        logging.error(f"Server Error: {e}")
        return jsonify({"error": "Internal server error"}), 500

    return app
    print("Flask app created successfully!")