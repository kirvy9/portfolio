import os
import sys
import selenium
import time
import random
import faker
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver  # 브라우저 제어
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains  # 연속 동작 수행 (예: 드래그 앤 드롭)
from selenium.webdriver.common.keys import Keys  # 키보드 입력 제어
from selenium.webdriver.common.by import By  # HTML 요소 탐색
from selenium.webdriver.support.ui import WebDriverWait  # 특정 요소가 나타날 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  


logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filename = 'test_03_06.log',
    encoding = 'utf-8',
    force='a'
)
logger = logging.getLogger(__name__)



# 여기까지 프로필 설정 되어있는 계정 로그인 이후 단계임 

class SoloEat:
    def __init__(self,driver):
        self.driver = driver

    # 혼자먹기 페이지 이동
    def go_solo_eat(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/main/section/div/div[1]/button[1]'))).click()
        logging.info("🔍 혼자먹기 페이지 이동중...")
        
    
    # 뒤로가기 버튼 (디테일 못잡음)
    def back_page(self):
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/header/div/svg').click()
        logging.info("뒤로가기 버튼 클릭")
        time.sleep(1)

    # 푸드 카테고리 선택
    def category_select(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button'))).click()
        logging.info("🔍 카테고리 선택중...")
        
        #select_category = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button').click()
        #time.sleep(1)

        # 임의의 카테고리 설정
        food_category_index = {
            "한식":2,
            "중식":3,
            "양식":4,
            "일식":5,
            "분식":6,
            "아시안":7,
            "패스트푸드":8,
            "기타":9
            }
        food = random.choice(list(food_category_index.keys()))
        index = food_category_index[food]

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//*[@id='radix-:r0:']/div/div/div[{index}]"))).click()
        
        logging.info(f"✅ 카테고리 : '{food}' 선택")

        # 이걸로 대체 가능함, 콤보박스누르고 안에 옵션 뜰때까지 기다렸다가 옵션이 뜨면 랜덤초이스가 선택을 하는것임
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))).click()
        #random.choice(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))).click()


    # 선택완료 
    def choice_complete(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/button'))).click()
        logging.info("선택완료 클릭")
        
        #self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/div/button').click()
        #time.sleep(1)
        #assert self.driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/recommendation"
        #logging.info("✅ 선택완료")

    # 추천 수락하기
    def choice_agree(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/button[2]'))).click()
        logging.info("추천 수락하기 클릭")
        
        #assert self.driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/history"
        #logging.info("✅ 추천 수락하기 완료")
        
        #self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/section/button[2]').click()
        #time.sleep(1)


    # 다시 추천 받기
    def RE_choice(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/button[1]'))).click()
        logging.info("다시 추천 받기 클릭")
       










