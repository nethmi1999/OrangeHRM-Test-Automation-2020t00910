from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Config import TestConfig

class AuthPage:
    input_user_name = "username"
    input_pass_name = "password"
    submit_btn_xpath = "//button[@type='submit']"

    def __init__(self, browser):
        self.browser = browser
        self.waiter = WebDriverWait(self.browser, TestConfig.TIMEOUT_DURATION)

    def enter_username(self, user_value):
        try:
            time.sleep(2)
            user_field = self.waiter.until(
                EC.visibility_of_element_located((By.NAME, self.input_user_name))
            )
            user_field.clear()
            user_field.send_keys(user_value)
        except Exception as err:
            try:
                user_field = self.waiter.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']"))
                )
                user_field.clear()
                user_field.send_keys(user_value)
            except Exception as err:
                print(f"Failed with alternative selector too: {str(err)}")
                raise

    def enter_password(self, pass_value):
        try:
            time.sleep(2)
            pass_field = self.waiter.until(
                EC.visibility_of_element_located((By.NAME, self.input_pass_name))
            )
            pass_field.clear()
            pass_field.send_keys(pass_value)
        except Exception as err:
            pass_field = self.waiter.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
            )
            pass_field.clear()
            pass_field.send_keys(pass_value)

    def press_login_button(self):
        try:
            time.sleep(2)
            login_btn = self.waiter.until(
                EC.element_to_be_clickable((By.XPATH, self.submit_btn_xpath))
            )
            login_btn.click()
        except Exception as err:
            login_btn = self.waiter.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            login_btn.click()

    def perform_login(self, user_value, pass_value):
        if "login" not in self.browser.current_url:
            self.browser.get(TestConfig.APP_URL)
            time.sleep(2)

        self.enter_username(user_value)
        self.enter_password(pass_value)
        self.press_login_button()
        time.sleep(2)

    def is_login_screen_displayed(self):
        try:
            self.waiter.until(
                EC.visibility_of_element_located((By.NAME, self.input_user_name))
            )
            return True
        except:
            return False
