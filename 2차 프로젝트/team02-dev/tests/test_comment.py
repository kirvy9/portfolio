import pytest
import os
import time
import logging
from dotenv import load_dotenv
from src.utils.helpers import Utils
from src.pages.comment import Comment
from selenium.webdriver.common.by import By

load_dotenv("src/config/.env")

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
COMMENT = "댓글입력하기"

@pytest.fixture
def setup(driver,request):
    #로그 및 스크린샷 설정
    PAGE_NAME = "test_comment"
    FUNC_NAME = request.node.name
    REPORT = Utils.utils_reports_setting(PAGE_NAME, FUNC_NAME)
    #공통 모듈
    comment = Comment(driver)
    helpers = Utils(driver)
    #로그인
    helpers.utils_login(EMAIL, PASSWORD)
    return REPORT,comment, helpers

class Testcomment:

    #로케이터
    GLOBAL_FEED = (By.XPATH, "//a[contains(text(), 'Global Feed')]")
    SEND_COMMENT = (By.CSS_SELECTOR, "textarea.form-control")
    COMMENT_BTN = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-primary")
    DELETE_BTN = (By.CSS_SELECTOR, "span.mod-options i.ion-trash-a")
    
    #댓글 작성 및 확인 후 삭제
    def test_comment(self,setup):
        REPORT, comment, helpers = setup
        logging.info("✅ 테스트 시작: 댓글 작성 및 삭제")

        # global feed 들어가기
        logging.info("➡ Global Feed 페이지 이동")
        helpers.xpath_element(self.GLOBAL_FEED)
        time.sleep(1)

        # n번째 게시글 들어가기
        logging.info("➡ 2번째 게시글 클릭")
        comment.find_article(2)
        time.sleep(1)

        # 댓글 입력 + 작성
        logging.info("📝 댓글 입력: '댓글 입력하기3'")
        helpers.css_selector_send(self.SEND_COMMENT, COMMENT)
        helpers.css_selector_element(self.COMMENT_BTN)
        time.sleep(1)

        # 댓글 작성 검증
        logging.info("🔍 댓글 작성 여부 검증")
        comment.comment_assert(COMMENT)
        time.sleep(1)

        # 쓰레기통 아이콘 찾은 후 마지막 댓글 삭제
        logging.info("🗑 댓글 삭제 시도")
        helpers.css_selector_elements(self.DELETE_BTN, -1)
        time.sleep(1)

        # 댓글 삭제 검증
        #logging.info("🔍 댓글 삭제 여부 검증")
        #comment.comment_del_assert(COMMENT)
        #time.sleep(2)

        logging.info("✅ 댓글 테스트 완료")


