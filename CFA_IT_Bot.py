# CFA_IT_Bot
# Nathan Weinberg
# Coded in Python 3.6

import sys
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def open_new_tab(br):
    br.execute_script('''window.open("about:blank", "_blank");''')
    windows = br.window_handles
    br.switch_to_window(windows[-1])

def main(auth):

	# load JSON file with userdata
	try:
		with open(auth) as auth:
			user_data = json.load(auth)
	except FileNotFoundError:
		print("No JSON file found.")
		sys.exit()

	# initialize Chrome webdriver
	executable_path = user_data["paths"]["chromedriver"]
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('user-data-dir=' + user_data["paths"]["chromeoptions"])
	br = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

	## BU Mail Login

	# Google Login
	br.get("https://mail.google.com/mail/u/0/#inbox")
	try:
	    button = br.find_element_by_class_name("gmail-nav__nav-link__sign-in")
	    button.click()
	except:
	    pass        
	username = WebDriverWait(br, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
	username.send_keys(user_data['credentials']['bu_email']['username'])
	button = br.find_element_by_id("identifierNext")
	button.click()

	# BU Login
	username = WebDriverWait(br, 10).until(EC.presence_of_element_located((By.ID, "j_username")))
	username.send_keys(user_data['credentials']['bu_login']['username'])
	password = br.find_element_by_id("j_password")
	password.send_keys(user_data['credentials']['bu_login']['password'])
	button = br.find_element_by_name("_eventId_proceed")
	button.click()

	# Open New Tab and Switch
	open_new_tab(br)

	## Papercut Login
	br.get("https://cfa-print.bu.edu/app")
	username = WebDriverWait(br, 10).until(EC.presence_of_element_located((By.ID, "inputUsername")))
	username.send_keys(user_data['credentials']['bu_login']['username'])
	password = br.find_element_by_id("inputPassword")
	password.send_keys(user_data['credentials']['bu_login']['password'])
	button = br.find_element_by_name("$Submit$0")
	button.click()

	# Open New Tab and Switch
	open_new_tab(br)

	## ServiceNow login
	br.get("https://bu.service-now.com")

	''' Note: Login should be unnessessary as upon testing previous BU
	    logins seems to automatically authenticate ServiceNow. In the
	    event this is no longer the case uncommnet the code below.
	'''
	# username = WebDriverWait(br, 10).until(EC.presence_of_element_located((By.ID, "j_username")))
	# username.send_keys(user_data['credentials']['bu_login']['username'])
	# password = br.find_element_by_id("j_password")
	# password.send_keys(user_data['credentials']['bu_login']['password'])
	# button = br.find_element_by_name("_eventId_proceed")
	# button.click()

	# Open New Tab and Switch
	open_new_tab(br)

	## TechWeb/TechInternal

	# TechWeb
	br.get("http://www.bu.edu/tech/")
	
	# Open New Tab and Switch
	open_new_tab(br)
	
	# TechInternal
	br.get("http://www.bu.edu/techinternal/")

if __name__ == "__main__":
	if len(sys.argv) > 2:
		print('Usage: CFA_IT_Bot [custom json] - open CFA IT websites. Uses "auth.json" be default.')
		sys.exit()
	elif len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		main("auth.json")

	end = input("Press any key to exit program.")
	if end == True:
		sys.exit()