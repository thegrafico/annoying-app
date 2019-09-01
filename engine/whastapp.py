import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#to use googlechrome
browser = webdriver.Chrome("./engine/drivers/chromedriver")
# browser.set_window_size(300, 500)
browser.set_window_position(0, 0)



# browser.execute_script("window.open('','_blank');")

#open chrome and go to github
browser.get("https://web.whatsapp.com/")

time.sleep(10)

def send_message(number, message):
    
    #Person to send message
    py_btn = browser.find_elements_by_xpath("//*[@id='side']/div[1]/div/label/input")[0]
    py_btn.send_keys(number, Keys.ENTER)

    py_btn = browser.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")[0]
    py_btn.send_keys(message, Keys.ENTER)

    # #password
    # py_btn = browser.find_elements_by_xpath("//*[@id='password']")[0]
    # py_btn.send_keys("Lana022107")

    # #Click login
    # py_btn = browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[7]")[0]
    # py_btn.click()

    # #go to create a new project
    # browser.get("https://github.com/new")

    # #given the name of the repo on github
    # py_btn = browser.find_elements_by_xpath("//*[@id='repository_name']")[0]
    # py_btn.send_keys(foldername)

    # #if go so fast maybe occurs a problem, so, do sleet to wait 3 secons
    # time.sleep(3)

    # #click submit
    # py_btn = browser.find_elements_by_xpath("//*[@id='new_repository']/div[3]/button")[0]
    # py_btn.click()

    # #exit browser
    # browser.quit()


send_message("9392321555", "automated message")
# browser.set_window_size(0, 0)
time.sleep(2)
send_message("7874318538", "automated message")
action = input("Open tap: ")

while action != '0':
    browser.execute_script("window.open('','_blank');")
    action = input("Select task: ")

print("Finish")
# if __name__ == "__main__":
#     create()
