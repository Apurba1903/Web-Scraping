# Traversing in Website
import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = uc.Chrome()
driver.maximize_window()


url = "https://www.google.com"
driver.get(url)
time.sleep(3)


search_bar_xpath = '//*[@id="APjFqb"]'
search_bar = driver.find_element(by = By.XPATH, value = search_bar_xpath)


# Enter Input
search_bar.clear()
time.sleep(2) 

search_bar.send_keys("Machine Learning")
time.sleep(2)


# Hitting Enter Button
search_bar.send_keys(Keys.ENTER)
time.sleep(2)


# Clicking A Button
link_xpath = '//*[@id="rso"]/div[4]/div/div/div[1]/div/div[2]/div/div/span/a/h3'
link = driver.find_element(By.XPATH, link_xpath)

link.click()
time.sleep(2)

driver.quit()


# Submitting a Form
driver = uc.Chrome()
driver.maximize_window()


url = "https://github.com/login"
driver.get(url)
time.sleep(3)


login_xpath = '//*[@id="login_field"]'
login_field = driver.find_element(By.XPATH, login_xpath)
login_field.send_keys('1234')
time.sleep(1)


pass_xpath = '//*[@id="password"]'
pass_field = driver.find_element(By.XPATH, pass_xpath)
pass_field.send_keys('pass1234')
time.sleep(1)


submit_btn = '//*[@id="login"]/div[4]/form/div/input[13]'
clk_btn = driver.find_element(By.XPATH, submit_btn)
clk_btn.click()


driver.quit()