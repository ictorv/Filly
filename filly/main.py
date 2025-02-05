import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def load_available_info():
    return {
        "First Name": "John",
        "Last Name": "Doe",
        "Email": "johndoe@example.com",
        "Phone": "1234567890"
    }

def init_driver():
    driver = webdriver.Chrome()  
    driver.maximize_window()
    return driver

def fill_form(driver, url):
    driver.get(url)
    time.sleep(2)  
    
    available_info = load_available_info()
    
    for field, value in available_info.items():
        input_element = driver.find_element(By.NAME, field.lower().replace(" ", "_"))
        input_element.send_keys(value)
    
    time.sleep(2)

def main():
    form_url = "https://www.w3schools.com/html/html_forms.asp"  # Replace with the actual form URL
    driver = init_driver()
    fill_form(driver, form_url)
    
    driver.quit()
    print("Form processing completed!")

if __name__ == "__main__":
    main()
