import time
from selenium import webdriver

driver = webdriver.Chrome('/Applications/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.douyu.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('login')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
