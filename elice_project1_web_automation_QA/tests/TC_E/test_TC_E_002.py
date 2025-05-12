import pytest
import logging
from selenium import webdriver  # 브라우저 제어
from selenium.webdriver.common.by import By  # HTML 요소 탐색
from selenium.webdriver.support.ui import WebDriverWait  # 특정 요소가 나타날 때까지 대기
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.webdriver import WebDriver 
from src.pages.loginPage import LoginPage
from src.pages.team_dinner import TeamDinner





@pytest.mark.usefixtures("driver")
class TestCaseE:
    def test_TC_E_002(self, driver:WebDriver):
        team_dinner = TeamDinner(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_E_002. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)
    
    
        # 회식하기 페이지 이동
        team_dinner.go_team_dinner()
        WebDriverWait(driver, 5).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"))
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"
        logging.info("✅ '📅회식하기' 페이지 정상 이동 완료.")
    
    
        # 먹는 인원(팀)에 대한 검증
        USER_TEAM = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[2]/div/span')))
        assert USER_TEAM.is_displayed(),"❌먹는 인원 오류"
        logging.info(f"🙌먹는 인원 : {USER_TEAM.text}")
        logging.info("✅ 소속 팀 정상 출력")
                                                 
        # 카테고리 설정
        team_dinner.category_select()
        CATEGORY_BOX = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button/span')))
        assert CATEGORY_BOX.text != "음식 카테고리를 설정해주세요","❌음식 카테고리 선택 오류"
        logging.info("✅ 카테고리 설정 완료")
