import time
import pytest
import logging
import random
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from faker import Faker
from src.pages.signupPage import SignupPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
class TestCase_B:
    def test_Case_B_06(self, driver:WebDriver):
        try : 
            #Test 시작
            logging.info("[테스트 시작] 회원가입 프로세스를 시작합니다.")
            signupPage = SignupPage(driver)
            wait = ws(driver, 10)
            faker = Faker()

            signupPage.open()
            time.sleep(1)
            logging.info("회원가입 페이지 열기 완료")
            
            signupPage.go_signup()
            time.sleep(1)
            logging.info("회원가입 폼으로 이동 완료")

            email, password=signupPage.generate_random_email_and_password()
            logging.info("이메일 : %s, 비밀번호 %s", email, password)
            time.sleep(1)

            signupPage.fill_signup_form(email,password)
            time.sleep(1)
            logging.info("이메일 및 비밀번호 입력 완료")

            signupPage.accept_btn()
            logging.info("Accept 버튼 클릭 완료")
            time.sleep(1)

            name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='name']")))
            name = faker.name()
            name_field.send_keys(name)
            time.sleep(1)
            logging.info("내 이름 : %s",name)

            assert name_field.get_attribute("value") == name, "이름 입력이 정상적으로 되지 않았습니다."
            logging.info("이름 입력 완료")

            team_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']")))
            team_button.click()
            my_team=random.choice(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']"))))
            logging.info("내 팀 : %s",my_team.text)
            time.sleep(1)
            my_team.click()
            logging.info("팀 선택 완료")

            sweet = round(random.uniform(1.0, 5.0), 1)
            salty = round(random.uniform(1.0, 5.0), 1)
            spicy = round(random.uniform(1.0, 5.0), 1)

            sweet_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[1]")))
            signupPage.drag_slider(sweet_slider, sweet)
            logging.info("단맛 설정 : %s", sweet)

            time.sleep(1)

            salty_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[2]")))
            signupPage.drag_slider(salty_slider, salty)
            logging.info("짠맛 설정 : %s", salty)

            time.sleep(1)

            spicy_slider = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='slider'])[3]")))
            signupPage.drag_slider(spicy_slider, spicy)
            logging.info("매운맛 설정 : %s", spicy)

            time.sleep(1)

        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False

