from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()


url = "https://www.google.com"
driver.get(url)


print(f"Title: {driver.title}")
print(f"Current URL: {driver.current_url}")


driver.save_screenshot("Google.PNG")
print("\nScreenShot Taken")


time.sleep(3)
driver.quit()