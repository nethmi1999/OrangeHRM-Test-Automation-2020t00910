import os
import pytest
import time
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.Login import AuthPage
from PageObjects.Dashboard import MainPage
from PageObjects.Leave import LeavePage
from Utilities.Logger import LoggerUtil
from Config import TestConfig


@pytest.mark.usefixtures("browser_setup")
class TestHRMSuite:
    log = LoggerUtil.get_logger()
    session_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def mark_success(self, msg):
        self.log.info(f"SUCCESS: {msg} [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")

    def test_01_check_login_title(self):
        self.log.info("Starting test_01_check_login_title")
        self.driver.get(TestConfig.APP_URL)
        time.sleep(TestConfig.DELAY_DURATION)
        page_title = self.driver.title
        required_title = "OrangeHRM"

        if page_title == required_title:
            self.mark_success(f"Login page title is correct: {page_title}")
            assert True
        else:
            self.log.error(f"❌ Incorrect login page title. Expected: {required_title}, Got: {page_title}")
            assert False, f"Expected title: {required_title}, but got: {page_title}"

    def test_02_user_login(self):
        self.log.info("Starting test_02_user_login")
        self.driver.get(TestConfig.APP_URL)
        time.sleep(TestConfig.DELAY_DURATION)

        login = AuthPage(self.driver)
        dashboard = MainPage(self.driver)
        login.perform_login(TestConfig.LOGIN_USER, TestConfig.LOGIN_PASS)

        if dashboard.is_dashboard_loaded():
            self.mark_success("Login successful and dashboard loaded")
            assert True
        else:
            self.log.error("❌ Dashboard not loaded after login")
            assert False, "Dashboard not loaded after login"

    def test_03_leave_check(self):
        self.log.info("Starting test_03_leave_check")
        self.driver.get(TestConfig.APP_URL)

        login = AuthPage(self.driver)
        dashboard = MainPage(self.driver)
        leave = LeavePage(self.driver)

        try:
            if login.is_login_screen_displayed():
                login.perform_login(TestConfig.LOGIN_USER, TestConfig.LOGIN_PASS)
                self.log.info("Logged in for leave check")

            if not dashboard.is_dashboard_loaded():
                self.log.error("❌ Dashboard not loaded in leave check")
                assert False, "Dashboard not loaded"

            leave_nav = WebDriverWait(self.driver, TestConfig.TIMEOUT_DURATION).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']"))
            )
            leave_nav.click()
            self.log.info("Clicked on Leave menu")

            my_leave_option = WebDriverWait(self.driver, TestConfig.TIMEOUT_DURATION).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='My Leave']"))
            )
            my_leave_option.click()
            self.log.info("Clicked on My Leave tab")

            WebDriverWait(self.driver, TestConfig.TIMEOUT_DURATION).until(
                EC.visibility_of_element_located((By.XPATH, "//h5[text()='My Leave List']"))
            )
            self.log.info("My Leave page loaded")

            WebDriverWait(self.driver, TestConfig.TIMEOUT_DURATION).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'oxd-table')]"))
            )
            self.log.info("Leave page fully loaded")

            if leave.is_leave_section_accessible():
                self.mark_success("Leave page loaded and verified")
                assert True
            else:
                self.log.error("❌ Leave page verification failed")
                assert False, "Leave page not verified"

        except TimeoutException as ex:
            self.log.error(f"Timeout in leave check test: {str(ex)}")
            assert False, f"Timeout occurred: {str(ex)}"

        except Exception as ex:
            self.log.error(f"Unexpected error in leave check test: {str(ex)}")
            assert False, f"Unexpected error occurred: {str(ex)}"

    def test_04_user_logout(self):
        self.log.info("Starting test_04_user_logout")
        self.driver.get(TestConfig.APP_URL)

        login = AuthPage(self.driver)
        dashboard = MainPage(self.driver)

        try:
            if login.is_login_screen_displayed():
                login.perform_login(TestConfig.LOGIN_USER, TestConfig.LOGIN_PASS)

            if not dashboard.is_dashboard_loaded():
                self.log.error("Dashboard not loaded before logout")
                assert False, "Dashboard not loaded"

            time.sleep(TestConfig.DELAY_DURATION)
            dashboard.perform_logout()

            WebDriverWait(self.driver, TestConfig.TIMEOUT_DURATION).until(
                EC.visibility_of_element_located((By.NAME, login.input_user_name))
            )

            assert self.driver.find_element(By.NAME, login.input_user_name).is_displayed(), \
                "Login field not displayed after logout"

            self.mark_success("Logout successful and login page displayed")

        except Exception as ex:
            self.log.error(f"Logout test encountered an error: {str(ex)}")
            assert False, f"Logout test failed: {str(ex)}"
