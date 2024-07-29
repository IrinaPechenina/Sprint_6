import pytest
from selenium import webdriver

import data
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.switch_page import SwitchPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.get_url(data.MAIN_PAGE_URL)
    return page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.get_url(data.MAIN_PAGE_URL)
    return page

@pytest.fixture
def switch_page(driver):
    page = SwitchPage(driver)
    return page


