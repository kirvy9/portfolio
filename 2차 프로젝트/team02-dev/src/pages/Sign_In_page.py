from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC



class Sign_In_Page:
    URL = "http://localhost:4100/login"

    def __init__(self,driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

# 주요 기능? 로케이터 정리한것임
    Email_input = (By.CSS_SELECTOR,'input[placeholder="Email"]')
    Password_input = (By.CSS_SELECTOR,'input[placeholder="Password"]')
    Need_an_account_button = (By.CSS_SELECTOR, 'a[href="/register"]')
    Sign_in_button = (By.XPATH, '//button[contains(text(),"Sign")]')

# 상단에 버튼 로케이터 정리한것
    conduit = (By.CSS_SELECTOR, 'a.navbar-brand')
    Home = (By.CSS_SELECTOR, 'a.nav-link[href="/"]')
    Sign_in = (By.CSS_SELECTOR, 'a.nav-link[href="/login"]')
    Sign_up = (By.CSS_SELECTOR, 'a.nav-link[href="/register"]')

# 로그인
    def sign_in(self,email,password):
        wait = WebDriverWait(self.driver,10)
        if email is not None:
            wait.until(EC.visibility_of_element_located(self.Email_input)).send_keys(email)
        if password is not None:
            wait.until(EC.visibility_of_element_located(self.Password_input)).send_keys(password)
        wait.until(EC.element_to_be_clickable(self.Sign_in_button)).click()

        
