from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Config import TestConfig

class MainPage:
    header_xpath = "//h6[text()='Dashboard']"
    profile_menu_xpath = "//li[@class='oxd-userdropdown']//span[contains(@class, 'oxd-userdropdown-tab')]"
    sign_out_xpath = "//a[text()='Logout']"
    leave_nav_xpath = "//span[text()='Leave']/ancestor::a"
    personal_leave_tab_xpath = "//a[contains(@class,'oxd-topbar-body-nav-tab-link') and text()='My Leave']"
    leave_list_header_xpath = "//h5[text()='My Leave List']"

    def __init__(self, browser):
        self.browser = browser
        self.wait_driver = WebDriverWait(self.browser, TestConfig.TIMEOUT_DURATION)

    def is_dashboard_loaded(self):
        try:
            self.wait_driver.until(EC.visibility_of_element_located((By.XPATH, self.header_xpath)))
            return True
        except TimeoutException:
            return False

    def open_my_leave_tab(self):
        try:
            leave_tab = self.wait_driver.until(
                EC.element_to_be_clickable((By.XPATH, self.personal_leave_tab_xpath))
            )
            leave_tab.click()
        except TimeoutException:
            print("My Leave tab not clickable or not found.")
        except Exception as err:
            print(f"Error while clicking 'My Leave': {str(err)}")

    def perform_logout(self):
        try:
            menu_button = self.wait_driver.until(
                EC.element_to_be_clickable((By.XPATH, self.profile_menu_xpath))
            )
            menu_button.click()
            self.wait_driver.until(
                EC.visibility_of_element_located((By.XPATH, "//ul[@class='oxd-dropdown-menu']"))
            )
            logout_button = self.wait_driver.until(
                EC.element_to_be_clickable((By.XPATH, self.sign_out_xpath))
            )
            logout_button.click()
            self.wait_driver.until(EC.url_contains("auth/login"))

        except Exception as err:
            print(f"Error during logout: {str(err)}")
            raise
