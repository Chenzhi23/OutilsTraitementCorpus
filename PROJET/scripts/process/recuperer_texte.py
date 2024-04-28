import requests
from bs4 import BeautifulSoup
import argparse
from pathlib import Path  # 导入 Path

def save_to_file(path, file_name, title, content):
    # 使用 Path 对象来确保正确的路径拼接
    full_path = path / file_name
    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(title + "\n\n")
        file.write(content)

def corpus_contenu(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果请求失败，抛出HTTPError异常
        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取标题
        title = soup.find('title').text

        # 获取所有段落内容
        paragraphs = soup.find_all('p')
        content = "\n".join(paragraph.text for paragraph in paragraphs)

        return title, content
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return "", ""

def main():
    parser = argparse.ArgumentParser(description="Scrape website content")
    parser.add_argument("inputfile", type=str, help="Text file containing URLs")
    parser.add_argument("output_folder_path", type=str, help="Folder for output txt files")

    args = parser.parse_args()

    # 确保输出目录存在
    output_path = Path(args.output_folder_path)
    output_path.mkdir(parents=True, exist_ok=True)

    # 读取URL文件
    with open(args.inputfile, 'r') as file:
        urls = file.readlines()
            # 遍历每个URL并保存内容
    for idx, url in enumerate(urls):
        url = url.strip()  # 去除可能的空白字符
        title, content = corpus_contenu(url)
        if title and content:  # 如果标题和内容不为空
            file_name = f"{idx + 1}.txt"
            save_to_file(output_path, file_name, title, content)
            print(f"Saved {url} to {output_path / file_name}")
        else:
            print(f"Failed to retrieve content for {url}")

if __name__ == "__main__":
    main()


# python3 ./PROJET/scripts/process/recuperer_texte.py ./corpus/urls.txt ./PROJET/data/raw

