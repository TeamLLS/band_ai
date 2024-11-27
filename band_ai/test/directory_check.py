import os

def print_directory_structure(directory, indent=0):
    """Recursively print directory structure."""
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        print("  " * indent + f"- {item}")
        if os.path.isdir(item_path):
            print_directory_structure(item_path, indent + 1)

# 확인하고자 하는 디렉토리 경로
target_directory = r"C:\Users\shwar\OneDrive\첨부 파일\바탕화면\band\band"
print(f"Directory structure for: {target_directory}")
print_directory_structure(target_directory)