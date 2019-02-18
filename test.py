from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


######### Common Functions ##########
def element_exist(b,element):
    if b.find_element_by_name(element):
        print "visible"
    else:
        print "not visible"


#-------------------------------------
b = webdriver.Firefox()
b.get('http://google.com')
sleep(3)
b.find_element_by_name("q").send_keys("Hello")
sleep(3)
b.find_element_by_name("btnK").click()


