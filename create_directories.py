import os

# 디렉토리 구조 정의
directories = [
    "band/band_ai/src/main/java/com/example/band_ai/analytics",
    "band/band_ai/src/main/java/com/example/band_ai/kafka",
    "band/band_ai/src/main/java/com/example/band_ai/models",
    "band/band_ai/src/main/java/com/example/band_ai/processor",
    "band/band_ai/src/main/java/com/example/band_ai/util",
    "band/band_ai/src/main/resources",
    "band/band_ai/simulation",
    "band/band_ai/test/unit_tests",
    "band/band_ai/test/integration_tests",
    "band_user",
    "band_front",
    "band_club",
    "band_activity",
    "band_budget"
]

# 기본 파일 정의
files = [
    "band/band_ai/simulation/simulation_example.py",
    "band/band_ai/test/conftest.py"
]

# 디렉토리 생성
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"Created directory: {directory}")

# 파일 생성
for file in files:
    with open(file, 'w') as f:
        f.write("# Placeholder file\n")
    print(f"Created file: {file}")