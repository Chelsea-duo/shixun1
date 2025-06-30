import requests
from lxml import etree
import os


def download_images():
    url = "http://pic.netbian.com/"

    # 创建保存图片的目录
    save_dir = r'd:\images'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    try:
        # 添加请求头避免被识别为爬虫
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }

        # 向目标网站发送请求并获取网页源码
        rs = requests.get(url, headers=headers)
        rs.encoding = "gbk"

        # 检查请求是否成功
        if rs.status_code != 200:
            print(f"请求失败，状态码: {rs.status_code}")
            return

        # 解析网页内容
        body = rs.text
        html = etree.HTML(body)

        # 获取图片路径列表
        listImg = html.xpath("//ul[@class='clearfix']/li/a/span/img/@src")
        print(f"找到 {len(listImg)} 张图片")

        if not listImg:
            print("未找到任何图片")
            return

        # 下载每张图片
        for i, img_src in enumerate(listImg, 1):
            try:
                # 拼接完整的图片URL
                if img_src.startswith("http"):
                    file_path = img_src
                else:
                    # 正确处理相对路径
                    if not img_src.startswith("/"):
                        img_src = "/" + img_src
                    file_path = f"http://pic.netbian.com{img_src}"

                # 获取图片内容
                img_response = requests.get(file_path, headers=headers)

                # 检查图片响应状态
                if img_response.status_code != 200:
                    print(f"图片 {file_path} 下载失败，状态码: {img_response.status_code}")
                    continue

                # 从URL中提取文件扩展名
                if '.' in img_src:
                    extension = img_src.split('.')[-1].lower()
                    # 确保扩展名有效
                    if extension not in ['jpg', 'jpeg', 'png', 'gif', 'webp']:
                        extension = 'jpg'  # 默认使用jpg格式
                else:
                    extension = 'jpg'

                # 保存路径
                save_path = os.path.join(save_dir, f'image_{i}.{extension}')

                # 保存图片
                with open(save_path, 'wb') as f:
                    f.write(img_response.content)

                print(f"已下载图片 {i}/{len(listImg)}: {save_path}")

            except Exception as e:
                print(f"下载图片 {file_path} 时出错: {e}")

        print("所有图片下载完毕")

    except Exception as e:
        print(f"程序出错: {e}")


if __name__ == "__main__":
    download_images()