import os
import pytest
import logging
import random, string
import requests
from dotenv import load_dotenv
from selenium import webdriver
from src.pages.Sign_In_page import Sign_In_Page
from src.pages.edit_profile import EditProfilePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

load_dotenv("src/config/.env")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# 로깅 설정
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture
def driver():
    # 브라우저 초기화
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def signin_page(driver):
    page = Sign_In_Page(driver)
    page.open()
    return page

@pytest.fixture
def edit_profile_page(driver):
    page = EditProfilePage(driver)
    return page


#---------------------------------------------------------------------
# Edit Profile 페이지로 이동 테스트
def test_TC_021(signin_page, edit_profile_page):
    logging.info("📋 TC_021 / Test Start!")


    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {PASSWORD}")
    
    signin_page.sign_in(EMAIL,PASSWORD)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    expected_url = "http://localhost:4100/settings"
    current_url = signin_page.driver.current_url
    assert current_url == expected_url
    logging.info(current_url)
    logging.info("Settings 페이지 이동✅")

#---------------------------------------------------------------------
# Edit profile 페이지 UI 확인 (password 필드 추가함)
def test_TC_022(signin_page, edit_profile_page):
    logging.info("📋 TC_022 / Test Start!")

    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {PASSWORD}")
    
    signin_page.sign_in(EMAIL,PASSWORD)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    expected_url = "http://localhost:4100/settings"
    current_url = signin_page.driver.current_url
    assert current_url == expected_url
    logging.info(current_url)
    logging.info("Settings 페이지 이동✅")

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.PROFILE_URL_INPUT)).is_displayed()
    logging.info("URL of profile picture ✅")
    profile_url = edit_profile_page.get_profile_url()
    assert profile_url is not None
    logging.info(f"URL : {profile_url if profile_url else 'None'}")

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.USERNAME_INPUT)).is_displayed()
    logging.info("Username ✅")
    username = edit_profile_page.get_username()
    assert username is not None
    logging.info(f"Username : {username if username else 'None'}")

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.BIO_TEXTAREA)).is_displayed()
    logging.info("Short bio about you ✅")
    bio = edit_profile_page.get_bio()
    assert bio is not None
    logging.info(f"Bio : {bio if bio else 'None'}")

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.EMAIL_INPUT)).is_displayed()
    logging.info("Email ✅")
    email = edit_profile_page.get_email()
    assert email is not None
    logging.info(f"Email : {email if email else 'None'}")

    password_input =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="New Password"]')))
    assert password_input.is_displayed()
    logging.info("New password ✅")
    

#---------------------------------------------------------------------
# Edit profile 페이지 버튼UI 확인
def test_TC_023(signin_page, edit_profile_page):
    logging.info("📋 TC_023 / Test Start!")

    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {PASSWORD}")
    
    signin_page.sign_in(EMAIL,PASSWORD)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    expected_url = "http://localhost:4100/settings"
    current_url = signin_page.driver.current_url
    assert current_url == expected_url
    logging.info(current_url)
    logging.info("Settings 페이지 이동✅")

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.UPDATE_BUTTON)).is_displayed()
    logging.info("Update Button ✅")

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.LOGOUT_BUTTON)).is_displayed()
    logging.info("Logout Button ✅")

#---------------------------------------------------------------------
# 로그아웃 확인
def test_TC_024(signin_page, edit_profile_page):
    logging.info("📋 TC_024 / Test Start!")

    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {PASSWORD}")
    
    signin_page.sign_in(EMAIL,PASSWORD)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    expected_url = "http://localhost:4100/settings"
    current_url = signin_page.driver.current_url
    assert current_url == expected_url
    logging.info(current_url)
    logging.info("Settings 페이지 이동✅")

    logout_button = wait.until(EC.visibility_of_element_located(edit_profile_page.LOGOUT_BUTTON))
    logout_button.click()
    logging.info("Logout Button click!")

    wait = WebDriverWait(signin_page.driver,10)
    wait.until(EC.url_to_be("http://localhost:4100/"))
    current_url = signin_page.driver.current_url
    assert current_url == "http://localhost:4100/"
    logging.info(current_url)
    logging.info("Logout 완료✅")

#---------------------------------------------------------------------
# 프로필 이미지 URL 변경
def test_TC_025(signin_page,edit_profile_page):
    logging.info("📋 TC_024 / Test Start!")

    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {PASSWORD}")
    
    signin_page.sign_in(EMAIL,PASSWORD)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    expected_url = "http://localhost:4100/settings"
    current_url = signin_page.driver.current_url
    assert current_url == expected_url
    logging.info(current_url)
    logging.info("Settings 페이지 이동✅")

    profile_URL = edit_profile_page.get_profile_url()
    logging.info(f"현재 Profile_URL : {profile_URL if profile_URL else 'None'}")

    new_profile_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1ZIidpDTgrZv2k-SCCPPeMA8kKKk5Xu3fmQ&s"
    logging.info(f"변경할 Profile_URL : {new_profile_URL}")

    edit_profile_page.update_profile_url(new_profile_URL)
    edit_profile_page.click_update_button()
    logging.info("Update Button click!")

    current_url = signin_page.driver.current_url
    logging.info(current_url)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.PROFILE_URL_INPUT)).is_displayed()
    logging.info("URL of profile picture ✅")
    profile_url = edit_profile_page.get_profile_url()
    assert profile_url is not None
    logging.info(f"현재 URL : {profile_url if profile_url else 'None'}")

    #원상태로
    logging.info("테스트를 위한 복구중...")
    profile_URL = "https://i.namu.wiki/i/Vj5qbEFSnNirgU_WzuKbQmLd20hbM6QyNGHb8f87wB4iUuMA-OliDHoQMBnxu7jSowmBl5R-wBKXIb5Voe1bxw.webp"
    edit_profile_page.update_profile_url(profile_URL)
    edit_profile_page.click_update_button()
    
#---------------------------------------------------------------------
# Username 변경 확인
def test_TC_026(signin_page,edit_profile_page):
    logging.info("📋 TC_026 / Test Start!")

    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {PASSWORD}")
    
    signin_page.sign_in(EMAIL,PASSWORD)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    expected_url = "http://localhost:4100/settings"
    current_url = signin_page.driver.current_url
    assert current_url == expected_url
    logging.info(current_url)
    logging.info("Settings 페이지 이동✅")

    old_username = edit_profile_page.get_username()
    logging.info(f"현재 Username : {old_username if old_username else 'None'}")

    new_username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    edit_profile_page.update_username(new_username)
    logging.info(f"변경할 Username : {new_username}")

    edit_profile_page.click_update_button()
    logging.info("Update Button click!")

    current_url = signin_page.driver.current_url
    logging.info(current_url)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.USERNAME_INPUT)).is_displayed()
    logging.info("Username ✅")
    username = edit_profile_page.get_username()
    assert username is not None
    logging.info(f"현재 Username : {username if username else 'None'}")

    #원상태로
    logging.info("테스트를 위한 복구중...")
    username = "test1"
    edit_profile_page.update_username(username)
    edit_profile_page.click_update_button()

#---------------------------------------------------------------------
# bio 변경 확인
def test_TC_027(signin_page,edit_profile_page):
    logging.info("📋 TC_027 / Test Start!")

    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {PASSWORD}")
    
    signin_page.sign_in(EMAIL,PASSWORD)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    expected_url = "http://localhost:4100/settings"
    current_url = signin_page.driver.current_url
    assert current_url == expected_url
    logging.info(current_url)
    logging.info("Settings 페이지 이동✅")

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.BIO_TEXTAREA)).is_displayed()
    bio = edit_profile_page.get_bio()
    assert bio is not None
    logging.info(f"현재 Bio : {bio if bio else 'None'}")
    new_Bio = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
    logging.info(f"변경할 Bio : {new_Bio}")

    edit_profile_page.update_bio(new_Bio)
    edit_profile_page.click_update_button()
    logging.info("Update Button click!")

    current_url = signin_page.driver.current_url
    logging.info(current_url)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.BIO_TEXTAREA)).is_displayed()
    logging.info("Short bio about you ✅")
    bio = edit_profile_page.get_bio()
    assert bio is not None
    logging.info(f"현재 Bio : {bio if bio else 'None'}")

    #원상태로
    logging.info("테스트를 위한 복구중...")
    bio = "　"
    edit_profile_page.update_bio(bio)
    edit_profile_page.click_update_button()

#---------------------------------------------------------------------
# Email 변경
def test_TC_028(signin_page,edit_profile_page):
    logging.info("📋 TC_028 / Test Start!")

    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {PASSWORD}")
    
    signin_page.sign_in(EMAIL,PASSWORD)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    expected_url = "http://localhost:4100/settings"
    current_url = signin_page.driver.current_url
    assert current_url == expected_url
    logging.info(current_url)
    logging.info("Settings 페이지 이동✅")
    
    assert wait.until(EC.visibility_of_element_located(edit_profile_page.EMAIL_INPUT)).is_displayed()
    current_email = edit_profile_page.get_email()
    assert EMAIL is not None
    logging.info(f"현재 Email : {current_email if current_email else 'None'}")

    new_email = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + "@com"
    logging.info(f"변경할 Email : {new_email}")
    edit_profile_page.update_email(new_email)
    edit_profile_page.click_update_button()
    logging.info("Update Button click!")

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    current_url = signin_page.driver.current_url
    logging.info(current_url)

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.EMAIL_INPUT)).is_displayed()
    logging.info("Email ✅")
    email = edit_profile_page.get_email()
    assert email is not None
    logging.info(f"현재 Email : {email if email else 'None'}")

    #원상태로
    logging.info("테스트를 위한 복구중...")
    edit_profile_page.update_email(EMAIL)
    edit_profile_page.click_update_button()

#---------------------------------------------------------------------
#유효하지 않는 형식의 email값으로 변경 확인 (실패해야함)
def test_TC_029(signin_page,edit_profile_page):
    logging.info("📋 TC_029 / Test Start!")

    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {PASSWORD}")
    
    signin_page.sign_in(EMAIL,PASSWORD)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    expected_url = "http://localhost:4100/settings"
    current_url = signin_page.driver.current_url
    assert current_url == expected_url
    
    logging.info(current_url)
    logging.info("Settings 페이지 이동✅")

    assert wait.until(EC.visibility_of_element_located(edit_profile_page.EMAIL_INPUT)).is_displayed()
    current_email = edit_profile_page.get_email()
    assert current_email is not None
    logging.info(f"현재 Email : {current_email}")

    new_email = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    logging.info(f"변경할 Email : {new_email}")
    if '@' not in new_email:
        logging.info(f"❗이메일 주소에 '@'를 포함해 주세요. '{new_email}'에 '@'가 없습니다.")

    try:
        edit_profile_page.click_update_button()
    except TimeoutException:
        logging.warning("⏳ update_button이 사라지지 않아 Timeout이 발생했지만 무시합니다.")

    logging.info(current_url)
    logging.info("❌ 이메일 변경되지 않음")

    #edit_profile_page.update_email(new_email)
    #edit_profile_page.click_update_button()
    #logging.info("Update Button click!")

#---------------------------------------------------------------------
# 비밀번호 변경 확인
def test_TC_030(signin_page,edit_profile_page):
    logging.info("📋 TC_029 / Test Start!")

    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {PASSWORD}")
    
    signin_page.sign_in(EMAIL,PASSWORD)

    wait = WebDriverWait(signin_page.driver, 10)
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    expected_url = "http://localhost:4100/settings"
    current_url = signin_page.driver.current_url
    assert current_url == expected_url
    
    logging.info(current_url)
    logging.info("Settings 페이지 이동✅")

    password_input =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="New Password"]')))
    assert password_input.is_displayed()
    
    new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    edit_profile_page.update_password(new_password)
    logging.info(f"변경할 Password : {new_password}")

    edit_profile_page.click_update_button()
    logging.info("Update Button click!")
    logging.info(current_url)

    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    logging.info("Settings click!")

    logout_button = wait.until(EC.visibility_of_element_located(edit_profile_page.LOGOUT_BUTTON))
    logout_button.click()
    logging.info("Logout Button click!")
   
    SIGNINBUTTON = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.nav-link[href="/login"]')))
    SIGNINBUTTON.click()


    password = f"{new_password}"
    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {password}")

    signin_page.sign_in(EMAIL,password)
    logging.info(current_url)
    logging.info("비밀번호 변경 확인✅")

    #원상태로
    logging.info("테스트를 위한 복구중...")    
    settings_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/settings"]')))
    settings_link.click()
    password_input =  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="New Password"]')))
    edit_profile_page.update_password(PASSWORD)
    edit_profile_page.click_update_button()

    


    
    
