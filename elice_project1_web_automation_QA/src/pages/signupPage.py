from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver 
import random
from faker import Faker
import string
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException , TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as ws
import logging


class SignupPage:
    URL = "https://kdt-pt-1-pj-2-team03.elicecoding.com/signin"

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def go_signup(self):
        wait=ws(self.driver,10)
        signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'회원가입')]")))
        signup_btn.click()

    def generate_random_email_and_password(self):
        faker = Faker()
        email = faker.email()

        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        special = random.choice("!@#$%^&()")
        remaining = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()", k=4))
        password = ''.join(random.sample(lower + upper + digit + special + remaining, 8))

        return email, password
    
    def fill_signup_form(self,email,password):
        wait=ws(self.driver,10)

        email_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
        password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))

        email_field.send_keys(email)
        time.sleep(2)
        password_field.send_keys(password)
        time.sleep(2)

        logging.info("사용자 이메일 : %s , 비밀번호 : %s",email,password)

        continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='action' and @value='default' and contains(text(), '계속하기')]")))
        continue_btn.click()
        time.sleep(2)

    def accept_btn(self):
        wait = ws(self.driver, 10)
        accept_btn=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='action' and @value='accept' and contains(text(), 'Accept')]")))
        accept_btn.click()

        
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
            actions.click_and_hold(slider_element).move_by_offset(-slider_width // 2, 0).pause(0.5).release().perform()
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
