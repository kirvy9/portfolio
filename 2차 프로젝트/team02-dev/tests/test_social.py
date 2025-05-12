import pytest
import logging
import time # time: 테스트 중 지연
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.webdriver import WebDriver
from src.utils.helpers import Utils # Utils: 로그인 등 유틸리티 함수
from src.pages.feed import FeedPage # FeedPage: 피드 및 팔로우/언팔로우 기능
from src.pages.favorited import FavoritePage # FavoritePage: 게시글 좋아요 기능

#.env 파일 로드
load_dotenv("src/config/.env")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,  # 로그 레벨 설정 (INFO 이상만 기록)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 로그 메시지 형식
    handlers=[
        logging.FileHandler("test_social.log"),  # 파일로 로그 출력
        logging.StreamHandler()  # 콘솔로 로그 출력
    ]
)
logger = logging.getLogger(__name__)  # 현재 모듈 이름의 로거

class TestSocialFeatures:
    """
    소셜 기능 테스트 클래스입니다.
    팔로우, 언팔로우, 게시글 좋아요 및 프로필 연동 기능을 검증합니다.
    """

    #@pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_ts002_follow_user(self, driver: WebDriver):
        """TS-002: 다른 사용자 팔로우 및 Your Feed 게시글 노출 확인 테스트"""
        logger.info("TS-002: 테스트 시작 - 다른 사용자 팔로우 및 Your Feed 확인")
        time.sleep(1)

        # 로그인
        utils = Utils(driver)
        logger.info("TS-002: 계정으로 로그인 시도")
        time.sleep(1)
        utils.utils_login(EMAIL, PASSWORD)  # TODO: 실제 로그인 정보 사용
        logger.info("TS-002: 로그인 성공")
        time.sleep(1)

        # 메인페이지 이동 확인 (URL)
        logger.info(f"TS-002: 현재 URL: {driver.current_url}")
        time.sleep(1)
        assert "http://localhost:4100/" in driver.current_url, "로그인 후 메인페이지로 이동하지 않았습니다."
        logger.info("TS-002: 메인페이지로 정상 이동 확인")
        time.sleep(1)

        # FeedPage 객체 생성 (팔로우/언팔로우 로직 포함)
        feed_page = FeedPage(driver)
        logger.info("TS-002: FeedPage 객체 생성")
        time.sleep(1)

        # Global Feed 탭 클릭
        logger.info("TS-002: Global Feed 탭 클릭 시도")
        time.sleep(1)
        feed_page.click_global_feed()
        logger.info("TS-002: Global Feed 탭 클릭 완료")
        time.sleep(1)

        # Global Feed 첫 번째 게시글 작성자 가져오기
        logger.info("TS-002: 첫 번째 게시글 작성자 이름 가져오기 시도")
        time.sleep(1)
        author_name = feed_page.get_first_article_author()
        assert author_name, "게시글 작성자를 찾을 수 없습니다."
        logger.info(f"TS-002: 첫 번째 게시글 작성자: {author_name}")
        time.sleep(1)

        # 작성자 프로필 클릭
        logger.info(f"TS-002: {author_name}의 프로필 클릭 시도")
        time.sleep(1)
        assert feed_page.click_author_profile(author_name), f"{author_name}의 프로필로 이동하지 못했습니다."
        logger.info(f"TS-002: {author_name}의 프로필 클릭 완료")
        time.sleep(1)

        # 다른 사용자 프로필 페이지 이동 확인
        logger.info("TS-002: 다른 사용자 프로필 페이지 이동 확인 시도")
        time.sleep(1)
        assert feed_page.is_other_profile_page(), "다른 사용자의 프로필 페이지로 이동하지 못했습니다."
        logger.info("TS-002: 다른 사용자 프로필 페이지 이동 확인 완료")
        profile_username = feed_page.get_profile_username() # 팔로우할 사용자 프로필 이름
        assert profile_username, "프로필 페이지에서 사용자 이름을 찾을 수 없습니다."
        logger.info(f"TS-002: 프로필 페이지 사용자 이름: {profile_username}")
        time.sleep(1)

        # 팔로우 버튼 클릭
        logger.info("TS-002: 팔로우 버튼 클릭 시도")
        time.sleep(1)
        assert feed_page.click_follow_button(), "팔로우 버튼 클릭에 실패했습니다."
        logger.info("TS-002: 팔로우 버튼 클릭 완료")
        time.sleep(1)

        # 팔로우 상태 확인 (언팔로우 버튼 표시)
        logger.info("TS-002: 팔로우 상태 확인 (언팔로우 버튼 표시 여부) 시도")
        time.sleep(1)
        assert feed_page.is_following(), "팔로우 버튼이 정상적으로 동작하지 않았습니다."
        logger.info("TS-002: 팔로우 상태 확인 완료 (팔로우 중)")
        time.sleep(1)

        # 메인 페이지로 이동 (뒤로 가기)
        logger.info("TS-002: 메인 페이지로 뒤로 가기 시도")
        time.sleep(1)
        feed_page.go_back_to_main_page()
        logger.info("TS-002: 메인 페이지로 뒤로 가기 완료")
        time.sleep(1)

        # Your Feed로 이동
        logger.info("TS-002: Your Feed 탭 클릭 시도")
        time.sleep(1)
        feed_page.click_your_feed()
        logger.info("TS-002: Your Feed 탭 클릭 완료")
        time.sleep(1)

        # Your Feed에서 팔로우한 사용자 게시글 노출 확인
        logger.info(f"TS-002: Your Feed에서 {profile_username}의 게시글 노출 확인 시도")
        time.sleep(1)
        assert feed_page.is_author_articles_visible(profile_username), f"{profile_username}의 게시글이 Your Feed에 표시되지 않았습니다."
        logger.info(f"TS-002: 팔로우한 사용자 {profile_username}의 게시글이 Your Feed에 성공적으로 표시되었습니다.")
        time.sleep(1)

        # 테스트 완료 로그
        logger.info("TS-002: 테스트 완료")
        time.sleep(1)

    #@pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")  
    def test_ts003_unfollow_user(self, driver: WebDriver):
        """TS-003: 사용자 언팔로우 후 Your Feed에서 해당 사용자 게시글 즉시 사라짐 확인 테스트"""
        logger.info("TS-003: 테스트 시작 - 사용자 언팔로우 및 Your Feed 확인")
        time.sleep(1)

        # 로그인
        utils = Utils(driver)
        logger.info("TS-003: 계정으로 로그인 시도")
        time.sleep(1)
        utils.utils_login(EMAIL, PASSWORD)  # TODO: 실제 로그인 정보 사용
        logger.info("TS-003: 로그인 성공")
        time.sleep(1)

        # 메인페이지 이동 확인
        logger.info(f"TS-003: 현재 URL: {driver.current_url}")
        time.sleep(1)
        assert "http://localhost:4100/" in driver.current_url, "로그인 후 메인페이지로 이동하지 않았습니다."
        logger.info("TS-003: 메인페이지로 정상 이동 확인")
        time.sleep(1)

        # FeedPage 객체 생성
        feed_page = FeedPage(driver)
        logger.info("TS-003: FeedPage 객체 생성")
        time.sleep(1)

        # Your Feed 탭으로 이동
        logger.info("TS-003: Your Feed 탭 클릭 시도")
        time.sleep(1)
        feed_page.click_your_feed()
        logger.info("TS-003: Your Feed 탭 클릭 완료")
        time.sleep(1)

        # Your Feed 첫 번째 게시글 작성자 확인 (언팔로우 대상)
        logger.info("TS-003: Your Feed에서 첫 번째 게시글 작성자 이름 가져오기 시도")
        time.sleep(1)
        author_name = feed_page.get_first_article_author()
        logger.info(f"TS-003: Your Feed 첫 번째 게시글 작성자: {author_name if author_name else '없음'}")
        time.sleep(1)

        # Your Feed에 게시글 없으면 Global Feed에서 사용자 팔로우 (테스트 데이터 확보)
        if not author_name:
            logger.info("TS-003: Your Feed에 게시글이 없어 Global Feed에서 사용자 팔로우 과정 실행")
            time.sleep(1)

            # Global Feed에서 사용자 팔로우 과정 실행
            logger.info("TS-003: Global Feed 탭 클릭 시도 (팔로우 목적)")
            time.sleep(1)

            feed_page.click_global_feed()
            logger.info("TS-003: Global Feed 탭 클릭 완료 (팔로우 목적)")
            time.sleep(1)

            logger.info("TS-003: Global Feed에서 첫 번째 게시글 작성자 이름 가져오기 시도")
            time.sleep(1)

            author_name = feed_page.get_first_article_author()
            assert author_name, "Global Feed에서도 게시글 작성자를 찾을 수 없습니다."
            logger.info(f"TS-003: Global Feed 첫 번째 게시글 작성자: {author_name}")
            time.sleep(1)

            logger.info(f"TS-003: {author_name}의 프로필 클릭 시도 (팔로우 목적)")
            time.sleep(1)

            assert feed_page.click_author_profile(author_name), f"{author_name}의 프로필로 이동하지 못했습니다."
            logger.info(f"TS-003: {author_name}의 프로필 클릭 완료 (팔로우 목적)")
            time.sleep(1)
            
            logger.info("TS-003: 팔로우 버튼 클릭 시도 (팔로우 목적)")
            time.sleep(1)
            assert feed_page.click_follow_button(), "팔로우 버튼 클릭에 실패했습니다."

            logger.info("TS-003: 팔로우 버튼 클릭 완료 (팔로우 목적)")
            time.sleep(1)

            logger.info("TS-003: 메인 페이지로 뒤로 가기 시도 (팔로우 후)")
            time.sleep(1)

            feed_page.go_back_to_main_page()
            logger.info("TS-003: 메인 페이지로 뒤로 가기 완료 (팔로우 후)")
            time.sleep(1)

            logger.info("TS-003: Your Feed 탭 다시 클릭 시도 (팔로우 후)")
            time.sleep(1)

            feed_page.click_your_feed()
            logger.info("TS-003: Your Feed 탭 다시 클릭 완료 (팔로우 후)")
            time.sleep(1)

            logger.info("TS-003: Your Feed에서 첫 번째 게시글 작성자 이름 다시 가져오기 시도")
            time.sleep(1)

            author_name = feed_page.get_first_article_author()
            logger.info(f"TS-003: Your Feed 첫 번째 게시글 작성자 (팔로우 후): {author_name}")
            time.sleep(1)

        assert author_name, "Your Feed에서 게시글 작성자를 찾을 수 없습니다."

        # 언팔로우할 사용자의 프로필 클릭
        logger.info(f"TS-003: {author_name}의 프로필 클릭 시도 (언팔로우 목적)")
        time.sleep(1)
        assert feed_page.click_author_profile(author_name), f"{author_name}의 프로필로 이동하지 못했습니다."

        logger.info(f"TS-003: {author_name}의 프로필 클릭 완료 (언팔로우 목적)")
        time.sleep(1)

        # 언팔로우 버튼 클릭
        logger.info("TS-003: 언팔로우 버튼 클릭 시도")
        time.sleep(1)
        assert feed_page.click_unfollow_button(), "언팔로우 버튼 클릭에 실패했습니다."

        logger.info("TS-003: 언팔로우 버튼 클릭 완료")
        time.sleep(1)

        # 언팔로우 상태 확인 (팔로우 버튼 표시)
        logger.info("TS-003: 팔로우 상태 확인 (팔로우 버튼 표시 여부) 시도")
        time.sleep(1)
        assert not feed_page.is_following(), "언팔로우 버튼이 정상적으로 동작하지 않았습니다."

        logger.info("TS-003: 팔로우 상태 확인 완료 (언팔로우됨)")
        time.sleep(1)

        # 메인 페이지로 이동 (뒤로 가기)
        logger.info("TS-003: 메인 페이지로 뒤로 가기 시도 (언팔로우 후)")
        time.sleep(1)

        feed_page.go_back_to_main_page()
        logger.info("TS-003: 메인 페이지로 뒤로 가기 완료 (언팔로우 후)")
        time.sleep(1)

        # Your Feed로 이동
        logger.info("TS-003: Your Feed 탭 클릭 시도 (언팔로우 후)")
        time.sleep(1)

        feed_page.click_your_feed()
        logger.info("TS-003: Your Feed 탭 클릭 완료 (언팔로우 후)")
        time.sleep(1)

        # Your Feed에서 언팔로우한 사용자 게시글 사라짐 확인
        logger.info(f"TS-003: Your Feed에서 {author_name}의 게시글 사라짐 확인 시도")
        time.sleep(1)
        assert not feed_page.is_author_articles_visible(author_name), f"언팔로우했는데도 {author_name}의 게시글이 Your Feed에 여전히 표시됩니다."

        logger.info(f"TS-003: 언팔로우한 사용자 {author_name}의 게시글이 Your Feed에서 성공적으로 제거되었습니다.")
        time.sleep(1)

        # 테스트 완료 로그
        logger.info("TS-003: 테스트 완료")
        time.sleep(1)
        
    #@pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")  
    def test_ts004_favorite_article_and_verify_in_profile(self, driver: WebDriver):
        """
        TS-004: 게시글 좋아요 및 프로필 연동 확인 테스트
        1. Global Feed에서 게시글에 '좋아요'를 누릅니다.
        2. 내 프로필의 'Favorited Articles' 탭에서 해당 게시글이 표시되는지 확인합니다.
        3. 다시 '좋아요'를 취소하고 'Favorited Articles' 탭에서 게시글이 사라지는지 확인합니다.
        """
        logger.info("TS-004: 테스트 시작 - 게시글 좋아요 및 프로필의 Favorited Articles 확인")
        time.sleep(1)
        
        # 로그인
        utils = Utils(driver)
        logger.info("TS-004: 계정으로 로그인 시도")
        time.sleep(1)

        utils.utils_login(EMAIL, PASSWORD)  # TODO: 실제 로그인 정보 사용
        logger.info("TS-004: 로그인 성공")
        time.sleep(1)
        
        # 메인페이지 이동 확인 (URL)
        logger.info(f"TS-004: 현재 URL: {driver.current_url}")
        time.sleep(1)
        assert "http://localhost:4100/" in driver.current_url, "로그인 후 메인페이지로 이동하지 않았습니다."

        logger.info("TS-004: 메인페이지로 정상 이동 확인")
        time.sleep(1)
        
        # FavoritePage 객체 생성
        favorite_page = FavoritePage(driver)
        logger.info("TS-004: FavoritePage 객체 생성")
        time.sleep(1)
        
        # Global Feed로 이동
        logger.info("TS-004: Global Feed 탭 클릭 시도")
        time.sleep(1)

        favorite_page.click_global_feed()
        logger.info("TS-004: Global Feed 탭 클릭 완료")
        time.sleep(1)
        
        # Global Feed 첫 번째 게시글 제목 가져오기 (테스트 대상)
        logger.info("TS-004: 게시글 제목 목록 가져오기 시도")
        time.sleep(1)
        
        article_titles = favorite_page.get_article_titles()
        assert len(article_titles) > 0, "게시글이 없습니다."
        first_article_title = article_titles[0]
        logger.info(f"TS-004: 테스트할 첫 번째 게시글 제목: {first_article_title}")
        time.sleep(1)
        
        # 첫 번째 게시글의 초기 좋아요 상태 확인
        logger.info("TS-004: 첫 번째 게시글의 초기 좋아요 상태 확인 시도")
        time.sleep(1)
        initial_state = favorite_page.is_article_favorited(0)
        assert initial_state is not None, "게시글의 좋아요 상태를 확인할 수 없습니다."
        
        initial_favorited = initial_state["is_favorited"] # 초기 좋아요 상태
        initial_count = initial_state["count"]
        logger.info(f"TS-004: 초기 상태: 좋아요 {'함' if initial_favorited else '안함'}, 좋아요 수: {initial_count}")
        time.sleep(1)
        
        # 이미 좋아요 상태면 먼저 취소 (테스트 일관성 확보)
        if initial_favorited:
            logger.info("TS-004: 이미 좋아요 상태입니다. 좋아요를 취소한 후 다시 테스트합니다.")
            time.sleep(1)
            favorite_page.click_favorite_button(0)
            logger.info("TS-004: 좋아요 취소 완료")
            time.sleep(1)
            
            # 좋아요 취소 후 상태를 초기 상태로 업데이트
            logger.info("TS-004: 좋아요 취소 후 상태 확인")
            time.sleep(1)
            current_state = favorite_page.is_article_favorited(0)
            initial_favorited = current_state["is_favorited"]
            initial_count = current_state["count"]
            assert not initial_favorited, "좋아요 취소에 실패했습니다."
            logger.info(f"TS-004: 좋아요 취소 후 상태: 좋아요 {'함' if initial_favorited else '안함'}, 좋아요 수: {initial_count}")
            time.sleep(1)
        
        # 좋아요 버튼 클릭
        logger.info("TS-004: 좋아요 버튼 클릭 시도")
        time.sleep(1)
        result = favorite_page.click_favorite_button(0)
        assert result["success"], "좋아요 버튼 클릭에 실패했습니다."
        logger.info("TS-004: 좋아요 버튼 클릭 완료")
        time.sleep(1)
        
        # 좋아요 상태 변경 확인
        logger.info("TS-004: 좋아요 상태 변경 확인 시도")
        time.sleep(1)
        assert result["after_state"]["is_favorited"], "좋아요 상태로 변경되지 않았습니다."
        logger.info(f"TS-004: 좋아요 상태 변경: {result['before_state']['is_favorited']} -> {result['after_state']['is_favorited']}")
        logger.info(f"TS-004: 좋아요 수 변경: {result['before_state']['count']} -> {result['after_state']['count']}")
        time.sleep(1)
        
        # 내 프로필 페이지로 이동
        logger.info("TS-004: 내 프로필 페이지로 이동 시도")
        time.sleep(1)
        assert favorite_page.go_to_my_profile(), "프로필 페이지 이동에 실패했습니다."
        logger.info("TS-004: 내 프로필 페이지로 이동 완료")
        time.sleep(1)
        
        # Favorited Articles 탭 클릭
        logger.info("TS-004: Favorited Articles 탭 클릭 시도")
        time.sleep(1)
        assert favorite_page.click_favorited_articles_tab(), "Favorited Articles 탭 클릭에 실패했습니다."
        logger.info("TS-004: Favorited Articles 탭 클릭 완료")
        time.sleep(1)
        
        # Favorited Articles 목록에서 좋아요한 게시글 확인
        logger.info(f"TS-004: '{first_article_title}' 게시글이 Favorited Articles 목록에 있는지 확인 시도")
        time.sleep(1)
        assert favorite_page.is_article_in_favorited_list(first_article_title), f"'{first_article_title}' 게시글이 Favorited Articles 목록에 표시되지 않습니다."
        logger.info(f"TS-004: '{first_article_title}' 게시글이 Favorited Articles 목록에 성공적으로 표시되었습니다.")
        time.sleep(1)
        
        # Global Feed로 이동 (테스트 원상 복구 준비)
        logger.info("TS-004: 메인 페이지로 이동 후 Global Feed 탭 클릭 시도")
        time.sleep(1)
        driver.get("http://localhost:4100/")
        favorite_page.click_global_feed()
        logger.info("TS-004: 메인 페이지로 이동 후 Global Feed 탭 클릭 완료")
        time.sleep(1)
        
        # Global Feed에서 좋아요 취소 (원상 복구)
        logger.info("TS-004: 좋아요 취소 (원상 복구) 시도")
        time.sleep(1)
        restore_result = favorite_page.click_favorite_button(0)
        assert restore_result["success"], "좋아요 상태 복구에 실패했습니다."
        logger.info("TS-004: 좋아요 취소 (원상 복구) 완료")
        time.sleep(1)
        
        # 좋아요 취소 후 버튼 상태 원복 확인
        logger.info("TS-004: 좋아요 취소 후 상태 확인 시도")
        time.sleep(1)
        final_state = favorite_page.is_article_favorited(0)
        assert final_state is not None, "최종 좋아요 상태를 확인할 수 없습니다."
        assert final_state["is_favorited"] == initial_favorited, "좋아요 상태가 원래대로 복구되지 않았습니다."
        logger.info(f"TS-004: 최종 상태: 좋아요 {'함' if final_state['is_favorited'] else '안함'}, 좋아요 수: {final_state['count']}")
        time.sleep(1)
        
        # 프로필로 이동하여 Favorited Articles 목록 재확인 (좋아요 취소 후)
        logger.info("TS-004: 내 프로필 페이지로 다시 이동 시도")
        time.sleep(1)
        assert favorite_page.go_to_my_profile(), "프로필 페이지 재이동에 실패했습니다."
        logger.info("TS-004: 내 프로필 페이지로 다시 이동 완료")
        time.sleep(1)
        
        # Favorited Articles 탭 클릭
        logger.info("TS-004: Favorited Articles 탭 다시 클릭 시도")
        time.sleep(1)
        assert favorite_page.click_favorited_articles_tab(), "Favorited Articles 탭 재클릭에 실패했습니다."
        logger.info("TS-004: Favorited Articles 탭 다시 클릭 완료")
        time.sleep(1)
        
        # Favorited Articles 목록에서 좋아요 취소한 게시글 사라짐 확인
        logger.info(f"TS-004: '{first_article_title}' 게시글이 Favorited Articles 목록에서 제거되었는지 확인 시도")
        time.sleep(1)
        assert not favorite_page.is_article_in_favorited_list(first_article_title), f"좋아요를 취소했는데도 '{first_article_title}' 게시글이 여전히 Favorited Articles 목록에 표시됩니다."
        logger.info(f"TS-004: 좋아요를 취소한 게시글 '{first_article_title}'이 Favorited Articles 목록에서 성공적으로 제거되었습니다.")
        time.sleep(1)
        
        # 테스트 완료 및 결과 로그
        logger.info("TS-004: 테스트 성공: 게시글의 좋아요 기능이 정상적으로 동작합니다.")
        logger.info("TS-004: 좋아요를 누른 게시글은 프로필의 Favorited Articles 탭에 표시되며, 좋아요를 취소하면 목록에서 제거됩니다.")
        logger.info("TS-004: 테스트 완료")
        time.sleep(1)