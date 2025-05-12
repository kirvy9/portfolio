import pytest
import random
import logging
import time
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from src.pages.loginPage import LoginPage
from src.pages.teamPage import TeamPage

@pytest.mark.usefixtures("driver")
class TestCaseH:
    def test_case_H_016(self, driver: WebDriver):
        wait = ws(driver, 10)
        login = LoginPage(driver)
        team = TeamPage(driver)

        logging.info("🔹 Precondition 시작")

        email = "team2@example.co.kr"
        password = "Team2@@@"

        try:
            login.do_login(email, password)
            my_team = team.my_team()
            logging.info(f"✅ 내 팀: {my_team}")
            time.sleep(2)

            # 프로필 수정 버튼 클릭
            max_attempts = 3  # 최대 3회 재시도
            for attempt in range(max_attempts):
                try:
                    correction_btn = wait.until(EC.element_to_be_clickable((
                        By.CSS_SELECTOR, '#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > section > section > div.flex.items-center.w-full.gap-4 > div > div > svg'
                    )))
                    correction_btn.click()
                    logging.info("✅ 프로필 수정 버튼 클릭 성공")
                    break
                except (StaleElementReferenceException, TimeoutException) as e:
                    logging.warning(f"⚠️ 프로필 수정 버튼 재시도 중... ({attempt+1}/{max_attempts})")
                    if attempt == max_attempts - 1:
                        pytest.fail(f"❌ 프로필 수정 버튼을 찾을 수 없음: {e}")

            # 프로필 수정 페이지 진입 확인
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='프로필 정보 수정']")))
            logging.info("✅ 프로필 정보 수정 페이지 진입 성공")

            # 장점 입력
            good_comment = ''.join([chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)])  # 한글 10글자 랜덤 생성
            good_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='pros']")))
            good_input.clear()
            good_input.send_keys(good_comment)
            logging.info(f"✅ 장점 입력 완료: {good_comment}")

            # 단점 입력
            bad_comment = ''.join([chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)])  # 한글 10글자 랜덤 생성
            bad_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='cons']")))
            bad_input.clear()
            bad_input.send_keys(bad_comment)
            logging.info(f"✅ 단점 입력 완료: {bad_comment}")

            logging.info("✅ test_case_H_016 테스트 완료")

        except Exception as e:
            pytest.fail(f"❌ 테스트 중 오류 발생: {e}")
