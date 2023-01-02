from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
from Pages.Login import LoginPage
from Pages.Jobs import Jobs

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

# # # jobs

    def test02_jobs(self):
        jobs= Jobs(driver=self.driver)
        sleep(1)
        jobs.enter_click_jobs()
        # assert jobs
        jobs.enter_jobs_assert()
        jobs.enter_jobs_fund()
        jobs.enter_jobs_fund_option()
        jobs.enter_jobs_config_rayanBuy()
        jobs.enter_jobs_config_WithdrawJob()
        jobs.enter_jobs_config_updatesOrdersStatus()
        jobs.enter_jobs_national("1234567890")
        jobs.enter_jobs_config_withdrawWithNationalCode()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
