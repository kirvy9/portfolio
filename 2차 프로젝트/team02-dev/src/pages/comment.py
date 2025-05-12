import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.utils.helpers import Utils

class Comment:

    #로케이터
    COMMENT_ELEMENTS = (By.CSS_SELECTOR, "p.card-text")

    def __init__(self,driver : WebDriver):
        self.driver = driver
        self.wait = ws(driver, 10)
        self.helpers = Utils(driver)

    #게시글 찾기 몇번쨰 게시글인지 num를 통해주어짐
    def find_article(self,num):
        # 선택자를 동적으로 변경
        selector = f".article-preview:nth-of-type({num}) h1"
        # 요소가 나타날 때까지 기다림
        h1_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))  # ✅ num을 반영한 선택자 사용
        h1_element.click()
    
    #마지막 댓글 비교 검증
    def comment_assert(self,str):
        comment_elements = self.wait.until(EC.presence_of_all_elements_located(self.COMMENT_ELEMENTS))
        # 마지막 번째 댓글의 텍스트 가져오기
        last_comment = comment_elements[-1].text  # ✅ 마지막 요소 접근

        # 기대 값과 비교하여 검증
        assert last_comment == str, f"❌ 댓글 불일치! 기대한 값: '{str}', 실제 값: '{last_comment}'"
        print(f"✅ 마지막 댓글 {last_comment} 이 정상적으로 입력되었습니다!")
    
    #마지막 댓글 사라졌는지 검증
    def comment_del_assert(self, expected_comment: str):
        try:
            # 모든 댓글 요소 가져오기
            comment_elements = self.wait.until(EC.presence_of_all_elements_located(self.COMMENT_ELEMENTS))

            # 댓글이 하나도 없는 경우 검증
            if not comment_elements:
                print("✅ 모든 댓글이 삭제되었습니다!")
                return True  # 테스트를 종료할 수 있도록 True 반환

            # 마지막 댓글 가져오기
            last_comment = comment_elements[-1].text

            # 기대 값과 비교하여 검증
            assert last_comment != expected_comment, f"❌ 댓글 불일치! 마지막 댓글 '{last_comment}' 이 안 사라졌습니다."
            print(f"✅ 마지막 댓글 '{expected_comment}' 이 정상적으로 삭제되었습니다!")

            return False  # 테스트 진행을 위해 False 반환

        except TimeoutException:
            # 댓글 요소 자체가 없는 경우 예외 처리
            print("⏰ Timeout: 댓글 요소를 찾을 수 없습니다.")
            pytest.fail("댓글 요소를 찾을 수 없었습니다. Timeout 발생!", pytrace=True)
            return False  # 테스트를 종료할 수 있도록 False 반환


