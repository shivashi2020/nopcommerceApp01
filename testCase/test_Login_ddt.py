import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities import XLUtils
#screenshotPath = ".\\Screenshots\\"

class Test_002_DDT_Login:
    path = ".//TestData/Login.xlsx"
    baseurl = Readconfig.getApplicationURL()
    screenshotPath = Readconfig.getscreenshotPath()
    logger = LogGen.loggen()


    def test_login_ddt(self,setup):
        self.logger.info("************************************* Test 002 DDT Started  *************************************")
        self.logger.info("************************************* Verifying Login DDT  *************************************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        time.sleep(3)
        self.lp = LoginPage(self.driver)

        self.totalrows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows in XL file " , self.totalrows)

        list_Status = [] # Empty list Variabls

        for rows in range(2, self.totalrows+1):
            self.username = XLUtils.readData(self.path,"Sheet1",rows,1)
            self.pwd = XLUtils.readData(self.path,"Sheet1",rows,2)
            self.expected = XLUtils.readData(self.path,"Sheet1",rows,3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.pwd)
            self.lp.clickLogin()
            time.sleep(5)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.expected == "Pass":
                    self.logger.info("************************************* Test Case Passed  *************************************")
                    self.lp.clickLogout()
                    list_Status.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info("************************************* Test Case Failed  *************************************")
                    self.lp.clickLogout()
                    list_Status.append("Fail")
            elif actual_title != expected_title:
                if self.expected == "Pass":
                    self.logger.info("************************************* Test Case Failed  *************************************")
                    list_Status.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info("************************************* Test Case Passed  *************************************")
                    list_Status.append("Pass")

        if "Fail" not in list_Status:
            self.logger.info("************************************* Login DDT Tests are Passed  *************************************")
            self.driver.close()
            assert True
        else:
            self.logger.info("************************************* Login DDT Tests are Failed  *************************************")
            self.driver.close()
            assert False

        self.logger.info("************************************* End of Login DDT Test  *************************************")
        self.logger.info("************************************* Completed Test_002_DDT_Login  *************************************")

