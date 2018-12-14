from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from variables import search_term, run_headless, path_to_chromedriver
from itertools import izip

options = ""

if run_headless == "true":
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
else:
	pass

driver = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options = options)

def load_and_set_prefs(search):
	driver.maximize_window()
	driver.get("https://google.com")
	driver.find_element_by_css_selector("input.gsfi").send_keys(search)
	driver.find_element_by_css_selector("input.gsfi").send_keys(Keys.RETURN)
	
def get_results():
	titles = driver.find_elements_by_css_selector(".LC20lb")
	for index, title in izip(xrange(5), titles):
		print str(index + 1) + " " + title.text
	driver.quit()

load_and_set_prefs(search_term)
get_results()