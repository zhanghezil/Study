from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract  # 需安装Tesseract
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# ------------------------------
# 新增验证码处理工具函数
# ------------------------------
def get_and_recognize_captcha(driver, element, save_path="captcha.png"):
    """验证码识别全流程"""
    # 截图验证码区域
    location = element.location
    size = element.size
    driver.save_screenshot(save_path)

    # 计算坐标
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']

    # 裁剪图像
    img = Image.open(save_path)
    captcha_img = img.crop((left * 2, top * 2, right * 2, bottom * 2))  # Retina屏需*2

    # 图像预处理（根据实际验证码调整）
    captcha_img = captcha_img.convert('L')  # 灰度化
    captcha_img.save(save_path)

    # OCR识别
    return pytesseract.image_to_string(captcha_img).strip()


# ------------------------------
# 修改后的主流程代码
# ------------------------------
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
service = Service('/Users/zhzzzz/Documents/study/chromedriver-mac-arm64/chromedriver')  # M2常用路径
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get('http://10.125.20.60:8088/login')

    # 定位验证码元素（根据实际页面调整定位方式）
    captcha_element = driver.find_element(By.XPATH, "//img[@class='captcha-img']")

    # 识别验证码
    captcha_text = get_and_recognize_captcha(driver, captcha_element)
    print(f"识别结果: {captcha_text}")

    # 输入验证码
    driver.find_element(By.ID, "captcha_input").send_keys(captcha_text)
    driver.find_element(By.ID, "submit_btn").click()

    time.sleep(2)  # 等待提交结果

finally:
    driver.quit()
