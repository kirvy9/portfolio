import time
import pytest
import random
import logging
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.loginPage import LoginPage
from src.pages.teamPage import TeamPage


@pytest.mark.usefixtures("driver")
class TestCaseH:
    def test_case_H_003(self, driver:WebDriver):
        try:

            wait = ws(driver, 10)
            login=LoginPage(driver)
            team=TeamPage(driver)

            logging.info("Preconditon")


            email="team2@example.co.kr"
            password="Team2@@@"
            login.do_login(email,password)

            my_team= team.my_team()
            logging.info("내 팀 : %s",my_team)

            logging.info("test_case_H_003")


            team_select_btn =wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@role='combobox']")))  #팀 선택 버튼
            team_select_btn.click() 

            teams_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='option']")))   #눌렀을떄 뜨는 팀 목록
            random_not_my_team = [option for option in teams_options if my_team not in option.text] # 내 팀 제외
            selected_not_my_team = random.choice(random_not_my_team) # 내 팀 제외 랜덤 선택
            logging.info(f"선택된 옵션: {selected_not_my_team.text}")
            selected_not_my_team.click()


            team.scroll_down()
            same_menu_btns = driver.find_elements(By.XPATH, "//button[contains(text(), '같은 메뉴 먹기')]")   #같은 메뉴 먹기 버튼(같은 팀에서만 존재)
            assert len(same_menu_btns) == 0, f"'같은 메뉴 먹기' 버튼이 존재합니다!!"
            logging.info("다른팀 test 완료")


            team.scroll_to_top()  # 다시 맨 위로 이동
            time.sleep(2)


            team_select_btn =wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@role='combobox']")))  #팀 선택 버튼
            team_select_btn.click() 
            time.sleep(2)
            teams_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='option']")))
            random_my_team = [option for option in teams_options if my_team in option.text]
            selected_my_team = random.choice(random_my_team)
            logging.info(f"선택된 옵션: {selected_my_team.text}")
            selected_my_team.click()

            same_menu_btns = driver.find_elements(By.XPATH, "//button[contains(text(), '같은 메뉴 먹기')]")  #다시 찾기
            team.scroll_down()
            assert len(same_menu_btns) > 0, "다른팀입니다."



            logging.info("test_case_H_003 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


