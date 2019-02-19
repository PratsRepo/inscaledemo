import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# create a new Firefox session and search for Topdanmark and launch application home page #
b = webdriver.Firefox()
b.get('http://google.com')
sleep(2)
b.find_element_by_name("q").send_keys("topdanmark")
sleep(5)
b.find_element_by_name("btnK").click()
b.get('https://www.topdanmark.dk')
sleep(5)
b.close()

# create a new Chrome session and launch application home page #
b1 = webdriver.Chrome()
b1.get('http://google.com')
sleep(2)
b1.get('https://www.topdanmark.dk')
sleep(5)
b1.close()

# create a new Internet Explorer session and launch application home page #
b2= webdriver.Ie("C:\\project_workspace\\inscaledemo\\IEDriverServer.exe")
b2.get('https://www.topdanmark.dk')
sleep(5)
b2.close()

