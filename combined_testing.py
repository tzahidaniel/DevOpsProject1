import time
#*****CLASS 4
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:/Users/Tzahi/Downloads/chromedriver_win32/chromedriver.exe"))
driver.get("http://127.0.0.1:5000/users/99ed1db2-4abc-42a9-8074-60a9584de1f1")






