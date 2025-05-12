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
    def test_case_H_005(self, driver:WebDriver):
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

            


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:  #화면에 '+' 뜰 때까지 스크롤 다운
                    try:
                        plus_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'bg-main-black') and contains(@class, 'cursor-pointer')]")))  
                        plus_button.click()

                        break  # 클릭 성공하면 루프 종료

                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1)  # 스크롤 후 페이지 로딩 대기


            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='새로운 후기 등록하기']")))   #새로운 후기 등록하기 뜰 때까지 대기
            logging.info("새로운 후기 페이지로 이동")
            time.sleep(2)


            logging.info("test_case_H_005")

            eat_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@role='radio']")))
            selected_eat_option = random.choice(eat_options)   #식사 유형 랜덤으로 선택(혼밥, 그룹, 회식)
            logging.info(f"선택된 옵션: {selected_eat_option.get_attribute('value')}")  
            selected_eat_option.click()
            logging.info("유형 선택 완료!")
            time.sleep(2)

            #그룹일때만 나타나는 같이 먹은 사람 
            if selected_eat_option.get_attribute('value') == "그룹":
                wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='이름을 검색해주세요']"))).send_keys("김정재")  #김정재 검색 후 클릭
                driver.find_element(By.XPATH, "//li[contains(@class, 'cursor-pointer')]").click()


            logging.info("test_case_H_005 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


