from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Locators import click_nps, nps_description
from Pages.Find_Element import FindElement
from Pages.Login import LoginPage
from Pages.Nps import Nps


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

###nps_categories

    def test02_nps_categories(self):
        nps= Nps(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_nps, 'href', '/nps')
        # nps.enter_click_nps()
        # assert nps
        nps.enter_nps_assert()
        nps.enter_nps_from_date()
        nps.enter_nps_from_date_option()
        nps.enter_nps_to_date()
        nps.enter_nps_to_date_option()
        nps.enter_nps_from_score()
        nps.enter_nps_from_score_option()
        nps.enter_nps_to_score()
        nps.enter_nps_to_score_option()
        nps.enter_nps_search("10")
        sleep(1)
        nps.enter_nps_result()
        findel.wait_until_element_has_an_attribute('xpath', nps_description, 'class', 'show_description btn btn-sm text-nowrap btn-primary')
        # nps.enter_nps_description()
        print("تمام المان های بخش nps بررسی شد")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
