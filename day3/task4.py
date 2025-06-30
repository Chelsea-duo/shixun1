import time
import random
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 待获取文献列表
LITERATURE_LIST = [
    "Automatic crater detection and age estimation for mare regions on the lunar surface",
    "The origin of planetary impactors in the inner solar system",
    "Deep learning based systems for crater detection: A review",
    "A preliminary study of classification method on lunar topography and landforms",
    "The CosmoQuest Moon mappers community science project: The effect of incidence angle on the Lunar surface crater distribution",
    "Fast r-cnn",
    "You only look once: Unified, real-time object detection",
    "Attention is all you need",
    "End-to-end object detection with transformers"
]

# 人类行为模拟参数
HUMAN_PARAMS = {
    "min_scroll_steps": 3,
    "max_scroll_steps": 8,
    "min_mouse_moves": 3,
    "max_mouse_moves": 7,
    "base_delay": (1.5, 4.0),
    "typing_speed": (0.08, 0.15)
}


def setup_stealth_browser():
    """配置隐身浏览器并设置反检测参数"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--start-maximized')

    # 随机用户代理
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    ]
    chrome_options.add_argument(f'user-agent={random.choice(user_agents)}')

    # 初始化浏览器
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 隐藏自动化特征
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver


def human_mouse_movement(driver):
    """模拟人类鼠标移动轨迹"""
    try:
        width = driver.execute_script("return document.documentElement.scrollWidth")
        height = driver.execute_script("return document.documentElement.scrollHeight")
        actions = ActionChains(driver)

        moves = random.randint(HUMAN_PARAMS["min_mouse_moves"], HUMAN_PARAMS["max_mouse_moves"])
        for _ in range(moves):
            x = random.randint(0, width)
            y = random.randint(0, height // 2)  # 主要在上半屏活动
            actions.move_to_element_with_offset(
                driver.find_element(By.TAG_NAME, 'body'),
                x, y
            ).pause(random.uniform(0.2, 0.8))
        actions.perform()
    except Exception as e:
        print(f"⚠️ 鼠标模拟异常: {str(e)[:70]}...")


def human_scroll(driver):
    """模拟人类滚动行为"""
    try:
        total_height = driver.execute_script("return document.body.scrollHeight")
        scroll_steps = random.randint(HUMAN_PARAMS["min_scroll_steps"], HUMAN_PARAMS["max_scroll_steps"])
        scroll_distance = total_height / scroll_steps

        for i in range(scroll_steps):
            scroll_by = random.randint(int(scroll_distance * 0.7), int(scroll_distance * 1.3))
            driver.execute_script(f"window.scrollBy(0, {scroll_by});")
            time.sleep(random.uniform(0.5, 1.8))

            # 随机回滚
            if random.random() > 0.8:
                driver.execute_script("window.scrollBy(0, -100);")
                time.sleep(random.uniform(0.3, 1.0))
    except Exception as e:
        print(f"⚠️ 滚动模拟异常: {str(e)[:50]}...")


def enable_bibtex_export(driver):
    """启用BibTeX导出功能（关键步骤）:cite[1]"""
    try:
        # 访问设置页面
        driver.get("https://scholar.google.com/scholar_settings?hl=en")
        time.sleep(random.uniform(2.0, 3.5))

        # 勾选BibTeX选项
        bibtex_checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[contains(., 'Show links to import citations into BibTeX')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", bibtex_checkbox)
        time.sleep(1)
        bibtex_checkbox.click()

        # 保存设置
        save_btn = driver.find_element(By.ID, "gs_settings_btn")
        save_btn.click()
        time.sleep(random.uniform(1.5, 2.5))
        print("✅ BibTeX导出功能已启用")
        return True
    except Exception as e:
        print(f"❌ BibTeX设置失败: {str(e)[:80]}...")
        return False


def human_type(element, text):
    """模拟人类输入速度"""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(*HUMAN_PARAMS["typing_speed"]))
        # 随机输入错误并修正
        if random.random() < 0.1:
            element.send_keys(random.choice(['a', 'e', 'i', 'o', 'u']))
            time.sleep(0.2)
            element.send_keys('\ue003')  # 退格键


def get_bibtex_from_result(driver):
    """从搜索结果页提取BibTeX:cite[1]"""
    try:
        # 定位BibTeX链接
        bibtex_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'BibTeX')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", bibtex_link)

        # 人类行为模拟
        time.sleep(random.uniform(0.8, 1.5))
        human_mouse_movement(driver)

        # 点击链接
        bibtex_link.click()
        time.sleep(random.uniform(1.0, 2.0))

        # 获取BibTeX内容
        bibtex_content = WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located((By.TAG_NAME, "pre"))
        ).text
        return bibtex_content
    except Exception as e:
        print(f"❌ BibTeX提取失败: {str(e)[:60]}...")
        return None


def search_scholar(driver, query, retry=0):
    """执行Google学术搜索并获取BibTeX"""
    try:
        driver.get("https://scholar.google.com")
        time.sleep(random.uniform(*HUMAN_PARAMS["base_delay"]))

        # 定位搜索框
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        # 模拟人类交互
        human_mouse_movement(driver)
        time.sleep(random.uniform(0.5, 1.2))

        # 清空并输入查询
        search_box.clear()
        human_type(search_box, query)
        time.sleep(random.uniform(0.3, 0.9))

        # 提交搜索
        search_box.submit()
        time.sleep(random.uniform(2.5, 4.0))

        # 模拟浏览行为
        human_scroll(driver)
        time.sleep(random.uniform(1.0, 2.0))

        # 获取第一条结果的BibTeX
        return get_bibtex_from_result(driver)

    except Exception as e:
        if retry < 2:
            print(f"⚠️ 搜索异常，重试中({retry + 1}/2)...")
            return search_scholar(driver, query, retry + 1)
        print(f"❌ 搜索失败: {str(e)[:70]}...")
        return None


def save_results(bibtex_data, filename="literature_bibtex.csv"):
    """保存结果到CSV文件"""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'BibTeX'])
            for title, bibtex in bibtex_data:
                # 清理换行符
                cleaned_bibtex = bibtex.replace('\n', '\\n').replace('\r', '')
                writer.writerow([title, cleaned_bibtex])
        print(f"💾 结果已保存至 {filename}")
    except Exception as e:
        print(f"❌ 保存失败: {e}")


def main():
    print("🚀 启动Google学术BibTeX爬虫")
    driver = setup_stealth_browser()
    results = []

    try:
        # 步骤1: 启用BibTeX导出 :cite[1]
        if not enable_bibtex_export(driver):
            print("⚠️ 无法启用BibTeX功能，可能影响后续操作")

        # 步骤2: 遍历文献列表
        total = len(LITERATURE_LIST)
        for idx, title in enumerate(LITERATURE_LIST):
            print(f"\n🔍 [{idx + 1}/{total}] 正在获取: \"{title[:40]}{'...' if len(title) > 40 else ''}\"")

            # 随机延迟
            delay = random.uniform(6.0, 15.0)
            print(f"⏳ 模拟人类思考 {delay:.1f}秒...")
            time.sleep(delay)

            # 执行搜索
            bibtex = search_scholar(driver, title)

            if bibtex:
                results.append((title, bibtex))
                print(f"✅ 成功获取 {len(bibtex)} 字符的BibTeX")
            else:
                print(f"❌ 未找到文献: {title[:50]}...")
                results.append((title, "NOT_FOUND"))

            # 随机长暂停 (每3次)
            if (idx + 1) % 3 == 0 and idx < total - 1:
                long_delay = random.uniform(25.0, 40.0)
                print(f"🕒 防爬虫休眠 {long_delay:.1f}秒...")
                time.sleep(long_delay)

        # 保存结果
        if results:
            save_results(results)
            print("\n" + "=" * 50)
            print(f"✅ 完成! 成功获取 {len([r for r in results if r[1] != 'NOT_FOUND'])}/{total} 篇文献的BibTeX")
            print("=" * 50)

            # 打印样例
            print("\n📄 样例输出 (第一篇文献):")
            print(results[0][1][:300] + "..." if results[0][1] != "NOT_FOUND" else "NOT_FOUND")
        else:
            print("❌ 未获取到任何有效数据")

    except Exception as e:
        print(f"💥 致命错误: {e}")
    finally:
        driver.quit()
        print("🛑 浏览器已关闭")


if __name__ == "__main__":
    main()