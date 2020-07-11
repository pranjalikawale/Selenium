from selenium import webdriver
from xls_util import XlsUtility
import time

class DataDrivenTestCase():
    driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\chromedriver.exe')
    url="http://newtours.demoaut.com/"
    driver.get(url)
    path="C://Users/User/Desktop/python/Book2.xlsx"
    sheet_name="Sheet1"
    rows=XlsUtility.get_row_count(path,sheet_name)
    for row in range(2,rows+1):
        user_name=XlsUtility.read_data(path,sheet_name,row,1)
        password=XlsUtility.read_data(path,sheet_name,row,2)
        driver.find_element_by_name("userName").send_keys(user_name)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_name("login").click()
        time.sleep(2)
        if driver.title=="Find a Flight: Mercury Tours:":
            status="Test pass"
            print(status)
            XlsUtility.write_data(path,sheet_name,row,3,status)
        else:
            status="Test fail"
            print(status)
            XlsUtility.write_data(path,sheet_name,row,3,status)
        driver.find_element_by_link_text("Home").click()
    driver.quit()

#invoke class
DataDrivenTestCase()



