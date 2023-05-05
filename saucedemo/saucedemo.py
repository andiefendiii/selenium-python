import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_loginSuccess(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        url = driver.current_url
        self.assertEqual(url, "https://www.saucedemo.com/inventory.html")
        # time.sleep(10)
        
    def test_loginFailedName(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_use")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        data = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertEqual(data, "Epic sadface: Username and password do not match any user in this service")
        

    def test_loginFailedPassword(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauc")
        driver.find_element(By.ID, "login-button").click()
        data = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        self.assertIn(data, "Epic sadface: Username and password do not match any user in this service")     


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()