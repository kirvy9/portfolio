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
    def test_TC_D_002(self, driver:WebDriver):
        together_eat = TogetherEat(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_D_002. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)

        # 같이먹기 페이지 이동
        together_eat.go_together_eat()
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/together"
        logging.info("✅ '👥같이먹기' 페이지로 정상 이동 완료.")

        # 카테고리 설정
        together_eat.category_select()
        CATEGORY_BOX = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button/span')))
        assert CATEGORY_BOX.text != "음식 카테고리를 설정해주세요","❌음식 카테고리 선택 오류"
        logging.info("✅ 카테고리 설정 완료")

        # 임의 인원 추가 함
        together_eat.human_check_box()
        SELECT_HUMAN = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > div > div:nth-child(2) > div.flex.gap-4.overflow-x-auto.scrollbar-hide.whitespace-nowrap > div')))
        assert len(SELECT_HUMAN) > 0,"❌인원 선택 오류"
        logging.info("✅ 인원 선택 완료")


        # 임의 인원 빼기
        together_eat.un_select_people()
        TO_SELECT_HUMAN = len(SELECT_HUMAN)
        SELECT_HUMAN = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > div > div:nth-child(2) > div.flex.gap-4.overflow-x-auto.scrollbar-hide.whitespace-nowrap > div')))
        assert len(SELECT_HUMAN) != TO_SELECT_HUMAN,"❌인원 선택 오류"
        logging.info(f"✅ 최종 선택 인원 {len(SELECT_HUMAN)} 명")
