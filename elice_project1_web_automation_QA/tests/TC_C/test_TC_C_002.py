import pytest
import logging
from selenium import webdriver  # 브라우저 제어
from selenium.webdriver.common.by import By  # HTML 요소 탐색
from selenium.webdriver.support.ui import WebDriverWait  # 특정 요소가 나타날 때까지 대기
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver 
from src.pages.solo_eat import SoloEat
from src.pages.loginPage import LoginPage



@pytest.mark.usefixtures("driver")
class TestCaseC:
    def test_TC_C_002(self, driver:WebDriver):
        solo_eat = SoloEat(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_C_002. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)

        # 메인에서 혼자먹기 페이지 이동 
        solo_eat.go_solo_eat()
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone","❌혼자먹기 페이지 이동 오류"
        logging.info("✅ '👤혼자먹기' 페이지 정상 이동 완료.")

        # 먹는 인원에 대한 검증
        USER_PROFILE = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[2]/div/div')))
        assert USER_PROFILE[0].is_displayed(),"❌먹는 인원 오류"
        logging.info(f"🙌먹는 인원 : {len(USER_PROFILE)} 명")
        logging.info("✅ 유저 프로필 정상 출력")
        USER_NAME = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[2]/div/div/div[1]')))
        assert USER_NAME.is_displayed(),"❌유저 이름 오류"
        USER_TEAM = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[2]/div/div/div[2]')))
        assert USER_TEAM.is_displayed(),"❌유저 소속 팀 오류"
        logging.info(f"\n 이름 : {USER_NAME.text}\n 소속 팀 : {USER_TEAM.text}")
