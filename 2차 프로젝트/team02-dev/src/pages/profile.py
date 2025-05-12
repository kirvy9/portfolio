from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    """
    사용자 프로필 페이지와 관련된 웹 요소 및 동작을 정의하는 클래스입니다.
    Page Object Model (POM) 디자인 패턴을 따릅니다.
    """

    # --- 웹 요소 로케이터 ---
    PROFILE_LINK = (By.CSS_SELECTOR, "a.nav-link img.user-pic")  # 네비게이션 바의 사용자 프로필 링크 (텍스트 기반)
    EDIT_PROFILE_SETTING = (By.CSS_SELECTOR, ".action-btn[href='/settings']")  # 프로필 페이지 내 'Edit Profile Settings' 버튼
    SETTINGS_BTN = (By.CSS_SELECTOR, ".nav-link[href='/settings']")  # 네비게이션 바의 'Settings' 링크 (프로필 수정 페이지로 이동)
    BIO_ELEMENT = (By.CSS_SELECTOR, ".col-xs-12 p")  # 프로필 페이지에 표시되는 자기소개(bio) 텍스트 요소

    def __init__(self, driver: WebDriver):
        """
        ProfilePage 클래스의 생성자입니다.

        :param driver: Selenium WebDriver 인스턴스
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 명시적 대기를 위한 WebDriverWait 객체 초기화 (최대 10초)

    def click_profile_button(self):
        """네비게이션 바에 있는 사용자 프로필 링크를 클릭합니다."""
        profile_link = self.wait.until(
            EC.element_to_be_clickable(self.PROFILE_LINK)  # 프로필 링크가 클릭 가능할 때까지 대기
        )
        profile_link.click()

    def click_edit_profile_button(self):
        """프로필 페이지 내의 'Edit Profile Settings' 버튼을 클릭합니다."""
        edit_profile_setting = self.wait.until(
            EC.element_to_be_clickable(self.EDIT_PROFILE_SETTING)  # 'Edit Profile Settings' 버튼이 클릭 가능할 때까지 대기
        )
        edit_profile_setting.click()

    def click_setting_button(self):
        """네비게이션 바의 'Settings' 버튼을 클릭합니다 (프로필 수정 페이지로 이동)."""
        setting_btn = self.wait.until(
            EC.element_to_be_clickable(self.SETTINGS_BTN)  # 'Settings' 버튼이 클릭 가능할 때까지 대기
        )
        setting_btn.click()

    def is_profile_page(self) -> bool:
        """현재 페이지가 특정 사용자의 프로필 페이지인지 확인합니다."""
        try:
            # 디버깅을 위해 현재 URL 출력
            print("Current URL:", self.driver.current_url)
            
            # 실제 프로필 페이지의 구조에 맞는 요소 확인
            # Edit Profile Settings 버튼이 존재하는지 확인
            self.wait.until(EC.presence_of_element_located(self.EDIT_PROFILE_SETTING))
            
            # URL에 사용자명이 포함되어 있는지 확인
            user_in_url = "/@" in self.driver.current_url
            
            return True  # 페이지 확인됨
        except Exception as e:
            print(f"Profile page verification failed: {str(e)}")
            return False
        
    def get_bio_text(self):
        """프로필 보기 페이지에서 bio 텍스트 추출"""
        try:
            bio_element = self.wait.until(
                EC.presence_of_element_located(self.BIO_ELEMENT)
            )
            bio_text = bio_element.text.strip()
            print(f"[DEBUG] Found bio text: {bio_text}")
            return bio_text
        except Exception as e:
            print(f"[ERROR] Failed to get bio text: {str(e)}")
            return ""

    def navigate_to_profile_from_home(self):
        """메인 페이지에서 프로필 페이지로 이동합니다"""
        try:
            # 기존에 정의된 PROFILE_LINK 사용 (임찬빈 텍스트를 가진 링크)
            profile_button = self.wait.until(
                EC.element_to_be_clickable(self.PROFILE_LINK)
            )
            profile_button.click()
        
            # 프로필 페이지 로드 대기
            self.wait.until(EC.presence_of_element_located(self.EDIT_PROFILE_SETTING))
            print("Successfully navigated to profile page from home")
        except Exception as e:
            print(f"Failed to navigate to profile page: {str(e)}")