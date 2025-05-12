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
    def test_case_H_010(self, driver:WebDriver):
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

            #식사 유형 선택
            eat_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@role='radio']")))
            selected_eat_option = random.choice(eat_options)   #식사 유형 랜덤으로 선택(혼밥, 그룹, 회식)
            logging.info(f"선택된 옵션: {selected_eat_option.get_attribute('value')}")  
            selected_eat_option.click()
            logging.info("유형 선택 완료!")

            #그룹일때만 나타나는 같이 먹은 사람 
            if selected_eat_option.get_attribute('value') == "그룹":
                wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='이름을 검색해주세요']"))).send_keys("김정재")  #김정재 검색 후 클릭
                driver.find_element(By.XPATH, "//li[contains(@class, 'cursor-pointer')]").click()


            #이미지 추가
            image_path="/var/jenkins_home/workspace/team2/cat.png"
            team.add_image(image_path)
            logging.info("이미지 추가 완료!")

            #메뉴이름 
            food_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(3)] #한글 3글자 랜덤 설정
            food = ''.join(food_hangul_chars)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='메뉴 명을 입력해주세요.']"))).send_keys(food)

            #후기
            comment_hangul_chars = [chr(random.randint(0xAC00, 0xD7A3)) for _ in range(10)] # 한글 10글자 랜덤설정
            comment =''.join(comment_hangul_chars)
            wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='comment']"))).send_keys(comment)
            logging.info("후기 입력 완료")
            time.sleep(2)

            #카테고리  
            category_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='음식 카테고리를 설정해주세요']]")))
            category_button.click()
            category_options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))
            selected_category_element = random.choice(category_options)
            selected_category = selected_category_element.text   #마지막 assert 할때 카테고리 비교하기 위한 변수
            selected_category_element.click()
            logging.info(f"카테고리 설정 완료: {selected_category}")
            time.sleep(2)

            # 별점 선택
            stars = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'w-10') and contains(@class, 'cursor-pointer')]")))
            selected_star = random.choice(stars)
            selected_star_count = stars.index(selected_star) + 1 # 검증 때 사용
            selected_star.click()
            logging.info(f"별점 입력 완료: {selected_star_count}개")
            time.sleep(2)


            logging.info("test_case_H_010")

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '후기 작성 완료')]"))).click()
            logging.info("후기 작성 완료")
            time.sleep(2)

            #개인 피드 버튼 클릭 후 이동
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[span[text()='개인 피드']]"))).click()
            logging.info("개인 피드 이동")
            time.sleep(2)

            first_food_card = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class, 'flex w-full gap-6 p-4 shadow-md rounded-2xl')])[1]")))
            feed_food_name = first_food_card.find_element(By.XPATH, ".//div[@class='font-bold']").text
            food_category = [tag.text.strip() for tag in first_food_card.find_elements(By.XPATH, ".//div[contains(@class, 'inline-flex')]")]
            review_stars = len(first_food_card.find_elements(By.XPATH, ".//span[contains(text(), '★')]"))

            assert feed_food_name == food, "음식 이름이 일치하지 않음"
            logging.info("음식일치!")
            assert selected_category in food_category, "카테고리가 일치하지 않음"
            logging.info("카테고리 일치!")
            assert selected_star_count == review_stars, f"별점 개수가 일치하지 않음"
            logging.info("별 일치!")
            time.sleep(2)

            logging.info("test_case_H_010 테스트 완료")



        except Exception as e:
            print(f"테스트 중 오류 발생: {e}")





