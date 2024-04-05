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


####### Pytest HTML Report  #########################
#Its the hook for adding Envionment info to HTML Report

'''
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester']='Shivashi'

## It is the hook for delete /modfiy Envionments info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadat):
    metadat.pop("JAVA_HOME", None)
    metadat.pop("Plugins", None) '''