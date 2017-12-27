from selenium import webdriver
from selenium.webdriver.common.by import By

class Automation():
    def Test(self):
        driver = webdriver.Firefox()
        driver.get("https://letskodeit.teachable.com/p/practice")
        Element = driver.find_element_by_id("name")
        if Element is not None:
            print("Id Element found")
        Element = None
        Element = driver.find_element_by_name("show-hide")
        if Element is not None:
            print("Name Element Found")
        Element = None
        Element = driver.find_element_by_xpath("//*[@id='name']")
        if Element is not None:
            print("Xpath Element found")
        Element = None
        Element = driver.find_element_by_css_selector("#displayed-text")
        if Element is not None:
            print("css selector Element found")
        Element = None
        Element = driver.find_element_by_link_text("Login")
        if Element is not None:
            print("Link text Element found")
        Element = None
        Element = driver.find_element_by_partial_link_text("Log")
        if Element is not None:
            print("Partial link text Element found")
        Element = None
        Element = driver.find_element_by_class_name("displayed-class")
        if Element is not None:
            print("Class name Element found")
        Element = None
        Element = driver.find_element_by_tag_name("a")
        if Element is not None:    
            print("Tag name Element found")

        #   Another Way
        Element = driver.find_element(By.XPATH, "//*[@id='name']")


AutomationObject = Automation()
AutomationObject.Test()
