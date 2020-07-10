import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class TestLocator():
    
    @pytest.fixture()
    def register_driver(self):
        global driver
        #driver = webdriver.Firefox(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\geckodriver.exe')
        driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\chromedriver.exe')
        #driver = webdriver.Ie(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\IEdriverServer.exe')
        yield
        driver.close()
        driver.quit()
    
    def test_for_demonstrate_locator_link_partiallink_name_and_css_selector(self,register_driver):
        url="http://newtours.demoaut.com/"
        driver.get(url)
        print(driver.title)
        #print(driver.page_source)
        print(driver.current_url)

        #count of link 
        link=driver.find_elements(By.LINK_TEXT,"a")
        print(len(link))

        #link
        driver.find_element_by_link_text("REGISTER").click()
        time.sleep(2)
        driver.back()

        #partial link
        driver.find_element_by_partial_link_text("REG").click()
        time.sleep(2)
        driver.back()

        #name
        driver.find_element_by_name("userName").send_keys("mercury")
        #print(username.is_displayed())#check status of element annd return true or false
        #print(username.is_enabled())# return true or false
        driver.find_element_by_name("password").send_keys("mercury")
        #print(password.is_displayed())#check status of element annd return true or false
        #print(password.is_enabled())# return true or false
        driver.find_element_by_name("login").click()

        #css selector
        roundtrip=driver.find_element_by_css_selector("input[value=roundtrip]")
        print("Status of round trip button is selected",roundtrip.is_selected())
        oneway=driver.find_element_by_css_selector("input[value=oneway]")
        print("Status of oneway trip radio button",oneway.is_selected())
        time.sleep(2)
        assert driver.title=="Find a Flight: Mercury Tours:"
        
    def test_for_id_locator_and_waits(self,register_driver):
        driver.implicitly_wait(5)
        driver.maximize_window()
        url="http://demo.guru99.com/test/facebook.html"
        driver.get(url)

        #id
        driver.find_element(By.ID,"email").send_keys("abc")
        driver.find_element(By.ID,"pass").send_keys("123")
        driver.find_element(By.ID,"loginbutton").click()
        time.sleep(3)
        
        #expicit wait
        wait=WebDriverWait(driver,5)
        status=wait.until(EC.title_is(u"Broward College - Fort Lauderdale, FL - Organization, College & University | Facebook"))
        assert status==True

    def test_for_class_locator_and_drop_down(self,register_driver):
        driver.implicitly_wait(5)
        driver.maximize_window()
        url="https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
        driver.get(url)

        #input text field
        inputboxes=driver.find_elements(By.CLASS_NAME,"text_field")
        print(len(inputboxes))
        driver.find_element(By.ID,"RESULT_TextField-1").send_keys("pranjali")
        driver.find_element(By.ID,"RESULT_TextField-2").send_keys("kawale")

        #drop down
        drop_down=Select(driver.find_element_by_id("RESULT_RadioButton-9"))

        #select by visible text
        drop_down.select_by_visible_text('Morning')

        #select by index
        drop_down.select_by_index(2)

        #select by index
        drop_down.select_by_value("Radio-2")

        #count of drop down option
        print(len(drop_down.options))

        #Capture all option
        all_options=drop_down.options

        for option in all_options:
            print(option.text)

        assert driver.current_url==url
   







        
        


    
