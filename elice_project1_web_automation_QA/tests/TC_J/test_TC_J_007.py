import pytest
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from src.pages.profile import profile
from src.pages.loginPage import LoginPage


@pytest.mark.usefixtures("driver")
class TestCaseJ:

    def test_case_J_007(self, driver: WebDriver):
        

        
        profile_page = profile(driver)
        login_page = LoginPage(driver)
        wait = ws(driver, 10)

        try:
            
            # 로그인 로직 실행
            test_email = "testid@test.com"
            test_password = "testpw1!"
            login_page.do_login(test_email, test_password)
            time.sleep(2)  

            # 개인 피드 접근
            profile_page.peed_open()
            time.sleep(2)  

            #개인 피드 접근 검증
            current_url = driver.current_url
            expected_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/my"

            assert current_url == expected_url, f"❌ 예상 URL: {expected_url}, 실제 URL: {current_url}"

            # 프로필 수정 페이지 접근
            profile_page.profile_modify()
            time.sleep(2)


            # 싫어하는 음식 입력
            print("🔧 싫어하는 음식 입력 중...")
            profile_page.hate_food()
            time.sleep(1)


            # 수정 완료 버튼 클릭
            print("✅ 수정 완료 버튼 클릭!")
            profile_page.modify_access()
            time.sleep(2)

            #싫어하는 음식 검증
            hate_xpath = '//*[@id="root"]/div[1]/main/section/section/section/div[2]/div[2]/p'

            hate_text = wait.until(EC.presence_of_element_located((By.XPATH, hate_xpath))).text

            # 비교 로직
            assert hate_text == "싫어하는 음식 테스트 입니다.", "❌ 싫어하는 음식 텍스트 값 불일치!"

            print("✅ 싫어하는 음식 검증 완료!")
            
        except Exception as e:
            print(f"⚠️ 테스트 실패: {e}")
            assert False