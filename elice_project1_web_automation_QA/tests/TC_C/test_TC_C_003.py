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
    def test_TC_C_003(self, driver:WebDriver):
        solo_eat = SoloEat(driver)
        login_page = LoginPage(driver)
        logging.info("\n[Test_C_003. Start!]")
        email="team2@example.co.kr"
        password="Team2@@@"
        login_page.do_login(email,password)
        # 메인에서 혼자먹기 페이지 이동 
        solo_eat.go_solo_eat()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone"))
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/alone","❌혼자먹기 페이지 이동 오류"
        logging.info("✅ '👤혼자먹기' 페이지 정상 이동 완료.")

        # 임의의 음식 카테고리 선택
        solo_eat.category_select()
        CATEGORY_BOX = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button/span')))
        assert CATEGORY_BOX.text != "음식 카테고리를 설정해주세요","❌음식 카테고리 선택 오류"
        logging.info("✅ 카테고리 설정 완료")

        # 그리고 선택완료 누름
        solo_eat.choice_complete()
        assert driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/recommendation","❌선택완료 오류"
        logging.info("✅ 선택완료")

        # 추천 메뉴및 맛집 검증
        recommand_menu = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/div[1]/span/span')))
        assert recommand_menu.is_displayed(),"❌ 메뉴추천 오류"
        logging.info("✅ 정상 출력")
        logging.info(f"✅ 추천 메뉴 : {recommand_menu.text}")
        menu_image = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/div[1]/div/img')))

        if menu_image:
            logging.info("✅ 메뉴 사진 정상 출력")
        else:
            logging.error("❌메뉴 사진 오류")

        recommand = driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/section/div[2]/span')
        recommand_list = driver.find_elements(By.CLASS_NAME,"swiper-slide")

        logging.info(f"✅ {recommand.text} : {len(recommand_list)}개의 맛집 발견")






