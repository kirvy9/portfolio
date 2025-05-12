import time
import pytest
import logging
from selenium import webdriver  # 브라우저 제어
from selenium.webdriver.common.by import By  # HTML 요소 탐색
from selenium.webdriver.support.ui import WebDriverWait  # 특정 요소가 나타날 때까지 대기
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.webdriver import WebDriver 
from src.pages.loginPage import LoginPage





@pytest.mark.usefixtures("driver")
class TestCaseF:
    def test_TC_F_002(self, driver:WebDriver):
        login_page = LoginPage(driver)
        logging.info("\n[Test_F_002. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)
       


        # 메인 타이틀 검증임
        TITLE = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/header/div/span')))
        title = TITLE.text
        assert title == "오늘 뭐먹지 ?","❌ 타이틀 오류"
        logging.info(f"✅ 타이틀 출력 : {title}")

        # 메뉴 버튼 검증
        SOLO_BUTTON = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[1]/div/p')))
        SOLO = SOLO_BUTTON.text
        
        TOGETHER_BUTTON = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[2]/div/p')))
        TOGETHER = TOGETHER_BUTTON.text

        TEAM_BUTTON = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[3]/div/p')))
        TEAM = TEAM_BUTTON.text

        assert SOLO_BUTTON.is_displayed(),"❌ '혼자먹기' 버튼 오류"
        assert TOGETHER_BUTTON.is_displayed(),"❌ '같이먹기' 버튼 오류"
        assert TEAM_BUTTON.is_displayed(),"❌ '회식하기' 버튼 오류"
        logging.info(f"'{SOLO}' '{TOGETHER}' '{TEAM}'")
        logging.info("✅ 상단 버튼 출력")
        

        # 홈에 그래프 검증
        GRAPH = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[2]/div/div/canvas')))
        assert GRAPH.is_displayed(),"❌ 출력 오류 (그래프)"
        logging.info("✅ 그래프 출력")

        # 추천 메뉴 이미지
        RECOMMEND_IMAGE = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[3]/div[2]/div[1]')))
        assert RECOMMEND_IMAGE.is_displayed(),"❌ 추천 메뉴 이미지 오류"
        logging.info("✅ 추천 메뉴 이미지 출력")

        # 추천 메뉴
        RECOMMEND_DISH = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[3]/div[2]/p')))
        assert RECOMMEND_DISH.is_displayed(),"❌ 추천 메뉴 오류"
        DISH = RECOMMEND_DISH.text
        logging.info(f"✅ {DISH}")

        # AI 분석
        AI = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[3]/div[2]/div[2]/span')))
        ai = AI.text
        PERCENT = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[3]/div[2]/div[2]/div')))
        percent = PERCENT.text
        assert AI,"❌ 분석오류"
        assert PERCENT,"❌ 분석오류"
        logging.info(f"✅ {ai} : {percent}")

        # 하단 버튼 검증
        HOME = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[1]/a')))
        assert HOME.is_displayed(),"❌ 홈 오류 "
        TEAM_PID = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[2]/a')))                                               
        assert TEAM_PID.is_displayed(),"❌ 팀 피드 오류"
        HISTORY = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[3]/a')))
        assert HISTORY.is_displayed(),"❌ 히스토리 오류"
        PID = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[4]/a')))
        assert PID.is_displayed(),"❌ 개인 피드 오류"

        logging.info(f"'{HOME.text}' '{TEAM_PID.text}' '{HISTORY.text}' '{PID.text}'")
        logging.info("✅ 하단 버튼 출력")




        
