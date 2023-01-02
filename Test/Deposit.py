from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
from Pages.Login import LoginPage
from Pages.Deposit import Deposit


import unittest

# o = Options()
# o.add_argument('--no-sandbox')
#
# s = Service('d:\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="E:\PRG_Test\Pinvest_Admin\chromedriver.exe")


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

# # # deposit

    def test02_deposit(self):
        deposit = Deposit(driver=self.driver)
        deposit.enter_click_deposit()
        # assert deposit
        deposit.enter_deposit_assert()
        deposit.enter_deposit_method()

# # # deposit_pose

    def test03_deposit_pose(self):
        deposit = Deposit(driver=self.driver)
        deposit.enter_deposit_pose()
        print("روش ثبت انتخابی تراکنش پز می باشد.")
        deposit.enter_deposit_pose_bank()
        deposit.enter_deposit_pose_bank_option()
        deposit.enter_deposit_pose_fund()
        # deposit.enter_deposit_pose_submit_btn()

# # # deposit_receipt

    def test04_deposit_receipt(self):
        deposit = Deposit(driver=self.driver)
        self.driver.refresh()
        deposit.enter_deposit_method()
        deposit.enter_deposit_receipt()
        print("روش ثبت انتخابی صدور فیش می باشد.")
        deposit.enter_deposit_receipt_code("1234567890")
        deposit.enter_deposit_receipt_fund()
        deposit.enter_deposit_receipt_fund_option()
        deposit.enter_deposit_receipt_amount("100000000")
        deposit.enter_deposit_receipt_date()
        deposit.enter_deposit_receipt_date_back()
        deposit.enter_deposit_receipt_date_option()
        deposit.enter_deposit_receipt_bank()
        deposit.enter_deposit_receipt_bank_option()
        deposit.enter_deposit_receipt_number("123456789987654321")
        deposit.enter_deposit_receipt_description("این یک تست است")
        # deposit.enter_deposit_receipt_submit_btn()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
