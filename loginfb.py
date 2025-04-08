from selenium import webdriver
from selenium.webdriver.common.by import By
url='https://facebook.com/'
email=''
password=''
driver=webdriver.Chrome()
driver.maximize_window()
driver.get()
driver.find_element(By.ID,'email').send_keys(email)
driver.find_element(By.ID,'pass').send_keys(password)
driver.find_element(By.NAME,'login').click()