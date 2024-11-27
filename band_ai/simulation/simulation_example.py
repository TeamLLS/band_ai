# 시뮬레이션 실행 파일
import simpy
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import os

# 시뮬레이션 설정
SIMULATION_TIME = 60  # 60일
NUM_MEMBERS = 10  # 멤버 수

# 사용자 유형별 특성 설정 (Weibull 분포 적용)
user_types = {
    'Teen': {'login_shape': 1.5, 'activity_rate': 3.0},
    'Young Adult': {'login_shape': 1.3, 'activity_rate': 2.0},
    'Middle-aged Adult': {'login_shape': 1.2, 'activity_rate': 1.5},
    'Senior': {'login_shape': 1.1, 'activity_rate': 0.5}
}

# 임의로 멤버 유형 할당
members = [random.choice(list(user_types.keys())) for _ in range(NUM_MEMBERS)]

# 데이터 수집용 리스트
event_data = []

# 시뮬레이션 데이터 경로
output_folder = r"C:\Users\shwar\OneDrive\첨부 파일\바탕화면\band"
output_path = os.path.join(output_folder, 'activity_simulation_data.txt')


def member_events(env, member_id, user_type):
    """로그인, 활동 참여를 시뮬레이션하는 프로세스"""
    login_shape = user_types[user_type]['login_shape']
    activity_interval = 1 / user_types[user_type]['activity_rate']

    while env.now < SIMULATION_TIME:
        # Weibull 분포를 이용한 로그인 이벤트 생성
        next_login_time = np.random.weibull(login_shape) * 10
        yield env.timeout(next_login_time)

        event_data.append({
            'member_id': member_id,
            'event': 'Login',
            'time': env.now,
            'user_type': user_type
        })

        # 활동 참여 이벤트 생성
        next_activity_time = np.random.exponential(activity_interval)
        yield env.timeout(next_activity_time)
        if random.random() < 0.7:
            event_data.append({
                'member_id': member_id,
                'event': 'Activity',
                'time': env.now,
                'user_type': user_type
            })


def fixed_activity_event(env, activity_name, participation_rate):
    """모든 회원이 참여 가능한 고정된 활동"""
    event_time = 30  # 고정된 활동 날짜 (30일차)
    yield env.timeout(event_time)
    for member_id in range(NUM_MEMBERS):
        if random.random() < participation_rate:
            event_data.append({
                'member_id': member_id,
                'event': activity_name,
                'time': env.now,
                'user_type': members[member_id]
            })


def setup(env):
    """모든 멤버의 이벤트 프로세스를 설정"""
    for i in range(NUM_MEMBERS):
        user_type = members[i]
        env.process(member_events(env, i, user_type))

    # 고정된 활동 추가 (예: 30일차 클럽 회식)
    env.process(fixed_activity_event(env, "FixedActivity", 0.8))


# 시뮬레이션 환경 초기화 및 실행
env = simpy.Environment()
setup(env)
env.run(until=SIMULATION_TIME)

# 시뮬레이션 결과를 데이터프레임으로 변환
df = pd.DataFrame(event_data)

# 결과 데이터 저장
df.to_csv(output_path, index=False, sep='\t', header=True)
print(f"Generated simulation data saved to {output_path}")

# 시각화
plt.figure(figsize=(12, 8))

# 이벤트 타입별로 색상과 마커 지정
markers = {'Login': 'o', 'Activity': 'x', 'FixedActivity': '^'}
colors = {'Login': 'blue', 'Activity': 'orange', 'FixedActivity': 'red'}

# 각 이벤트 플로팅
for event_type in df['event'].unique():
    subset = df[df['event'] == event_type]
    plt.scatter(subset['time'], subset['member_id'], label=event_type, marker=markers[event_type],
                color=colors[event_type])

# 각 Member ID별 가로줄 추가
for member_id in range(NUM_MEMBERS):
    plt.hlines(y=member_id, xmin=0, xmax=SIMULATION_TIME, colors='gray', linestyles='dotted', alpha=0.5)

plt.xlim(0, SIMULATION_TIME)
plt.xlabel("Time (days)")
plt.ylabel("Member ID")
plt.title("Login, Activity, and Fixed Activity Events Over Time")
plt.legend(title="Event Type")
plt.show()

def run_simulation(duration, num_members):
    # 시뮬레이션 로직 예제
    simulated_data = []
    for i in range(num_members):
        simulated_data.append({
            "member_id": i + 1,
            "activity_score": duration * (i + 1)  # 단순 예제 로직
        })

    return simulated_data