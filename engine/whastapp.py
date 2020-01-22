import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

browser = None


def init():
    print("Init whastapp")
    global browser
    # to use googlechrome
    browser = webdriver.Chrome("../web_driver/chromedriver.exe")
    # browser.set_window_size(300, 500)
    # browser.set_window_position(0, 0)

    # browser.execute_script("window.open('','_blank');")

    # open chrome and go to github
    browser.get("https://web.whatsapp.com/")

    time.sleep(5)

def send_message(number, message):
    global browser
    try:
        #Person to send message
        py_btn = browser.find_elements_by_xpath("//*[@id='side']/div[1]/div/label/input")[0]
        py_btn.send_keys(number, Keys.ENTER)
        time.sleep(1)
        py_btn = browser.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")[0]
        py_btn.send_keys(message, Keys.ENTER)
    except:
        print("Error: Try again or later")
#==


if __name__ == "__main__": 
    init()
    msg = ["Puto", "Putazo", "Putazo 3"]
    nran = random.randint(0, len(msg)-1)
    send_message("9392752555", msg[nran])
    
    userInp = int (input("press 0 to exit"))
    
    while userInp != 0:
        nran = random.randint(0, len(msg)-1)
        send_message("7875188867", msg[nran])
        userInp = int (input("press 0 to exit"))
        
        
    # browser.set_window_size(0, 0)