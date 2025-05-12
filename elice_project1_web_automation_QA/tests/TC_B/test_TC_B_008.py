import time
import pytest
import random
import logging
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from faker import Faker
from src.pages.signupPage import SignupPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
class TestCase_B:
    def test_Case_B_08(self, driver:WebDriver):
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

            like_input = driver.find_element(By.NAME, "pros")
            dislike_input = driver.find_element(By.NAME, "cons")

            # 잘못된 입력 (고의로 10자 미만 입력)
            like_input.send_keys(faker.text(max_nb_chars=9))  # 10자 미만
            time.sleep(1)

            dislike_input.send_keys(faker.text(max_nb_chars=9))  # 10자 미만
            logging.info("잘못된 좋아요/싫어요 입력 완료 (10자 미만)")

            time.sleep(1)

            submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='제출하기']")
            submit_button.click()
            logging.info("회원가입 '제출하기' 버튼 클릭")

            # 실패 확인 및 수정 (10자 미만인 경우 오류 메시지 표시)
            time.sleep(2)

            # 에러 메시지 확인: '10자 이상 입력해주세요'
            error_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'flex')]/p[contains(text(),'10자 이상 입력해주세요')]")))

            if error_message:
                logging.warning("⚠️ 좋아요/싫어요 입력이 10자 미만입니다. 재입력합니다.")

                # 100자 이내로 수정
                like_input.clear()
                dislike_input.clear()

                like_input.send_keys(faker.text(max_nb_chars=100))  # 100자 이내
                dislike_input.send_keys(faker.text(max_nb_chars=100))  # 100자 이내
                logging.info("올바른 좋아요/싫어요 입력 완료 (100자 이내)")

            time.sleep(1)

      # 마지막 회원가입 버튼 클릭
            submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='제출하기']")
            submit_button.click()
            logging.info("회원가입 '제출하기' 버튼 클릭")

            ws(driver, 10)
            wait.until(
              EC.presence_of_element_located((By.XPATH, "//button[.//p[text()='혼자 먹기']]"))
            )

            logging.info("[테스트 종료] 회원가입 프로세스 종료되었습니다.")
        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False

