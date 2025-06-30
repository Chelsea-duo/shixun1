import requests
from lxml import etree
import json


def fetch_job_data():
    url = "https://we.51job.com/pc/search?jobArea=090200&keyword=java&searchType=2&sortType=0&metro="

    # 更新请求头，添加更多字段避免被识别为爬虫
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'https://we.51job.com/',
        'Upgrade-Insecure-Requests': '1'
    }

    try:
        # 添加超时参数
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = "utf-8"  # 改为utf-8编码，更通用

        # 检查响应状态
        if response.status_code != 200:
            print(f"请求失败，状态码: {response.status_code}")
            return

        # 使用更健壮的方式提取JSON数据
        script_content = response.text
        start_index = script_content.find('{')
        if start_index == -1:
            print("未找到有效JSON数据")
            return

        json_str = script_content[start_index:-1]  # 去掉最后的';'

        # 解析JSON
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
            return

        # 提取招聘信息
        job_list = data.get("engine_search_result", [])

        if not job_list:
            print("未找到招聘信息")
            return

        print(f"共找到 {len(job_list)} 条招聘信息:")
        print("-" * 70)

        # 格式化输出
        for idx, job in enumerate(job_list, 1):
            print(f"【{idx}】职位: {job.get('job_name', '未知职位')}")
            print(f"    公司: {job.get('company_name', '未知公司')}")
            print(f"    薪资: {job.get('providesalary_text', '薪资面议')}")
            print(f"    地点: {job.get('workarea_text', '未知地点')}")
            print(f"    经验: {job.get('workyear', '经验不限')}")
            print(f"    学历: {job.get('degreefrom', '学历不限')}")
            print(f"    福利: {job.get('jobwelf', '无')}")
            print("-" * 70)

    except requests.exceptions.RequestException as e:
        print(f"网络请求出错: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


# 调用函数
if __name__ == "__main__":
    fetch_job_data()