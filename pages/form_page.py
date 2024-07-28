
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

    def open(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )

    def set_first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys(first_name)
        time.sleep(2)

    def set_last_name(self, last_name):
        self.driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys(last_name)
        time.sleep(2)

    def set_email(self, email):
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
        time.sleep(2)

    def select_gender(self):
        gender_label = WebDriverWait(self.driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".custom-radio:nth-child(2) > .custom-control-label"))
        )
        gender_label.click()
        time.sleep(2)

    def set_mobile(self, mobile):
        mobile_input = WebDriverWait(self.driver, 1).until(
            EC.presence_of_element_located((By.ID, "userNumber"))
        )
        mobile_input.send_keys(mobile)
        time.sleep(2)

    def set_date_of_birth(self, date):
        date_input = WebDriverWait(self.driver, 1).until(
            EC.element_to_be_clickable((By.ID, "dateOfBirthInput"))
        )
        date_input.click()
        date_input.send_keys(Keys.CONTROL + "a")
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def set_subjects(self, subject):
        # Находим и кликаем на поле Subjects
        subjects_input = WebDriverWait(self.driver, 1).until(
            EC.element_to_be_clickable((By.ID, "subjectsInput"))
        )
        subjects_input.click()

        subjects_input.send_keys(subject)
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div").click()

        time.sleep(1)  # Добавляем паузу для обработки клика

    def upload_picture(self, file_path):
        picture_path = os.path.abspath(file_path)
        picture_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "uploadPicture"))
        )
        picture_input.send_keys(picture_path)
        time.sleep(2)

    def set_address(self, address):
        address_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "currentAddress"))
        )
        address_input.send_keys(address)
        time.sleep(2)

    def select_state(self):
        state_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#state > div > div.css-1hwfws3 > div.css-1wa3eu0-placeholder"))
        )
        state_dropdown.click()
        state_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-select-3-option-1"))
        )
        state_option.click()
        time.sleep(2)

    def select_city(self):
        city_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#city > div > div.css-1hwfws3 > div.css-1wa3eu0-placeholder"))
        )
        city_dropdown.click()
        city_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-select-4-option-1"))
        )
        city_option.click()
        time.sleep(2)

    def submit(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
        submit_button.click()
        time.sleep(2)
