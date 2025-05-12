import os
import sys
import selenium
import time
import random
import faker
import logging
from selenium import webdriver  # 브라우저 제어
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains  # 연속 동작 수행 (예: 드래그 앤 드롭)
from selenium.webdriver.common.keys import Keys  # 키보드 입력 제어
from selenium.webdriver.common.by import By  # HTML 요소 탐색
from selenium.webdriver.support.ui import WebDriverWait  # 특정 요소가 나타날 때까지 대기
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains  


logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    filename = 'test_03_06.log',
    encoding = 'utf-8',
    force='a'
)
logger = logging.getLogger(__name__)



# 여기까지 프로필 설정 되어있는 계정 로그인 이후 단계임 

class TogetherEat:
    def __init__(self,driver):
        self.driver = driver
        self.human_checked = False

    # 같이먹기 페이지 이동
    def go_together_eat(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[2]'))).click()
        logging.info("🔍 같이먹기 페이지 이동중...")
        
        #self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button[2]').click()
        #assert self.driver.current_url == "https://kdt-pt-1-pj-2-team03.elicecoding.com/selectoptions/together"
        #logging.info("✅ '👥같이먹기' 페이지로 정상 이동 완료.") #최적화 완
    

    # 뒤로가기 버튼 클릭
    def back_page(self):
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/header/div/svg').click()
        logging.info("뒤로가기 버튼 클릭")
        time.sleep(1)


    # 푸드 카테고리 선택
    def category_select(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button'))).click()
        logging.info("🔍 카테고리 선택중...")

        # 임의의 카테고리 설정
        food_category_index = {
            "한식":2,
            "중식":3,
            "양식":4,
            "일식":5,
            "분식":6,
            "아시안":7,
            "패스트푸드":8,
            "기타":9
            }
        food = random.choice(list(food_category_index.keys()))
        index = food_category_index[food]

        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//*[@id='radix-:r0:']/div/div/div[{index}]"))).click()
        logging.info(f"✅ 카테고리 : '{food}' 선택")

        #select_category = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/main/section/div/div[1]/button').click()
        #time.sleep(1)
        #self.driver.find_element(By.XPATH,f"//*[@id='radix-:r0:']/div/div/div[{index}]").click()


        # 이걸로 대체 가능함, 콤보박스누르고 안에 옵션 뜰때까지 기다렸다가 옵션이 뜨면 랜덤초이스가 선택을 하는것임
        #wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))).click()
        #random.choice(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']")))).click()


    # 함께 먹을 임의의 인원 선택
    def human_check_box(self):
        if self.human_checked:
            return []
        check_boxes = self.driver.find_elements(By.CSS_SELECTOR, 'div.flex.flex-col.gap-2.py-2 > div > input')

        if not check_boxes:
            logging.error("❌ 체크박스를 찾을 수 없음")
            return []  # 빈 리스트 반환 (None X)

        num_to_check = random.randint(1, len(check_boxes))  # 최소 1개 이상 선택
        selected_checkboxes = []
        selected_people = []

        for _ in range(num_to_check):
            checkbox = random.choice(check_boxes)  # 랜덤 선택
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)  # 스크롤 이동

            if not checkbox.is_selected():  # 체크 안 되어 있으면 클릭
                self.driver.execute_script("arguments[0].click();", checkbox)
                selected_checkboxes.append(checkbox)  # ✅ 클릭한 항목만 리스트에 추가

        if not selected_checkboxes:
            logging.warning("⚠️ 선택된 체크박스가 없음")
        else:
            logging.info(f"✅ {len(selected_checkboxes)}명 선택")

        self.driver.execute_script("window.scrollTo(0, 0);")

        self.human_checked = True
        self.selected_count = len(selected_checkboxes)

        return self.selected_count  # ✅ 선택한 항목만 반환


#################################################################

#    # 선택한 인원들을 로그로 출력
#    def select_print(self):
#        self.driver.execute_script("window.scrollTo(0, 0);")
#        try:
#            # 요소가 로드될 때까지 기다림
#            WebDriverWait(self.driver, 10).until(
#                EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > div > div:nth-child(2) > div.flex.gap-4.overflow-x-auto.scrollbar-hide.whitespace-nowrap > div > div.pt-2.font-semibold.text-center.text-description')))
#            WebDriverWait(self.driver, 10).until(
#                EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > div > div:nth-child(2) > div.flex.gap-4.overflow-x-auto.scrollbar-hide.whitespace-nowrap > div > div.text-gray-500.text-description')))
#
#            # 요소 가져오기
#            name_elements = self.driver.find_elements(By.CSS_SELECTOR,'#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > div > div:nth-child(2) > div.flex.gap-4.overflow-x-auto.scrollbar-hide.whitespace-nowrap > div > div.pt-2.font-semibold.text-center.text-description')
#                
#            team_elements = self.driver.find_elements(By.CSS_SELECTOR,'#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > div > div:nth-child(2) > div.flex.gap-4.overflow-x-auto.scrollbar-hide.whitespace-nowrap > div > div.text-gray-500.text-description')
#                
#            # 선택한 인원 리스트 생성
#            selected_people = []
#            for name_element, team_element in zip(name_elements, team_elements):
#                name = name_element.text.strip()
#                team = team_element.text.strip()
#                selected_people.append({name: team})
#                logging.info(f"선택됨: {name} - {team} ✅")
#
#            # 선택한 인원 리스트 반환 (필요하다면)
#            return selected_people
#
#        except Exception as e:
#            logging.error(f"❌ 오류 발생: {e}")
#            return []
############################################################################

   # 선택 해제하기
    def un_select_people(self):
        if not self.human_checked:
            logging.warning("⚠️선택된 인원이 없습니다.")
            return 
        
        max_unselect = self.selected_count

        if max_unselect == 0:
            logging.warning("⚠️ 선택된 인원이 없어서 해제할 수 없습니다.")
            return

        num_to_unselect = random.randint(1, max_unselect)  # 최대값을 human_check_box에서 반환된 값으로 제한

        count = 0
    # 체크박스를 클릭하여 하나씩 해제하는 로직
        for _ in range(num_to_unselect):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR,'#root > div.flex.flex-col.mx-auto.min-h-screen.max-w-\\[600px\\] > main > section > div > div:nth-child(2) > div.flex.gap-4.overflow-x-auto.scrollbar-hide.whitespace-nowrap > div:nth-child(1) > div'))).click()  # 클릭하여 해제
            
            count += 1
            
        logging.info(f"✅ {count}명 선택 해체")
        #logging.info(f"✅ 최종 선택 인원 {max_unselect-count}명")
    
    # 선택완료 
    def choice_complete(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/div/button'))).click()
        logging.info("선택완료 클릭")
        

    # 추천 수락하기
    def choice_agree(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/button[2]'))).click()
        logging.info("추천 수락하기 클릭")
        time.sleep(1)

    # 다시 추천 받기
    def RE_choice(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/main/section/section/button[1]'))).click()
        logging.info("다시 추천 받기 클릭")
        time.sleep(1)










