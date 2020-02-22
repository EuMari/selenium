#import bibliotek
from selenium import webdriver
from time import sleep


#tworzymy obiekt  -instalacje klasy webdriver
driver = webdriver.Firefox()
driver.get("http://www.wsb.pl")
driver.maximize_window()
#spij 5 s
sleep(5)
driver.quit()
