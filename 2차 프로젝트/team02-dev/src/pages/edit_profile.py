from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditProfilePage:
    """
    프로필 수정 페이지("Your Settings")와 관련된 웹 요소 및 동작을 정의하는 클래스입니다.
    Page Object Model (POM) 디자인 패턴을 따릅니다.
    """

    # --- 페이지 식별자 로케이터 ---
    SETTINGS_PAGE = (By.CLASS_NAME, "settings-page")  # 프로필 수정 페이지 전체를 감싸는 컨테이너 요소
    PAGE_TITLE = (By.XPATH, "//h1[text()='Your Settings']")  # 페이지 제목 "Your Settings"

    # --- 입력 필드 로케이터 ---
    PROFILE_URL_INPUT = (By.CSS_SELECTOR, "input[placeholder='URL of profile picture']")  # 프로필 사진 URL 입력 필드
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Username']")  # 사용자 이름 입력 필드
    BIO_TEXTAREA = (By.CSS_SELECTOR, "textarea[placeholder='Short bio about you']")  # 자기소개 입력 텍스트 영역
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")  # 이메일 입력 필드
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='New Password']")  # 새 비밀번호 입력 필드

    # --- 버튼 로케이터 ---
    UPDATE_BUTTON = (By.CSS_SELECTOR, ".btn-primary")  # "Update Settings" 버튼
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".btn-outline-danger")  # "Or click here to logout." 버튼

    def __init__(self, driver: WebDriver):
        """
        EditProfilePage 클래스의 생성자입니다.

        :param driver: Selenium WebDriver 인스턴스
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 명시적 대기를 위한 WebDriverWait 객체 초기화 (최대 10초)

    def is_edit_profile_page(self) -> bool:
        """
        현재 페이지가 프로필 수정 페이지("Your Settings")인지 확인합니다.
        페이지의 특정 요소(컨테이너, 제목) 존재 여부로 판단합니다.

        :return: 프로필 수정 페이지이면 True, 아니면 False
        """
        try:
            self.wait.until(EC.presence_of_element_located(self.SETTINGS_PAGE))  # 페이지 컨테이너 요소 확인
            self.wait.until(EC.presence_of_element_located(self.PAGE_TITLE))  # 페이지 제목 요소 확인
            return True
        except:
            # 요소 중 하나라도 없으면 프로필 수정 페이지가 아님
            return False

    def get_profile_url(self) -> str:
        """프로필 이미지 URL 입력 필드의 현재 값을 가져옵니다."""
        url_field = self.wait.until(EC.visibility_of_element_located(self.PROFILE_URL_INPUT))  # URL 입력 필드가 보일 때까지 대기
        return url_field.get_attribute('value')  # 입력 필드의 'value' 속성 값 반환

    def update_profile_url(self, url: str):
        """프로필 이미지 URL 입력 필드의 값을 주어진 URL로 업데이트합니다."""
        url_field = self.wait.until(EC.visibility_of_element_located(self.PROFILE_URL_INPUT))  # URL 입력 필드가 보일 때까지 대기
        url_field.clear()  # 기존 값 삭제
        url_field.send_keys(url)  # 새 URL 입력
        return self  # 메서드 체이닝을 위해 self 반환

    def get_username(self) -> str:
        """사용자 이름 입력 필드의 현재 값을 가져옵니다."""
        username_field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))  # 사용자 이름 입력 필드가 보일 때까지 대기
        return username_field.get_attribute('value')  # 입력 필드의 'value' 속성 값 반환

    def update_username(self, username: str):
        """사용자 이름 입력 필드의 값을 주어진 사용자 이름으로 업데이트합니다."""
        username_field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))  # 사용자 이름 입력 필드가 보일 때까지 대기
        username_field.clear()  # 기존 값 삭제
        username_field.send_keys(username)  # 새 사용자 이름 입력
        return self  # 메서드 체이닝을 위해 self 반환

    def get_bio(self) -> str:
        """자기소개 텍스트 영역의 현재 값을 가져옵니다."""
        bio_field = self.wait.until(EC.visibility_of_element_located(self.BIO_TEXTAREA))  # 자기소개 텍스트 영역이 보일 때까지 대기
        return bio_field.get_attribute('value')  # 텍스트 영역의 'value' 속성 값 반환

    def update_bio(self, bio: str):
        """자기소개 텍스트 영역의 값을 주어진 자기소개로 업데이트합니다."""
        bio_field = self.wait.until(EC.visibility_of_element_located(self.BIO_TEXTAREA))  # 자기소개 텍스트 영역이 보일 때까지 대기
        bio_field.clear()  # 기존 값 삭제
        bio_field.send_keys(bio)  # 새 자기소개 입력
        return self  # 메서드 체이닝을 위해 self 반환

    def get_email(self) -> str:
        """이메일 입력 필드의 현재 값을 가져옵니다."""
        email_field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))  # 이메일 입력 필드가 보일 때까지 대기
        return email_field.get_attribute('value')  # 입력 필드의 'value' 속성 값 반환

    def update_email(self, email: str):
        """이메일 입력 필드의 값을 주어진 이메일로 업데이트합니다."""
        email_field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))  # 이메일 입력 필드가 보일 때까지 대기
        email_field.clear()  # 기존 값 삭제
        email_field.send_keys(email)  # 새 이메일 입력
        return self  # 메서드 체이닝을 위해 self 반환

    def update_password(self, password: str):
        """새 비밀번호 입력 필드의 값을 주어진 비밀번호로 업데이트합니다."""
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))  # 비밀번호 입력 필드가 보일 때까지 대기
        password_field.clear()  # 기존 값 삭제 (보통 비밀번호 필드는 clear하지 않지만, 여기서는 명시적으로)
        password_field.send_keys(password)  # 새 비밀번호 입력
        return self  # 메서드 체이닝을 위해 self 반환

    def click_update_button(self):
        """ "Update Settings" 버튼을 클릭합니다.
        클릭 후, 페이지가 변경되거나 요소가 사라질 수 있으므로 staleness_of를 사용하여 대기합니다.
        """
        update_button = self.wait.until(EC.element_to_be_clickable(self.UPDATE_BUTTON))  # 업데이트 버튼이 클릭 가능할 때까지 대기
        update_button.click()
        # 업데이트 후 페이지가 변경되거나 해당 버튼이 DOM에서 사라지는 것을 대기 (새로고침 또는 리다이렉션)
        self.wait.until(EC.staleness_of(update_button))
        return self  # 메서드 체이닝을 위해 self 반환

    def click_logout_button(self):
        """ "Or click here to logout." 버튼을 클릭합니다."""
        logout_button = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))  # 로그아웃 버튼이 클릭 가능할 때까지 대기
        logout_button.click()
        return self  # 메서드 체이닝을 위해 self 반환