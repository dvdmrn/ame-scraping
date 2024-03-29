import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import helpers
import tqdm

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


OUTPUT_FOLDER = "scraped-teams" # name of output folder


driver = webdriver.Chrome(chrome_options=chrome_options)


def crawl_pages(pages,settings):
	print("crawling teams...")
	for i in tqdm.tqdm(range(settings["teams"]["min_team_ID"],settings["teams"]["max_team_ID"])): 
		
		try: 
			url = "https://play.apocalypsemadeeasy.com/admin/teams/"+str(i)+"/show"
			# print("...........................................................\n    accessing: ",url)
			driver.get(url)
			content = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
					By.XPATH, 
					"//*[contains(text(), 'First name')]"
					)))
			body = driver.find_element_by_tag_name("body")
			# print(body.get_attribute("innerHTML"))
			pages[str(i)] = body.get_attribute("innerHTML")

		except:
			print("null page: ",url)

	driver.close()


def write_pages(toWrite):
	# generates .html files from page contents
	print("✏️    writing contents to",OUTPUT_FOLDER)

	for p in tqdm.tqdm(toWrite):
		file = open(OUTPUT_FOLDER+"/"+p+".html","w")
		file.write(toWrite[p])
		file.close()
		time.sleep(0.02)
	time.sleep(1)

def main(settings):

	print("===========================================================",
		"\n🔥 accessing team data 🔥")
	print("logging in...")
	driver.get(settings["login"])

	body = driver.find_element_by_tag_name("body")
	helpers.verifyLogin(body.get_attribute("innerHTML"))

	print("initializing...")
	
	pages = {}
	crawl_pages(pages,settings)
	write_pages(pages)
	helpers.linearScanMissingFiles(settings["teams"]["min_team_ID"],settings["teams"]["max_team_ID"],"scraped-teams")


