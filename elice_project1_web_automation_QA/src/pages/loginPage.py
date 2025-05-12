
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pickle
#from config import EMAIL, PASSWORD
import time

class LoginPage: 
  
  URL = "https://kdt-pt-1-pj-2-team03.elicecoding.com/signin"

  def __init__(self,driver):
    self.driver = driver

  def open(self):
    self.driver.get(self.URL)

  def input_password_and_email(self,email,password):
    login_button = ws(self.driver, 10).until(
      EC.element_to_be_clickable((By.XPATH, "//button[text()='로그인하기']"))
    )
    login_button.click()

            # 로그인 입력 페이지로 이동될 때까지 대기
    ws(self.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))
    )
    input_email = self.driver.find_element(By.XPATH, "//input[@id='username']")
    input_email.send_keys(email)
    input_password = self.driver.find_element(By.XPATH, "//input[@type='password']")
    input_password.send_keys(password)

    login_button = self.driver.find_element(By.XPATH, "//button[text()='계속하기']")
    login_button.click()
  
  def do_login(self,email, password):
    wait = ws(self.driver, 10)
    self.open()

    wait.until(EC.url_contains("signin"))
    assert "signin" in self.driver.current_url  
    time.sleep(2)

    self.input_password_and_email(email, password) 

    wait.until(EC.url_contains("team03"))
    assert "team03" in self.driver.current_url
    time.sleep(2)

  def do_login_get_cookies(self,email, password):
    wait = ws(self.driver, 10)
    self.open()

    wait.until(EC.url_contains("signin"))
    assert "signin" in self.driver.current_url  
    time.sleep(2)

    self.input_password_and_email(email, password) 

    wait.until(EC.url_contains("team03"))
    assert "team03" in self.driver.current_url
    time.sleep(2)

    pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))




