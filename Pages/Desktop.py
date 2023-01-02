from Locators import *


class Desktop:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_desktop(self):
        self.driver.find_element('xpath', click_desktop).click()

    def enter_desktop_show(self):
        assert_desktop_show= self.driver.find_element('xpath', desktop_show).text
        assert assert_desktop_show== "کل کارمزد ساخته شده من"
        print("شما با موفقیت وارد میز کار پینوست شدید ")

    def enter_desktop_sub_percent(self):
        desktop_sub_percent_show= self.driver.find_element('xpath', desktop_sub_percent).text
        print("درصد ارزش دارایی زیرمجموعه: ", desktop_sub_percent_show, "است.")

    def enter_desktop_sub_value(self):
        desktop_sub_value_show= self.driver.find_element('xpath', desktop_sub_value).text
        print("مقدار ارزش دارایی زیرمجموعه: ", desktop_sub_value_show, "است.")

    def enter_desktop_sub_active_units(self):
        desktop_sub_active_units_show= self.driver.find_element('xpath', desktop_sub_active_units).text
        print("تعداد واحد فعال از صندوق: ", desktop_sub_active_units_show, "است.")

    def enter_desktop_sub_price_unit(self):
        desktop_sub_price_unit_show= self.driver.find_element('xpath', desktop_sub_price_unit).text
        print("ارزش هر واحد: ", desktop_sub_price_unit_show, "است.")

    def enter_desktop_all_users(self):
        desktop_all_users_show= self.driver.find_element('xpath', desktop_all_users).text
        print("معرف های زیر مجموعه: ", desktop_all_users_show, "است.")

    def enter_desktop_direct_customers(self):
        desktop_direct_customers_show= self.driver.find_element('xpath', desktop_direct_customers).text
        print("مشتریان مستقیم: ", desktop_direct_customers_show, "است.")

    def enter_desktop_indirect_customers(self):
        desktop_indirect_customers_show= self.driver.find_element('xpath', desktop_indirect_customers).text
        print("مشتریان غیرمستقیم: ", desktop_indirect_customers_show, "است.")
