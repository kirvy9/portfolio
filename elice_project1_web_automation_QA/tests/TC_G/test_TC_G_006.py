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
    def test_case_G_006(self, driver:WebDriver):
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


            logging.info("test_case_G_006")

            rcm_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'text-main') and contains(@class, 'text-title')]"))).text
            logging.info("최종 추천 메뉴 : %s",rcm_menu)

            rcm.accept()

            wait.until(EC.url_contains("history"))
            assert "history" in driver.current_url
            logging.info("히스토리 페이지 이동")
            time.sleep(2)

            recent_menu =wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class, 'flex w-full gap-6 p-4 shadow-md rounded-2xl')])[1]"))).find_element(By.CLASS_NAME, "font-bold").text
            logging.info("히스토리 최근 메뉴 : %s",recent_menu)


            assert rcm_menu == recent_menu , "메뉴 일치하지 않음"
            time.sleep(2)



            logging.info("test_case_G_006 테스트 완료")


        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")










            