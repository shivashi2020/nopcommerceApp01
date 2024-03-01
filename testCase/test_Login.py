import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseurl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(3)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True, "Home Page Title is Matched " + actual_title
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            assert False, "Home Page Title is not matching"
            self.driver.close()


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_page_name = self.driver.title

        if actual_page_name =="Dashboard / nopCommerce administration":
            assert True , "Login Success"
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            assert False, "Login Failed"
            self.driver.close()

