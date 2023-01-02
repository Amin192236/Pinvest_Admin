from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Pages.Roles import Roles
from Pages.Login import LoginPage

import unittest

# o = Options()
# o.add_argument('--no-sandbox')
#
# s = Service('d:\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="chromedriver.exe")


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
        print("عملیات ورود با موفقیت انجام شد.")
# # # Roles_Add

    def test02_roles_add(self):
        roles = Roles(driver=self.driver)
        roles.enter_click_roles()
        roles.enter_roles_assert()
        roles.enter_roles_add()
        roles.enter_roles_add_donat_save()
        roles.enter_roles_add()
        roles.enter_roles_add_name("Test")
        roles.enter_roles_add_permission1()
        roles.enter_roles_add_permission2()
        roles.enter_roles_add_permission3()
        roles.enter_roles_add_access_role_id()
        roles.enter_roles_add_permission_all()
        roles.enter_roles_add_save_role_button()
        print("نقش مورد نظر ایجاد شد")

# # # Roles_edit

    def test03_roles_edit(self):
        roles = Roles(driver=self.driver)
        roles.enter_click_roles()
        roles.enter_roles_edit()
        sleep(2)
        roles.enter_roles_add_permission1()
        roles.enter_roles_add_permission2()
        roles.enter_roles_add_permission3()
        roles.enter_roles_edit_button()
        print("نقش مورد نظر ویرایش شد")

# # # Roles_delete

    def test04_roles_delete(self):
        roles = Roles(driver=self.driver)
        roles.enter_click_roles()
        roles.enter_roles_delete()
        roles.enter_roles_delete_no()
        roles.enter_roles_delete()
        roles.enter_roles_delete_button()
        print("نقش مورد نظر حذف شد")


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
