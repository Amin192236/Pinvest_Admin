from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Locators import click_cashout
from Pages.Find_Element import FindElement
from Pages.Login import LoginPage
from Pages.Cashout import Cashout


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
        cls.driver.implicitly_wait(15)

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

# # # cashout

    def test02_cashout(self):
        cashout= Cashout(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_cashout, 'href', '/user-cashout')
        # cashout.enter_click_cashout()
        # assert cashout
        cashout.enter_cashout_assert()
        cashout.enter_cashout_user_id("5769388412")
        cashout.enter_cashout_fund()
        cashout.enter_cashout_unit("1000000")
        cashout.enter_cashout_date()
        cashout.enter_cashout_date_next()
        cashout.enter_cashout_date_option()
        cashout.enter_cashout_value()
        # cashout.enter_cashout_submit_btn()
        print("تمام فیلد های این قسمت به درستی اجرا شدند.")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
