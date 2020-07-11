from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\chromedriver.exe')
url="http://demo.automationtesting.in/FileDownload.html"
driver.get(url)
driver.maximize_window()
#download file
driver.find_element_by_id("textbox").send_keys("Testing for doenload") 
time.sleep(5)
driver.find_element_by_id("createTxt").click()
time.sleep(5)
driver.find_element_by_id("link-to-download").click()
driver.close()
