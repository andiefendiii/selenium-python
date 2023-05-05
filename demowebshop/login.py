import unittest
import time
import baseLogin
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from locator import elem
from data import input

class Login(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_loginSuccess(self):
        driver = self.driver
        baseLogin.testLogin(driver, input.valid_email, input.valid_pwd)
        data = driver.find_element(By.CLASS_NAME, elem.tab_logout).text
        self.assertEqual(data, input.verify_tabLogout)
        

    def test_loginFailedEmail(self):
        driver = self.driver
        baseLogin.testLogin(driver, input.invallid_email, input.valid_pwd)
        data = driver.find_element(By.XPATH, elem.error_msg_login).text
        self.assertEqual(data, input.verify_failedLogin)
       

    def test_loginFailedPassword(self):
        driver = self.driver
        baseLogin.testLogin(driver, input.valid_email, input.invalid_pwd)
        data = driver.find_element(By.XPATH, elem.error_msg_login).text
        self.assertEqual(data, input.verify_failedLogin)
        
        

        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()