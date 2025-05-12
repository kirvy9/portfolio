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
    def test_case_H_012(self, driver:WebDriver):
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

            menus = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'shadow-md') and contains(@class, 'rounded-2xl')]"))) #팀원들이 먹은 메뉴
            random_select_menu = random.choice(menus)  #메뉴들 중 랜덤으로 하나 선택
            menu_name = random_select_menu.find_element(By.XPATH, ".//div[@class='font-bold']").text
            logging.info(menu_name) #메뉴 이름 출력
            time.sleep(2) 


            scroll_step = 500  # 한 번에 내릴 픽셀 수
            max_scroll = 5000  # 최대 스크롤 제한 (필요에 따라 조절)
            current_scroll = 0

            while current_scroll <= max_scroll:   #화면에 보일 떄 까지 스크롤
                    try:
                        same_menu_button = random_select_menu.find_element(By.XPATH, ".//button[contains(@class, 'bg-main-black')]")
                        tag = random_select_menu.find_element(By.XPATH, ".//div[contains(concat(' ', normalize-space(@class), ' '), ' bg-main ')]").text  #혼밥,그룹,회식 태그                   
                        same_menu_button.click()
            
                        break  # 클릭 성공하면 루프 종료
                    except:
                        driver.execute_script(f"window.scrollBy(0, {scroll_step});")  # 500px 아래로 스크롤
                        current_scroll += scroll_step
                        time.sleep(1) 

            logging.info(tag)
            time.sleep(2) 
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='또 먹은 후기 등록하기']")))
            logging.info("또 먹은 후기 등록하기 페이지로 이동")
            time.sleep(2)

            checked_tag = wait.until(EC.presence_of_element_located((By.XPATH, ".//button[@aria-checked='true']"))).get_attribute('value')  #미리 선택되어 있는 태그 이름
            menu_input = driver.find_element(By.XPATH, ".//input[@name='menu']").get_attribute('value')  #미리 선택 되어 있는 메뉴 이름
            logging.info(checked_tag)     
            logging.info(menu_input)   

            #랜덤으로 고른 메뉴랑 눌러서 들어간 거랑 메뉴,태그가 같은지 검증
            assert tag == checked_tag, "태그가 바뀜"
            assert menu_name == menu_input, "메뉴가 바뀜"

            logging.info("test_case_H_012")

            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)]
            comment = ''.join(comment_hangul_chars)
            cmt = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='comment']")))
            cmt.clear()
            cmt.send_keys(comment)
            logging.info("후기 입력 완료")

            stars = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "//div[contains(@class, 'w-10') and contains(@class, 'cursor-pointer')]"
            )))
            selected_star = random.choice(stars)
            selected_star_count = stars.index(selected_star) + 1
            selected_star.click()
            logging.info(f"별점 입력 완료: {selected_star_count}개")

            logging.info("test_case_H_012 테스트 완료")

        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")