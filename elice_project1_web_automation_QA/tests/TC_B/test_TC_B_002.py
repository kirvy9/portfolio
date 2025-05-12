import time
import pytest
import logging
from selenium.webdriver.chrome.webdriver import WebDriver
from src.pages.signupPage import SignupPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver")
class TestCase_B:
    def test_Case_B_02(self, driver:WebDriver):
        try : 
            #Test 시작
            logging.info("[테스트 시작] 회원가입 프로세스를 시작합니다.")
            signupPage = SignupPage(driver)
            wait = ws(driver, 10)

            signupPage.open()
            time.sleep(1)
            logging.info("회원가입 페이지 열기 완료")
            
            signupPage.go_signup()
            time.sleep(1)
            logging.info("회원가입 폼으로 이동 완료")

            # 1. 소문자 입력 후 clear
            password_field_test = driver.find_element(By.XPATH, "//input[@id='password']")
            password_field_test.send_keys("a")  # 소문자 'a' 입력
            time.sleep(1)
            password_field_test.clear()  # 입력 후 클리어
            time.sleep(1)

            # 2. 대문자 입력 후 clear
            password_field_test.send_keys("A")  # 대문자 'A' 입력
            time.sleep(1)
            password_field_test.clear()  # 입력 후 클리어
            time.sleep(1)

            # 3. 숫자 입력 후 clear
            password_field_test.send_keys("1")  # 숫자 '1' 입력
            time.sleep(1)
            password_field_test.clear()  # 입력 후 클리어
            time.sleep(1)

            # 4. 특수문자 입력 후 clear
            password_field_test.send_keys("!")  # 특수문자 '!' 입력
            time.sleep(1)
            password_field_test.clear()  # 입력 후 클리어
            time.sleep(1)

            wait = ws(driver, 10)

            #정상적으로 이메일, 비밀번호 입력
            email, password=signupPage.generate_random_email_and_password()
            logging.info("이메일 : %s, 비밀번호 %s", email, password)
            time.sleep(1)

            signupPage.fill_signup_form(email,password)
            time.sleep(3)
            logging.info("이메일 및 비밀번호 입력 완료")

        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False

