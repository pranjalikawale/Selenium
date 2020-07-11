import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from PIL import Image #crop image and save

class TestBasicOfSelenium():
    
    @pytest.fixture()
    def register_driver(self):
        global driver
        #driver = webdriver.Firefox(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\geckodriver.exe')
        driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\chromedriver.exe')
        #driver = webdriver.Ie(executable_path=r'C:\Users\User\Desktop\python\Automation\driver\IEdriverServer.exe')
        yield
        #driver.close()
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
        oneway.click()
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

    def test_for_alert_popup_click_on_ok(self,register_driver):
        driver.implicitly_wait(10)
        driver.maximize_window()
        url="https://testautomationpractice.blogspot.com"
        driver.get(url)
        driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
        time.sleep(10)
        #Click on ok of alert popup
        driver.switch_to_alert().accept()

    def test_for_alert_popup_click_on_cancel(self,register_driver):
        driver.implicitly_wait(5)
        driver.maximize_window()
        url="https://testautomationpractice.blogspot.com"
        driver.get(url)
        driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
        time.sleep(10)
        #Click on cancel of alert popup 
        driver.switch_to_alert().dismiss()
    
    def test_for_frame(self,register_driver):
        driver.implicitly_wait(5)
        driver.maximize_window()
        url="https://www.selenium.dev/selenium/docs/api/java/index.html"
        driver.get(url)
        driver.switch_to.frame("packageListFrame")# 1st frame
        driver.find_element_by_link_text("com.thoughtworks.selenium.webdriven").click()
        driver.switch_to_default_content()# main frame content
        time.sleep(5)
        driver.switch_to.frame("packageFrame")# 2nd frame
        driver.find_element_by_link_text("WebDriverBackedSelenium").click()
        driver.switch_to_default_content()# main frame
        time.sleep(5)
        driver.switch_to.frame("classFrame")# 3rd or main frame
        driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()
        time.sleep(5)
    
    def test_for_window_handle(self,register_driver):
        driver.implicitly_wait(5)
        driver.maximize_window()
        url="http://demo.automationtesting.in/Windows.html"
        driver.get(url)
        driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
        print(driver.current_window_handle)
        handles=driver.window_handles
        for handle in handles:
            driver.switch_to_window(handle)
            print(driver.title)
            if driver.title=="Frames & windows":
                driver.close()
               
    def test_for_mouse_hover_action(self,register_driver):
        driver.implicitly_wait(5)
        driver.maximize_window()
        url="https://opensource-demo.orangehrmlive.com/"
        driver.get(url)
        driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
        driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
        driver.find_element_by_xpath("//*[@id='btnLogin']").click()
        admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
        user_management=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
        user=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")
        action=ActionChains(driver)
        #mouse hover
        action.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform()        
        time.sleep(5)

    def test_for_mouse_double_click_action(self,register_driver):
        driver.implicitly_wait(5)
        driver.maximize_window()
        url="https://testautomationpractice.blogspot.com"
        driver.get(url)
        element=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
        action=ActionChains(driver)
        #mouse double click
        action.double_click(element).perform()        
        time.sleep(5)

    def test_for_mouse_right_click_action(self,register_driver):
        driver.implicitly_wait(5)
        driver.maximize_window()
        url="https://swisnl.github.io/jQuery-contextMenu/demo.html"
        driver.get(url)
        element=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
        action=ActionChains(driver)
        #mouse right click
        action.context_click(element).perform()        
        time.sleep(5)

    def test_for_mouse_drag_and_drop_action(self,register_driver):
        driver.implicitly_wait(5)
        driver.maximize_window()
        url="http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
        driver.get(url)
        source_element=driver.find_element_by_xpath("//*[@id='box3']")
        destination_element=driver.find_element_by_xpath("//*[@id='box103']")
        action=ActionChains(driver)
        #mouse right click
        action.drag_and_drop(source_element,destination_element).perform()        
        time.sleep(5)
    
    def test_for_upload_file(self,register_driver):
        url="http://demo.guru99.com/test/upload/"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        #upload image
        driver.find_element_by_id("uploadfile_0").send_keys("C://Users/User/Desktop/impQuestionForTesting.txt")
        driver.find_element_by_id("terms").click()
        driver.find_element_by_name("send").click()
        time.sleep(3)
    
    def test_for_download_file(self,register_driver):
        url="http://demo.automationtesting.in/FileDownload.html"
        driver.get(url)
        driver.maximize_window()
        #download file
        driver.find_element_by_id("textbox").send_keys("Testing for doenload") 
        time.sleep(5)
        driver.find_element_by_id("createTxt").click()
        time.sleep(5)
        driver.find_element_by_id("link-to-download").click()

    def test_for_screen_shot(self,register_driver):
        url="http://www.google.com"
        driver.get(url)
        driver.save_screenshot("screenshot.png")

    def test_for_crop_screen_shot(self,register_driver):
        url="http://www.google.com"
        driver.get(url)
        element = driver.find_element_by_id("hplogo")
        location = element.location
        size = element.size
        driver.save_screenshot("screenshot.png")
        # crop image
        x = location['x']
        y = location['y']
        width = location['x']+size['width']
        height = location['y']+size['height']
        crop_image = Image.open('screenshot.png')
        crop_image = crop_image.crop((int(x), int(y), int(width), int(height)))
        crop_image.save('crop_element.png')



