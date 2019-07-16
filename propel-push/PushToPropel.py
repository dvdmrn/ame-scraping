import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import os
from tqdm import tqdm
import json

sys.path.insert(0, '../')
import helpers

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=chrome_options)

def getLogin():
	print("accessing loging credentials")
	
	if not os.path.isfile("login.json"):
		print("💀 cannot find login.json!")
		sys.exit()
	
	loginFile = open("login.json")
	login = json.load(loginFile)
	loginFile.close()

	print("username: ",login["username"])

	maskPw = ""
	for c in login["password"]:
		maskPw += "💀"	
	print("password: ",maskPw)

	return login



def login(driver,loginInfo):
	print("entering login credentials to propel website")

	userName = driver.find_element_by_id("username")
	userName.clear()
	userName.send_keys(loginInfo["username"])

	password = driver.find_element_by_id("password")
	password.clear()
	password.send_keys(loginInfo["password"])

	loginBtn = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/ul[2]/form/button")
	print("logging in...")
	loginBtn.click()
	# for i in tqdm(range(0,30)):
	# 	time.sleep(0.1)

	title = driver.find_element_by_id("mainContent")
	try:
		print(title.text[0:113])
	except:
		print("ERROR: cannot find control panel text!")
		exit()


def addSubject(driver, fname, lname, email, age, gender):

	print("adding subject:",fname,lname,"...")
	addSubj = WebDriverWait(driver, 20).until(
		EC.element_to_be_clickable((By.XPATH, "//*[@title='Add']")))

	# driver.find_element_by_xpath('//*[@title="Add"]')
	addSubj.click()
	# time.sleep(1)

	firstName = WebDriverWait(driver, 20).until(
		EC.element_to_be_clickable((By.ID, "firstname")))
	lastName = driver.find_element_by_id("lastname")
	emailField = driver.find_element_by_id("email")
	ageSelector = Select(driver.find_element_by_id("age"))
	genderSelector = Select(driver.find_element_by_id("gender"))

	firstName.send_keys(fname)
	lastName.send_keys(lname)
	emailField.send_keys(email)
	ageSelector.select_by_visible_text(ageToBucket(age))
	genderSelector.select_by_visible_text(genderToBucket(gender))

	submit = driver.find_element_by_id("subjectFrmSubmit")
	submit.click()


def ageToBucket(age):
	try:
		int(age)
	except:
		return ""
	age = int(age)
	buckets = ["0-4","5-14","15-24","25-34","35-44","45-54","55-64","65+"]
	if(0 <= age <= 4):
		return buckets[0]
	elif(5<=age<=14):
		return buckets[1]
	elif(14<=age<=24):
		return buckets[2]
	elif(25<=age<=34):
		return buckets[3]
	elif(35<=age<=44):
		return buckets[4]
	elif(45<=age<=54):
		return buckets[5]
	elif(55<=age<=64):
		return buckets[6]
	elif(age>=65):
		return buckets[7]
	else:
		return ""

def genderToBucket(gender):
	buckets = ["Male","Female","Other"]
	if "m" in gender.lower():
		return buckets[0]
	elif "f" in gender.lower():
		return buckets[1]
	elif "o" in gender.lower():
		return buckets[2]
	else:
		return ""

def sliceNames(name):
	firstLast = name.split(" ")
	print(firstLast)
	try:
		return [firstLast[0]," ".join(firstLast[1:])]
	except:
		return [firstLast[0],""]


def addMultipleSubjects(driver):
	users = helpers.openCSVdict("../active_users.csv")
	print("adding multiple subjects...")
	for user in tqdm(users):
		if user["OPT IN?"] == "n":
			name = sliceNames(user["NAME"])
			addSubject(driver,name[0],name[1],user["EMAIL"],user["AGE"],user["GENDER"])
			time.sleep(0.5)


def main():	
	print("in main!")
	loginURL = "https://propelsurveysolutions.ca/"
	print("...........................................................\n    accessing: ",loginURL)
	driver.get(loginURL)
	loginInfo = getLogin()
	login(driver,loginInfo)

	driver.get("https://propelsurveysolutions.ca/projectLead/project/43/participants/")
	addMultipleSubjects(driver)


main()

