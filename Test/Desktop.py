from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
from Pages.Login import LoginPage
from Pages.Desktop import Desktop


import unittest

o = Options()
o.add_argument('--no-sandbox')

s = Service('d:\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_Pinvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=s, options=o)
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

# # # desktop

    def test02_desktop(self):
        desktop = Desktop(driver=self.driver)
        desktop.enter_click_desktop()
        # assert desktop
        desktop.enter_desktop_show()
        desktop.enter_desktop_sub_percent()
        desktop.enter_desktop_sub_value()
        desktop.enter_desktop_sub_active_units()
        desktop.enter_desktop_sub_price_unit()
        desktop.enter_desktop_all_users()
        desktop.enter_desktop_direct_customers()
        desktop.enter_desktop_indirect_customers()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
