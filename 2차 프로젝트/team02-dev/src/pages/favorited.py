from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List, Tuple

class FavoritePage:
    """
    게시글 좋아요 기능 및 프로필의 'Favorited Articles' 탭과 관련된 웹 요소 및 동작을 정의합니다.
    """
    # 피드 관련 선택자
    GLOBAL_FEED_TAB = (By.XPATH, "//a[text()='Global Feed']")
    FEED_TOGGLE = (By.CSS_SELECTOR, ".feed-toggle")  # 페이지 로딩 확인용
    
    # 게시글과 관련 선택자
    ARTICLE_PREVIEWS = (By.CSS_SELECTOR, ".article-preview")
    ARTICLE_TITLE = (By.CSS_SELECTOR, ".preview-link h1")
    NO_ARTICLES_MESSAGE = (By.XPATH, "//div[contains(@class, 'article-preview') and contains(text(), 'No articles are here... yet.')]")
    
    # 좋아요 버튼 관련 선택자
    FAVORITE_BUTTONS = (By.CSS_SELECTOR, ".btn.btn-sm.btn-outline-primary, .btn.btn-sm.btn-primary")
    UNFAVORITED_BUTTON = (By.CSS_SELECTOR, ".btn.btn-sm.btn-outline-primary")  # 좋아요 안한 상태
    FAVORITED_BUTTON = (By.CSS_SELECTOR, ".btn.btn-sm.btn-primary")  # 좋아요 한 상태
    
    # 프로필 페이지 관련 선택자 (HTML에 맞게 수정)
    USERNAME_LINK = (By.CSS_SELECTOR, "a.nav-link[href^='/@']")  # 상단 네비게이션 바의 사용자 이름 링크
    MY_ARTICLES_TAB = (By.CSS_SELECTOR, ".nav-pills .nav-link[href*='/@']")  # My Articles 탭
    FAVORITED_ARTICLES_TAB = (By.CSS_SELECTOR, ".nav-pills .nav-link[href*='/favorites']")  # Favorited Articles 탭
    
    def __init__(self, driver: WebDriver):
        """
        FavoritePage 클래스의 생성자입니다.
        :param driver: Selenium WebDriver 인스턴스
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) # 명시적 대기를 위한 WebDriverWait 객체 (최대 10초)
    
    def click_global_feed(self):
        """Global Feed 탭을 클릭하고, 게시글 목록이 로드될 때까지 대기합니다."""
        global_feed_tab = self.wait.until(
            EC.element_to_be_clickable(self.GLOBAL_FEED_TAB)
        )
        global_feed_tab.click()
        # 페이지 로드 대기
        self.wait.until(
            EC.presence_of_element_located(self.ARTICLE_PREVIEWS)
        )
        print("Global Feed 탭으로 전환했습니다.")
    
    def get_favorite_buttons(self):
        """
        현재 페이지에 표시된 모든 게시글의 좋아요 버튼 요소 목록을 가져옵니다.
        :return: 좋아요 버튼 웹 요소의 리스트
        """
        # 모든 좋아요 버튼 요소를 찾을 때까지 대기
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.FAVORITE_BUTTONS)
        )
        return buttons
    
    def get_article_titles(self):
        """
        현재 페이지에 표시된 모든 게시글의 제목 텍스트 목록을 가져옵니다.
        게시글이 없다는 메시지가 표시되면 빈 리스트를 반환합니다.
        :return: 게시글 제목 문자열 리스트
        """
        try:
            # "No articles" 메시지가 있는지 확인
            no_articles = self.driver.find_elements(*self.NO_ARTICLES_MESSAGE)
            if no_articles:
                print("게시글이 없습니다.")
                return []
            
            # 모든 게시글 제목 요소를 찾을 때까지 대기
            titles = self.wait.until(
                EC.presence_of_all_elements_located(self.ARTICLE_TITLE)
            )
            return [title.text for title in titles]
        except Exception as e:
            print(f"게시글 제목 가져오기 실패: {str(e)}")
            return []
    
    def click_favorite_button(self, article_index=0):
        """
        지정된 인덱스에 해당하는 게시글의 좋아요 버튼을 클릭합니다.
        클릭 전후의 좋아요 상태(여부, 개수)를 반환합니다.
        :param article_index: 좋아요 버튼을 클릭할 게시글의 인덱스 (0부터 시작)
        :return: 작업 성공 여부와 클릭 전후 상태를 담은 딕셔너리.
                 성공 시: {"success": True, "before_state": {...}, "after_state": {...}}
                 실패 시: {"success": False} 또는 {"success": False, "error": "에러 메시지"}
        """
        try:
            # 모든 좋아요 버튼 가져오기
            favorite_buttons = self.get_favorite_buttons()
            
            if article_index < len(favorite_buttons):
                # 클릭 전 상태 확인
                button = favorite_buttons[article_index]
                is_favorited_before = "btn-primary" in button.get_attribute("class") # 'btn-primary' 클래스가 있으면 좋아요 된 상태
                initial_count = self.get_favorite_count(button) # 버튼 텍스트에서 좋아요 수 추출
                
                # 버튼 클릭
                button.click()
                print(f"게시글 #{article_index}의 좋아요 버튼을 클릭했습니다.")
                
                # DOM 업데이트 및 상태 변경을 위한 잠시 대기
                import time
                time.sleep(1)
                
                # 클릭 후 상태 확인을 위해 버튼 다시 가져오기
                favorite_buttons = self.get_favorite_buttons()
                button = favorite_buttons[article_index]
                is_favorited_after = "btn-primary" in button.get_attribute("class")
                after_count = self.get_favorite_count(button)
                
                return {
                    "success": True,
                    "before_state": {
                        "is_favorited": is_favorited_before,
                        "count": initial_count
                    },
                    "after_state": {
                        "is_favorited": is_favorited_after,
                        "count": after_count
                    }
                }
            else:
                print(f"인덱스 {article_index}에 해당하는 게시글이 없습니다.")
                return {"success": False}
        except Exception as e:
            print(f"좋아요 버튼 클릭 중 오류 발생: {str(e)}")
            return {"success": False, "error": str(e)}
    
    def get_favorite_count(self, button_element):
        """
        주어진 좋아요 버튼 웹 요소에서 좋아요 수를 추출합니다.
        버튼 텍스트에서 숫자 부분만 파싱하여 정수형으로 반환합니다. 숫자가 없으면 0을 반환합니다.
        :param button_element: 좋아요 수를 추출할 버튼의 웹 요소
        :return: 추출된 좋아요 수 (정수), 실패 시 0
        """
        try:
            button_text = button_element.text.strip()
            # 버튼 텍스트에서 숫자 부분만 추출 (예: " 5" -> 5)
            count_text = ''.join(filter(str.isdigit, button_text))
            count = int(count_text) if count_text else 0
            return count
        except Exception as e:
            print(f"좋아요 수 추출 중 오류 발생: {str(e)}")
            return 0
    
    def is_article_favorited(self, article_index=0):
        """
        지정된 인덱스의 게시글이 현재 좋아요 상태인지 확인하고, 좋아요 수도 함께 반환합니다.
        :param article_index: 확인할 게시글의 인덱스 (0부터 시작)
        :return: 좋아요 상태와 수를 담은 딕셔너리 ({"is_favorited": bool, "count": int})
                 해당 인덱스의 게시글이 없거나 오류 발생 시 None 반환.
        """
        try:
            favorite_buttons = self.get_favorite_buttons()
            if article_index < len(favorite_buttons):
                button = favorite_buttons[article_index]
                is_favorited = "btn-primary" in button.get_attribute("class")
                count = self.get_favorite_count(button)
                return {
                    "is_favorited": is_favorited,
                    "count": count
                }
            else:
                print(f"인덱스 {article_index}에 해당하는 게시글이 없습니다.")
                return None
        except Exception as e:
            print(f"좋아요 상태 확인 중 오류 발생: {str(e)}")
            return None
    
    # 프로필 페이지 이동 및 확인 메서드
    def go_to_my_profile(self):
        """
        상단 네비게이션 바의 사용자 이름 링크를 클릭하여 내 프로필 페이지로 이동합니다.
        이동 후 'My Articles' 탭이 로드될 때까지 대기합니다.
        :return: 이동 성공 시 True, 실패 시 False
        """
        try:
            # 상단 네비게이션 바의 사용자 이름 링크 클릭
            username_link = self.wait.until(
                EC.element_to_be_clickable(self.USERNAME_LINK)
            )
            username_link.click()
            
            # 프로필 페이지 로딩 대기
            self.wait.until(
                EC.presence_of_element_located(self.MY_ARTICLES_TAB)
            )
            print("내 프로필 페이지로 이동했습니다.")
            return True
        except Exception as e:
            print(f"프로필 페이지 이동 중 오류 발생: {str(e)}")
            return False
    
    def click_favorited_articles_tab(self):
        """
        프로필 페이지 내의 'Favorited Articles' 탭을 클릭합니다.
        클릭 후 내용 로드를 위해 잠시 대기합니다.
        :return: 클릭 성공 시 True, 실패 시 False
        """
        try:
            favorited_tab = self.wait.until(
                EC.element_to_be_clickable(self.FAVORITED_ARTICLES_TAB)
            )
            favorited_tab.click()
            
            # 탭 클릭 후 로딩 대기
            import time # DOM 업데이트 대기
            time.sleep(1)
            print("Favorited Articles 탭으로 전환했습니다.")
            return True
        except Exception as e:
            print(f"Favorited Articles 탭 클릭 중 오류 발생: {str(e)}")
            return False
    
    def is_article_in_favorited_list(self, article_title):
        """
        'Favorited Articles' 탭의 목록에서 특정 제목의 게시글이 있는지 확인합니다.
        게시글이 없다는 메시지가 표시되면 False를 반환합니다.
        :param article_title: 확인할 게시글의 제목
        :return: 해당 제목의 게시글이 목록에 있으면 True, 없으면 False
        """
        try:
            # "No articles" 메시지가 있는지 확인
            no_articles = self.driver.find_elements(*self.NO_ARTICLES_MESSAGE)
            if no_articles:
                print("Favorited Articles 목록이 비어 있습니다.")
                return False
                
            # 현재 표시된 모든 게시글 제목 가져오기
            titles = self.get_article_titles()
            
            # 특정 제목이 목록에 있는지 확인
            is_found = article_title in titles
            if is_found:
                print(f"게시글 '{article_title}'이 Favorited Articles 목록에 있습니다.")
            else:
                print(f"게시글 '{article_title}'이 Favorited Articles 목록에 없습니다.")
                print(f"현재 목록의 게시글들: {titles}")
            
            return is_found
        except Exception as e:
            print(f"즐겨찾기 목록 확인 중 오류 발생: {str(e)}")
            return False