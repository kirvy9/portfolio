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
    def test_case_G_001(self, driver:WebDriver):
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
            #1.메뉴 추천 페이지 들어간다
            wait.until(EC.url_contains("recommendation"))
            assert "recommendation" in driver.current_url
            logging.info("추천 페이지")
            time.sleep(2)

            logging.info("test_case_G_001")


            first_rcm = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'text-main') and contains(@class, 'text-title')]"))).text #변경전 메뉴 
            logging.info("변경전 메뉴 : %s", first_rcm)
            time.sleep(2)

        
            rcm.refresh_recommendation()
            time.sleep(2)
            new_rcm= wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'text-main') and contains(@class, 'text-title')]"))).text
            logging.info("변경후 메뉴 : %s", new_rcm)
            time.sleep(2)


            logging.info("test_case_G_001 테스트 완료")


        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")










            