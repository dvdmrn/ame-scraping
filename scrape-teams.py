import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


OUTPUT_FOLDER = "scraped-teams" # name of output folder


# min/max values of user pages to scrape. Min is inclusive and max is exclusive. So if your range was [0-4) it would provide values 0,1,2,3,4
_MIN_INDEX = 226 # inclusive
_MAX_INDEX = 243 # exclusive

_LOGIN_URL = os.environ["AME_LOGIN"] # access an environment variable with login credentials 

driver = webdriver.Chrome(chrome_options=chrome_options)

print("logging in...")
driver.get(_LOGIN_URL)
print("initializing...\n========================")


def crawl_pages(pages):

	for i in range(_MIN_INDEX,_MAX_INDEX): 
		
		try: 
			url = "https://play.apocalypsemadeeasy.com/admin/teams/"+str(i)+"/show"
			print("~~~~~~~~~\n    accessing: ",url)
			driver.get(url)
			content = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
					By.XPATH, 
					"//*[contains(text(), 'First name')]"
					)))
			body = driver.find_element_by_tag_name("body")
			print(body.get_attribute("innerHTML"))
			pages[str(i)] = body.get_attribute("innerHTML")

		except:
			print("null page")

	driver.close()


def write_pages(toWrite):
	# generates .html files from page contents
	for p in toWrite:
		file = open(OUTPUT_FOLDER+"/"+p+".html","w")
		file.write(toWrite[p])
		file.close()

def main():
	pages = {}
	crawl_pages(pages)
	write_pages(pages)

main()

# response = requests.get(my_url)
# soup = BeautifulSoup(response.text)
# soup.find(id="intro-text")

