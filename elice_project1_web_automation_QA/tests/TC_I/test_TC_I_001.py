import pytest
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.loginPage import LoginPage

@pytest.mark.usefixtures("driver")
class TestCaseI:

    def test_case_I_001(self, driver: WebDriver):

        login_page = LoginPage(driver)
        wait = ws(driver, 10)


        try:
            
            

            # 테스트용 로그인 로직 실행
            test_email = "testid@test.com"
            test_password = "testpw1!"
            login_page.do_login(test_email, test_password)
            time.sleep(2)


            #개인 피드 접근 
            mypd = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div/ul/li[4]/a")))
            mypd.click()

            time.sleep(2)

            #개인 피드 접근 검증
            current_url = driver.current_url
            expected_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/my"

            assert current_url == expected_url, f"❌ 예상 URL: {expected_url}, 실제 URL: {current_url}"

        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False