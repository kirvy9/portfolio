import pytest
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from src.pages.profile import profile
from src.pages.loginPage import LoginPage


@pytest.mark.usefixtures("driver")
class TestCaseJ:

    def test_case_J_003(self, driver: WebDriver):
        

        
        profile_page = profile(driver)
        login_page = LoginPage(driver)

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

            #단맛 슬라이더 조절 ( 3 )
            slider_name = "단맛"
            target_value = 3.0
            print(f"🔧 {slider_name} 슬라이더 값을 {target_value}로 설정 중...")
            profile_page.drag_slider(slider_name, target_value)
            time.sleep(2)

            
        except Exception as e:
            print(f"⚠️ 테스트 실패: {e}")
            assert False