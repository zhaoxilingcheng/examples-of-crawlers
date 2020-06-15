from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


def login_and_get_cookie(username, password):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('--disable-gpu')
    # options.add_argument('–no-sandbox')
    options.add_argument('--proxy-server=http://127.0.0.1:9000')
    # 隐藏滚动条, 应对一些特殊页面
    options.add_argument('--hide-scrollbars')
    # 不加载图片
    options.add_argument('blink-settings=imagesEnabled=false')
    # 无头模式
    # options.add_argument('--headless')
    driver = webdriver.Chrome(binary_location, chrome_options=options)
    driver.maximize_window()
    status = driver.get("https://login.taobao.com")
    # 设置显示等待
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'fm-login-id')))

    # 进行填写
    user_input = driver.find_element_by_id("fm-login-id")
    user_input.send_keys(str(username))
    password_input = driver.find_element_by_id("fm-login-password")
    password_input.send_keys(str(password))
    time.sleep(1)

    # 判断验证码
    captcha = driver.find_elements_by_id('nc_1_n1z')
    if captcha:
        button = driver.find_element_by_id('nc_1_n1z')
        ActionChains(driver).click_and_hold(button).perform()
        ActionChains(driver).move_by_offset(258, 0).perform()
        ActionChains(driver).release(button).perform()
        time.sleep(2)
    # 点击登录按钮
    login_butt = driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button')
    login_butt.click()

    # 进行判断是否登录成功
    user_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'site-nav-login-info-nick')))
    print(user_name.text)
    cookies = driver.get_cookies()
    driver.quit()
    return cookies


if __name__ == '__main__':
    # 驱动地址
    # 修改为对应谷歌浏览器版本的驱动
    binary_location = '../chromedriver'
    login_and_get_cookie('username', 'password')
