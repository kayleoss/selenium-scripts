import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from variables import *

driver = webdriver.Chrome(executable_path=path_to_chromedriver)
driver.get("https://hotmail.ca")
driver.find_element_by_css_selector(".officeHeaderMenu a.office-signIn").click()
driver.find_element_by_name("loginfmt").send_keys(email_addr)
driver.find_element_by_name("loginfmt").send_keys(Keys.RETURN)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "passwd")))
driver.find_element_by_name('passwd').send_keys(psswd)
time.sleep(2)
driver.find_element_by_name('passwd').send_keys(Keys.RETURN)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.ms-Button.root-50")))
driver.find_element_by_css_selector("button.ms-Button.root-50").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input._1HK2RYE88FOZ7nmxlyoSaw")))
driver.find_element_by_css_selector("input._1HK2RYE88FOZ7nmxlyoSaw").send_keys(send_to)
driver.find_element_by_css_selector("input#subjectLine0").send_keys(subject_line)
driver.find_element_by_css_selector("div[aria-label='Message body']").send_keys(message)
try:
    driver.find_element_by_css_selector("button[aria-label='Send']").click()
    print "SENDING EMAIL TO " + send_to + " - " + date
except:
    print "Unable to send mail"
driver.quit()
    
