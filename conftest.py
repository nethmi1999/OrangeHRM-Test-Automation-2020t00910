import pytest
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def browser_setup(request):
    chrome_options = Options()
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
