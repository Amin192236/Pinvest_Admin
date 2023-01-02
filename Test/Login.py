from selenium import webdriver
from time import sleep
from Pages.Login import LoginPage
import unittest


driver = webdriver.Chrome(executable_path="E:\PRG_Test\Pinvest_Admin\chromedriver.exe")



class Test_Pinvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # cls.driver = webdriver.Chrome(service=s, options=o)
        cls.driver = driver
        cls.driver.maximize_window()
        # cls.set_window_size(1000, 1000)
        cls.driver.implicitly_wait(3)
        # cls.driver.execute_script("document.body.style.zoom='80 %'")


    def test01_login_register(self):
        self.driver.get("https://admin-ha1.pinvest.ir/signin")
        login = LoginPage(driver=self.driver)
        login.enter_username("superadmin")
        login.enter_password("1234kaKA!")
        login.enter_show_password()
        login.enter_btn_submit()
        sleep(3)
        login.enter_site_header()
        login.enter_logout()
        login.enter_logout_no()
        # login.enter_logout()
        # login.enter_logout_yes()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
