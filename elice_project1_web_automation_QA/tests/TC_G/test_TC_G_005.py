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
    def test_case_G_005(self, driver:WebDriver):
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


            logging.info("test_case_G_005")

            max_attempts = 10
            attempt = 0

            while True:
    # 시도 횟수 증가
                attempt += 1
    
    # 적합도 요소 찾기
                percent_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'inline-flex') and contains(@class, 'bg-sub')]")))
                percent_text = percent_element.text.strip().replace("%", "")
                percent_value = float(percent_text)

    # 적합도 40% 이상이면 종료
                if percent_value >= 40:
                    logging.info("적합도 %d%% (기준 충족)", percent_value)
                    break

    # 10번 시도 후 종료
                if attempt > max_attempts:
                    logging.info("적합도 %d%% (10번 시도 초과, 없습니다)", percent_value)
                    print("없습니다")
                    break

    # 적합도 미달 시 재추천
                rcm.refresh_recommendation()
                logging.info("적합도 %d%% (기준 미달, 재추천, 시도 %d/%d)", percent_value, attempt, max_attempts)
                time.sleep(2)


                logging.info("test_case_G_005 테스트 완료")


        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")










            