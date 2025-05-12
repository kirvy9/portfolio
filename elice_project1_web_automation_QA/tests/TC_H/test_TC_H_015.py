import time
import pytest
import random
import logging
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.loginPage import LoginPage
from src.pages.teamPage import TeamPage


@pytest.mark.usefixtures("driver")
class TestCaseH:
    def test_case_H_015(self, driver:WebDriver):
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

            


            
            correction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > section > section > div.flex.items-center.w-full.gap-4 > div > div > svg')))
            correction_btn.click()
            time.sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='프로필 정보 수정']")))  
            
            time.sleep(2)

            logging.info("test_case_H_015")

            sweet = round(random.uniform(1.0, 5.0), 1)
            salty = round(random.uniform(1.0, 5.0), 1)
            spicy = round(random.uniform(1.0, 5.0), 1)


            sweet_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[4]")))
            team.drag_slider(sweet_slider, sweet)

            time.sleep(2)

            salty_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[5]")))
            team.drag_slider(salty_slider, salty)

            time.sleep(2)

            spicy_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[6]")))
            team.drag_slider(spicy_slider, spicy)


            logging.info("test_case_H_015 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


