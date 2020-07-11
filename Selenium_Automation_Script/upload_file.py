from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\chromedriver.exe')
driver.implicitly_wait(15)
driver.get("http://demo.guru99.com/test/upload/")
driver.find_element_by_id("uploadfile_0").send_keys("C://Users/User/Desktop/impQuestionForTesting.txt")
driver.find_element_by_id("terms").click()
driver.find_element_by_name("send").click()
driver.close()
