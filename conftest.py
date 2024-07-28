# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Запуск в headless режиме
    chrome_options.add_argument('--no-sandbox')  # Отключение sandbox режима
    chrome_options.add_argument('--disable-dev-shm-usage')  # Использование shared memory
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--disable-gpu')  # Отключение GPU, не требуется в headless режиме

    # Используем webdriver_manager для автоматической установки chromedriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(1920, 1080)  # Установка разрешения окна на 1920x1080
    driver.implicitly_wait(10)  # Установка неявного ожидания
    yield driver
    driver.quit()
