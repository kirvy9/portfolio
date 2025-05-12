import time
import pytest
import logging
from selenium.webdriver.chrome.webdriver import WebDriver
from faker import Faker
from src.pages.reset_password import ResetPasswordPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestCase_A:
    def test_Case_A_02(self, driver:WebDriver):
        try:
            logging.info("로그인 비밀번호 찾기를 시작합니다.")
            faker = Faker()
            email = faker.email() 
            reset_password = ResetPasswordPage(driver)

            reset_password.open()
            time.sleep(1)

            reset_password.reset_password()
            logging.info("'비밀번호를 잊으셨나요?' 버튼을 클릭합니다.")
            time.sleep(1)

            reset_password.fill_email_form(email)
            logging.info("이메일 입력 / '계속' 버튼을 클릭합니다.") 
            time.sleep(1)

            wait = ws(driver, 10)

            wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Resend email')]"))
            )
            logging.info("로그인 비밀번호 찾기를 종료합니다.")

        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False