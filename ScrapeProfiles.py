import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import helpers
from tqdm import tqdm

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


OUTPUT_FOLDER = "scraped-profiles" # name of output folder

driver = webdriver.Chrome(chrome_options=chrome_options)



def crawl_pages(pages,settings):

	for i in range(settings["profiles"]["min_profile_ID"],settings["profiles"]["max_profile_ID"]): 
		
		try: 
			url = "https://play.apocalypsemadeeasy.com/admin/users/"+str(i)+"/show"
			print("...........................................................\n    accessing: ",url)
			driver.get(url)
			content = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
					By.XPATH, 
					"//*[contains(text(), 'in Tech')]"
					)))
			body = driver.find_element_by_tag_name("body")
			print(body.get_attribute("innerHTML"))
			pages[str(i)] = body.get_attribute("innerHTML")

		except:
			print("null page")

	driver.close()


def write_pages(toWrite):

	print("✏️    writing contents to",OUTPUT_FOLDER)
	# generates .html files from page contents
	for p in tqdm(toWrite):
		file = open(OUTPUT_FOLDER+"/"+p+".html","w")
		file.write(toWrite[p])
		file.close()
		time.sleep(0.01)
	time.sleep(1) # sleeps are there because I think not all the files load before ScrapeTeams.py gets to them


def main(settings):
	print("===========================================================",
		"\n👤 accessing profiles 👤")
	print("🔑 logging in with url: ",settings["login"])
	driver.get(settings["login"])
	print("initializing...")

	pages = {}
	crawl_pages(pages,settings)
	write_pages(pages)
	helpers.linearScanMissingFiles(settings["profiles"]["min_profile_ID"],settings["profiles"]["max_profile_ID"],"scraped-profiles")



