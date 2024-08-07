'''Алан Бадзиев 2024'''
import pytest
from selenium.webdriver.common.by import By

URL = "https://postcard.qa.studio/"

def test_smoke(browser):
    '''SMK-1. Smoke test'''
    browser.get(URL)

    buttton = browser.find_element(by=By.ID, value="send")
    assert buttton.text == "Отправить", "Unnexpected text on button"

def test_empty_input_send(browser):
    '''SMK-2. Negative case'''
    browser.get(URL)

    email_label = browser.find_element(by=By.CSS_SELECTOR, value="div.email h2")
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == "requered", "Unnexpected attribute class"

    buttton = browser.find_element(by=By.ID, value="send")
    buttton.click()

    email_label = browser.find_element(by=By.CSS_SELECTOR, value="div.email h2")
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == "requered error", "Unnexpected attribute class"

CASE = [
    0, 1
]
@pytest.mark.parametrize("case", CASE)
def test_send_postcard(browser, case):
    '''SMK-3. Positive case'''
    browser.get(URL)

    email = browser.find_element(by=By.ID, value="email")
    email.click()
    email.send_keys("test@test.com")

    cards = browser.find_elements(by=By.CSS_SELECTOR, value='[class*="photo-parent"]')
    cards[case].click()

    message = browser.find_element(by=By.ID, value="textarea")
    message.click()
    message.send_keys("Hello world")

    buttton = browser.find_element(by=By.ID, value="send")
    buttton.click()

    modal = browser.find_element(by=By.ID, value="modal")
    assert modal.text == "Открытка успешно отправлена!", "Unnexpected text on modal"
