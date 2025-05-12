import pytest
import logging
from selenium import webdriver  # 브라우저 제어
from selenium.webdriver.common.by import By  # HTML 요소 탐색
from selenium.webdriver.support.ui import WebDriverWait  # 특정 요소가 나타날 때까지 대기
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver   
from src.pages.together_eat import TogetherEat
from src.pages.loginPage import LoginPage



@pytest.mark.usefixtures("driver")
class TestCaseD:
    def test_TC_D_001(self, driver:WebDriver):
        together_eat = TogetherEat(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_D_001. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)

        # 메인에서 같이먹기 버튼 검증
        TOGETHER_BUTTON = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[2]')))
        assert TOGETHER_BUTTON.is_displayed(),"❌'👥같이먹기' 버튼 오류"
        logging.info("✅ '👥같이먹기' 버튼 정상 출력")

        # 같이먹기 페이지 이동
        TOGETHER_BUTTON.click()
        logging.info("🔍 같이먹기 페이지 이동중...")
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/together"
        logging.info("✅ '👥같이먹기' 페이지로 정상 이동 완료.")


        # 카테고리 버튼 검증
        categorybutton = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button')
        assert categorybutton.is_displayed(),"❌음식 카테고리 버튼 오류"
        logging.info("✅ 카테고리 버튼 정상 출력")

        # 카테고리 설정
        together_eat.category_select()
        CATEGORY_BOX = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button/span')))
        assert CATEGORY_BOX.text != "음식 카테고리를 설정해주세요","❌음식 카테고리 선택 오류"
