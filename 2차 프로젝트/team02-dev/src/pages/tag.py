import random
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.utils.helpers import Utils

class Tag:

    #로케이터
    TAG_PARENT_DIV = (By.CSS_SELECTOR, "div.tag-list") #태그 요소 부모
    TAG_CHILD_ELEMENTS = (By.XPATH, "./a") #태그 요소 부모를 활용한 자식
    TAG_LIST = (By.CSS_SELECTOR, "ul.tag-list")
    TAG_ITEMS = (By.XPATH, "./li")

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.wait = ws(driver, 10)
        self.helpers = Utils(driver)

    def tag_elements(self):
        # 태그 요소 부모요소 찾고 자식요소 모두 찾기
        parent_div = self.wait.until(EC.presence_of_element_located(self.TAG_PARENT_DIV))
        # 부모 기준 모든 직계 자식
        child_elements = parent_div.find_elements(*self.TAG_CHILD_ELEMENTS)
        # 모든 <a> 태그의 텍스트 출력
        if child_elements:
            for child in child_elements:
                print(child.text)
        else:
            print("ERROR: No child elements found!")
        return child_elements

    def random_choice(self,str):
        random_element = random.choice(str)
        random_element.click()
        print("Selected Element:", random_element.text)
        return random_element.text

    #게시글 찾기 몇번쨰 게시글인지 num를 통해주어짐
    def find_article(self,num):
        # 선택자를 동적으로 변경
        selector = f".article-preview:nth-of-type({num}) h1"
        # 요소가 나타날 때까지 기다림
        h1_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))  # ✅ num을 반영한 선택자 사용
        h1_element.click()

    def validate_selection(self, selected_text):
        """ 선택된 태그가 <ul class='tag-list'> 내부에 포함되어 있는지 확인 """
        tag_list = self.wait.until(EC.presence_of_element_located(self.TAG_LIST))
        tag_items = tag_list.find_elements(*self.TAG_ITEMS)  # <ul> 내부의 모든 <li> 요소 가져오기

        tag_texts = [item.text for item in tag_items]  # <li> 요소들의 텍스트 리스트 생성

        if selected_text in tag_texts:
            print(f"✅ Selected Tag '{selected_text}' is in the tag-list!")
            return True
        else:
            print(f"❌ Selected Tag '{selected_text}' is NOT in the tag-list!")
            return False

    def find_tag(self, str):
        # 태그 요소 부모요소 찾고 자식요소 모두 찾기
        parent_div = self.wait.until(EC.presence_of_element_located((self.TAG_PARENT_DIV)))
        # 부모 기준 모든 직계 자식
        child_elements = parent_div.find_elements(*self.TAG_CHILD_ELEMENTS)

        # 특정 tags 값이 포함된 요소 찾기
        matched_elements = [child for child in child_elements if child.text.strip() in str]

        if matched_elements:
            for matched in matched_elements:
                print(f"✅ Found Tag: {matched.text}")
            return matched_elements  # 찾은 요소 리스트 반환
        else:
            print("❌ No matching tags found!")
            return []