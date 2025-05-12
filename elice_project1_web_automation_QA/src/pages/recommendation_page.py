from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import logging


class RecommendationPage:
    
    def __init__(self, driver :WebDriver):
        self.driver = driver

    def backward(self):
        wait=ws(self.driver,10)
        backward_btn=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"rounded-full")))
        backward_btn.click()

    def swipe(self,times=1):
        wait=ws(self.driver,10)

        for i in range(times):
            pagination_btns = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "swiper-pagination-bullet")))
            active_btn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "swiper-pagination-bullet-active")))
            available_btns = [btn for btn in pagination_btns if btn != active_btn and btn != pagination_btns[0]]
            random_btn = random.choice(available_btns)
            random_btn.click()
            logging.info("%d번쨰 swipe",(i+1))
            time.sleep(2)


    def refresh_recommendation(self):
        wait=ws(self.driver,10)
        refresh_btn =wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '다시 추천 받기')]")))
        refresh_btn.click()

    def accept(self):
        wait=ws(self.driver,10)
        accept_btn =wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '추천 수락하기')]")))
        accept_btn.click()