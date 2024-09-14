from docutils.nodes import topic
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.ikea.com/th/th/cat/beds-bm003/?page=3")
topick = driver.find_element(By.CLASS_NAME, "plp-fragment-wrapper")
a = topick.find_element(By.CLASS_NAME, "plp-mastercard ")
b = a.find_element(By.TAG_NAME, "a")


print(b.get_attribute("href"))
driver.quit()
