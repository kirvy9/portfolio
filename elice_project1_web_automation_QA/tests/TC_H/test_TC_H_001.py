import pytest
import logging
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from src.pages.loginPage import LoginPage
from src.pages.teamPage import TeamPage

@pytest.mark.usefixtures("driver")
class TestCaseH:
    def test_case_H_001(self, driver: WebDriver):
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

            logging.info("🔹 test_case_H_001 시작")

            # 팀 이름 요소 찾기 (최대 3회 재시도)
            max_attempts = 3
            for attempt in range(max_attempts):
                try:
                    team_feed_team = wait.until(EC.presence_of_element_located(
                        (By.XPATH, '//div[contains(@class, "bg-sub-2")]//span')
                    )).text
                    logging.info(f"✅ 팀 피드에 표시된 팀명: {team_feed_team}")
                    break
                except (StaleElementReferenceException, TimeoutException) as e:
                    logging.warning(f"⚠️ 팀 이름 요소 재시도 중... ({attempt+1}/{max_attempts})")
                    if attempt == max_attempts - 1:
                        pytest.fail(f"❌ 팀 정보를 가져올 수 없습니다: {e}")

            # 팀 이름 검증
            assert my_team == team_feed_team, f"❌ 팀이 다릅니다! 예상: {my_team}, 실제: {team_feed_team}"

            logging.info("✅ test_case_H_001 테스트 완료")

        except Exception as e:
            pytest.fail(f"❌ 테스트 중 오류 발생: {e}")
