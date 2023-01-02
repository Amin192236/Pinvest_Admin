from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Locators import click_payment, payment_copy, payment_delete, payment_resend_no
from Pages.Find_Element import FindElement
from Pages.Login import LoginPage
from Pages.Payment import Payment

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

# # # payment_send

    def test02_payment(self):
        payment= Payment(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_payment, 'href', 'payment-link')
        # payment.enter_click_payment()
        # assert payment
        payment.enter_payment_assert()
        payment.enter_payment_search("4073422571")
        payment.enter_payment_coefficient_fee("100")
        payment.enter_payment_payment_link_name("Test")
        payment.enter_payment_send()
        print("تست ارسال لینک بررسی شد")

# # # payment_graph

    def test03_payment_graph(self):
        payment = Payment(driver=self.driver)
        payment.enter_payment_from_date()
        payment.enter_payment_from_date_back()
        payment.enter_payment_from_date_option()
        payment.enter_payment_to_date()
        payment.enter_payment_to_date_next()
        payment.enter_payment_to_date_option()
        print("نمودار کارمزد ساخته شده در تاریخ های مورد نظر قابل مشاهده است")


# # # payment_actions

    def test04_payment_actions(self):
        payment = Payment(driver=self.driver)
        findel = FindElement(driver=self.driver)
        payment.enter_payment_table_search("4120")
        self.driver.refresh()
        payment.enter_payment_referral("کیانوش")
        self.driver.refresh()
        # payment.enter_payment_send_to_link()
        findel.wait_until_element_has_an_attribute('xpath', payment_copy, 'class', 'copy_link icon pi-copy cursor_pointer ms-3')
        # sleep(1)
        # payment.enter_payment_copy()
        payment.enter_payment_qr()
        payment.enter_payment_resend()
        sleep(1)
        # findel.wait_until_element_has_an_attribute('xpath', payment_resend_no, 'class', 'btn btn-danger')
        payment.enter_payment_resend_no()
        print("باز ارسال بنا به درخواست شما بررسی شد")
        # payment.enter_payment_resend()
        # payment.enter_payment_resend_yes()

# # # payment_edit

    def test05_payment_edit(self):
        payment = Payment(driver=self.driver)
        self.driver.refresh()
        payment.enter_payment_edit()
        payment.enter_payment_update_coefficient_fee("1")
        payment.enter_payment_update_payment_link_name("1111")
        sleep(1)
        payment.enter_payment_update_link_modal()
       ### payment.enter_payment_update_link_confirm()
        print("ویرایش بررسی شد")

# # # payment_delete

    def test06_payment_delete(self):
        payment = Payment(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', payment_delete, 'class', 'delete_link icon pi-delete cursor_pointer')
        # payment.enter_payment_delete()
        sleep(1)
        payment.enter_payment_delete_link_modal()
       ### payment.enter_payment_delete_link_confirm()
        print("حذف بررسی شد")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(1)
        cls.driver.close()
        cls.driver.quit()
