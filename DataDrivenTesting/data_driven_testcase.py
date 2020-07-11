from selenium import webdriver
import xls_utility
import time

#class DataDrivenTestCase():

driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\chromedriver.exe')
url="http://newtours.demoaut.com/"
driver.get(url)
path="C://Users/User/Desktop/python/Book1.xlsx"
sheet_name="Sheet1"

rows=xls_utility.get_row_count(path,sheet_name)

for row in range(2,rows+1):
    user_name=xls_utility.read_data(path,sheet_name,row,1)
    password=xls_utility.read_data(path,sheet_name,row,2)
    driver.find_element_by_name("userName").send_keys(user_name)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()
    time.sleep(2)
    if driver.title=="Find a Flight: Mercury Tours:":
        status="Test pass"
        print(status)
        xls_utility.write_data(path,sheet_name,row,3,status)
    else:
        status="Test fail"
        print(status)
        xls_utility.write_data(path,sheet_name,row,3,status)
    driver.find_element_by_link_text("Home").click()
driver.quit()


