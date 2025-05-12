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
    def test_case_H_006(self, driver:WebDriver):
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


            logging.info("test_case_H_006")


            image_path="/var/jenkins_home/workspace/team2/cat.png"
            team.add_image(image_path)
            logging.info("이미지 추가 완료!")

            review_image = driver.find_element(By.XPATH, '//img[@alt="후기 사진"]')  #사진 추가 시 생김

            assert review_image is not None, "후기 사진이 존재하지 않습니다!"


            logging.info("test_case_H_006 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")


