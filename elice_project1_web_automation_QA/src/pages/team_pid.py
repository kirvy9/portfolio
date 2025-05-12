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

class TeamPid:
    def __init__(self,driver):
        self.driver = driver

    # 팀피드 페이지 이동
    def go_team_pid(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/ul/li[2]/a'))).click()
        logging.info("🔍 팀피드 페이지 이동중...")
        
        
    
    # 뒤로가기 버튼 (디테일 못잡음)
    def back_page(self):
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/header/div/svg').click()
        logging.info("뒤로가기 버튼 클릭")  
        time.sleep(1)

    # 팀 카테고리 선택
    def team_category_select(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/div[1]/button'))).click()
        logging.info("🔍 카테고리 선택중...")
        

        # 임의의 카테고리 설정
        team_category_index = {
            "개발 1팀":2,
            "개발 2팀":3,
            "디자인 1팀":4,
            "디자인 2팀":5
            }
        team = random.choice(list(team_category_index.keys()))
        index = team_category_index[team]

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="radix-:r0:"]/div/div/div[{index}]'))).click()
        logging.info(f"✅ 카테고리 : {team} 선택")                                                   

        # 이걸로 대체 가능함, 콤보박스누르고 안에 옵션 뜰때까지 기다렸다가 옵션이 뜨면 랜덤초이스가 선택을 하는것임
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))).click()
        #random.choice(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))).click()

    # 임의로 '같은메뉴먹기' 클릭함
    def review_write(self):
        try:
            WRITE_REVIEW = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//button[contains(text(), '같은 메뉴 먹기')]")))

            if WRITE_REVIEW:
                random_review_select = random.choice(WRITE_REVIEW)
                
                # 버튼을 못찾길래 스크롤로 버튼 센터에 맞추는..
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",random_review_select)

                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(random_review_select))            
                ActionChains(self.driver).move_to_element(random_review_select).click().perform()                                
                logging.info("'같은 메뉴 먹기' 클릭")
                return True
            else:
                logging.info("❌ 버튼찾기 오류")
                return False
        except:
            return False
            #font-bold
    

    ############### 팀 피드 -> 후기 작성 페이지에서 
    
    # 식사 유형 랜덤으로 선택
    def type_select(self):
        button_list = ["혼밥","그룹","회식"]
        random_choice = random.choice(button_list)
        button_xpath = f'//*[@id="{random_choice}"]'
        try:    
            button = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,button_xpath)))
            if "selected" not in button.get_attribute("class"):
                button.click()
        except:
            pass
        logging.info(f"식사 유형 : {random_choice} 선택")

        return 

  
    # 혼밥 or 회식 일 경우
    # 후기
    def review_input(self):

        taste = ["진짜 맛있다", "정말 담백하다", "달콤하면서도 고소하다", "적당히 짭짤하다", "깊은 감칠맛이 난다"]
        texture = ["쫄깃쫄깃하다", "부드럽게 씹힌다", "겉은 바삭하고 속은 촉촉하다", "탱글탱글한 식감이 좋다"]
        smell = ["향긋한 냄새가 난다", "구수한 향이 퍼진다", "진한 풍미가 입안을 감싼다"]
        recommendation = ["다시 방문하고 싶다", "친구들에게 추천하고 싶다", "가성비가 좋다", "한 번쯤 먹어볼 만하다"]
        extra = ["양이 넉넉하다", "비주얼도 훌륭하다", "소스가 아주 잘 어울린다"]

        review = (f"{random.choice(taste)}. {random.choice(texture)}. {random.choice(smell)}. {random.choice(recommendation)}. {random.choice(extra)}.")


        try:
            content = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="modal-root"]/div/div[2]/section/form/div[5]/textarea')))
        except:
            try:
                content = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="modal-root"]/div/div[2]/section/form/div[6]/textarea')))
            except:
                logging.error("❌ 후기 작성란을 찾을 수 없습니다. 페이지 로딩 오류.")
                return 
        content.click()
        content.clear()
        content.send_keys(review)
        logging.info(f"후기 : {review}")


    # 별점 버튼
    def star_click(self):
        star_list = ["1", "2", "3", "4", "5"]
        random_star = random.choice(star_list)
        selectors = [
            f'#modal-root > div > div.flex-1.overflow-auto > section > form > div:nth-child(6) > div > div:nth-child({random_star})',
            f'#modal-root > div > div.flex-1.overflow-auto > section > form > div:nth-child(7) > div > div:nth-child({random_star})'
        ]

        for selector in selectors:
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector))).click()
                logging.info(f"{'⭐' * int(random_star)} 선택")
                return
            except Exception as e:
                #logging.error(f"별점 선택 실패 : {str(e)}")
                pass
                                    
                                                                                                                                                               
    # 후기 작성 완료 버튼 클릭 
    def review_complete(self):
        # WebDriverWait으로 버튼이 로드될 때까지 기다린 후 클릭
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#modal-root > div > div.flex-1.overflow-auto > section > form > button'))).click()
        logging.info("후기 작성 버튼 클릭")


   
    # 개인 피드 이동 버튼
    def personal_pid(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/ul/li[4]/a'))).click()
        logging.info("🔍 개인 피드 페이지 이동중...")
    

    
  