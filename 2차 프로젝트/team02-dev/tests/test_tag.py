import pytest
import os
import time
import logging
from dotenv import load_dotenv
from src.utils.helpers import Utils
from src.pages.tag import Tag
from src.pages.postpage import PostPage, generate_unique_text

load_dotenv("src/config/.env")

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
tags = "aasdfasdf"

@pytest.fixture
def setup(driver,request):
    #로그 및 스크린샷 설정
    PAGE_NAME = "test_tag"
    FUNC_NAME = request.node.name
    REPORT = Utils.utils_reports_setting(PAGE_NAME, FUNC_NAME)
    #공통 모듈
    tag = Tag(driver)
    helpers = Utils(driver)
    postpage = PostPage(driver)
    #로그인
    helpers.utils_login(EMAIL, PASSWORD)
    return REPORT,tag, helpers, postpage

class TestTag:

    def test_TC_501(self,setup):
        logging.info("📝 TC_501 테스트 시작")
        REPORT, tag, _, _ = setup  # helpers, postpage 미사용

        # 태그 요소 찾고 출력
        logging.info("🔍 태그 요소 검색")
        tag_elements = tag.tag_elements()
        time.sleep(1)

        # 찾은 태그 바탕으로 랜덤하게 클릭
        logging.info("🎯 랜덤 태그 선택 및 클릭")
        random_element = tag.random_choice(tag_elements)
        time.sleep(1)

        # 첫 번째 게시글 클릭
        logging.info("📌 첫 번째 게시글 클릭")
        tag.find_article(1)
        time.sleep(1)

        # 게시글 안에 태그 있는지 확인
        logging.info(f"✅ 게시글 내 태그 확인: {random_element}")
        tag.validate_selection(random_element)
        time.sleep(1)

        logging.info("🎉 TC_501 테스트 완료")

    def test_TC_502(self,setup):
        logging.info("📝 TC_502 테스트 시작")
        REPORT, tag, helpers, postpage = setup

        for i in range(2):  # 2번 반복 실행
            logging.info(f"📄 {i+1}번째 게시글 작성 시작")

            title = generate_unique_text("제목")
            topic = generate_unique_text("주제")
            body = generate_unique_text("내용")

            # 새 게시글 작성 클릭
            logging.info("🆕 새 게시글 작성 시작")
            postpage.click_newpost()

            # 제목, 내용 입력
            logging.info(f"🖊️ 제목: {title}, 주제: {topic}")
            postpage.enter_post_title(title)
            postpage.enter_post_topic(topic)
            postpage.enter_post_body(body)

            # 태그 입력
            logging.info(f"🏷️ 태그 입력: {tags}")
            postpage.enter_post_tags(tags)
            time.sleep(1)

            # 게시글 발행
            logging.info("🚀 게시글 발행 클릭")
            postpage.click_publish_article()
            time.sleep(1)

            logging.info(f"✅ {i+1}번째 게시글 작성 완료")

        # 메인 로고 클릭하여 홈으로 이동
        logging.info("🏠 메인 페이지로 이동")
        helpers.main_logo()
        time.sleep(1)

        # 태그 찾아서 확인
        logging.info(f"🔎 입력한 태그({tags}) 확인 중...")
        tag.find_tag(tags)
        time.sleep(1)

        logging.info("🎉 TC_502 테스트 완료")