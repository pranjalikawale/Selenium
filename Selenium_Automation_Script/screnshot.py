from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.binary_location = "C://Program Files (x86)/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\chromedriver.exe',chrome_options=options)
driver.get('https://python.org')
#take screenshot
driver.save_screenshot("screenshot.png")
driver.close()