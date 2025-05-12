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
    def test_TC_E_001(self, driver:WebDriver):
        team_dinner = TeamDinner(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_E_001. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)
        
        # 메인에서 회식하기 버튼 검증
        TEAM_BUTTON = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[3]')))
        assert TEAM_BUTTON.is_displayed(),"❌'📅회식하기' 버튼 오류"
        logging.info("✅ '📅회식하기' 버튼 정상 출력")
    
    
        # 회식하기 페이지 이동
        TEAM_BUTTON.click()
        logging.info("🔍 회식하기 페이지 이동중...")
        WebDriverWait(driver, 5).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"))
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/team"
        logging.info("✅ '📅회식하기' 페이지 정상 이동 완료.")
    
    
        # 카테고리 버튼 검증                                
        categorybutton = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button')
        assert categorybutton.is_displayed(),"❌음식 카테고리 버튼 오류"
        logging.info("✅ 카테고리 버튼 정상 출력")
