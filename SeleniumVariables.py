from selenium import webdriver

class test():
    def AutomationTestFunction(self):
        BaseURL = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.get(BaseURL)
        Element_CSSSelector = driver.find_element_by_css_selector('#name')
        if Element_CSSSelector is not None:
            print('Element Found CSS Selector')
        Element_Name = driver.find_element_by_name('show-hide')
        Ele = driver.find_element_by_id('displayed-text')
        if Element_Name is not None:
            print('Element Name found')
        if Ele is not None:
            print('element id found')

AutomationTest = test()
AutomationTest.AutomationTestFunction()