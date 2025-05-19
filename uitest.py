from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------------------------
# 初始化浏览器配置（无头模式）
# ------------------------------
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
service = Service('/Users/zhzzzz/Documents/study/chromedriver-mac-arm64/chromedriver')  # 替换为你的ChromeDriver路径
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # ------------------------------
    # 唯一测试场景：验证页面基础加载
    # ------------------------------
    driver.get('http://10.125.20.60:8088/login')  # 替换为实际URL

    # 断言1：验证页面标题是否正确
    assert "数据安全事件发现与有效响应系统" in driver.title, \
        f"标题校验失败，当前标题：{driver.title}"

    # 断言2：验证关键JS资源是否加载（jQuery示例）
    jquery_loaded = driver.execute_script("return typeof jQuery !== 'undefined';")
    assert jquery_loaded, "jQuery未正确加载"

    # 断言3：验证核心CSS文件是否加载（通过检查某个元素的样式）
    body_element = driver.find_element(By.TAG_NAME, 'body')
    assert body_element.value_of_css_property('font-family') != 'serif', \
        "基础CSS样式未生效"

finally:
    driver.quit()
