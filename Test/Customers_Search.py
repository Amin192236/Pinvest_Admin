from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Locators import customers_from_date, customers_to_date
from Pages.Find_Element import FindElement
from Pages.Login import LoginPage
from Pages.Customers import CustomersPage



import unittest

# o = Options()
# o.add_argument('--no-sandbox')
#
# s = Service('d:\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path="chromedriver.exe")

class Test_Pinvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        # cls.driver = webdriver.Chrome(service=s, options=o)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(7)

    def test01_login_register(self):
        self.driver.get("https://admin-ha1.pinvest.ir/signin")
        login = LoginPage(driver=self.driver)
        login.enter_username("superadmin")
        login.enter_password("1234kaKA!")
        login.enter_show_password()
        login.enter_btn_submit()
        sleep(3)
        login.enter_site_header()
        # login.enter_logout()
        # login.enter_logout_no()
        # login.enter_logout()
        # login.enter_logout_yes()
        print("عملیات ورود با موفقیت انجام شد.")

# # # customers_phone_search

    def test02_customers_phone_search(self):
        customers = CustomersPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        customers.enter_customers_click()
        # assert customers
        customers.enter_customers_assert()
        customers.enter_customers_fund()
        customers.enter_customers_fund_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_from_date, 'class', 'form-control pwt-datepicker-input-element')
        # customers.enter_customers_from_date()
        customers.enter_customers_from_date_before()
        customers.enter_customers_from_date_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_to_date, 'name', 'filter_to_date_dp')
        # customers.enter_customers_to_date()
        customers.enter_customers_to_date_next()
        customers.enter_customers_to_date_option()
        customers.enter_customers_phone_search("4120")
        sleep(1)
        customers.enter_customers_phone_search_result()

    def test03_customers_phone_search_direct(self):
        customers = CustomersPage(driver=self.driver)
        customers.enter_customers_search_direct()
        sleep(1)
        customers.enter_customers_phone_search_result()

    def test04_customers_phone_search_indirect(self):
        customers = CustomersPage(driver=self.driver)
        customers.enter_customers_search_indirect()
        sleep(1)
        customers.enter_customers_phone_search_result()

# # # customers_name_search

    def test05_customers_name_search(self):
        customers = CustomersPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        customers.enter_customers_click()
        # assert customers
        customers.enter_customers_assert()
        customers.enter_customers_fund()
        customers.enter_customers_fund_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_from_date, 'class', 'form-control pwt-datepicker-input-element')
        # customers.enter_customers_from_date()
        customers.enter_customers_from_date_before()
        customers.enter_customers_from_date_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_to_date, 'name', 'filter_to_date_dp')
        # customers.enter_customers_to_date()
        customers.enter_customers_to_date_next()
        customers.enter_customers_to_date_option()
        customers.enter_customers_name_search("کیانوش")
        sleep(1)
        customers.enter_customers_name_search_result()

    def test06_customers_name_search_direct(self):
        customers = CustomersPage(driver=self.driver)
        customers.enter_customers_search_direct()
        sleep(1)
        customers.enter_customers_name_search_result()

    def test07_customers_name_search_indirect(self):
        customers = CustomersPage(driver=self.driver)
        customers.enter_customers_search_indirect()
        sleep(1)
        customers.enter_customers_name_search_result()






    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
