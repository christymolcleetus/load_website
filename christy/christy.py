import time
from selenium import webdriver


website =input("whish wesite you want me to open: ")

driver = webdriver.Chrome(r"\chromedriver.exe")    
driver.get("https:" + website)

time.sleep(1000)