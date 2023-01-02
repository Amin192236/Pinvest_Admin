from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Locators import transactions_select_option, transactions_reject, transactions_reject_reason
from Pages.Find_Element import FindElement
from Pages.Login import LoginPage
from Pages.Transactions import Transactions


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

    def test02_transactions(self):
        transactions = Transactions(driver=self.driver)
        transactions.enter_click_transactions()
        print("شما با موفقیت وارد قسمت لیست تراکنش ها شدید.")

# # # transactions_search

    def test03_transactions_phone_search(self):
        transactions = Transactions(driver=self.driver)
        transactions.enter_transactions_from_date()
        transactions.enter_transactions_from_date_back()
        transactions.enter_transactions_from_date_option()
        transactions.enter_transactions_to_date()
        transactions.enter_transactions_to_date_next()
        transactions.enter_transactions_to_date_option()
        transactions.enter_transactions_status()
        transactions.enter_transactions_status_option()
        transactions.enter_transactions_fund()
        transactions.enter_transactions_fund_option()
        transactions.enter_transactions_method()
        transactions.enter_transactions_method_option()
        transactions.enter_transactions_trace_id_search("p1nv3st-dev-89b9e14cee")
        transactions.enter_transactions_select_all()
        # transactions.enter_transactions_select_all()
        # transactions.enter_transactions_result()
        # transactions.enter_transactions_select_option()
        # transactions.enter_transactions_approve()
        # transactions.enter_transactions_result()
        # transactions.enter_transactions_reject()

# # # transactions_reject_reason

    def test04_transactions_reject_reason(self):
        transactions = Transactions(driver=self.driver)
        findel = FindElement(driver=self.driver)
        # self.driver.refresh()
        findel.wait_until_element_has_an_attribute('xpath', transactions_select_option, 'class', 'form-check-input')
        # transactions.enter_transactions_select_option()
        # transactions.enter_transactions_approve()
        findel.wait_until_element_has_an_attribute('xpath', transactions_reject, 'class', 'btn btn-danger w-100')
        # transactions.enter_transactions_reject()
        print("در اینجا باید دلیل ردکردن را انتخاب کنید.")
        findel.wait_until_element_has_an_attribute('xpath', transactions_reject_reason, 'class', 'form-select')
        # transactions.enter_transactions_reject_reason()
        transactions.enter_transactions_reject_reason_option()
        # transactions.enter_transactions_reject_reason_yes()
        transactions.enter_transactions_reject_reason_no()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
