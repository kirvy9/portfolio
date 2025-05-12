import time
import pytest
import random
import logging
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.recommendation_page import RecommendationPage
from src.pages.loginPage import LoginPage


@pytest.mark.usefixtures("driver")
class TestCaseG:
    def test_case_G_002(self, driver:WebDriver):
        try:
            wait = ws(driver, 10)
            login=LoginPage(driver)
            rcm=RecommendationPage(driver)
            logging.info("Precondition")

            email="team2@example.co.kr"
            password="Team2@@@"
            login.do_login(email,password)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='혼자 먹기']]"))).click()
            wait.until(EC.url_contains("alone"))
            assert "alone" in driver.current_url    # 페이지 이동 검증
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))).click()
            random.choice(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))).click()  # 카테고리에서 랜덤으로 하나 고르기
            logging.info("카테고리 선택 완료")
            time.sleep(2)


            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='선택 완료']"))).click() #선택 완료 버튼 누르기

            wait.until(EC.url_contains("recommendation"))
            assert "recommendation" in driver.current_url
            logging.info("추천 페이지")
            time.sleep(2)

            logging.info("test_case_G_002")

            while True:
                no_result = len(driver.find_elements(By.XPATH, "//h1[contains(text(), '검색 결과가 없습니다')]")) > 0

                pagination_btns = driver.find_elements(By.CLASS_NAME, "swiper-pagination-bullet")
                pagination_exists = len(pagination_btns) > 2  #2개 이상일때 스크롤 가능


                if not no_result and pagination_exists:
                    break
  
                rcm.refresh_recommendation()
                logging.info("검색 결과가 없거나 swipe 버튼이 없습니다. 다시 추천 받기")
                time.sleep(2)
                
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "swiper-pagination-bullet")))


            logging.info("test_case_G_002 테스트 완료")


        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")










            