from selenium.webdriver.common.by import By 
from locator import elem
from data import input

def testLogin(driver, inputemail, inputpwd ):
    driver.get(input.baseUrl)
    driver.find_element(By.CLASS_NAME, elem.tab_login).click()
    driver.find_element(By.ID, elem.email).send_keys(inputemail)
    driver.find_element(By.ID, elem.password).send_keys(inputpwd)
    driver.find_element(By.XPATH, elem.login_btn).click() 