from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
from Pages.Login import LoginPage
from Pages.Reports import Reports
from Locators import *
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

# # # reports_cms_sell_orders

    def test02_reports_cms_sell_orders(self):
        reports= Reports(driver=self.driver)
        reports.enter_click_reports()
        reports.wait_until_element_has_an_attribute('xpath', click_reports_cms_sell_orders, 'href', 'reports/superAdmin')
        # reports.enter_click_reports_cms_sell_orders()
        # assert reports
        reports.enter_reports_cms_sell_orders_assert()
        reports.enter_reports_cms_sell_orders_from_date()
        reports.enter_reports_cms_sell_orders_from_date_back()
        reports.enter_reports_cms_sell_orders_from_date_option()
        reports.enter_reports_cms_sell_orders_to_date()
        reports.enter_reports_cms_sell_orders_to_date_next()
        reports.enter_reports_cms_sell_orders_to_date_option()
        reports.enter_reports_cms_sell_orders_type()
        reports.enter_reports_cms_sell_orders_type_option()
        reports.enter_reports_cms_sell_orders_status()
        reports.enter_reports_cms_sell_orders_status_option()
        # reports.enter_reports_cms_sell_orders_search("4120")
        print("گزارشات کاربران:")
        sleep(1)
        reports.enter_reports_cms_sell_orders_result()

    def test3_reports_shaba(self):
        reports = Reports(driver=self.driver)
        reports.enter_reports_cms_sell_orders_shaba()
        print("اطلاعات شبا یک کاربر:")
        reports.enter_reports_cms_sell_orders_shaba_result()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
