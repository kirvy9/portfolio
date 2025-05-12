from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC



class Sign_Up_page:
    URL = "http://localhost:4100/register"

    def __init__(self,driver: WebDriver):
        self.driver = driver
        self.sign_up_url = "http://localhost:4100/register"
    def open(self):
        self.driver.get(self.URL)

# 주요 기능? 로케이터 정리한것임
    Username_input = (By.CSS_SELECTOR,'input[placeholder="Username"]')
    Email_input = (By.CSS_SELECTOR,'input[placeholder="Email"]')
    Password_input = (By.CSS_SELECTOR,'input[placeholder="Password"]')
    Have_an_account_button = (By.CSS_SELECTOR, 'a[href="/login"]')
    Sign_up_button = (By.XPATH, '//button[contains(text(),"Sign")]')

# 상단에 버튼 로케이터 정리한것
    conduit = (By.CSS_SELECTOR, 'a.navbar-brand')
    Home = (By.CSS_SELECTOR, 'a.nav-link[href="/"]')
    Sign_in = (By.CSS_SELECTOR, 'a.nav-link[href="/login"]')
    Sign_up = (By.CSS_SELECTOR, 'a.nav-link[href="/register"]')

# 회원가입
    def sign_up(self,username,email,password):
        wait = WebDriverWait(self.driver,10)

        if email is not None:
            wait.until(EC.presence_of_element_located(self.Username_input)).send_keys(username)
        if email is not None:
            wait.until(EC.presence_of_element_located(self.Email_input)).send_keys(email)
        if password is not None:
            wait.until(EC.presence_of_element_located(self.Password_input)).send_keys(password)
        self.driver.find_element(*self.Sign_up_button).click()

        
