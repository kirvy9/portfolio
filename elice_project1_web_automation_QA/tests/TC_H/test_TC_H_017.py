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
    def test_case_H_017(self, driver:WebDriver):
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

            
            correction_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > section > section > div.flex.items-center.w-full.gap-4 > div > div > svg')))
            correction_btn.click()

            time.sleep(2)

            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='프로필 정보 수정']")))  
            
            time.sleep(2)

            logging.info("test_case_H_017")

            sweet = round(random.uniform(0.0, 0.9), 1)  # 1점 미만 하나 추가
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


            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(9)] # 한글 9글자 랜덤설정
            good_comment =''.join(comment_hangul_chars)
            good_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='pros']")))
            good_input.clear()
            good_input.send_keys(good_comment)

            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            bad_comment =''.join(comment_hangul_chars)
            bad_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='cons']")))
            bad_input.clear()
            bad_input.send_keys(bad_comment)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '프로필 수정 완료')]"))).click()

            flavor_error_msg = driver.find_element(By.XPATH,  "//p[@class='font-semibold text-red-500 text-description' and text()='맛에 대한 성향은 최소 1 이상 설정해주세요']")
            assert flavor_error_msg.is_displayed()

            text_error_msg = driver.find_element(By.XPATH, "//p[@class='font-semibold text-red-500 text-description' and text()='10자 이상 입력해주세요']")


            assert text_error_msg.is_displayed()

            sweet = round(random.uniform(1.0, 5.0), 1)
            team.drag_slider(sweet_slider, sweet)


            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            good_comment =''.join(comment_hangul_chars)
            good_input = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='pros']")))
            good_input.clear()
            good_input.send_keys(good_comment)
            corr_num = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[contains(@class, "w-8")]')))
            corr_sweet = corr_num[3].text
            corr_salty = corr_num[4].text
            corr_spicy = corr_num[5].text

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '프로필 수정 완료')]"))).click()

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.font-bold.text-sub-2.text-title")))

            time.sleep(2)

            feed_num = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[contains(@class, "w-8")]')))
            feed_sweet = feed_num[0].text
            feed_salty = feed_num[1].text
            feed_spicy = feed_num[2].text
            assert corr_sweet == feed_sweet  # +0.1 은 보정
            assert corr_salty  == feed_salty
            assert corr_spicy  == feed_spicy

            feed_write = driver.find_elements(By.XPATH, "//p[contains(@class, 'w-4/5')]")
            feed_good = feed_write[0].text
            feed_bad = feed_write[1].text

            assert good_comment == feed_good
            assert bad_comment == feed_bad

            logging.info("test_case_H_017 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


