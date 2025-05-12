from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List

class FeedPage:
    """
    피드(Global Feed, Your Feed) 및 사용자 프로필 페이지의 팔로우/언팔로우 기능과 관련된 웹 요소 및 동작을 정의합니다.
    """
    # 피드 관련 선택자
    GLOBAL_FEED_TAB = (By.XPATH, "//a[text()='Global Feed']")
    YOUR_FEED_TAB = (By.XPATH, "//a[text()='Your Feed']")
    FEED_TOGGLE = (By.CSS_SELECTOR, ".feed-toggle")
    
    # 게시글과 작성자 관련 선택자
    ARTICLE_PREVIEWS = (By.CSS_SELECTOR, ".article-preview")
    ARTICLE_AUTHOR = (By.CSS_SELECTOR, ".article-meta .author")
    
    # 프로필 페이지 관련 선택자
    USERNAME = (By.CSS_SELECTOR, ".user-info h4")
    # 정확한 팔로우/언팔로우 버튼 선택자
    FOLLOW_BUTTON = (By.CSS_SELECTOR, ".btn.btn-sm.action-btn.btn-outline-secondary")
    UNFOLLOW_BUTTON = (By.CSS_SELECTOR, ".btn.btn-sm.action-btn.btn-secondary")
    
    def __init__(self, driver: WebDriver):
        """
        FeedPage 클래스의 생성자입니다.
        :param driver: Selenium WebDriver 인스턴스
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) # 명시적 대기를 위한 WebDriverWait 객체 (최대 10초)
    
    # 피드 탭 관련 메서드
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
    
    def click_your_feed(self):
        """Your Feed 탭을 클릭하고, 피드 토글 요소가 로드될 때까지 대기합니다."""
        your_feed_tab = self.wait.until(
            EC.element_to_be_clickable(self.YOUR_FEED_TAB)
        )
        your_feed_tab.click()
        # 페이지 로드 대기
        self.wait.until(
            EC.presence_of_element_located(self.FEED_TOGGLE)
        )
        print("Your Feed 탭으로 전환했습니다.")
    
    # 게시글 작성자 관련 메서드
    def get_article_authors(self) -> List[str]:
        """
        현재 페이지에 표시된 모든 게시글의 작성자 이름 목록을 가져옵니다.
        :return: 작성자 이름 문자열 리스트
        """
        # 모든 게시글 작성자 요소를 찾을 때까지 대기
        authors = self.wait.until(
            EC.presence_of_all_elements_located(self.ARTICLE_AUTHOR)
        )
        author_names = [author.text for author in authors]
        print(f"현재 페이지의 게시글 작성자들: {author_names}")
        return author_names
    
    def get_first_article_author(self) -> str:
        """
        현재 페이지의 첫 번째 게시글 작성자 이름을 가져옵니다.
        게시글이 없으면 빈 문자열을 반환합니다.
        :return: 첫 번째 게시글 작성자 이름 또는 빈 문자열
        """
        try:
            authors = self.get_article_authors()
            if authors:
                print(f"첫 번째 게시글 작성자: {authors[0]}")
                return authors[0]
            else:
                print("게시글이 없습니다.")
                return ""
        except Exception as e:
            print(f"첫 번째 게시글 작성자 가져오기 실패: {str(e)}")
            return ""
    
    def click_author_profile(self, author_name: str):
        """
        주어진 작성자 이름에 해당하는 프로필 링크를 클릭합니다.
        클릭 후 프로필 페이지의 사용자 이름이 로드될 때까지 대기합니다.
        :param author_name: 클릭할 작성자의 이름
        :return: 클릭 성공 시 True, 실패 시 False
        """
        try:
            # 정확한 선택자로 작성자 링크를 직접 클릭
            author_link = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//a[@class='author' and text()='{author_name}']")
                )
            )
            author_link.click()
            print(f"{author_name}의 프로필 링크를 클릭했습니다.")
            # 프로필 페이지 로딩 대기
            self.wait.until(
                EC.presence_of_element_located(self.USERNAME)
            )
            return True
        except Exception as e:
            print(f"작성자 프로필 클릭 중 오류 발생: {str(e)}")
            return False
    
    # 프로필 페이지 관련 메서드
    def is_other_profile_page(self) -> bool:
        """
        현재 페이지가 다른 사용자의 프로필 페이지인지 URL과 특정 요소(사용자 이름) 존재 여부로 확인합니다.
        프로필 URL은 '/@' 패턴을 포함한다고 가정합니다.
        :return: 다른 사용자의 프로필 페이지이면 True, 아니면 False
        """
        try:
            # 현재 URL 확인 (프로필 페이지는 보통 특정 패턴이 있음)
            current_url = self.driver.current_url
            if "/@" in current_url:  # 프로필 URL 패턴
                # 프로필 사용자 이름 표시 확인
                self.wait.until(EC.presence_of_element_located(self.USERNAME))
                print(f"다른 사용자의 프로필 페이지입니다. URL: {current_url}")
                return True
            return False
        except Exception as e:
            print(f"프로필 페이지 확인 중 오류 발생: {str(e)}")
            return False
    
    def get_profile_username(self) -> str:
        """
        현재 프로필 페이지에 표시된 사용자 이름을 가져옵니다.
        사용자 이름 요소를 찾지 못하면 빈 문자열을 반환합니다.
        :return: 프로필 페이지의 사용자 이름 또는 빈 문자열
        """
        try:
            username_element = self.wait.until(
                EC.presence_of_element_located(self.USERNAME)
            )
            username = username_element.text
            print(f"프로필 페이지 사용자: {username}")
            return username
        except Exception as e:
            print(f"사용자 이름 가져오기 실패: {str(e)}")
            return ""
    
    def click_follow_button(self):
        """
        프로필 페이지의 팔로우 버튼을 클릭합니다.
        클릭 후 버튼 상태 변경을 위해 잠시 대기합니다.
        :return: 클릭 성공 시 True, 실패 시 False
        """
        try:
            follow_button = self.wait.until(
                EC.element_to_be_clickable(self.FOLLOW_BUTTON)
            )
            button_text = follow_button.text
            follow_button.click()
            print(f"'{button_text}' 버튼을 클릭했습니다.")
            # 버튼 상태 변경 대기
            import time
            time.sleep(1)
            return True
        except Exception as e:
            print(f"팔로우 버튼 클릭 중 오류 발생: {str(e)}")
            return False
    
    def click_unfollow_button(self):
        """
        프로필 페이지의 언팔로우 버튼을 클릭합니다.
        클릭 후 버튼 상태 변경을 위해 잠시 대기합니다.
        :return: 클릭 성공 시 True, 실패 시 False
        """
        try:
            unfollow_button = self.wait.until(
                EC.element_to_be_clickable(self.UNFOLLOW_BUTTON)
            )
            button_text = unfollow_button.text
            unfollow_button.click()
            print(f"'{button_text}' 버튼을 클릭했습니다.")
            # 버튼 상태 변경 대기
            import time
            time.sleep(1)
            return True
        except Exception as e:
            print(f"언팔로우 버튼 클릭 중 오류 발생: {str(e)}")
            return False
    
    def is_following(self) -> bool:
        """
        현재 프로필의 사용자를 팔로우 중인지 확인합니다.
        언팔로우 버튼의 존재 여부로 판단합니다.
        :return: 팔로우 중이면 True, 아니면 False
        """
        try:
            # 언팔로우 버튼이 있는지 확인
            unfollow_buttons = self.driver.find_elements(*self.UNFOLLOW_BUTTON)
            if unfollow_buttons:
                print("사용자를 팔로우 중입니다.")
                return True
                
            print("사용자를 팔로우 중이 아닙니다.")
            return False
        except Exception as e:
            print(f"팔로우 상태 확인 중 오류 발생: {str(e)}")
            return False
    
    # Your Feed 게시글 확인 메서드
    def is_author_articles_visible(self, author_name: str) -> bool:
        """
        현재 피드(Your Feed 또는 Global Feed)에 특정 작성자의 게시글이 하나 이상 표시되는지 확인합니다.
        :param author_name: 확인할 게시글의 작성자 이름
        :return: 해당 작성자의 게시글이 보이면 True, 아니면 False
        """
        try:
            # 정확한 선택자로 작성자 이름 찾기
            authors = self.driver.find_elements(*self.ARTICLE_AUTHOR)
            for author in authors:
                if author.text == author_name:
                    print(f"{author_name}의 게시글이 피드에 표시됩니다.")
                    return True
            print(f"{author_name}의 게시글이 피드에 표시되지 않습니다.")
            return False
        except Exception as e:
            print(f"작성자 게시글 확인 중 오류 발생: {str(e)}")
            return False
    
    # 메인 페이지로 이동하는 메서드 (뒤로 가기)
    def go_back_to_main_page(self):
        """
        브라우저의 '뒤로 가기' 기능을 사용하여 이전 페이지(주로 메인 피드 페이지)로 이동합니다.
        이동 후 피드 토글 요소가 로드될 때까지 대기합니다.
        """
        self.driver.back()
        # 메인 페이지 로드 대기
        self.wait.until(
            EC.presence_of_element_located(self.FEED_TOGGLE)
        )
        print("이전 페이지로 이동했습니다.")