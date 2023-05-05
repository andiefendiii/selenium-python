import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from locator import elem
from data import input

class Register(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # def test_registerSuccess(self):
    #     driver = self.driver
    #     driver.get("https://demowebshop.tricentis.com/")
    #     driver.find_element(By.CLASS_NAME, "ico-register").click()
    #     driver.find_element(By.ID, "gender-male").click()
    #     driver.find_element(By.ID, "FirstName").send_keys("Andi")
    #     driver.find_element(By.ID, "LastName").send_keys("Efendi")
    #     driver.find_element(By.ID, "Email").send_keys("andiefendi@yopmail.com")
    #     driver.find_element(By.ID, "Password").send_keys("Andi123")
    #     driver.find_element(By.ID, "ConfirmPassword").send_keys("Andi123")
    #     driver.find_element(By.ID, "register-button").click()
    #     url = driver.current_url
    #     self.assertEqual(url, "https://demowebshop.tricentis.com/registerresult/1")
        # time.sleep(5)


    def test_registerFailed_existingEmail(self):
        driver = self.driver
        driver.get(input.baseUrl)
        driver.find_element(By.CLASS_NAME, elem.tab_regist).click()
        driver.find_element(By.ID, elem.rb_male).click()
        driver.find_element(By.ID, elem.firstname).send_keys(input.firstname_data)
        driver.find_element(By.ID, elem.lastname).send_keys(input.lastname_data)
        driver.find_element(By.ID, elem.email_regist).send_keys(input.valid_email)
        driver.find_element(By.ID, elem.pwd_regist).send_keys(input.valid_pwd)
        driver.find_element(By.ID, elem.confirm_pwd_regist).send_keys(input.valid_pwd)
        driver.find_element(By.ID, elem.regist_btn).click()
        data = driver.find_element(By.XPATH, elem.error_msg_existingemail).text
       


    def test_registerFailed_emptyFirstName(self):
        driver = self.driver
        driver.get(input.baseUrl)
        driver.find_element(By.CLASS_NAME, elem.tab_regist).click()
        driver.find_element(By.ID, elem.rb_male).click()
        driver.find_element(By.ID, elem.firstname).send_keys()
        driver.find_element(By.ID, elem.lastname).send_keys(input.lastname_data)
        driver.find_element(By.ID, elem.email_regist).send_keys(input.valid_email)
        driver.find_element(By.ID, elem.pwd_regist).send_keys(input.valid_pwd)
        driver.find_element(By.ID, elem.confirm_pwd_regist).send_keys(input.valid_pwd)
        driver.find_element(By.ID, elem.regist_btn).click()
        data = driver.find_element(By.XPATH, elem.error_msg_emptyfirstname).text
        self.assertEqual(data, input.verify_emptyfirstname)
              
   
    def test_registerFailed_emptyLasttName(self):
        driver = self.driver
        driver.get(input.baseUrl)
        driver.find_element(By.CLASS_NAME, elem.tab_regist).click()
        driver.find_element(By.ID, elem.rb_male).click()
        driver.find_element(By.ID, elem.firstname).send_keys(input.firstname_data)
        driver.find_element(By.ID, elem.lastname).send_keys()
        driver.find_element(By.ID, elem.email_regist).send_keys(input.valid_email)
        driver.find_element(By.ID, elem.pwd_regist).send_keys(input.valid_pwd)
        driver.find_element(By.ID, elem.confirm_pwd_regist).send_keys(input.valid_pwd)
        driver.find_element(By.ID, elem.regist_btn).click()
        data = driver.find_element(By.XPATH, elem.error_msg_emptylasttname).text
        self.assertEqual(data, input.verify_emptylastname)
             

    def test_registerFailed_emptyEmail(self):
        driver = self.driver
        driver.get(input.baseUrl)
        driver.find_element(By.CLASS_NAME, elem.tab_regist).click()
        driver.find_element(By.ID, elem.rb_male).click()
        driver.find_element(By.ID, elem.firstname).send_keys(input.firstname_data)
        driver.find_element(By.ID, elem.lastname).send_keys(input.lastname_data)
        driver.find_element(By.ID, elem.email_regist).send_keys()
        driver.find_element(By.ID, elem.pwd_regist).send_keys(input.valid_pwd)
        driver.find_element(By.ID, elem.confirm_pwd_regist).send_keys(input.valid_pwd)
        driver.find_element(By.ID, elem.regist_btn).click()
        data = driver.find_element(By.XPATH, elem.error_msg_emptyemail).text
        self.assertEqual(data, input.verify_emptyemail)
          

    def test_registerFailed_emptyPassword(self):
        driver = self.driver
        driver.get(input.baseUrl)
        driver.find_element(By.CLASS_NAME, elem.tab_regist).click()
        driver.find_element(By.ID, elem.rb_male).click()
        driver.find_element(By.ID, elem.firstname).send_keys(input.firstname_data)
        driver.find_element(By.ID, elem.lastname).send_keys(input.lastname_data)
        driver.find_element(By.ID, elem.email_regist).send_keys(input.valid_email)
        driver.find_element(By.ID, elem.pwd_regist).send_keys()
        driver.find_element(By.ID, elem.confirm_pwd_regist).send_keys(input.valid_pwd)
        driver.find_element(By.ID, elem.regist_btn).click()
        data = driver.find_element(By.XPATH, elem.error_msg_emptypassword).text
        self.assertEqual(data, input.verify_emptypwd)
      

    def test_registerFailed_passwordNotMatch(self):
        driver = self.driver
        driver.get(input.baseUrl)
        driver.find_element(By.CLASS_NAME, elem.tab_regist).click()
        driver.find_element(By.ID, elem.rb_male).click()
        driver.find_element(By.ID, elem.firstname).send_keys(input.firstname_data)
        driver.find_element(By.ID, elem.lastname).send_keys(input.lastname_data)
        driver.find_element(By.ID, elem.email_regist).send_keys(input.valid_email)
        driver.find_element(By.ID, elem.pwd_regist).send_keys(input.valid_pwd)
        driver.find_element(By.ID, elem.confirm_pwd_regist).send_keys(input.invalid_pwd)
        driver.find_element(By.ID, elem.regist_btn).click()
        data = driver.find_element(By.XPATH, elem.error_msg_notmatchpassword).text
        self.assertEqual(data, input.verify_pwdnotmatch)
           

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()