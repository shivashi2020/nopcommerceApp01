import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome()
        print("Chrome Browser Opend")
    elif browser == "Firefox":
        driver = webdriver.Firefox()
        print("Firefox Browser Opend")
    else:
        driver = webdriver.Edge()
        print("Default Edge Browser Opend")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser") #this will get teh value from CLI

@pytest.fixture()
def browser(request): # This will return the browser value to setup method
    return request.config.getoption("--browser")