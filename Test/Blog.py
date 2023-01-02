from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Locators import click_blog
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

# # # blog

    def test02_blog(self):
        blog= Blog(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_blog, 'href', '/blog/posts')
        # blog.enter_click_blog()
        # assert blog
        blog.enter_blog_assert()
        blog.enter_blog_category()
        blog.enter_blog_category_option()
        blog.enter_blog_search("پینوست در مسیر موفقیت")
        blog.enter_blog_result()
        print("تمام المان های بخش بلاگ پینوست بررسی شد")


###Blog_add

    def test03_blog_add(self):
        blog = Blog(driver=self.driver)
        blog.enter_blog_add()
        blog.enter_blog_add_title("Test")
        blog.enter_blog_add_category()
        # blog.enter_blog_add_category_option()
        blog.enter_blog_add_description("description")
        blog.enter_blog_add_content("content")
        # blog.enter_blog_add_submit_form()
        print("تمام المان های بخش اضافه کردن بلاگ پینوست بررسی شد")

###Blog_edit

    def test03_blog_edit(self):
        blog = Blog(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_blog, 'href', '/blog/posts')
        blog.enter_blog_edit()
        blog.enter_blog_edit_title("Test")
        blog.enter_blog_edit_category()
        blog.enter_blog_edit_description("description")
        # blog.enter_blog_edit_content("content")
        # blog.enter_blog_edit_submit_form()
        print("تمام المان های بخش ویرایش کردن بلاگ پینوست بررسی شد")


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
