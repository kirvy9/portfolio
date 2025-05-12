import pytest
import logging
import time # time: 테스트 중 지연
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.webdriver import WebDriver
from src.utils.helpers import Utils
from src.pages.profile import ProfilePage
from src.pages.edit_profile import EditProfilePage

#.env 파일 로드
load_dotenv("src/config/.env")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,  # 로그 레벨 설정 (INFO 이상만 기록)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 로그 메시지 형식
    handlers=[
        logging.FileHandler("test_profile.log"),  # 파일로 로그 출력
        logging.StreamHandler()  # 콘솔로 로그 출력
    ]
)
logger = logging.getLogger(__name__) # 현재 모듈 이름의 로거

class TestProfileFeatures:
    """프로필 및 프로필 수정 관련 테스트 클래스"""
    #@pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_ts001_access_profile(self, driver: WebDriver):
        """TS-001: 로그인 후 프로필 페이지 접근 테스트"""
        utils = Utils(driver)
        time.sleep(1)
        logger.info("TS-001: 계정으로 로그인 시도")
        utils.utils_login(EMAIL, PASSWORD) # TODO: 실제 로그인 정보 사용
        time.sleep(1)
        logger.info("TS-001: 로그인 성공")

        profile_page = ProfilePage(driver)
        time.sleep(1)
        logger.info("TS-001: 프로필 버튼 클릭")
        profile_page.click_profile_button()

        time.sleep(1)
        logger.info("TS-001: 프로필 페이지 로딩 확인")
        assert profile_page.is_profile_page(), "프로필 페이지로 이동하지 못했습니다."
        time.sleep(1)
        logger.info("TS-001: 프로필 페이지 로딩 성공")

        time.sleep(1)
        logger.info("TS-001: 테스트 완료")

    #@pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_ts001_edit_profile_settings(self, driver: WebDriver):
        """TS-001: 프로필 설정 수정 기능 테스트"""
        utils = Utils(driver)
        time.sleep(1)
        logger.info("TS-001: 계정으로 로그인 시도")
        utils.utils_login(EMAIL, PASSWORD) # TODO: 실제 로그인 정보 사용
        time.sleep(1)
        logger.info("TS-001: 로그인 성공")

        profile_page = ProfilePage(driver)
        time.sleep(1)
        logger.info("TS-001: 프로필 버튼 클릭")
        profile_page.click_profile_button()

        time.sleep(1)
        logger.info("TS-001: 'Edit Profile Settings' 버튼 클릭")
        profile_page.click_edit_profile_button()

        edit_profile_page = EditProfilePage(driver)
        time.sleep(1)
        logger.info("TS-001: 프로필 수정 페이지 로딩 확인")
        assert edit_profile_page.is_edit_profile_page(), "프로필 수정 페이지로 이동하지 못했습니다."
        time.sleep(1)
        logger.info("TS-001: 프로필 수정 페이지 로딩 성공")

        # TODO: 실제 정보 수정 및 검증 로직 추가 필요
        time.sleep(1)
        logger.info("TS-001: 테스트 완료")

    def test_ts001_profile_info_display(self, driver: WebDriver):
        """TS-001: 프로필 페이지의 사용자 정보(Bio) 표시 확인 테스트
    
        이 테스트는 로그인 후 프로필 페이지로 이동하여 표시된 Bio 정보가 
        존재하는지 확인합니다.
        """
        logger.info("TS-001: 테스트 시작 - 프로필 Bio 정보 표시 확인")
    
        utils = Utils(driver)
        time.sleep(1)
        logger.info("TS-001: 계정으로 로그인 시도")
        utils.utils_login(EMAIL, PASSWORD)  # TODO: 실제 로그인 정보 사용
        time.sleep(1)
        logger.info("TS-001: 로그인 성공")
    
        profile_page = ProfilePage(driver)
        time.sleep(1)
        logger.info("TS-001: 프로필 버튼 클릭")
        profile_page.click_profile_button()
        time.sleep(1)
    
        logger.info("TS-001: 프로필 페이지 로딩 확인")
        assert profile_page.is_profile_page(), "프로필 페이지로 이동하지 못했습니다."
        time.sleep(1)
        logger.info("TS-001: 프로필 페이지 로딩 성공")
    
        logger.info("TS-001: 프로필 Bio 정보 가져오기 시도")
        bio_text = profile_page.get_bio_text()
        time.sleep(1)
    
        # Bio 정보 존재 여부 확인 (구체적인 내용보다는 존재 여부만 검증)
        logger.info(f"TS-001: 가져온 Bio 정보: '{bio_text}'")
        assert bio_text != "", "프로필 페이지에 Bio 정보가 표시되지 않습니다."
        logger.info("TS-001: Bio 정보가 존재함을 확인")
    
        # 추가적인 검증이 필요한 경우 여기에 구현
        # 예: 특정 문자열 포함 여부, 최대 길이 초과 여부 등
    
        logger.info("TS-001: 테스트 완료 - 프로필 Bio 정보 표시 확인 성공")