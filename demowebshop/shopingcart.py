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
        
        
    def test_shoppingCart(self):
        driver = self.driver
        baseLogin.testLogin(driver, input.valid_email, input.valid_pwd)
        driver.find_element(By.XPATH, elem.tab_book).click()
        driver.find_element(By.XPATH, elem.book_card).click()
        driver.find_element(By.ID, elem.addtocart_btn).click()
        time.sleep(3)
        data = driver.find_element(By.CLASS_NAME, elem.tab_logout).text
        self.assertEqual(data, input.verify_tabLogout)










        # driver.maximize_window()
        # time.sleep(3)
        # driver.find_element(By.XPATH, elem.cart_product).click()
        # time.sleep(5)
        # # driver.find_element(By.ID, elem.recipient_name).send_keys(input.firstname_data)
        # # driver.find_element(By.ID, elem.recipient_email).send_keys(input.valid_email)
        # # time.sleep(3)
        # driver.find_element(By.ID, elem.addtocard_btn).click()
        # time.sleep(5)
        # driver.find_element(By.XPATH, elem.tab_shoppingcart).click()
        # time.sleep(3)
        # driver.find_element(By.ID, elem.cb_agree_shopcart).click()
        # time.sleep(3)
        # driver.find_element(By.ID, elem.checkout_btn).click()
        # time.sleep(3)
        # data = driver.find_element(By.XPATH, elem.checkout_title).text
        # self.assertEqual(data, input.verify_checkout)
        
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()