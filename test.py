import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Common Functions #
#def element_exist(b,element):
#    if b.find_element_by_name(element):
#        print "visible"
#    else:
#        print "not visible"
#-------------------------------------
b = webdriver.Firefox()
b.get('http://google.com')
sleep(3)
b.find_element_by_name("q").send_keys("topdanmark")
sleep(3)
b.find_element_by_name("btnK").click()
b.close()
b = webdriver.Firefox()
b.get('https://www.topdanmark.dk')
sleep(5)
b.close()

# create a new Chrome session and launch application home page #
b1 = webdriver.Chrome()
b1.get('http://google.com')
sleep(3)
b1.get('https://www.topdanmark.dk')
sleep(5)
b1.close()

# create a new Internet Explorer session and launch application home page #
b2 = webdriver.Ie()
b2.get('http://google.com')
sleep(3)
b2.find_element_by_name("q").send_keys("topdanmark")
sleep(3)
b2.find_element_by_name("btnK").click()
b2.close()
b2 = webdriver.Ie()
b2.get('https://www.topdanmark.dk')
sleep(5)
b2.close()

