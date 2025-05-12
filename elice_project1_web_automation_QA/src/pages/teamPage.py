from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import logging
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class TeamPage:

    def __init__(self, driver :WebDriver):
        self.driver = driver

    def my_team(self):
        wait=ws(self.driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[text()='개인 피드']]"))).click()


        my_team=wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='text-white']"))).text
        

        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[text()='팀 피드']]"))).click()

        return my_team
    
    def scroll_down(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 아래로 스크롤
            time.sleep(2)  # 로딩 대기

            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:  # 더 이상 스크롤할 게 없으면 종료
                break
            last_height = new_height

    def add_image(self, image_path):
        wait=ws(self.driver,10)
        addimagebtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-main-black')]")))
        try:
            addimagebtn.click()  # 기본 클릭
        except:
            self.driver.execute_script("arguments[0].click();", addimagebtn) 
        time.sleep(2)

        file_input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )

        file_input.send_keys(image_path)
        time.sleep(2)

    def scroll_to_top(self):
    
        self.driver.execute_script("window.scrollTo(0, 0)")



    def drag_slider(self, slider_element, target_value, max_value=5):


        actions = ActionChains(self.driver)

        # 슬라이더 크기 가져오기
        slider_bar = slider_element.find_element(By.XPATH, "./parent::span/preceding-sibling::span")
        slider_width = slider_bar.size['width']
    
        # 최소값과 최대값 가져오기
        min_value = float(slider_element.get_attribute("aria-valuemin"))  # 기본적으로 0
        max_value = float(slider_element.get_attribute("aria-valuemax"))  # 기본적으로 5

        # 현재 값 가져오기
        current_value = float(slider_element.get_attribute("aria-valuenow"))
        print(f"현재 슬라이더 값: {current_value}")

        # 1. 슬라이더를 0으로 초기화 (왼쪽 끝으로 이동)
        if current_value != min_value:
            print("슬라이더 초기화 중...")
            actions.click_and_hold(slider_element).move_by_offset(-slider_width, 0).pause(0.5).release().perform()
            time.sleep(1)  # UI 반영 대기 시간 추가

        # 초기화 확인 (값이 정상적으로 0으로 바뀌었는지 확인)
            current_value = float(slider_element.get_attribute("aria-valuenow"))
            print(f"초기화 후 슬라이더 값: {current_value}")

        # 2. 목표 값으로 이동
        move_ratio = (target_value - min_value) / (max_value - min_value)  # 0에서 target_value까지의 비율
        move_distance = int(slider_width * move_ratio)  # 실제 이동할 거리(px)

        print(f"이동 거리: {move_distance}px")

        actions.click_and_hold(slider_element).move_by_offset(move_distance, 0).pause(0.5).release().perform()
        time.sleep(1)  # UI 반영 대기 시간 추가

        # 최종 값 확인
        updated_value = float(slider_element.get_attribute("aria-valuenow"))
        print(f"✅ 업데이트된 슬라이더 값: {updated_value}")


