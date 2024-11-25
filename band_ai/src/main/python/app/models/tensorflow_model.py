import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 모델 정의
model = Sequential([
    Dense(16, activation='relu', input_shape=(2,)),  # 입력 데이터 크기: 2
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')  # 이진 분류
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# 예제 데이터로 모델 학습
def train_model():
    # 데이터 예제 (예산 사용량, 목표 예산)
    X_train = [[1000, 2000], [1500, 2000], [2500, 2000], [3000, 2000]]
    y_train = [0, 0, 1, 1]  # 0: 정상, 1: 부족

    # 모델 학습
    model.fit(X_train, y_train, epochs=50, batch_size=2)

# 모델 학습 실행
train_model()
