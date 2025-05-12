import time
import pytest
import logging
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.loginPage import LoginPage
from src.pages.teamPage import TeamPage


@pytest.mark.usefixtures("driver")
class TestCaseH:
    def test_case_H_014(self, driver:WebDriver):
        try:

            wait = ws(driver, 10)
            login=LoginPage(driver)
            team=TeamPage(driver)

            logging.info("Preconditon")


            email="team2@example.co.kr"
            password="Team2@@@"
            login.do_login(email,password)

            my_team= team.my_team()
            logging.info("내 팀 : %s",my_team)
            time.sleep(2) 

            logging.info("test_case_H_014")


           
            correction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > section > section > div.flex.items-center.w-full.gap-4 > div > div > svg')))
            correction_btn.click()

            time.sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='프로필 정보 수정']")))  
            
            time.sleep(2)



            logging.info("test_case_H_014 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


