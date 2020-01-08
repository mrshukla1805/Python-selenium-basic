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

ele_signin = driver.find_element_by_name('login').click()

no_pass = driver.find_element_by_name('passCount')

drp1= Select(no_pass)

drp1.select_by_visible_text('3')

dept_from = driver.find_element_by_name('fromPort')

drp2 = Select(dept_from)

drp2.select_by_visible_text('Sydney')

month_on = driver.find_element_by_name('fromMonth')

drp3 = Select(month_on)

drp3.select_by_visible_text('May')

date_on = driver.find_element_by_name('fromDay')

drp4 = Select(date_on)

drp4.select_by_visible_text('18')

arr_from = driver.find_element_by_name('toPort')

drp5= Select(arr_from)

drp5.select_by_visible_text('San Francisco')

month_to = driver.find_element_by_name('toMonth')

drp6 = Select(month_to)

drp6.select_by_visible_text('September')

date_to = driver.find_element_by_name('toDay')

drp7 = Select(date_to)

drp7.select_by_visible_text('17')

driver.find_elements_by_css_selector("input[type='radio'][name='servClass'][value='First']")[0].click()


ele_class = driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[2]').click()


driver.find_element_by_name('findFlights').click()

driver.find_elements_by_css_selector("input[type='radio'][name='outFlight'][value='Pangea Airlines$362$274$9:17']")[0].click()

driver.find_elements_by_css_selector("input[type='radio'][name='inFlight'][value='Unified Airlines$633$303$18:44']")[0].click()

driver.find_element_by_name('reserveFlights').click()

driver.find_element_by_name('buyFlights').click()
