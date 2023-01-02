from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
from Pages.Login import LoginPage
from Pages.Orders import Orders


import unittest

# o = Options()
# o.add_argument('--no-sandbox')
#
# s = Service('d:\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path="E:\PRG_Test\Pinvest_Admin\chromedriver.exe")


class Test_Pinvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        # cls.driver = webdriver.Chrome(service=s, options=o)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

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

# # # orders_codee_search

    def test02_orders_search(self):
        orders = Orders(driver=self.driver)
        orders.enter_orders_click()
        orders.enter_orders_code_search("4120")
        orders.enter_orders_from_date()
        orders.enter_orders_from_date_back()
        orders.enter_orders_from_date_option()
        orders.enter_orders_to_date()
        orders.enter_orders_to_date_next()
        orders.enter_orders_to_date_option()
        orders.enter_orders_fund()
        orders.enter_orders_fund_option()
        orders.enter_orders_status()
        orders.enter_orders_status_option()
        orders.enter_orders_type()
        orders.enter_orders_fund_option()
        orders.enter_orders_fund_option()
        orders.enter_orders_fund_option()
        orders.enter_orders_fund_option()
        sleep(1)
        orders.enter_orders_result()

    def test03_orders_search_direct(self):
        orders = Orders(driver=self.driver)
        orders.enter_orders_direct()
        sleep(1)
        orders.enter_orders_result()

    def test04_orders_search_indirect(self):
        orders = Orders(driver=self.driver)
        orders.enter_orders_indirect()
        sleep(1)
        orders.enter_orders_result()

# # # orders_name_search

    def test05_orders_name_search(self):
        orders = Orders(driver=self.driver)
        orders.enter_orders_click()
        orders.enter_orders_name_search("کیانوش")
        orders.enter_orders_from_date()
        orders.enter_orders_from_date_back()
        orders.enter_orders_from_date_option()
        orders.enter_orders_to_date()
        orders.enter_orders_to_date_next()
        orders.enter_orders_to_date_option()
        orders.enter_orders_fund()
        orders.enter_orders_fund_option()
        orders.enter_orders_status()
        orders.enter_orders_status_option()
        orders.enter_orders_type()
        orders.enter_orders_fund_option()
        orders.enter_orders_fund_option()
        orders.enter_orders_fund_option()
        orders.enter_orders_fund_option()
        sleep(1)
        orders.enter_orders_result()

    def test06_orders_name_search_direct(self):
        orders = Orders(driver=self.driver)
        orders.enter_orders_direct()
        sleep(1)
        orders.enter_orders_result()

    def test07_orders_name_search_indirect(self):
        orders = Orders(driver=self.driver)
        orders.enter_orders_indirect()
        sleep(1)
        orders.enter_orders_result()






    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
