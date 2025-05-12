import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from src.pages.loginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver")
class TestCase_A:
    def test_Case_A_01(self, driver:WebDriver):
        try:
            login_page = LoginPage(driver)
            login_page.open()

            time.sleep(1)

            email="team2@example.co.kr"
            password="Team2@@@"
            login_page.input_password_and_email(email,password)
            time.sleep(1)

            ws(driver, 10).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/"))  # URL 변경 확인
            assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/"

        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False