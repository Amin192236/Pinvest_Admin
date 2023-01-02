from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
from Pages.Login import LoginPage
from Pages.Invite import Invite


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

# # # invite_send

    def test02_invite(self):
        invite= Invite(driver=self.driver)
        invite.wait_until_element_has_an_attribute('xpath', "//*[@id='desktop_sidebar']/ul/li[16]/a", 'class', 'pi-send')
        # invite.enter_click_invite()
        # assert invite
        invite.enter_invite_assert()
        invite.enter_invite_msisdn("09379161533")
        invite.enter_invite_send_link()
        sleep(1)
        invite.enter_invite_msisdn("09379161533")
        invite.enter_invite_send_card()

# # # invite_show_link

    def test03_invite_show_link(self):
        invite = Invite(driver=self.driver)
        invite.enter_invite_show_link()
        sleep(1)
        invite.enter_invite_result()

# # # invite_show_card

    def test04_invite_show_card(self):
        invite = Invite(driver=self.driver)
        invite.enter_invite_show_card()
        sleep(1)
        invite.enter_invite_result()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
