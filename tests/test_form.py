

import pytest
from pages.form_page import FormPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_form_submission(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.set_first_name("Vera")
    form_page.set_last_name("Po")
    form_page.set_email("verapo@example.com")
    form_page.select_gender()
    form_page.set_mobile("1234567890")
    form_page.set_date_of_birth("12 Dec 1986")
    form_page.set_subjects("Math")  # Убираем параметр
    form_page.upload_picture("assets/test_image.png")
    form_page.set_address("123 Main St")
    form_page.select_state()
    form_page.select_city()
    form_page.submit()

    # Явное ожидание появления всплывающего окна
    WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.CLASS_NAME, "modal-header"))
    )

    assert "Thanks for submitting the form" in driver.page_source
