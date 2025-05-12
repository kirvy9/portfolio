import pytest
import random, string
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.pages.Sign_Up_page import Sign_Up_page
from src.pages.mainpage import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def generate_random_email():
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    domain = ''.join(random.choices(string.ascii_lowercase, k=4))
    return f"{user}@{domain}.com"

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def generate_special_username():
    base = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    special = ''.join(random.choices("~!@#$%^&*()_+", k=1))
    username = ''.join(random.sample(base + special, len(base + special)))
    return username

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def signup_page(driver):
    page = Sign_Up_page(driver)
    page.open()
    return page
    
@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page

#---------------------------------------------------------------------
# 회원가입 페이지 진입
def test_TC_001(main_page):
    logging.info("📋 TC_001 / Test Start!")
    wait = WebDriverWait(main_page.driver, 10)

    assert main_page.driver.current_url == main_page.URL
    logging.info(main_page.driver.current_url)

    signup_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.nav-link[href="/register"]')))
    signup_button.click()
    logging.info("Sign up Button click!")

    expected_signup_url = "http://localhost:4100/register"
    current_url = main_page.driver.current_url
    assert current_url == expected_signup_url
    logging.info(current_url)

#---------------------------------------------------------------------
# 입력란 UI 확인
def test_TC_002(signup_page):
    logging.info("📋 TC_002 / Test Start!")
    wait = WebDriverWait(signup_page.driver,10)

    assert wait.until(EC.visibility_of_element_located(signup_page.Username_input)).is_displayed()
    logging.info("Username input Box ✅")
    assert wait.until(EC.visibility_of_element_located(signup_page.Email_input)).is_displayed()
    logging.info("Email input Box ✅")
    assert wait.until(EC.visibility_of_element_located(signup_page.Password_input)).is_displayed()
    logging.info("Password input Box ✅")

#---------------------------------------------------------------------
# 버튼 UI 확인
def test_TC_003(signup_page):
    logging.info("📋 TC_003 / Test Start!")
    wait = WebDriverWait(signup_page.driver,10)

    assert wait.until(EC.element_to_be_clickable(signup_page.Sign_up_button)).is_displayed()
    logging.info("Sign up Button ✅")
    assert wait.until(EC.element_to_be_clickable(signup_page.Have_an_account_button)).is_displayed()
    logging.info("Have an account Link ✅")
    assert wait.until(EC.element_to_be_clickable(signup_page.conduit)).is_displayed()
    logging.info("Conduit Link ✅")
    assert wait.until(EC.element_to_be_clickable(signup_page.Home)).is_displayed()
    logging.info("Home Link ✅")
    assert wait.until(EC.element_to_be_clickable(signup_page.Sign_in)).is_displayed()
    logging.info("sign in Link ✅")
    assert wait.until(EC.element_to_be_clickable(signup_page.Sign_up)).is_displayed()
    logging.info("Sign up Link ✅")


#---------------------------------------------------------------------
# 회원가입 확인
def test_TC_004(signup_page):
    logging.info("📋 TC_004 / Test Start!")

    username = generate_random_username()
    email = generate_random_email()
    password = generate_random_password()
    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: ********")
    signup_page.sign_up(username,email,password)
    
    wait = WebDriverWait(signup_page.driver,10)
    expected_url = "http://localhost:4100"
    wait.until(EC.url_changes(expected_url))  
    assert signup_page.driver.current_url != expected_url
    logging.info(expected_url)
    logging.info("회원가입 완료! ✅")


#---------------------------------------------------------------------
# username 미 입력 확인
def test_TC_005(signup_page):
    logging.info("📋 TC_005 / Test Start!")

    email = generate_random_email()
    password = generate_random_password()
    username = ""

    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: ********")
    signup_page.sign_up(username,email,password)
    
    
    assert signup_page.driver.current_url == signup_page.sign_up_url
    logging.info(signup_page.driver.current_url)
    logging.info("Username 미입력❌ ")
    logging.info("회원가입 실패 ✅")
#---------------------------------------------------------------------
# Username에 특수문자 포함
def test_TC_006(signup_page):
    logging.info("📋 TC_006 / Test Start!")

    email = generate_random_email()
    password = generate_random_password()
    username = generate_special_username()

    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: ********")

    logging.info("Username에 특수문자 포함됨❌")
    signup_page.sign_up(username, email, password)

    assert signup_page.driver.current_url == signup_page.sign_up_url,"회원가입 성공✅ : ❌버그발견!!!"
    logging.info(signup_page.driver.current_url)
    logging.info("회원가입 실패 ✅")

#---------------------------------------------------------------------
# email 미 입력 확인
def test_TC_007(signup_page):
    logging.info("📋 TC_007 / Test Start!")

    email = "" 
    password = generate_random_password()
    username = generate_random_username()

    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: ********")
    signup_page.sign_up(username,email,password)

    assert signup_page.driver.current_url == signup_page.sign_up_url
    logging.info(signup_page.driver.current_url)
    logging.info("Email 미입력❌ ")
    logging.info("회원가입 실패 ✅")
   
#---------------------------------------------------------------------
# 잘못된 email 형식 확인
def test_TC_008(signup_page):
    logging.info("📋 TC_008 / Test Start!")

    email = generate_random_username()
    password = generate_random_password()
    username = generate_random_username()

    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: ********")
    signup_page.sign_up(username,email,password)

    assert signup_page.driver.current_url == signup_page.sign_up_url
    logging.info(signup_page.driver.current_url)
    logging.info("Email 형식 오류❌ ")
    logging.info("회원가입 실패 ✅")

#---------------------------------------------------------------------
# password 미 입력 확인
def test_TC_009(signup_page):
    logging.info("📋 TC_009 / Test Start!")

    email = generate_random_email()
    password = ""
    username = generate_random_username()

    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: ")
    signup_page.sign_up(username,email,password)

    assert signup_page.driver.current_url == signup_page.sign_up_url
    logging.info(signup_page.driver.current_url)
    logging.info("Password 미입력❌ ")
    logging.info("회원가입 실패 ✅")

#---------------------------------------------------------------------    
# username, email, password 미 입력 확인
def test_TC_010(signup_page):
    logging.info("📋 TC_010 / Test Start!")
    email = ""
    password = ""
    username = ""

    logging.info(f"Username: {username}")
    logging.info(f"Email: {email}")
    logging.info(f"Password: {password}")
    signup_page.sign_up(username,email,password)

    assert signup_page.driver.current_url == signup_page.sign_up_url
    logging.info(signup_page.driver.current_url)
    logging.info("Email 미입력❌ ")
    logging.info("Password 미입력❌ ")
    logging.info("Username 미입력❌ ")
    logging.info("회원가입 실패✅")

#---------------------------------------------------------------------    
# Have an account 버튼 클릭 확인
def test_TC_011(signup_page):
    logging.info("📋 TC_011 / Test Start!")

    wait = WebDriverWait(signup_page.driver,10)
    wait.until(EC.element_to_be_clickable(signup_page.Have_an_account_button)).click()
    logging.info("Have an account Button click!✅")

    expected_url = "http://localhost:4100/login"
    wait.until(EC.url_to_be(expected_url))
    assert signup_page.driver.current_url == expected_url
    logging.info(signup_page.driver.current_url)
    logging.info("로그인 페이지 이동 완료✅")

