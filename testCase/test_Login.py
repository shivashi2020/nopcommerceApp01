import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseurl = Readconfig.getApplicationURL()
    username = Readconfig.getUserEmail()
    password = Readconfig.getUserPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("************************************* Test Case : Test_001_Login  *************************************")
        self.logger.info("************************************* Verify Home Page Test Started  *************************************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(3)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True, "Home Page Title is Matched " + actual_title
            self.driver.close()
            self.logger.info("************************************* Home Page Verification Passed *************************************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.save_screenshot("01sample.png")
            assert False, "Home Page Title is not matching"
            self.driver.close()
            self.logger.error("************************************* Home Page Verification Failed *************************************")

    def test_login(self,setup):
        self.logger.info("************************************* Login Test Started  *************************************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.logger.info("************************************* Username Entered  *************************************")
        self.lp.setPassword(self.password)
        self.logger.info("************************************* Password Entered  *************************************")
        self.lp.clickLogin()
        actual_page_name = self.driver.title

        if actual_page_name =="Dashboard / nopCommerce administration":
            assert True , "Login Success"
            self.driver.close()
            self.logger.info("************************************* Login Page Verification Passed *************************************")
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_homepageTitle.png")
            assert False, "Login Failed"
            self.driver.close()

            self.logger.error("************************************* Login Page Verification Failed *************************************")
