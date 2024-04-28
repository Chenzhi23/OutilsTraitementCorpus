import argparse
from pathlib import Path

def load_data(folder_path):
    data = []
    # 确保路径是一个目录
    folder = Path(folder_path)
    if not folder.is_dir():
        raise ValueError(f"The path {folder_path} is not a directory.")

    # 遍历目录中的所有.txt文件
    for txt_file in folder.glob('*.txt'):
        with open(txt_file, 'r', encoding='utf-8') as file:
            data.append(file.read())
    
    return data

def main():
    parser = argparse.ArgumentParser(description="Load data from text files")
    parser.add_argument("data", type=str, help="Folder containing txt files")

    args = parser.parse_args()
    folder_path = args.data

    all_data = load_data(folder_path)
    for index, content in enumerate(all_data):
        print(f"--- Content of file {index + 1} ---")
        print(content)

if __name__ == "__main__":
    main()



# python3 load_data.py ../../data/raw