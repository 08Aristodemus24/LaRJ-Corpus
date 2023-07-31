import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

def get_all_images(path: str) -> list[str]:
    return [file for file in os.listdir(path) if ".png" in file or ".jpeg" in file or ".jpg" in file]


if __name__ == "__main__":
    
    # somehow get absolute path to downloads directory
    abs_downloads_path = sys.argv[1]
    print(abs_downloads_path)
    
    # list all files in directory
    files = "\n".join(get_all_images(abs_downloads_path))
    print(files)
    
    # use current working directory of this file
    # as directory for output texts
    print(os.getcwd())
    
    # make directory for output texts
    
    # open chrome
    PATH = "C:\Program Files (x86)\Chrome Driver\chromedriver.exe"
    service = Service(executable_path=PATH)
    driver = webdriver.Chrome(service=service)
    
    
    try:
        driver.get('https://www.onlineocr.net/')
        driver.maximize_window()
        wait_val = WebDriverWait(driver, timeout=10).until(lambda driver: driver.execute_script('return document.readyState === "complete"'))
        
        # extract select element
        output_select = Select(driver.find_element(By.XPATH, '/html/body/form/div[6]/div/div/div/div[1]/div[4]/div[2]/div/div/div[1]/table/tbody/tr[2]/td/select[2]'))
        
        # select text file for option in select element
        output_select.select_by_value('Text Plain (txt)')
        
        # extract input element
        upload_button = driver.find_element(By.XPATH, '/html/body/form/div[6]/div/div/div/div[1]/div[4]/div[1]/span/input')
        
        # place absolute path of image
        upload_button.send_keys("C:/Users/Mig/Downloads/Image (28).jpg")
        
        # wait until #MainContent_btnOCRConvert is enabled or until this script is
        # finished since the element has event onclick with it set to this script 
        wait_val = WebDriverWait(driver, timeout=10).until(lambda driver: driver.execute_script('return document.querySelector(`input[type="submit"]#MainContent_btnOCRConvert`).getAttribute("disabled") !== null'))
        
        if wait_val == True:
            
            
            # extract button element
            convert_button = driver.find_element(By.XPATH, '/html/body/form/div[6]/div/div/div/div[1]/div[4]/div[2]/div/div/div[2]/input')
            #convert_button.click()
            #convert_button_x_loc, convert_button_y_loc = convert_button.location['x'], convert_button.location['y']
            #print(convert_button_x_loc, convert_button_y_loc)
            
            # instantiate an action for the button element
            action = ActionChains(driver)
            
            # once cursor is moved on the convert to text button click convert
            action.move_by_offset(1057, 402)
            action.click()
            action.perform()
            
            # wait until textarea element is available then extract 
            # textarea element containing the resulting text
            #textarea = driver.find_element(By.XPATH, '/html/body/form/div[6]/div/div/div/div[1]/div[8]/div/div[2]/textarea')
            
            # extract text
            #resultant_text = textarea.text
            #print(resultant_text)
        
        
    except (NoSuchElementException, StaleElementReferenceException) as error:
        print("Error {} has occured".format(error))
        
    except TimeoutError as error:
        print("Error {} has occured".format(error))
    
    