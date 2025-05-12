import time
import pytest
import logging
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from faker import Faker
from src.pages.signupPage import SignupPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures("driver")
class TestCase_B:
    def test_Case_B_04(self, driver:WebDriver):
        try : 
            #Test 시작
            logging.info("[테스트 시작] 회원가입 프로세스를 시작합니다.")
            signupPage = SignupPage(driver)
            wait = ws(driver, 10)
            faker = Faker()

            signupPage.open()
            time.sleep(1)
            logging.info("회원가입 페이지 열기 완료")
            
            signupPage.go_signup()
            time.sleep(1)
            logging.info("회원가입 폼으로 이동 완료")

            email, password=signupPage.generate_random_email_and_password()
            logging.info("이메일 : %s, 비밀번호 %s", email, password)
            time.sleep(1)

            signupPage.fill_signup_form(email,password)
            time.sleep(1)
            logging.info("이메일 및 비밀번호 입력 완료")

            signupPage.accept_btn()
            logging.info("Accept 버튼 클릭 완료")
            time.sleep(1)

            name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='name']")))
            name = faker.name()
            name_field.send_keys(name)
            time.sleep(1)
            logging.info("내 이름 : %s",name)

            assert name_field.get_attribute("value") == name, "이름 입력이 정상적으로 되지 않았습니다."
            logging.info("이름 입력 완료")

        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False

