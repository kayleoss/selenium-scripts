from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from variables import search_item, run_headless, region, category, send_message, budget, path_to_chromedriver, num_of_results
from itertools import izip
import time

options = ""
links = []

if run_headless == "true":
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
else:
	pass

driver = webdriver.Chrome(executable_path=path_to_chromedriver, chrome_options = options)

def go_to_kijiji():
	driver.maximize_window()
	driver.get("https://www.kijiji.ca/" + category + "/" + region + "/c10l1700273")

def search():
	time.sleep(1)
	driver.find_element_by_css_selector('input#SearchKeyword').send_keys(search_item)
	driver.find_element_by_css_selector('input#SearchKeyword').send_keys(Keys.RETURN)

def collect_results():
	results = driver.find_elements_by_css_selector(".search-item:not(.top-feature) a.title.enable-search-navigation-flag")
	for index, result in izip(xrange(num_of_results), results):
		print str(index + 1) + ") " + result.text
		links.append(result.get_attribute("href"))

def replace_all(str, replacements):
	for i, j in replacements.iteritems():
		text = str.replace(i, j)
	return text
	
def send_messages():
	for link in links:
		driver.get(link)
		d = { ",": "", "$": ""}
		price = replace_all(driver.find_element_by_css_selector("span[itemprop='price']").text, d)
		if float(price) <= budget:
			#handle message sending here
			print str(price) + " can send message" 


go_to_kijiji()
search()
collect_results()
if send_message == "true":
	send_messages()