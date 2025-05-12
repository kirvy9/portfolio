import time
import pytest
import logging
from selenium.webdriver.chrome.webdriver import WebDriver
from src.pages.signupPage import SignupPage
from selenium.webdriver.support.ui import WebDriverWait as ws


@pytest.mark.usefixtures("driver")
class TestCase_B:
    def test_Case_B_01(self, driver:WebDriver):
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


        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False

