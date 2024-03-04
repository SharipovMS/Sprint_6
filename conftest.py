from selenium import webdriver
import pytest

import data
from data import *

@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get(data.Site.scooter)
    yield driver
    driver.quit()
