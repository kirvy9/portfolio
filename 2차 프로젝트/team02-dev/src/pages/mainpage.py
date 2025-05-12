from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class MainPage:
    URL = "http://localhost:4100/"  # 직접 URL을 설정

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)  # 하드코딩된 URL을 사용

    def go_to_login(self):
        login_btn = self.driver.find_element(By.LINK_TEXT, "Sign in")
        login_btn.click()