from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Locators import click_blog, click_blog_categories, blog_categories_edit
from Pages.Find_Element import FindElement
from Pages.Login import LoginPage
from Pages.Blog import Blog


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

###Blog_categories

    def test02_blog_categories(self):
        blog= Blog(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_blog_categories, 'href', '/blog/categories')
        # blog.enter_click_blog_categories()
        # assert blog
        blog.enter_blog_categories_assert()
        blog.enter_blog_categories_result()
        blog.enter_blog_categories_name("Test")
        blog.enter_blog_categories_fa_name("تست")
        blog.enter_blog_categories_submit()
        print("تمام المان های بخش دسته بندی بلاگ و اضافه کردن بلاگ بررسی شد")


###Blog_categories_edit

    def test03_blog_categories_edit(self):
        blog = Blog(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', blog_categories_edit, 'class', 'update_link icon pi-edit cursor_pointer mx-2')
        # blog.enter_blog_categories_edit()
        blog.enter_blog_categories_edit_name_update("Test")
        blog.enter_blog_categories_edit_fa_name_update("تست")
        blog.enter_blog_categories_edit_update_no()
        print("تمام المان های بخش ویرایش کردن دسته بندی بلاگ بررسی شد")

###Blog_categories_delete

    def test04_blog_categories_delete(self):
        blog = Blog(driver=self.driver)
        blog.enter_blog_categories_delete()
        blog.enter_blog_categories_delete_no()
        self.driver.refresh()
        print("تمام المان های بخش حذف کردن دسته بندی بلاگ بررسی شد")


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
