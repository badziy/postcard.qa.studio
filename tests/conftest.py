'''Fixture'''

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    '''Main fixture'''
    chrome__options = Options()
    chrome__options.add_argument("--no-sandbox")
    chrome__options.add_argument("start-maximized")
    chrome__options.add_argument("disable-infobars")
    chrome__options.add_argument("disable-extensions")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome__options)
    yield driver
    driver.quit()