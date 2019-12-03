from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

#Now will create driver object

driver = webdriver.Chrome("/usr/bin/chromedriver")

driver.get("http://newtours.demoaut.com")

print(driver.title)

ele_username = driver.find_element_by_name('userName').send_keys('abcd')
ele_password = driver.find_element_by_name('password').send_keys('abcd')

time.sleep(2)
ele_signin = driver.find_element_by_name('login').click()

no_pass = driver.find_element_by_name('passCount')

drp1= Select(no_pass)

drp1.select_by_visible_text('3')


ele_class = driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[2]').click()


driver.find_element_by_name('findFlights').click()

driver.find_element_by_name('reserveFlights').click()


driver.find_element_by_name('buyFlights').click()
