from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Config import TestConfig


class LeavePage:
    def __init__(self, browser):
        self.browser = browser

    def is_leave_section_accessible(self):
        try:
            time.sleep(TestConfig.DELAY_DURATION)
            WebDriverWait(self.browser, TestConfig.TIMEOUT_DURATION).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/leave/viewLeaveModule']"))
            ).click()
            return True
        except:
            return False
