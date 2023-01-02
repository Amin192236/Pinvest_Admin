from time import sleep
from Locators import *


class FindElement:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_has_an_attribute(self, element_selector, element_locator, attribute, attribute_value, timeout=5):
        for i in range(timeout * 5):
            try:
                element = self.driver.find_element(element_selector, element_locator)
                element.click()
                # if exact:
                #     assert element.get_attribute(attribute) == attribute_value
                # else:
                #     assert attribute_value in element.get_attribute(attribute)
                return
            except:
                sleep(0.2)
        raise Exception("Element attribute is not: " + str(attribute))

    def lod_page(self):
            try:
                navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
                responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
                domComplete = self.driver.execute_script("return window.performance.timing.domComplete")

                ''' Calculate the performance'''
                backendPerformance_calc = responseStart - navigationStart
                frontendPerformance_calc = domComplete - responseStart
                print("Front End:", frontendPerformance_calc," _ ", "Back End:", backendPerformance_calc)

                return
            except:
                raise Exception("The page not load")
                # raise Exception("The page not load")

