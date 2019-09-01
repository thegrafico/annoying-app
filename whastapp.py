import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

#to use googlechrome
browser = webdriver.Chrome("./chromedriver")

browser.execute_script("window.open('','_blank');")

#open chrome and go to github
browser.get("https://web.whatsapp.com/")

# def create():
    
#     #creating the folder
#     foldername = str(sys.argv[1])
#     os.makedirs(projects_path + foldername)
    
#     #username
#     py_btn = browser.find_elements_by_xpath("//*[@id='login_field']")[0]
#     py_btn.send_keys("thegrafico")

#     #password
#     py_btn = browser.find_elements_by_xpath("//*[@id='password']")[0]
#     py_btn.send_keys("Lana022107")

#     #Click login
#     py_btn = browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[7]")[0]
#     py_btn.click()

#     #go to create a new project
#     browser.get("https://github.com/new")

#     #given the name of the repo on github
#     py_btn = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
#     py_btn.send_keys(foldername)

#     #if go so fast maybe occurs a problem, so, do sleet to wait 3 secons
#     time.sleep(3)

#     #click submit
#     py_btn = browser.find_elements_by_xpath("//*[@id='new_repository']/div[3]/button")[0]
#     py_btn.click()

#     #exit browser
#     browser.quit()

x = input("Open tap: ")
while x != '0':
    browser.execute_script("window.open('','_blank');")
    x = input("Select task: ")

print("Finish")
# if __name__ == "__main__":
#     create()
