from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
from Locators import *
from Pages.Accounting import Accounting
from Pages.Blog import Blog

from Pages.Cashout import Cashout
from Pages.Compass import Compass
from Pages.Consultations import Consultations
from Pages.Deposit import Deposit
from Pages.Faq import Faq
from Pages.Find_Element import FindElement
from Pages.Invite import Invite
from Pages.Jobs import Jobs
from Pages.Login import LoginPage
from Pages.Desktop import Desktop
from Pages.Customers import CustomersPage
from Pages.Logs import Logs
from Pages.Nps import Nps
from Pages.Orders import Orders
from Pages.Payment import Payment
from Pages.Policy import PolicyPage
from Pages.Reinvesting import Reinvesting
from Pages.Reports import Reports
from Pages.Roles import Roles
from Pages.Settings import Settings
from Pages.Transactions import Transactions
from Pages.Users import Users
import unittest

# o = Options()
# o.add_argument('--no-sandbox')
#
# s = Service('d:\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path="chromedriver.exe")


class Test_Pinvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        # cls.driver = webdriver.Chrome(service=s, options=o)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(7)

    def test01_login_register(self):
        self.driver.get("https://admin-ha1.pinvest.ir/signin")
        login = LoginPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        login.enter_username("superadmin")
        login.enter_password("1234kaKA!")
        login.enter_show_password()
        login.enter_btn_submit()
        # sleep(3)
        findel.lod_page()
        login.enter_site_header()
        # login.enter_logout()
        # login.enter_logout_no()
        # login.enter_logout()
        # login.enter_logout_yes()
        print("عملیات ورود با موفقیت انجام شد.")
#
# # # # desktop

    def test02_desktop(self):
        desktop = Desktop(driver=self.driver)
        findel = FindElement(driver=self.driver)
        desktop.enter_click_desktop()
        findel.lod_page()
        # assert desktop
        desktop.enter_desktop_show()
        desktop.enter_desktop_sub_percent()
        desktop.enter_desktop_sub_value()
        desktop.enter_desktop_sub_active_units()
        desktop.enter_desktop_sub_price_unit()
        desktop.enter_desktop_all_users()
        desktop.enter_desktop_direct_customers()
        desktop.enter_desktop_indirect_customers()
        print("تمام المان های میز کار بررسی شد.")

# # # customers

    def test03_customers(self):
        customers = CustomersPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        customers.enter_customers_click()
        findel.lod_page()
        # assert customers
        customers.enter_customers_assert()
        customers.enter_customers_fund()
        customers.enter_customers_fund_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_from_date, 'class','form-control pwt-datepicker-input-element')
        # customers.enter_customers_from_date()
        customers.enter_customers_from_date_before()
        customers.enter_customers_from_date_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_to_date, 'name', 'filter_to_date_dp')
        # customers.enter_customers_to_date()
        customers.enter_customers_to_date_next()
        customers.enter_customers_to_date_option()
        customers.enter_customers_referral("فرشید نصرتیان سعد آباد")
        # customers.enter_customers_referral_option()
        sleep(1)
        # customers.enter_customers_result()

    # def test03_customers_direct(self):
    #     customers = CustomersPage(driver=self.driver)
    #     customers.enter_customers_search_direct()
    #     sleep(1)
    #     customers.enter_customers_result()

    # def test04_customers_indirect(self):
    #     customers = CustomersPage(driver=self.driver)
    #     customers.enter_customers_search_indirect()
    #     sleep(1)
    #     customers.enter_customers_result()
        print("المان مشتریان بررسی شد.")

# # #customers_show_account

    def test04_customers_show_account(self):
        customers = CustomersPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        customers.enter_customers_click()
        findel.lod_page()
        # customers.enter_customers_show_account()
        # customers.enter_customers_show_account_name()
        print("تمام المان گزارش حساب های مخاطب بررسی شد.")

# # #customers_show_funds

    def test05_customers_show_funds(self):
        customers = CustomersPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        customers.enter_customers_click()
        findel.lod_page()
        # assert customers
        customers.enter_customers_assert()
        customers.enter_customers_fund()
        customers.enter_customers_fund_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_from_date, 'class','form-control pwt-datepicker-input-element')
        # customers.enter_customers_from_date()
        customers.enter_customers_from_date_before()
        customers.enter_customers_from_date_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_to_date, 'name', 'filter_to_date_dp')
        # customers.enter_customers_to_date()
        customers.enter_customers_to_date_next()
        customers.enter_customers_to_date_option()
        customers.enter_customers_referral("فرشید نصرتیان سعد آباد")
        # customers.enter_customers_referral_option()
        sleep(3)
        # customers.enter_customers_show_funds()
        # customers.enter_customers_show_funds_name()
        print("تمام المان صندوق های مخاطب بررسی شد.")

# # # customers_phone_search

    def test06_customers_phone_search(self):
        customers = CustomersPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        customers.enter_customers_click()
        findel.lod_page()
        # assert customers
        customers.enter_customers_assert()
        customers.enter_customers_fund()
        customers.enter_customers_fund_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_from_date, 'class', 'form-control pwt-datepicker-input-element')
        # customers.enter_customers_from_date()
        customers.enter_customers_from_date_before()
        customers.enter_customers_from_date_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_to_date, 'name', 'filter_to_date_dp')
        # customers.enter_customers_to_date()
        customers.enter_customers_to_date_next()
        customers.enter_customers_to_date_option()
        customers.enter_customers_phone_search("4120")
        # sleep(1)
        # customers.enter_customers_phone_search_result()
        print("تمام المان جستجو با کد ملی بررسی شد.")

    def test07_customers_phone_search_direct(self):
        customers = CustomersPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        customers.enter_customers_search_direct()
        findel.lod_page()
        sleep(2)
        customers.enter_customers_phone_search_result()
        print("تمام المان جستجو با کد ملی بصورت مستقیم بررسی شد.")

    def test08_customers_phone_search_indirect(self):
        customers = CustomersPage(driver=self.driver)
        customers.enter_customers_search_indirect()
        sleep(2)
        customers.enter_customers_phone_search_result()
        print("تمام المان جستجو با کد ملی بصورت غیر مستقیم بررسی شد.")

# # # customers_name_search

    def test09_customers_name_search(self):
        customers = CustomersPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        customers.enter_customers_click()
        findel.lod_page()
        # assert customers
        customers.enter_customers_assert()
        customers.enter_customers_fund()
        customers.enter_customers_fund_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_from_date, 'class', 'form-control pwt-datepicker-input-element')
        # customers.enter_customers_from_date()
        customers.enter_customers_from_date_before()
        customers.enter_customers_from_date_option()
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', customers_to_date, 'name', 'filter_to_date_dp')
        # customers.enter_customers_to_date()
        customers.enter_customers_to_date_next()
        customers.enter_customers_to_date_option()
        customers.enter_customers_name_search("کیانوش")
        # sleep(1)
        # customers.enter_customers_name_search_result()
        print("تمام المان جستجو با نام بررسی شد.")

    def test10_customers_name_search_direct(self):
        customers = CustomersPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        customers.enter_customers_search_direct()
        findel.lod_page()
        sleep(1)
        customers.enter_customers_name_search_result()
        print("تمام المان جستجو با نام بصورت مستقیم بررسی شد.")

    def test11_customers_name_search_indirect(self):
        customers = CustomersPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        customers.enter_customers_search_indirect()
        findel.lod_page()
        sleep(1)
        customers.enter_customers_name_search_result()
        print("تمام المان جستجو با نام بصورت غیر مستقیم بررسی شد.")

# # # Roles_Add

    def test12_roles_add(self):
        roles = Roles(driver=self.driver)
        findel = FindElement(driver=self.driver)
        roles.enter_click_roles()
        findel.lod_page()
        roles.enter_roles_assert()
        roles.enter_roles_add()
        findel.lod_page()
        # roles.enter_roles_add_donat_save()
        # roles.enter_roles_add()
        roles.enter_roles_add_name("Test")
        roles.enter_roles_add_permission1()
        roles.enter_roles_add_permission2()
        # roles.enter_roles_add_permission3()
        roles.enter_roles_add_access_role_id()
        roles.enter_roles_add_permission_all()
        # roles.enter_roles_add_save_role_button()
        print("نقش مورد نظر ایجاد شد")

# # # Roles_edit

    def test13_roles_edit(self):
        roles = Roles(driver=self.driver)
        findel = FindElement(driver=self.driver)
        roles.enter_click_roles()
        findel.lod_page()
        roles.enter_roles_edit()
        findel.lod_page()
        sleep(2)
        roles.enter_roles_add_permission1()
        # roles.enter_roles_add_permission2()
        # roles.enter_roles_add_permission3()
        # roles.enter_roles_edit_button()
        print("نقش مورد نظر ویرایش شد")

# # # Roles_delete

    def test14_roles_delete(self):
        roles = Roles(driver=self.driver)
        findel = FindElement(driver=self.driver)
        roles.enter_click_roles()
        findel.lod_page()
        roles.enter_roles_delete()
        findel.lod_page()
        # roles.enter_roles_delete_no()
        # roles.enter_roles_delete()
        # roles.enter_roles_delete_button()
        # roles.enter_roles_delete_no()
        driver.refresh()
        print("نقش مورد نظر حذف شد")

# # # # users_Add

    def test15_users_add(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        users.enter_click_users()
        findel.lod_page()
        users.enter_users_assert()
        users.enter_users_add()
        findel.lod_page()
        users.enter_users_type()
        users.enter_users_type_option()
        users.enter_users_first_name("Test_Name")
        users.enter_users_last_name("Test")
        users.enter_users_national_code("12345678")
        users.enter_users_phone_number("09309303333")
        # # # users.enter_users_username_delete()
        users.enter_users_username("UsernameTest")
        users.enter_users_password("Test12345678*")
        users.enter_users_password_confirmation("Test12345678*")
        # users.enter_users_role_id()
        # users.enter_users_role_option()
        users.enter_users_parent("کیانوش آریانفر")
        users.enter_users_shaba_number("123456789987654321123456")
        # users.enter_users_bank_id()
        # users.enter_users_bank_option()
        users.enter_users_cac("100")
        users.enter_users_address("تهران میرداماد خیابان نفت شمالی")
        # users.enter_users_add_donat_save()
        # users.enter_users_add_save_role_button()
        print("متاسفانه نمیتونم معرف اضافه کنم چون کدهای ولید میخواد و من ندارم :) ")
        print("اما تمام المان ها بررسی شدند. ")

# # # users_edit

    def test16_users_edit(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        self.driver.refresh()
        users.enter_click_users()
        findel.lod_page()
        users.enter_users_assert()
        users.enter_users_search_from_date()
        users.enter_users_search_from_date_back()
        users.enter_users_search_from_date_option()
        findel.wait_until_element_has_an_attribute('xpath', users_edit, 'class', 'icon pi-edit')
        # users.enter_users_edit()
        # users.enter_users_edit_save_user_button()
        # users.enter_users_edit()
        users.enter_users_edit_assert()
        users.enter_users_edit_national_code()
        users.enter_users_edit_username()
        users.enter_users_edit_first_name("Test")
        users.enter_users_edit_last_name("Test")
        users.enter_users_edit_phone_number("001")
        users.enter_users_edit_parent("Test")
        findel.wait_until_element_has_an_attribute('xpath', users_edit_role, 'name', 'role')
        # users.enter_users_edit_role()
        users.enter_users_edit_role_option()
        users.enter_users_edit_shaba("000000")
        findel.wait_until_element_has_an_attribute('xpath', users_edit_bank, 'name', 'bank')
        # users.enter_users_edit_bank()
        users.enter_users_edit_bank_option()
        users.enter_users_edit_address("Test")
        # sleep(2)
        findel.wait_until_element_has_an_attribute('xpath', users_edit_save_no, 'class', 'btn border-primary bg-transparent')
        # users.enter_users_edit_save_no()
        self.driver.refresh()
        print(" تمام المان های بخش ویرایش معرف بررسی شدند. ")

# # # change_password

    def test17_users_change_password(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        users.enter_click_users()
        findel.lod_page()
        users.enter_users_search_from_date()
        users.enter_users_search_from_date_back()
        users.enter_users_search_from_date_option()
        findel.wait_until_element_has_an_attribute('xpath', users_change_password, 'class', '  w-0')
        # users.enter_users_change_password()
        users.enter_users_change_password_assert()
        findel.wait_until_element_has_an_attribute('xpath', users_change_password_yes, 'class', 'btn btn-primary')
        # users.enter_users_change_password_yes()
        users.enter_users_change_password_new("12345678")
        users.enter_users_change_password_show()
        users.enter_users_change_password_confirmation("1234567899")
        users.enter_users_change_password_confirmation_show()
        users.enter_users_change_password_no()
        self.driver.refresh()
        print(" تمام المان های بخش تغییر رمز معرف بررسی شدند. ")

    # # # users_deactivation_activation

    def test18_users_deactivation_activation(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_users, 'href', '/users')
        # users.enter_click_users()
        findel.lod_page()
        users.enter_users_search_from_date()
        users.enter_users_search_from_date_back()
        users.enter_users_search_from_date_option()
        findel.wait_until_element_has_an_attribute('xpath', users_change_password, 'class', '  w-0')
        # users.enter_users_change_password()
        users.enter_users_change_password_assert()
        findel.wait_until_element_has_an_attribute('xpath', users_change_password_yes, 'class', 'btn btn-primary')
        # users.enter_users_change_password_yes()
        users.enter_users_change_password_new("12345678")
        users.enter_users_change_password_show()
        users.enter_users_change_password_confirmation("1234567899")
        users.enter_users_change_password_confirmation_show()
        # users.enter_users_change_password_no()
        self.driver.refresh()
        print("شما با موفقیت یک یوزر را غیرفعال و فعال کردید.")

# # # users_phone_search

    def test19_users_phone_search(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_users, 'href', '/users')
        users.enter_click_users()
        findel.lod_page()
        users.enter_users_search_role()
        users.enter_users_search_role_option()
        users.enter_users_search_from_date()
        users.enter_users_search_from_date_back()
        users.enter_users_search_from_date_option()
        users.enter_users_search_to_date()
        users.enter_users_search_to_date_next()
        users.enter_users_search_to_date_option()
        users.enter_users_search_code("4120")
        sleep(3)
        users.enter_users_search_result()
        print("جستجو با کد ملی انجام و المان ها بررسی شد.")

    def test20_users_phone_search_direct(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.lod_page()
        sleep(1)
        users.enter_users_search_direct()
        sleep(1)
        users.enter_users_search_result()
        print("جستجو با کد ملی بصورت مستقیم انجام و المان ها بررسی شد.")

    def test21_users_phone_search_indirect(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.lod_page()
        users.enter_users_search_indirect()
        sleep(1)
        users.enter_users_search_result()
        print("جستجو با کد ملی بصورت غیر مستقیم انجام و المان ها بررسی شد.")

# # # users_name_search

    def test22_users_name_search(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        self.driver.refresh()
        findel.lod_page()
        users.enter_users_search_role()
        users.enter_users_search_role_option()
        # users.enter_users_search_from_date()
        # users.enter_users_search_from_date_back()
        # users.enter_users_search_from_date_option()
        users.enter_users_search_to_date()
        users.enter_users_search_to_date_next()
        users.enter_users_search_to_date_option()
        users.enter_users_search_name("کیانوش")
        sleep(1)
        users.enter_users_search_result()
        print("جستجو با نام انجام و المان ها بررسی شد.")

    def test23_users_name_search_direct(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        users.enter_users_search_direct()
        findel.lod_page()
        sleep(1)
        users.enter_users_search_result()
        print("جستجو با نام بصورت مستقیم انجام و المان ها بررسی شد.")

    def test24_users_name_search_indirect(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        users.enter_users_search_indirect()
        findel.lod_page()
        sleep(1)
        users.enter_users_search_result()
        print("جستجو با نام بصورت غیر مستقیم انجام و المان ها بررسی شد.")

    def test25_transactions(self):
        transactions = Transactions(driver=self.driver)
        findel = FindElement(driver=self.driver)
        transactions.enter_click_transactions()
        findel.lod_page()
        print("شما با موفقیت وارد قسمت لیست تراکنش ها شدید.")

    # # # transactions_search

    def test26_transactions_phone_search(self):
        transactions = Transactions(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.lod_page()
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
        print("المان های بخش سرچ بررسی شدند.")

# # # transactions_reject_reason

    def test27_transactions_reject_reason(self):
        transactions = Transactions(driver=self.driver)
        findel = FindElement(driver=self.driver)
        # self.driver.refresh()
        findel.lod_page()
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
        self.driver.refresh()
        print("المان های بخش رد شدن درخواست بررسی شدند.")

    # # # orders_codee_search

    def test28_orders_search(self):
        orders = Orders(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders.enter_orders_click()
        findel.lod_page()
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
        print("المان های بخش لیست سفارشات و سرچ با کد بررسی شدند.")

    def test29_orders_search_direct(self):
        orders = Orders(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders.enter_orders_direct()
        findel.lod_page()
        sleep(1)
        orders.enter_orders_result()
        print("المان های بخش لیست سفارشات و سرچ با کد، مستقیم بررسی شدند.")

    def test30_orders_search_indirect(self):
        orders = Orders(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders.enter_orders_indirect()
        findel.lod_page()
        sleep(1)
        orders.enter_orders_result()
        print("المان های بخش لیست سفارشات و سرچ با کد، غیر مستقیم بررسی شدند.")

    # # # orders_name_search

    def test31_orders_name_search(self):
        orders = Orders(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders.enter_orders_click()
        findel.lod_page()
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
        print("المان های بخش لیست سفارشات و سرچ با نام بررسی شدند.")

    def test32_orders_name_search_direct(self):
        orders = Orders(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders.enter_orders_direct()
        findel.lod_page()
        sleep(1)
        orders.enter_orders_result()
        print("المان های بخش لیست سفارشات و سرچ با نام، مستقیم بررسی شدند.")

    def test33_orders_name_search_indirect(self):
        orders = Orders(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders.enter_orders_indirect()
        findel.lod_page()
        sleep(1)
        orders.enter_orders_result()
        print("المان های بخش لیست سفارشات و سرچ با نام، غیر مستقیم بررسی شدند.")

        # # # reports_sell_orders

    def test34_reports_sell_orders(self):
        reports= Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_reports, 'class', 'cursor_pointer')
        # reports.enter_click_reports()
        findel.lod_page()
        findel.wait_until_element_has_an_attribute('xpath', click_reports_sell_orders, 'class', '/reports/sell-orders')
        # reports.enter_click_reports_sell_orders()
        # assert reports
        reports.enter_reports_sell_orders_assert()
        reports.enter_reports_sell_orders_from_date()
        reports.enter_reports_sell_orders_from_date_back()
        reports.enter_reports_sell_orders_from_date_option()
        reports.enter_reports_sell_orders_to_date()
        reports.enter_reports_sell_orders_to_date_next()
        reports.enter_reports_sell_orders_to_date_option()
        reports.enter_reports_sell_orders_type()
        reports.enter_reports_sell_orders_type_option()
        reports.enter_reports_sell_orders_fund()
        reports.enter_reports_sell_orders_fund_option()
        reports.enter_reports_sell_orders_status()
        reports.enter_reports_sell_orders_status_option()
        reports.enter_reports_sell_orders_method()
        reports.enter_reports_sell_orders_method_option()
        reports.enter_reports_sell_orders_search("4120")
        # sleep(2)
        # reports.enter_reports_sell_orders_result()
        # self.driver.refresh()
        print("المان های بخش گزارشات، گزارشات ابطال بررسی شدند.")

# # # reports_cms_sell_orders

    def test35_reports_cms_sell_orders(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        # sleep(1)
        # findel.wait_until_element_has_an_attribute('xpath', click_reports, 'class', 'cursor_pointer')
        # reports.enter_click_reports()
        # sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', click_reports_cms_sell_orders, 'href', '/reports/cms')
        findel.lod_page()
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
        print("المان های بخش گزارشات، گزارشات ابطال کارت از پنل بررسی شدند.")

    def test36_reports_shaba(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        reports.enter_reports_cms_sell_orders_shaba()
        findel.lod_page()
        print("اطلاعات شبا یک کاربر:")
        reports.enter_reports_cms_sell_orders_shaba_result()
        print("المان های بخش گزارشات، گزارشات ابطال کارت از پنل، شبا بررسی شدند.")

# # # reinvesting_search

    def test37_reinvesting_search(self):
        reinvesting = Reinvesting(driver=self.driver)
        findel = FindElement(driver=self.driver)
        # sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', click_reinvesting, 'href', '/reinvesting')
        # reinvesting.enter_reinvesting_click()
        findel.lod_page()
        # sleep(2)
        reinvesting.enter_reinvesting_search("4120")
        # reinvesting.enter_reinvesting_result()
        reinvesting.enter_reinvesting_funds()
        reinvesting.enter_reinvesting_funds_name()
        reinvesting.enter_reinvesting_investment()
        # reinvesting.enter_reinvesting_investment_option()
        reinvesting.enter_reinvesting_hide()
        print("المان های بخش درصد سرمایه گذاری مجدد کاربران بررسی شدند.")

    # # # deposit

    def test38_deposit(self):
        deposit = Deposit(driver=self.driver)
        findel = FindElement(driver=self.driver)
        deposit.enter_click_deposit()
        findel.lod_page()
        # assert deposit
        deposit.enter_deposit_assert()
        deposit.enter_deposit_method()
        print("المان های بخش ثبت واریز کاربران بررسی شدند.")

    # # # deposit_pose

    def test39_deposit_pose(self):
        deposit = Deposit(driver=self.driver)
        findel = FindElement(driver=self.driver)
        deposit.enter_deposit_pose()
        findel.lod_page()
        print("روش ثبت انتخابی تراکنش پز می باشد.")
        deposit.enter_deposit_pose_bank()
        deposit.enter_deposit_pose_bank_option()
        deposit.enter_deposit_pose_fund()
        # deposit.enter_deposit_pose_submit_btn()
        print("المان های بخش ثبت واریز کاربران، روش ثبت تراکنش پوز بررسی شدند.")

    # # # deposit_receipt

    def test40_deposit_receipt(self):
        deposit = Deposit(driver=self.driver)
        findel = FindElement(driver=self.driver)
        self.driver.refresh()
        findel.lod_page()
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
        print("المان های بخش ثبت واریز کاربران، روش ثبت صدور فیش بررسی شدند.")

# # # reports_providers

    def test41_reports_providers(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_reports, 'class', 'cursor_pointer')
        # sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', click_reports_providers, 'href', '/reports/providers')
        # reports.enter_click_reports_providers()
        findel.lod_page()
        # assert reports
        reports.enter_reports_providers_assert()
        reports.enter_reports_providers_value_report_1()
        reports.enter_reports_providers_report_1_month()
        # reports.enter_reports_providers_report_1_month_option()
        reports.enter_reports_providers_report_1_year()
        reports.enter_reports_providers_report_1_year_option()
        reports.enter_reports_providers_report_1_graph()
        reports.enter_reports_providers_report_1_graph()
        reports.enter_reports_providers_report_1_fund()
        # sleep(1)
        # reports.enter_reports_providers_report_1_fund_result()
        reports.enter_reports_providers_report_1_fund()
        reports.enter_reports_providers_value_report_2()
        reports.enter_reports_providers_report_2_month()
        reports.enter_reports_providers_report_2_month_option()
        reports.enter_reports_providers_report_2_year()
        reports.enter_reports_providers_report_2_year_option()
        reports.enter_reports_providers_report_2_graph()
        reports.enter_reports_providers_report_2_graph()
        reports.enter_reports_providers_report_2_fund()
        # sleep(1)
        # reports.enter_reports_providers_report_2_fund_result()
        reports.enter_reports_providers_report_2_fund()
        print("المان های بخش گزارشات، گزارشات تامین کنندگان بررسی شدند.")

# # # reports_cards_daily

    def test42_reports_cards_daily(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        # findel.wait_until_element_has_an_attribute('xpath', click_reports, 'class', 'cursor_pointer')
        # reports.enter_click_reports()
        findel.wait_until_element_has_an_attribute('xpath', click_reports_cards_daily, 'href', '/reports/cards-daily')
        # reports.enter_click_reports_cards_daily()
        findel.lod_page()
        # assert reports
        reports.enterreports_cards_daily_assert()
        reports.enter_reports_cards_daily_date()
        # reports.enter_reports_cards_daily_date_back()
        reports.enter_reports_cards_daily_date_option()
        # sleep(1)
        # reports.enter_reports_cards_daily_result()
        print("المان های بخش گزارشات، گزارشات روزانه کارت‌ها بررسی شدند.")

# # # reports_users_invited_phone_search

    def test43_reports_users_invited_phone_search(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        # findel.wait_until_element_has_an_attribute('xpath', click_reports, 'class', 'cursor_pointer')
        # reports.enter_click_reports()
        findel.wait_until_element_has_an_attribute('xpath', click_reports_users_invited, 'href', '/reports/users-invited')
        # reports.enter_click_reports_users_invited()
        findel.lod_page()
        # assert reports
        reports.enter_reports_users_invited_assert()
        reports.enter_reports_users_invited_phone_search("4120")
        reports.enter_reports_users_invited_from_date()
        reports.enter_reports_users_invited_from_date_back()
        reports.enter_reports_users_invited_from_date_option()
        reports.enter_reports_users_invited_to_date()
        reports.enter_reports_users_invited_to_date_next()
        reports.enter_reports_users_invited_to_date_option()
        sleep(1)
        reports.enter_reports_users_invited_phone_search_result()
        print("المان های بخش گزارشات، گزارش تعداد کاربران دعوت شده با کد ملی بررسی شدند.")

# # # reports_users_invited_phone_search

    def test44_enter_reports_users_invited_name_search(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        self.driver.refresh()
        findel.lod_page()
        reports.enter_reports_users_invited_name_search("کیانوش")
        sleep(1)
        reports.enter_reports_users_invited_phone_search_result()
        print("المان های بخش گزارشات، گزارش تعداد کاربران دعوت شده با نام بررسی شدند.")

# # # reports_users_buy_sell_phone_search

    def test45_reports_users_buy_phone_search(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        # findel.wait_until_element_has_an_attribute('xpath', click_reports, 'class', 'cursor_pointer')
        # reports.enter_click_reports()
        findel.wait_until_element_has_an_attribute('xpath', click_reports_users_buy_sell, 'href', '/reports/users-buy-sell')
        # reports.enter_click_reports_users_buy_sell()
        findel.lod_page()
        # assert reports
        reports.enter_reports_users_buy_sell_assert()
        reports.enter_reports_users_buy_sell_phone_search("4120")
        reports.enter_reports_users_buy_sell_from_date()
        reports.enter_reports_users_buy_sell_from_date_back()
        reports.enter_reports_users_buy_sell_from_date_option()
        reports.enter_reports_users_buy_sell_to_date()
        reports.enter_reports_users_buy_sell_to_date_next()
        reports.enter_reports_users_buy_sell_to_date_option()
        sleep(1)
        reports.enter_reports_users_buy_sell_phone_search_result()
        print("المان های بخش گزارشات، واریز و برداشت زیرمجموعه ادمین ها با کدملی، بخش خرید بررسی شدند.")

# # # reports_users_sell_phone_search

    def test46_reports_users_sell_phone_search(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        reports.enter_reports_users_buy_sell_btn_sale()
        findel.lod_page()
        sleep(1)
        reports.enter_reports_users_buy_sell_phone_search_result()
        print("المان های بخش گزارشات، واریز و برداشت زیرمجموعه ادمین ها با کدملی، بخش فروش بررسی شدند.")

# # # reports_users_buy_sell_name_search

    def test47_reports_users_buy_sell_name_search(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        self.driver.refresh()
        findel.lod_page()
        reports.enter_reports_users_buy_sell_name_search("h.soleimani")
        # sleep(2)
        # reports.enter_reports_users_buy_sell_phone_search_result()
        print("المان های بخش گزارشات، واریز و برداشت زیرمجموعه ادمین ها با نام کاربری، بخش خرید بررسی شدند.")

# # # reports_users_sell_name_search

    def test48_reports_users_sell_name_search(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        reports.enter_reports_users_buy_sell_btn_sale()
        findel.lod_page()
        sleep(1)
        reports.enter_reports_users_buy_sell_phone_search_result()
        print("المان های بخش گزارشات، واریز و برداشت زیرمجموعه ادمین ها با نام کاربری، بخش فروش بررسی شدند.")

# # # reports_disabled_accounts

    def test49_reports_disabled_accounts(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        # findel.wait_until_element_has_an_attribute('xpath', click_reports, 'class', 'cursor_pointer')
        # reports.enter_click_reports()
        findel.wait_until_element_has_an_attribute('xpath', click_reports_disabled_accounts, 'href', '/reports/disabled-accounts')
        # reports.enter_click_reports_disabled_accounts()
        findel.lod_page()
        # assert reports
        reports.enter_reports_disabled_accounts_assert()
        reports.enter_reports_disabled_accounts_phone_search("412")
        reports.enter_reports_disabled_accounts_from_date()
        reports.enter_reports_disabled_accounts_from_date_back()
        reports.enter_reports_disabled_accounts_from_date_option()
        reports.enter_reports_disabled_accounts_to_date()
        reports.enter_reports_disabled_accounts_to_date_next()
        reports.enter_reports_disabled_accounts_to_date_option()
        sleep(1)
        reports.enter_reports_disabled_accounts_phone_search_result()
        print("المان های بخش گزارشات، حساب های غیرفعال یا حذف شده بررسی شدند.")

# # # cashout

    def test50_cashout(self):
        cashout= Cashout(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_cashout, 'href', '/user-cashout')
        # cashout.enter_click_cashout()
        findel.lod_page()
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
        print("المان های بخش  ثبت برداشت کاربران بررسی شدند.")

# # # jobs

    def test51_jobs(self):
        jobs = Jobs(driver=self.driver)
        findel = FindElement(driver=self.driver)
        sleep(1)
        jobs.enter_click_jobs()
        findel.lod_page()
        # assert jobs
        jobs.enter_jobs_assert()
        jobs.enter_jobs_fund()
        jobs.enter_jobs_fund_option()
        jobs.enter_jobs_config_rayanBuy()
        jobs.enter_jobs_config_WithdrawJob()
        jobs.enter_jobs_config_updatesOrdersStatus()
        jobs.enter_jobs_national("1234567890")
        jobs.enter_jobs_config_withdrawWithNationalCode()
        print("المان های بخش  ثبت جاب ها بررسی شدند.")

# # # invite_send

    def test52_invite(self):
        invite = Invite(driver=self.driver)
        findel = FindElement(driver=self.driver)
        invite.wait_until_element_has_an_attribute('xpath', "//*[@id='desktop_sidebar']/ul/li[16]/a", 'class', 'pi-send')
        # invite.enter_click_invite()
        findel.lod_page()
        # assert invite
        invite.enter_invite_assert()
        invite.enter_invite_msisdn("09379161533")
        invite.enter_invite_send_link()
        sleep(1)
        invite.enter_invite_msisdn("09379161533")
        invite.enter_invite_send_card()

# # # invite_show_link

    def test53_invite_show_link(self):
        invite = Invite(driver=self.driver)
        findel = FindElement(driver=self.driver)
        invite.enter_invite_show_link()
        findel.lod_page()
        # sleep(1)
        # invite.enter_invite_result()

# # # invite_show_card

    def test54_invite_show_card(self):
        invite = Invite(driver=self.driver)
        findel = FindElement(driver=self.driver)
        invite.enter_invite_show_card()
        findel.lod_page()
        sleep(1)
        invite.enter_invite_result()

# # # settings

    def test55_settings(self):
        settings = Settings(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_settings, 'href', 'settings')
        # settings.enter_click_settings()
        findel.lod_page()
        ###assert settings
        settings.enter_settings_add()
        settings.enter_settings_name("aa")
        settings.enter_settings_trans("aa")
        settings.enter_settings_add_config_form("2")
        settings.enter_settings_value()
        settings.enter_settings_value_option()
        # settings.enter_settings_save()
        settings.enter_settings_no_save()
        self.driver.refresh()
        print("تمام المان های اضافه کردن تنضیمات بررسی شد.")

    def test56_settings(self):
        settings = Settings(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.lod_page()
        settings.enter_settings_version()
        settings.enter_settings_version_option()
        settings.enter_settings_transactions_daily()
        settings.enter_settings_transactions_daily_option()
        settings.enter_settings_transactions_monthly()
        settings.enter_settings_transactions_monthly_option()
        settings.enter_settings_FARABOOM_PAYMAN_API_MAX_CONTRACT_EXPIRATION_YEARS()
        settings.enter_settings_FARABOOM_PAYMAN_API_MAX_CONTRACT_EXPIRATION_YEARS_option()
        settings.enter_settings_POD_API_MAX_COUNT()
        settings.enter_settings_POD_API_MAX_COUNT_option()
        settings.enter_settings_FINNOTECH_API_MAX_MONTHLY_TRANSACTION_COUNT()
        settings.enter_settings_FINNOTECH_API_MAX_MONTHLY_TRANSACTION_COUNT_option()
        # settings.enter_settings_CAPTCHA()
        findel.wait_until_element_has_an_attribute('xpath', settings_CAPTCHA, 'name', 'CAPTCHA')
        settings.enter_settings_CAPTCHA_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_SMS_PANEL, 'name', 'SMS_PANEL')
        # settings.enter_settings_SMS_PANEL()
        settings.enter_settings_SMS_PANEL_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_OTP_EXPIRE, 'name', 'OTP_EXPIRE')
        # settings.enter_settings_OTP_EXPIRE()
        settings.enter_settings_OTP_EXPIRE_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_TEST_MODE, 'name', 'TEST_MODE')
        findel.wait_until_element_has_an_attribute('xpath', settings_TEST_MODE, 'name', 'TEST_MODE')
        # settings.enter_settings_TEST_MODE()
        findel.wait_until_element_has_an_attribute('xpath', settings_MAX_OTP_CHECK, 'name', 'MAX_OTP_CHECK')
        # settings.enter_settings_MAX_OTP_CHECK()
        settings.enter_settings_MAX_OTP_CHECK_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_TIME_SCOPE_EXPIRE, 'name', 'TIME_SCOPE_EXPIRE')
        # settings.enter_settings_TIME_SCOPE_EXPIRE()
        settings.enter_settings_TIME_SCOPE_EXPIRE_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_LOGIN_TIME_EXPIRE, 'name', 'LOGIN_TIME_EXPIRE')
        # settings.enter_settings_LOGIN_TIME_EXPIRE()
        settings.enter_settings_LOGIN_TIME_EXPIRE_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_MAX_RETRY_SCOPE, 'name', 'MAX_RETRY_SCOPE')
        # settings.enter_settings_MAX_RETRY_SCOPE()
        settings.enter_settings_MAX_RETRY_SCOPE_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_GOOGLE_CAPTCHA_PAGES, 'name', 'GOOGLE_CAPTCHA_PAGES')
        findel.wait_until_element_has_an_attribute('xpath', settings_GOOGLE_CAPTCHA_PAGES, 'name', 'GOOGLE_CAPTCHA_PAGES')
        # settings.enter_settings_GOOGLE_CAPTCHA_PAGES()
        findel.wait_until_element_has_an_attribute('xpath', settings_REQUIREMENT_BANK_ACCOUNT_REGISTRATION, 'name', 'REQUIREMENT_BANK_ACCOUNT_REGISTRATION')
        findel.wait_until_element_has_an_attribute('xpath', settings_REQUIREMENT_BANK_ACCOUNT_REGISTRATION, 'name', 'REQUIREMENT_BANK_ACCOUNT_REGISTRATION')
        # settings.enter_settings_REQUIREMENT_BANK_ACCOUNT_REGISTRATION()
        findel.wait_until_element_has_an_attribute('xpath', settings_INCREASE_COEFFICIENT, 'name','INCREASE_COEFFICIENT')
        # settings.enter_settings_INCREASE_COEFFICIENT()
        settings.enter_settings_INCREASE_COEFFICIENT_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_GOOGLE_2F_AUTH, 'name', 'GOOGLE_2F_AUTH')
        findel.wait_until_element_has_an_attribute('xpath', settings_GOOGLE_2F_AUTH, 'name', 'GOOGLE_2F_AUTH')
        # settings.enter_settings_GOOGLE_2F_AUTH()
        findel.wait_until_element_has_an_attribute('xpath', settings_WRAPPER_SEND_MESSAGE_BY_SMS, 'name', 'WRAPPER_SEND_MESSAGE_BY_SMS')
        # settings.enter_settings_WRAPPER_SEND_MESSAGE_BY_SMS()
        settings.enter_settings_WRAPPER_SEND_MESSAGE_BY_SMS_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_WRAPPER_SEND_PATTERN_BY_SMS, 'name', 'WRAPPER_SEND_PATTERN_BY_SMS')
        # settings.enter_settings_WRAPPER_SEND_PATTERN_BY_SMS()
        settings.enter_settings_WRAPPER_SEND_PATTERN_BY_SMS_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_SHAHKAR_PANEL, 'name', 'SHAHKAR_PANEL')
        # settings.enter_settings_SHAHKAR_PANEL()
        settings.enter_settings_SHAHKAR_PANEL_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_WRAPPER_SHAHKAR, 'name', 'WRAPPER_SHAHKAR')
        # settings.enter_settings_WRAPPER_SHAHKAR()
        settings.enter_settings_WRAPPER_SHAHKAR_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_JIBIMO_CHECK_NATIONAL_CODE, 'name', 'IPG_JIBIMO_CHECK_NATIONAL_CODE')
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_JIBIMO_CHECK_NATIONAL_CODE, 'name', 'IPG_JIBIMO_CHECK_NATIONAL_CODE')
        # settings.enter_settings_IPG_JIBIMO_CHECK_NATIONAL_CODE()
        findel.wait_until_element_has_an_attribute('xpath', settings_CARD_SERVICE_MENU, 'name', 'CARD_SERVICE_MENU')
        # settings.enter_settings_CARD_SERVICE_MENU()
        settings.enter_settings_CARD_SERVICE_MENU_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_RAYAN_REQUEST_TIMEOUT, 'name', 'RAYAN_REQUEST_TIMEOUT')
        # settings.enter_settings_RAYAN_REQUEST_TIMEOUT()
        settings.enter_settings_RAYAN_REQUEST_TIMEOUT_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_DOMAIN_SEND_SMS, 'name', 'DOMAIN_SEND_SMS')
        # settings.enter_settings_DOMAIN_SEND_SMS()
        settings.enter_settings_DOMAIN_SEND_SMS_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_MIN_NAV, 'name', 'MIN_NAV')
        # settings.enter_settings_MIN_NAV()
        settings.enter_settings_MIN_NAV_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_MAX_NAV, 'name', 'MAX_NAV')
        # settings.enter_settings_MAX_NAV()
        settings.enter_settings_MAX_NAV_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_SEJAM_DEFAULT, 'name', 'SEJAM_DEFAULT')
        # settings.enter_settings_SEJAM_DEFAULT()
        settings.enter_settings_SEJAM_DEFAULT_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_WRAPPER_SEJAM, 'name', 'WRAPPER_SEJAM')
        # settings.enter_settings_WRAPPER_SEJAM()
        settings.enter_settings_WRAPPER_SEJAM_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_WRAPPER_FUND_REGISTER, 'name', 'WRAPPER_FUND_REGISTER')
        # settings.enter_settings_WRAPPER_FUND_REGISTER()
        settings.enter_settings_WRAPPER_FUND_REGISTER_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_SEP, 'name', 'IPG_SEP')
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_SEP, 'name', 'IPG_SEP')
        # settings.enter_settings_IPG_SEP()
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_PEP, 'name', 'IPG_PEP')
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_PEP, 'name', 'IPG_PEP')
        # settings.enter_settings_IPG_PEP()
        findel.wait_until_element_has_an_attribute('xpath', settings_EXPIRE_FUND_LICENSE_AFTER_DAY, 'name', 'EXPIRE_FUND_LICENSE_AFTER_DAY')
        settings.enter_settings_EXPIRE_FUND_LICENSE_AFTER_DAY()
        settings.enter_settings_EXPIRE_FUND_LICENSE_AFTER_DAY_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_PROFIT_CALCULATION_DAY, 'name', 'PROFIT_CALCULATION_DAY')
        # settings.enter_settings_PROFIT_CALCULATION_DAY()
        settings.enter_settings_PROFIT_CALCULATION_DAY_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_SEPEHR, 'name', 'IPG_SEPEHR')
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_SEPEHR, 'name', 'IPG_SEPEHR')
        # settings.enter_settings_IPG_SEPEHR()
        findel.wait_until_element_has_an_attribute('xpath', settings_PAYMENT_LINK_GATEWAY, 'name', 'PAYMENT_LINK_GATEWAY')
        # settings.enter_settings_PAYMENT_LINK_GATEWAY()
        settings.enter_settings_PAYMENT_LINK_GATEWAY_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_JIBIMO, 'name', 'IPG_JIBIMO')
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_JIBIMO, 'name', 'IPG_JIBIMO')
        # settings.enter_settings_IPG_JIBIMO()
        findel.wait_until_element_has_an_attribute('xpath', settings_BASE_NAV, 'name', 'BASE_NAV')
        # settings.enter_settings_BASE_NAV()
        settings.enter_settings_BASE_NAV_option()
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_SADAD, 'name', 'IPG_SADAD')
        findel.wait_until_element_has_an_attribute('xpath', settings_IPG_SADAD, 'name', 'IPG_SADAD')
        # settings.enter_settings_IPG_SADAD()
        print("تمام المان های ویرایش کردن تنضیمات بررسی شد.")

# # # Accounting

    def test57_accounting(self):
        accounting = Accounting(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.lod_page()
        findel.wait_until_element_has_an_attribute('xpath', click_accounting, 'href', '/accounting')
        # accounting.enter_click_accounting()
        accounting.enter_accounting_assert()
        accounting.enter_accounting_referral("کیانوش")
        accounting.enter_accounting_referral_btn()
        print("المان های بخش  حسابداری بررسی شدند.")

# # # compass

    def test58_compass(self):
        compass = Compass(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.lod_page()
        findel.wait_until_element_has_an_attribute('xpath', click_compass, 'href', '/accounting')
        # compass.enter_click_compass()
        compass.enter_compass_assert()
        compass.enter_compass_fund()
        compass.enter_compass_fund_option()
        compass.enter_compass_from_date()
        compass.enter_compass_from_date_option()
        compass.enter_compass_to_date()
        compass.enter_compass_to_date_option()
        compass.enter_compass_chart()
        print("المان های بخش  قطب‌نما بررسی شدند.")

# # # payment_send

    def test59_payment(self):
        payment = Payment(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.lod_page()
        findel.wait_until_element_has_an_attribute('xpath', click_payment, 'href', '/payment-link')
        # payment.enter_click_payment()
        # assert payment
        payment.enter_payment_assert()
        payment.enter_payment_search("4073422571")
        payment.enter_payment_coefficient_fee("100")
        payment.enter_payment_payment_link_name("Test")
        payment.enter_payment_send()
        print("تست ارسال لینک بررسی شد")

# # # payment_graph

    def test60_payment_graph(self):
        payment = Payment(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.lod_page()
        payment.enter_payment_from_date()
        payment.enter_payment_from_date_back()
        payment.enter_payment_from_date_option()
        payment.enter_payment_to_date()
        payment.enter_payment_to_date_next()
        payment.enter_payment_to_date_option()
        print("نمودار کارمزد ساخته شده در تاریخ های مورد نظر قابل مشاهده است")

# # # payment_actions

    def test61_payment_actions(self):
        payment = Payment(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.lod_page()
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

    def test62_payment_edit(self):
        payment = Payment(driver=self.driver)
        findel = FindElement(driver=self.driver)
        self.driver.refresh()
        findel.lod_page()
        payment.enter_payment_edit()
        payment.enter_payment_update_coefficient_fee("1")
        payment.enter_payment_update_payment_link_name("1111")
        sleep(1)
        payment.enter_payment_update_link_modal()
        ### payment.enter_payment_update_link_confirm()
        print("ویرایش بررسی شد")

# # # payment_delete

    def test63_payment_delete(self):
        payment = Payment(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.lod_page()
        findel.wait_until_element_has_an_attribute('xpath', payment_delete, 'class', 'delete_link icon pi-delete cursor_pointer')
        # payment.enter_payment_delete()
        sleep(1)
        payment.enter_payment_delete_link_modal()
        ### payment.enter_payment_delete_link_confirm()
        print("حذف بررسی شد")

# # # consultations_send

    def test64_consultations(self):
        consultations = Consultations(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_consultations, 'href', '/consultations-list')
        # consultations.enter_click_consultations()
        findel.lod_page()
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

# # # blog

    def test65_blog(self):
        blog = Blog(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_blog, 'href', '/blog/posts')
        # blog.enter_click_blog()
        findel.lod_page()
        # assert blog
        blog.enter_blog_assert()
        blog.enter_blog_category()
        blog.enter_blog_category_option()
        blog.enter_blog_search("پینوست در مسیر موفقیت")
        blog.enter_blog_result()
        print("تمام المان های بخش بلاگ پینوست بررسی شد")

###Blog_add

    def test66_blog_add(self):
        blog = Blog(driver=self.driver)
        findel = FindElement(driver=self.driver)
        blog.enter_blog_add()
        findel.lod_page()
        blog.enter_blog_add_title("Test")
        blog.enter_blog_add_category()
        # blog.enter_blog_add_category_option()
        blog.enter_blog_add_description("description")
        blog.enter_blog_add_content("content")
        # blog.enter_blog_add_submit_form()
        print("تمام المان های بخش اضافه کردن بلاگ پینوست بررسی شد")

###Blog_edit

    def test67_blog_edit(self):
        blog = Blog(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_blog, 'href', '/blog/posts')
        findel.lod_page()
        blog.enter_blog_edit()
        findel.lod_page()
        blog.enter_blog_edit_title("Test")
        blog.enter_blog_edit_category()
        blog.enter_blog_edit_description("description")
        # blog.enter_blog_edit_content("content")
        # blog.enter_blog_edit_submit_form()
        print("تمام المان های بخش ویرایش کردن بلاگ پینوست بررسی شد")

###Blog_categories

    def test68_blog_categories(self):
        blog = Blog(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_blog_categories, 'href', '/blog/categories')
        # blog.enter_click_blog_categories()
        findel.lod_page()
        # assert blog
        blog.enter_blog_categories_assert()
        # blog.enter_blog_categories_result()
        blog.enter_blog_categories_name("Test")
        blog.enter_blog_categories_fa_name("تست")
        blog.enter_blog_categories_submit()
        print("تمام المان های بخش دسته بندی بلاگ و اضافه کردن بلاگ بررسی شد")

###Blog_categories_edit

    def test69_blog_categories_edit(self):
        blog = Blog(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', blog_categories_edit, 'class', 'update_link icon pi-edit cursor_pointer mx-2')
        # blog.enter_blog_categories_edit()
        findel.lod_page()
        blog.enter_blog_categories_edit_name_update("Test")
        blog.enter_blog_categories_edit_fa_name_update("تست")
        sleep(1)
        blog.enter_blog_categories_edit_update_no()
        print("تمام المان های بخش ویرایش کردن دسته بندی بلاگ بررسی شد")

###Blog_categories_delete

    def test70_blog_categories_delete(self):
        blog = Blog(driver=self.driver)
        findel = FindElement(driver=self.driver)
        blog.enter_blog_categories_delete()
        findel.lod_page()
        blog.enter_blog_categories_delete_no()
        self.driver.refresh()
        print("تمام المان های بخش حذف کردن دسته بندی بلاگ بررسی شد")

###Logs_login

    def test71_logs_categories(self):
        logs = Logs(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_logs, 'href', '/logs/login')
        # logs.enter_click_logs()
        findel.lod_page()
        # assert logs
        logs.enter_logs_assert()
        # logs.enter_logs_result()
        print("تمام المان های بخش  گزارشات ورود و خروج")

###nps_categories

    def test72_nps_categories(self):
        nps = Nps(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_nps, 'href', '/nps')
        # nps.enter_click_nps()
        findel.lod_page()
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
        # findel.wait_until_element_has_an_attribute('xpath', nps_description, 'class', 'show_description btn btn-sm text-nowrap btn-primary')
        # nps.enter_nps_description()
        print("تمام المان های بخش nps بررسی شد")

###policy

    def test73_policy(self):
        policy = PolicyPage(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_policy, 'href', '/policy')
        # policy.enter_click_policy()
        findel.lod_page()
        policy.enter_policy_assert()
        print("تمام المان های قوانین و مقررات بررسی شد.")
        policy.enter_policy_show()

    ###faq

    def test74_faq(self):
        faq = Faq(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_faq, 'href', '/faq')
        # faq.enter_click_faq()
        findel.lod_page()
        faq.enter_faq_assert()
        faq.enter_faq_pinvest()
        faq.enter_faq_account()
        faq.enter_faq_investment()
        faq.enter_faq_funds()
        faq.enter_faq_messages()
        print("تمام المان های سوالات متداول بررسی شد.")

    # # # reports_superAdmin

    def test75_reports_superAdmin(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_reports, 'class', 'cursor_pointer')
        # reports.enter_click_reports()
        findel.lod_page()
        # sleep(1)
        # findel.wait_until_element_has_an_attribute('xpath', click_reports_superAdmin, 'href', '/reports/superAdmin')
        reports.enter_click_reports_superAdmin()
        # assert reports
        reports.enter_reports_superAdmin_assert()
        reports.enter_reports_superAdmin_value_report_1()
        reports.enter_reports_superAdmin_value_report_2()
        reports.enter_reports_superAdmin_value_report_3()
        reports.enter_reports_superAdmin_value_report_4()
        reports.enter_reports_superAdmin_report_4_month()
        reports.enter_reports_superAdmin_report_4_month_option()
        reports.enter_reports_superAdmin_report_4_year()
        reports.enter_reports_superAdmin_report_4_year_option()
        reports.enter_reports_superAdmin_report_4_graph()
        reports.enter_reports_superAdmin_report_4_graph()
        vw = self.driver.find_element('xpath', "//*[@id='value_report_7']")
        vw.location_once_scrolled_into_view
        reports.enter_reports_superAdmin_value_report_5()
        findel.lod_page()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_5_month, 'class', 'form-select form-select-sm month_select')
        # reports.enter_reports_superAdmin_report_5_month()
        reports.enter_reports_superAdmin_report_5_month_option()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_5_year, 'class', 'form-select form-select-sm year_select')
        # reports.enter_reports_superAdmin_report_5_year()
        reports.enter_reports_superAdmin_report_5_year_option()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_5_graph, 'class', 'icon pi-account-reports show_chart')
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_5_graph, 'class', 'icon pi-account-reports show_chart')
        # reports.enter_reports_superAdmin_report_5_graph()
        # reports.enter_reports_superAdmin_report_5_graph()
        reports.enter_reports_superAdmin_value_report_6()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_6_month, 'class', 'form-select form-select-sm month_select')
        # reports.enter_reports_superAdmin_report_6_month()
        reports.enter_reports_superAdmin_report_6_month_option()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_6_year, 'class', 'form-select form-select-sm year_select')
        # reports.enter_reports_superAdmin_report_6_year()
        reports.enter_reports_superAdmin_report_6_year_option()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_6_graph, 'class', 'icon pi-account-reports show_chart')
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_6_graph, 'class', 'icon pi-account-reports show_chart')
        # reports.enter_reports_superAdmin_report_6_graph()
        # reports.enter_reports_superAdmin_report_6_graph()
        vw2 = self.driver.find_element('xpath', "//*[@id='value_report_9']")
        vw2.location_once_scrolled_into_view
        reports.enter_reports_superAdmin_value_report_7()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_7_month, 'class', 'form-select form-select-sm month_select')
        # reports.enter_reports_superAdmin_report_7_month()
        reports.enter_reports_superAdmin_report_7_month_option()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_7_year, 'class', 'form-select form-select-sm year_select')
        # reports.enter_reports_superAdmin_report_7_year()
        reports.enter_reports_superAdmin_report_7_year_option()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_7_graph, 'class', 'icon pi-account-reports show_chart')
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_7_graph, 'class', 'icon pi-account-reports show_chart')
        # reports.enter_reports_superAdmin_report_7_graph()
        # reports.enter_reports_superAdmin_report_7_graph()
        reports.enter_reports_superAdmin_value_report_8()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_8_month, 'class', 'form-select form-select-sm month_select')
        # reports.enter_reports_superAdmin_report_8_month()
        reports.enter_reports_superAdmin_report_8_month_option()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_8_year, 'class', 'form-select form-select-sm year_select')
        # reports.enter_reports_superAdmin_report_8_year()
        reports.enter_reports_superAdmin_report_8_year_option()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_8_graph, 'class', 'icon pi-account-reports show_chart')
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_8_graph, 'class', 'icon pi-account-reports show_chart')
        # reports.enter_reports_superAdmin_report_8_graph()
        # reports.enter_reports_superAdmin_report_8_graph()
        reports.enter_reports_superAdmin_value_report_9()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_9_month, 'class', 'form-select form-select-sm month_select')
        # reports.enter_reports_superAdmin_report_9_month()
        reports.enter_reports_superAdmin_report_9_month_option()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_9_year, 'class', 'form-select form-select-sm year_select')
        # reports.enter_reports_superAdmin_report_9_year()
        reports.enter_reports_superAdmin_report_9_year_option()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_9_graph, 'class', 'icon pi-account-reports show_chart')
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_9_graph, 'class', 'icon pi-account-reports show_chart')
        # reports.enter_reports_superAdmin_report_9_graph()
        # reports.enter_reports_superAdmin_report_9_graph()
        vw2 = self.driver.find_element('xpath', "//*[@id='value_report_13']")
        vw2.location_once_scrolled_into_view
        reports.enter_reports_superAdmin_value_report_10()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_10_month, 'class', 'form-select form-select-sm month_select')
        # reports.enter_reports_superAdmin_report_10_month()
        reports.enter_reports_superAdmin_report_10_month_option()
        findel.wait_until_element_has_an_attribute('xpath', reports_superAdmin_report_10_year, 'class', 'form-select form-select-sm year_select')
        # reports.enter_reports_superAdmin_report_10_year()
        reports.enter_reports_superAdmin_report_10_year_option()
        print("المان های بخش گزارشات، گزارشات مدیرکل بررسی شدند.")
    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
