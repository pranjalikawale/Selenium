from selenium import webdriver
import time

#driver = webdriver.Firefox(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\geckodriver.exe')
driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\chromedriver.exe')
#driver = webdriver.Ie(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\IEdriverServer.exe')
url="http://newtours.demoaut.com"
driver.get(url)
print(driver.title)
#print(driver.page_source)
print(driver.current_url)
driver.close()
driver.quit()