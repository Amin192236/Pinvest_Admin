from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Locators import click_consultations
from Pages.Find_Element import FindElement
from Pages.Login import LoginPage
from Pages.Consultations import Consultations


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

# # # consultations_send

    def test02_consultations(self):
        consultations= Consultations(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_consultations, 'href', '/consultations-list')
        # consultations.enter_click_consultations()
        # assert consultations
        consultations.enter_consultations_assert()
        consultations.enter_consultations_from_date()
        consultations.enter_consultations_from_date_back()
        consultations.enter_consultations_from_date_back()
        consultations.enter_consultations_from_date_back()
        consultations.enter_consultations_from_date_back()
        consultations.enter_consultations_from_date_back()
        consultations.enter_consultations_from_date_option()
        consultations.enter_consultations_to_date()
        consultations.enter_consultations_to_date_next()
        consultations.enter_consultations_to_date_option()
        sleep(1)
        consultations.enter_consultations_result()
        consultations.enter_consultations_switching()
        # consultations.enter_consultations_switching()
        print("تمام المان های درخواست های مشاوره بررسی شد")


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
