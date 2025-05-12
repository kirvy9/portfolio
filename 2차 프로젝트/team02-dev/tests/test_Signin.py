import os
import pytest
import logging
import requests
import random, string
from selenium import webdriver
from src.pages.mainpage import MainPage
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from src.pages.Sign_In_page import Sign_In_Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv("src/config/.env")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_email():
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=6))
    return f"{user}@{domain}.com"

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

@pytest.fixture
def driver():
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
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page
#---------------------------------------------------------------------
# 로그인 페이지 진입
def test_TC_012(main_page):
    logging.info("📋 TC_012 / Test Start!")
    wait = WebDriverWait(main_page.driver, 10)

    assert main_page.driver.current_url == main_page.URL
    logging.info(main_page.driver.current_url)

    signin_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.nav-link[href="/login"]')))
    signin_button.click()
    logging.info("Sign in Button click!")

    expected_signin_url = "http://localhost:4100/login"
    current_url = main_page.driver.current_url
    assert current_url == expected_signin_url
    logging.info(current_url)

#---------------------------------------------------------------------
# 로그인 페이지 입력란 UI 확인
def test_TC_013(signin_page):
    logging.info("📋 TC_013 / Test Start!")

    wait = WebDriverWait(signin_page.driver, 10)

    assert wait.until(EC.visibility_of_element_located(signin_page.Email_input)).is_displayed()
    logging.info("Email input Box✅")
    assert wait.until(EC.visibility_of_element_located(signin_page.Password_input)).is_displayed()
    logging.info("Password input Box✅")
    
#---------------------------------------------------------------------
# 버튼 UI 확인
def test_TC_014(signin_page):
    logging.info("📋 TC_014 / Test Start!")

    wait = WebDriverWait(signin_page.driver, 10)

    assert wait.until(EC.element_to_be_clickable(signin_page.Need_an_account_button)).is_displayed()
    logging.info("Need_an_account Link✅")
    assert wait.until(EC.element_to_be_clickable(signin_page.Sign_in_button)).is_displayed()
    logging.info("Sign in Button✅")
    assert wait.until(EC.element_to_be_clickable(signin_page.conduit)).is_displayed()
    logging.info("Conduit Link✅")
    assert wait.until(EC.element_to_be_clickable(signin_page.Home)).is_displayed()
    logging.info("Home Link✅")
    assert wait.until(EC.element_to_be_clickable(signin_page.Sign_in)).is_displayed()
    logging.info("Sign in Link✅")
    assert wait.until(EC.element_to_be_clickable(signin_page.Sign_up)).is_displayed()
    logging.info("Sign up Link✅")

#---------------------------------------------------------------------
# Need_an_account 버튼 클릭 확인
def test_TC_015(signin_page):
    logging.info("📋 TC_015 / Test Start!")

    wait = WebDriverWait(signin_page.driver,10)
    wait.until(EC.element_to_be_clickable(signin_page.Need_an_account_button)).click()
    logging.info("Need an account Link click!")

    expected_url = "http://localhost:4100/register"
    wait.until(EC.url_to_be(expected_url))
    assert signin_page.driver.current_url == expected_url
    logging.info(signin_page.driver.current_url)
    logging.info("회원가입 페이지 이동✅")

#---------------------------------------------------------------------
# email 미입력시 로그인
def test_TC_016(signin_page):
    logging.info("📋 TC_016 / Test Start!")
    
    wait = WebDriverWait(signin_page.driver,10)

    email = ''
    password = generate_random_password()
    logging.info(f"Email: {email}")
    logging.info(f"Password: {password}")

    signin_page.sign_in(email,password)

    wait.until(EC.url_to_be(signin_page.URL))
    assert signin_page.driver.current_url == signin_page.URL
    logging.info(signin_page.URL)
    logging.info("Email 미입력❌ ")
    logging.info("로그인 실패✅")

#---------------------------------------------------------------------
# 유효하지 않는 email 입력시 로그인
def test_TC_017(signin_page):
    logging.info("📋 TC_017 / Test Start!")

    wait = WebDriverWait(signin_page.driver,10)

    email = generate_random_email()
    password = generate_random_password()
    logging.info(f"Email: {email}")
    logging.info(f"Password: {password}")

    signin_page.sign_in(email,password)

    wait.until(EC.url_to_be(signin_page.URL))
    assert signin_page.driver.current_url == signin_page.URL
    logging.info(signin_page.URL)
    logging.info("유효하지 않는 Email 입력❌ ")
    logging.info("로그인 실패✅")

#---------------------------------------------------------------------
# password 미입력시 로그인
def test_TC_018(signin_page):
    logging.info("📋 TC_018 / Test Start!")

    wait = WebDriverWait(signin_page.driver,10)

    email = generate_random_email()
    password = ''
    logging.info(f"Email: {email}")
    logging.info(f"Password: {password}")

    signin_page.sign_in(email,password)

    wait.until(EC.url_to_be(signin_page.URL))
    assert signin_page.driver.current_url == signin_page.URL
    logging.info(signin_page.URL)
    logging.info("Password 미입력❌ ")
    logging.info("로그인 실패✅")

#---------------------------------------------------------------------
# 유효하지 않는 password 입력시 로그인
def test_TC_019(signin_page):
    logging.info("📋 TC_019 / Test Start!")
    wait = WebDriverWait(signin_page.driver,10)

    
    password = generate_random_password()
    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {password}")

    signin_page.sign_in(EMAIL,password)

    wait.until(EC.url_to_be(signin_page.URL))
    assert signin_page.driver.current_url == signin_page.URL
    logging.info(signin_page.URL)
    logging.info("유효하지 않는 Password 입력❌ ")
    logging.info("로그인 실패✅")

#---------------------------------------------------------------------
# 유효한 값으로 로그인 시도
def test_TC_020(signin_page):
    logging.info("📋 TC_020 / Test Start!")
    wait = WebDriverWait(signin_page.driver,10)

    logging.info(f"Email: {EMAIL}")
    logging.info(f"Password: {PASSWORD}")

    api_url = "http://localhost:3000/api/users/login"
    payload ={
        "user":{
            "email": EMAIL,
            "password": PASSWORD
        }
    }
    response = requests.post(api_url, json=payload)

    assert response.status_code == 200
    token = response.json()["user"]["token"]
    logging.info(f"Token: {token}")

    signin_page.sign_in(EMAIL,PASSWORD)
    expected_url = "http://localhost:4100/"
    wait.until(EC.url_to_be(expected_url))
    current_url = signin_page.driver.current_url
  
    assert current_url == expected_url
    logging.info(current_url)
    logging.info("로그인 성공✅")

#---------------------------------------------------------------------
    
  
