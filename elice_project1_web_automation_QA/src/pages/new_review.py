import random
import os
import time
from selenium.webdriver.chrome.webdriver import WebDriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC


class NewReview:


    def __init__(self, driver :WebDriver):
        self.driver = driver
        self.wait = ws(self.driver,10)
        


    #후기 추가 페이지 접근
    def review_open(self):
        add_reviewbtn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/main/section/section/div[2]/div[1]/button")))
        add_reviewbtn.click()


    #식사 타입 랜덤 초이스
    def select_meal_type(self):
        meal_types = ["//*[@id='혼밥']", "//*[@id='회식']", "//*[@id='그룹']"]
        
        selected_type = random.choice(meal_types)

        meal_button = self.wait.until(EC.presence_of_element_located((By.XPATH, selected_type)))
        meal_button.click()

        # '그룹' 타입 선택 시 추가 동작 수행
        if selected_type == "//*[@id='그룹']":
            group_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='modal-root']/div/div[2]/section/form/div[3]/div[1]/input"))
            )
            group_input.send_keys("테스트")

        return selected_type  # 선택된 식사 타입 반환

    #리뷰 사진 등록
    def add_image(self):
        file_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )

        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(script_dir))
        image_path = os.path.join(project_root, "resources", "assets", "cat.png")

        if not os.path.exists(image_path):
            raise FileNotFoundError(f"❌ 이미지 파일을 찾을 수 없습니다: {image_path}")

        file_input.send_keys(image_path)

    def add_menuname(self):
        menuname = self.driver.find_element(By.NAME, "menu")
        # 10~999 사이의 난수를 생성하여 메뉴 이름에 추가
        menu_name_with_random = f"테스트용 음식 {random.randint(10, 999)}"
        menuname.clear()  # 기존 텍스트 초기화
        menuname.send_keys(menu_name_with_random)  # 텍스트 입력
        

    #카테고리 선택
    def select_category(self):
        # 카테고리 열기 버튼 클릭
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))).click()
        
        # 모든 카테고리 옵션 가져오기
        category_options = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']"))
        )
        
        # 랜덤으로 하나 선택
        selected_category = random.choice(category_options)
        
        # 선택한 카테고리 클릭
        selected_category.click()


    #후기 등록
    def add_comment(self):
        commentbox = self.wait.until(EC.presence_of_element_located((By.NAME, "comment")))
        commentbox.send_keys("테스트용 음식 후기입니다.")


    # 별점 추가
    def add_star(self, selected_type):
        # 식사 타입이 '그룹'일 경우 XPath 변경 (이 부분은 유지)
        if selected_type == "//*[@id='그룹']":
            random_score = random.randint(1, 5)
            star_xpath = f"//*[@id='modal-root']/div/div[2]/section/form/div[7]/div/div[{random_score}]"

            starclick = self.wait.until(EC.presence_of_element_located((By.XPATH, star_xpath)))
            time.sleep(2)
        else:
            # 1~5점 중 랜덤 선택
            random_score = random.randint(1, 5)
            star_xpath = f"//*[@id='modal-root']/div/div[2]/section/form/div[6]/div/div[{random_score}]"

            # 랜덤으로 선택한 별점 XPath 찾기
            starclick = self.wait.until(EC.presence_of_element_located((By.XPATH, star_xpath)))
            time.sleep(2)  # 클릭 전에 약간의 대기 추가

        starclick.click()

    #작성 완료
    def comment_submit(self):
        submitbtn = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='modal-root']/div/div[2]/section/form/button")))
        submitbtn.click()

