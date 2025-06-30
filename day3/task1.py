import requests
from bs4 import BeautifulSoup

# 设置请求头模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 豆瓣电影Top250链接
url = 'https://movie.douban.com/top250'

try:
    # 发送HTTP请求
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 检查请求是否成功

    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有电影条目
    movie_items = soup.find_all('div', class_='item')[:10]  # 只取前10部

    # 提取电影名称
    top_10_movies = []
    for item in movie_items:
        title_tag = item.find('span', class_='title')
        if title_tag:
            # 获取中文标题（排除外文标题）
            title = title_tag.get_text(strip=True)
            top_10_movies.append(title)

    # 打印结果
    print("豆瓣电影Top10：")
    for i, title in enumerate(top_10_movies, 1):
        print(f"{i}. {title}")

except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except Exception as e:
    print(f"发生错误: {e}")