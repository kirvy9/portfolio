import time
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

class ResetPasswordPage:
    URL = "https://kdt-pt-1-pj-2-team03.elicecoding.com/signin"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        #사이트에 접속하고 로그인 버튼을 클릭
        self.driver.get(self.URL)
        login_button = ws(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='로그인하기']"))
        )
        login_button.click()

    def reset_password(self):
        #비밀번호 찾기 페이지로 이동
        forgot_password = ws(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "비밀번호를 잊으셨나요?"))
        )
        forgot_password.click()

    def fill_email_form(self, email):
        #이메일 입력 필드에 이메일 입력 후 계속 버튼 클릭
        wait = ws(self.driver, 10)

        email_field = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
        )
        email_field.send_keys(email)

        continue_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@name='action' and @value='default' and contains(text(), '계속')]")
            )
        )
        continue_btn.click()