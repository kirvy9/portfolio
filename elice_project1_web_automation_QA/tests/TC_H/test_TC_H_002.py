import pytest
import random
import logging
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from src.pages.loginPage import LoginPage
from src.pages.teamPage import TeamPage


@pytest.mark.usefixtures("driver")
class TestCaseH:
    def test_case_H_002(self, driver: WebDriver):
        wait = ws(driver, 10)
        login = LoginPage(driver)
        team = TeamPage(driver)

        logging.info("🔹 Precondition 시작")

        email = "team2@example.co.kr"
        password = "Team2@@@"
        
        try:
            login.do_login(email, password)

            my_team = team.my_team()
            logging.info(f"내 팀: {my_team}")

            logging.info("🔹 test_case_H_002 시작")

            first_team_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "bg-sub-2")]//span')))
            first_team = first_team_element.text

            team_select_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@role='combobox']")))  
            team_select_btn.click() 

            teams_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='option']")))

            # 내 팀 제외한 팀 목록 필터링
            random_not_first_team = [option for option in teams_options if first_team not in option.text]
            if not random_not_first_team:
                pytest.fail("❌ 선택할 다른 팀이 없습니다.")

            selected_not_first_team = random.choice(random_not_first_team)

            # 🔹 Stale Element 방지: 요소를 다시 찾고 클릭
            for _ in range(3):
                try:
                    selected_not_first_team.click()
                    break
                except StaleElementReferenceException:
                    logging.warning("⚠️ StaleElementReferenceException 발생, 팀 선택 요소 다시 찾는 중...")
                    teams_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='option']")))
                    random_not_first_team = [option for option in teams_options if first_team not in option.text]
                    selected_not_first_team = random.choice(random_not_first_team)

            second_team_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "bg-sub-2")]//span')))
            second_team = second_team_element.text

            assert second_team != first_team, "❌ 팀 변경이 되지 않았습니다."

            logging.info("✅ test_case_H_002 테스트 완료")

        except Exception as e:
            pytest.fail(f"❌ 테스트 중 오류 발생: {e}")
