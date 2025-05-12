import pytest
import time
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.loginPage import LoginPage
from src.pages.new_review import NewReview 


@pytest.mark.usefixtures("driver")
class TestCaseI:

    def test_case_I_009(self, driver: WebDriver):

        review = NewReview(driver)
        login_page = LoginPage(driver)
        wait = ws(driver, 10)

        try:

            # 테스트용 로그인 로직 실행
            test_email = "testid@test.com"
            test_password = "testpw1!"
            login_page.do_login(test_email, test_password)
            time.sleep(2)


            #개인 피드 접근 
            mypd = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div/ul/li[4]/a")))
            mypd.click()

            time.sleep(2)

            #개인 피드 접근 검증
            current_url = driver.current_url
            expected_url = "https://kdt-pt-1-pj-2-team03.elicecoding.com/my"

            assert current_url == expected_url, f"❌ 예상 URL: {expected_url}, 실제 URL: {current_url}"


            # 검증 전: 초기 후기 리스트 개수 확인
            
            initial_reviews = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'flex w-full gap-6 p-4 shadow-md rounded-2xl')]")))
            initial_review_count = len(initial_reviews)

            print(f"초기 후기 개수: {initial_review_count}")


            #스크롤 다운
            driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(1)


            # 후기 작성 페이지 접근
            review.review_open()
            time.sleep(1)

            # 랜덤 식사 타입 선택 및 반환받기
            selected_type = review.select_meal_type()  # 식사 타입 반환
            time.sleep(1)

            # 사진 업로드
            review.add_image()  
            time.sleep(1)

            # 메뉴 이름 추가
            review.add_menuname()
            time.sleep(1)
            
            # 랜덤 카테고리 선택
            review.select_category()
            time.sleep(1)

            # 후기 내용 작성
            review.add_comment()
            time.sleep(1)

            # 별점 추가 (selected_type을 전달)
            review.add_star(selected_type)  # 선택된 식사 타입에 따라 별점 추가
            time.sleep(1)

            # 후기 작성 완료 버튼 클릭
            review.comment_submit()
            time.sleep(2)


            #스크롤을 끝까지 내려 추가된 후기 리스트 업데이트
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)


            # 후기 추가 후 검증
            updated_reviews = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'flex w-full gap-6 p-4 shadow-md rounded-2xl')]")))
            updated_review_count = len(updated_reviews)

            # 초기 후기 개수와 비교하여 검증
            assert initial_review_count <  updated_review_count, "❌ 새로운 후기가 추가되지 않았습니다."
            print("✅ 새로운 후기가 추가되었습니다. 후기가 성공적으로 등록되었습니다!")
            print("✅ 현재 후기 개수 :", updated_review_count)

        except Exception as e:
            # 실패 시 에러 출력
            print(f"⚠️ 테스트 실패: {e}")
            assert False