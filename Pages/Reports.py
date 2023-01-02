from time import sleep

from Locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# import org.openqa.selenium.JavascriptExecutor


class Reports:
    def __init__(self, driver):
        self.driver = driver

# # # reports

    def enter_click_reports(self):
        # vi= self.driver.find_element('xpath', click_reports)
        # vi.location_once_scrolled_into_view
        htmll= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_reports)))
        htmll.location_once_scrolled_into_view
        self.driver.find_element('xpath', click_reports).click()

# # # reports_sell_orders

    def enter_click_reports_sell_orders(self):
        html= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_reports_sell_orders)))
        html.location_once_scrolled_into_view
        self.driver.find_element('xpath', click_reports_sell_orders).click()

    def enter_reports_sell_orders_assert(self):
        print("با موفقیت وارد قسمت گزارشات ابطال شد.")

    def enter_reports_sell_orders_from_date(self):
        self.driver.find_element('xpath', reports_sell_orders_from_date).click()

    def enter_reports_sell_orders_from_date_back(self):
        self.driver.find_element('xpath', reports_sell_orders_from_date_back).click()

    def enter_reports_sell_orders_from_date_option(self):
        self.driver.find_element('xpath', reports_sell_orders_from_date_option).click()

    def enter_reports_sell_orders_to_date(self):
        self.driver.find_element('xpath', reports_sell_orders_to_date).click()

    def enter_reports_sell_orders_to_date_next(self):
        self.driver.find_element('xpath', reports_sell_orders_to_date_next).click()

    def enter_reports_sell_orders_to_date_option(self):
        self.driver.find_element('xpath', reports_sell_orders_to_date_option).click()

    def enter_reports_sell_orders_type(self):
        self.driver.find_element('xpath', reports_sell_orders_type).click()

    def enter_reports_sell_orders_type_option(self):
        self.driver.find_element('xpath', reports_sell_orders_type_option).click()

    def enter_reports_sell_orders_fund(self):
        self.driver.find_element('xpath', reports_sell_orders_fund).click()

    def enter_reports_sell_orders_fund_option(self):
        self.driver.find_element('xpath', reports_sell_orders_fund_option).click()

    def enter_reports_sell_orders_status(self):
        self.driver.find_element('xpath', reports_sell_orders_status).click()

    def enter_reports_sell_orders_status_option(self):
        self.driver.find_element('xpath', reports_sell_orders_status_option).click()

    def enter_reports_sell_orders_method(self):
        self.driver.find_element('xpath', reports_sell_orders_method).click()

    def enter_reports_sell_orders_method_option(self):
        self.driver.find_element('xpath', reports_sell_orders_method_option).click()

    def enter_reports_sell_orders_search(self, code):
        self.driver.find_element('xpath', reports_sell_orders_search).send_keys(code)

    def enter_reports_sell_orders_result(self):
        table_id = self.driver.find_element('xpath', reports_sell_orders_result)
        for row in range(1, 2):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

# # # reports_cms_sell_orders
    def wait_until_element_has_an_attribute(self, element_selector, element_locator, attribute, attribute_value, timeout=5):
        for i in range(timeout * 5):
            try:
                element = self.driver.find_element(element_selector, element_locator)
                element.click()
                # if exact:
                #     assert element.get_attribute(attribute) == attribute_value
                # else:
                #     assert attribute_value in element.get_attribute(attribute)
                return
            except:
                sleep(0.2)
        raise Exception("Element attribute is not: " + str(attribute))

    def enter_click_reports_cms_sell_orders(self):
        htmla= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_reports_cms_sell_orders)))
        htmla.location_once_scrolled_into_view
        self.driver.find_element('xpath', click_reports_cms_sell_orders).click()

    def enter_reports_cms_sell_orders_assert(self):
        print("با موفقیت وارد قسمت گزارشات ابطال کارت از پنل شد.")

    def enter_reports_cms_sell_orders_from_date(self):
        self.driver.find_element('xpath', reports_cms_sell_orders_from_date).click()

    def enter_reports_cms_sell_orders_from_date_back(self):
        self.driver.find_element('xpath', reports_cms_sell_orders_from_date_back).click()

    def enter_reports_cms_sell_orders_from_date_option(self):
        self.driver.find_element('xpath', reports_cms_sell_orders_from_date_option).click()

    def enter_reports_cms_sell_orders_to_date(self):
        self.driver.find_element('xpath', reports_cms_sell_orders_to_date).click()

    def enter_reports_cms_sell_orders_to_date_next(self):
        self.driver.find_element('xpath', reports_cms_sell_orders_to_date_next).click()

    def enter_reports_cms_sell_orders_to_date_option(self):
        self.driver.find_element('xpath', reports_cms_sell_orders_to_date_option).click()

    def enter_reports_cms_sell_orders_type(self):
        self.driver.find_element('xpath', reports_cms_sell_orders_type).click()

    def enter_reports_cms_sell_orders_type_option(self):
        self.driver.find_element('xpath', reports_cms_sell_orders_type_option).click()

    def enter_reports_cms_sell_orders_status(self):
        self.driver.find_element('xpath', reports_cms_sell_orders_status).click()

    def enter_reports_cms_sell_orders_status_option(self):
        self.driver.find_element('xpath', reports_cms_sell_orders_status_option).click()

    def enter_reports_cms_sell_orders_search(self, code):
        self.driver.find_element('xpath', reports_cms_sell_orders_search).send_keys(code)

    def enter_reports_cms_sell_orders_result(self):
        table_id = self.driver.find_element('xpath', reports_cms_sell_orders_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_cms_sell_orders_shaba(self):
        self.driver.find_element('xpath', reports_cms_sell_orders_shaba).click()

    def enter_reports_cms_sell_orders_shaba_result(self):
        table_id = self.driver.find_element('xpath', reports_cms_sell_orders_shaba_result)
        for row in range(1, 2):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

# # # reports_superAdmin

    def enter_click_reports_superAdmin(self):
        viewsuperAdmin= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_reports_superAdmin)))
        viewsuperAdmin.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', click_reports_superAdmin).click()

    def enter_reports_superAdmin_assert(self):
        print("با موفقیت وارد قسمت گزارشات مدیرکل شد.")

    def enter_reports_superAdmin_value_report_1(self):
        report_1= self.driver.find_element('xpath', reports_superAdmin_value_report_1).text
        print("تعداد کل کاربران ثبت نام شده", report_1, "است.")

    def enter_reports_superAdmin_value_report_2(self):
        report_2= self.driver.find_element('xpath', reports_superAdmin_value_report_2).text
        print("تعداد کل کاربران صندوق دوم", report_2, "است.")

    def enter_reports_superAdmin_value_report_3(self):
        report_3= self.driver.find_element('xpath', reports_superAdmin_value_report_3).text
        print("تعداد کل کاربرانی که حداقل یک حساب بانکی ثبت شده دارند", report_3, "است.")

    def enter_reports_superAdmin_value_report_4(self):
        report_4= self.driver.find_element('xpath', reports_superAdmin_value_report_4).text
        print("مقدار کل واریز های موفق (ریال)", report_4, "است.")

    def enter_reports_superAdmin_report_4_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_4_month).click()

    def enter_reports_superAdmin_report_4_month_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_4_month_option).click()

    def enter_reports_superAdmin_report_4_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_4_year).click()

    def enter_reports_superAdmin_report_4_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_4_year_option).click()

    def enter_reports_superAdmin_report_4_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_4_graph).click()

    def enter_reports_superAdmin_value_report_5(self):
        report_5= self.driver.find_element('xpath', reports_superAdmin_value_report_5).text
        print("مقدار کل واریز های موفق درگاه آنلاین (ریال)", report_5, "است.")

    def enter_reports_superAdmin_report_5_month(self):
        viewreport5month= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', reports_superAdmin_report_5_month)))
        viewreport5month.location_once_scrolled_into_view
        self.driver.find_element('xpath', reports_superAdmin_report_5_month).click()

    def enter_reports_superAdmin_report_5_month_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_5_month_option).click()

    def enter_reports_superAdmin_report_5_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_5_year).click()

    def enter_reports_superAdmin_report_5_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_5_year_option).click()

    def enter_reports_superAdmin_report_5_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_5_graph).click()

    def enter_reports_superAdmin_value_report_6(self):
        report_6= self.driver.find_element('xpath', reports_superAdmin_value_report_6).text
        print("مقدار کل واریز های موفق حساب های ثبت شده (ریال)", report_6, "است.")

    def enter_reports_superAdmin_report_6_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_6_month).click()

    def enter_reports_superAdmin_report_6_month_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_6_month_option).click()

    def enter_reports_superAdmin_report_6_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_6_year).click()

    def enter_reports_superAdmin_report_6_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_6_year_option).click()

    def enter_reports_superAdmin_report_6_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_6_graph).click()

    def enter_reports_superAdmin_value_report_7(self):
        report_7= self.driver.find_element('xpath', reports_superAdmin_value_report_7).text
        print("مقدار کل واریز های موفق پرداخت با فیش بانکی (ریال)", report_7, "است.")

    def enter_reports_superAdmin_report_7_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_7_month).click()

    def enter_reports_superAdmin_report_7_month_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_7_month_option).click()

    def enter_reports_superAdmin_report_7_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_7_year).click()

    def enter_reports_superAdmin_report_7_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_7_year_option).click()

    def enter_reports_superAdmin_report_7_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_7_graph).click()

    def enter_reports_superAdmin_value_report_8(self):
        report_8= self.driver.find_element('xpath', reports_superAdmin_value_report_8).text
        print("مقدار کل واریز های موفق پرداخت از طریق پوز (ریال)", report_8, "است.")

    def enter_reports_superAdmin_report_8_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_8_month).click()

    def enter_reports_superAdmin_report_8_month_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_8_month_option).click()

    def enter_reports_superAdmin_report_8_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_8_year).click()

    def enter_reports_superAdmin_report_8_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_8_year_option).click()

    def enter_reports_superAdmin_report_8_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_8_graph).click()

    def enter_reports_superAdmin_value_report_9(self):
        report_9= self.driver.find_element('xpath', reports_superAdmin_value_report_9).text
        print("مقدار کل واریز های موفق پرداخت با لینک پرداخت (ریال)", report_9, "است.")

    def enter_reports_superAdmin_report_9_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_9_month).click()

    def enter_reports_superAdmin_report_9_month_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_9_month_option).click()

    def enter_reports_superAdmin_report_9_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_9_year).click()

    def enter_reports_superAdmin_report_9_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_9_year_option).click()

    def enter_reports_superAdmin_report_9_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_9_graph).click()

    def enter_reports_superAdmin_value_report_10(self):
        report_10= self.driver.find_element('xpath', reports_superAdmin_value_report_10).text
        print("مقدار کل سفارشات خرید لینک پرداخت (ریال)", report_10, "است.")

    def enter_reports_superAdmin_report_10_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_10_month).click()

    def enter_reports_superAdmin_report_10_month_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_10_month_option).click()

    def enter_reports_superAdmin_report_10_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_10_year).click()

    def enter_reports_superAdmin_report_10_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_10_year_option).click()

    def enter_reports_superAdmin_report_10_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_10_graph).click()

    # def enter_reports_superAdmin_report_10_fund(self):
    #     self.driver.find_element('xpath', reports_superAdmin_report_10_fund).click()

    def enter_reports_superAdmin_report_11_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_11_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_superAdmin_value_report_11(self):
        report_11= self.driver.find_element('xpath', reports_superAdmin_value_report_11).text
        print("مقدار کل سودهای تقسیم شده (ریال)", report_11, "است.")

    def enter_reports_superAdmin_report_11_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_11_month).click()

    def enter_reports_superAdmin_report_11_month_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_11_month_option).click()

    def enter_reports_superAdmin_report_11_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_11_year).click()

    def enter_reports_superAdmin_report_11_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_11_year_option).click()

    def enter_reports_superAdmin_report_11_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_11_graph).click()

    def enter_reports_superAdmin_value_report_12(self):
        report_12 = self.driver.find_element('xpath', reports_superAdmin_value_report_12).text
        print("تعداد کل حساب های بانکی", report_12, "است.")

    def enter_reports_superAdmin_report_12_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_12_month).click()

    def enter_reports_superAdmin_report_12_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_12_year).click()

    def enter_reports_superAdmin_report_12_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_12_year_option).click()

    def enter_reports_superAdmin_report_12_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_12_graph).click()

    def enter_reports_superAdmin_report_12_fund(self):
        self.driver.find_element('xpath', reports_superAdmin_report_12_fund).click()

    def enter_reports_superAdmin_report_12_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_12_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_superAdmin_value_report_13(self):
        report_13 = self.driver.find_element('xpath', reports_superAdmin_value_report_13).text
        print("ارزش کل دارایی های سپرده شده (ریال)", report_13, "است.")

    def enter_reports_superAdmin_report_13_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_13_month).click()

    def enter_reports_superAdmin_report_13_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_13_year).click()

    def enter_reports_superAdmin_report_13_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_13_year_option).click()

    def enter_reports_superAdmin_report_13_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_13_graph).click()

    def enter_reports_superAdmin_report_13_fund(self):
        self.driver.find_element('xpath', reports_superAdmin_report_13_fund).click()

    def enter_reports_superAdmin_report_13_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_13_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_superAdmin_value_report_14(self):
        report_14 = self.driver.find_element('xpath', reports_superAdmin_value_report_14).text
        print("مقدار کل واحد های صادر شده", report_14, "است.")

    def enter_reports_superAdmin_report_14_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_14_month).click()

    def enter_reports_superAdmin_report_14_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_14_year).click()

    def enter_reports_superAdmin_report_14_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_14_year_option).click()

    def enter_reports_superAdmin_report_14_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_14_graph).click()

    def enter_reports_superAdmin_report_14_fund(self):
        self.driver.find_element('xpath', reports_superAdmin_report_14_fund).click()

    def enter_reports_superAdmin_report_14_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_14_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_superAdmin_value_report_15(self):
        report_15 = self.driver.find_element('xpath', reports_superAdmin_value_report_15).text
        print("مقدار کل واحد های باطل شده", report_15, "است.")

    def enter_reports_superAdmin_report_15_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_15_month).click()

    def enter_reports_superAdmin_report_15_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_15_year).click()

    def enter_reports_superAdmin_report_15_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_15_year_option).click()

    def enter_reports_superAdmin_report_15_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_15_graph).click()

    def enter_reports_superAdmin_report_15_fund(self):
        self.driver.find_element('xpath', reports_superAdmin_report_15_fund).click()

    def enter_reports_superAdmin_report_15_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_15_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_superAdmin_value_report_16(self):
        report_16 = self.driver.find_element('xpath', reports_superAdmin_value_report_16).text
        print("مقدار کل کارمزد محاسبه شده", report_16, "است.")

    def enter_reports_superAdmin_report_16_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_16_month).click()

    def enter_reports_superAdmin_report_16_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_16_year).click()

    def enter_reports_superAdmin_report_16_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_16_year_option).click()

    def enter_reports_superAdmin_report_16_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_16_graph).click()

    def enter_reports_superAdmin_report_16_fund(self):
        self.driver.find_element('xpath', reports_superAdmin_report_16_fund).click()

    def enter_reports_superAdmin_report_16_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_16_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_superAdmin_value_report_17(self):
        report_17 = self.driver.find_element('xpath', reports_superAdmin_value_report_17).text
        print("مقدار کل کارمزد متعلق به پینوست", report_17, "است.")

    def enter_reports_superAdmin_report_17_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_17_month).click()

    def enter_reports_superAdmin_report_17_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_17_year).click()

    def enter_reports_superAdmin_report_17_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_17_year_option).click()

    def enter_reports_superAdmin_report_17_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_17_graph).click()

    def enter_reports_superAdmin_report_17_fund(self):
        self.driver.find_element('xpath', reports_superAdmin_report_17_fund).click()

    def enter_reports_superAdmin_report_17_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_17_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_superAdmin_value_report_18(self):
        report_18 = self.driver.find_element('xpath', reports_superAdmin_value_report_18).text
        print("مقدار کل کارمزد توزیع شده", report_18, "است.")

    def enter_reports_superAdmin_report_18_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_18_month).click()

    def enter_reports_superAdmin_report_18_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_18_year).click()

    def enter_reports_superAdmin_report_18_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_18_year_option).click()

    def enter_reports_superAdmin_report_18_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_18_graph).click()

    def enter_reports_superAdmin_report_18_fund(self):
        self.driver.find_element('xpath', reports_superAdmin_report_18_fund).click()

    def enter_reports_superAdmin_report_18_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_18_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_superAdmin_value_report_19(self):
        report_19 = self.driver.find_element('xpath', reports_superAdmin_value_report_19).text
        print("تعداد کل سفارشات خرید", report_19, "است.")

    def enter_reports_superAdmin_report_19_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_19_month).click()

    def enter_reports_superAdmin_report_19_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_19_year).click()

    def enter_reports_superAdmin_report_19_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_19_year_option).click()

    def enter_reports_superAdmin_report_19_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_19_graph).click()

    def enter_reports_superAdmin_report_19_fund(self):
        self.driver.find_element('xpath', reports_superAdmin_report_19_fund).click()

    def enter_reports_superAdmin_report_19_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_19_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_superAdmin_value_report_20(self):
        report_20 = self.driver.find_element('xpath', reports_superAdmin_value_report_20).text
        print("تعداد کل سفارشات فروش", report_20, "است.")

    def enter_reports_superAdmin_report_20_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_20_month).click()

    def enter_reports_superAdmin_report_20_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_20_year).click()

    def enter_reports_superAdmin_report_20_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_20_year_option).click()

    def enter_reports_superAdmin_report_20_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_20_graph).click()

    def enter_reports_superAdmin_report_20_fund(self):
        self.driver.find_element('xpath', reports_superAdmin_report_20_fund).click()

    def enter_reports_superAdmin_report_20_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_20_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_superAdmin_value_report_21(self):
        report_21 = self.driver.find_element('xpath', reports_superAdmin_value_report_21).text
        print("مقدار کل سفارشات خرید", report_21, "است.")

    def enter_reports_superAdmin_report_21_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_21_month).click()

    def enter_reports_superAdmin_report_21_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_21_year).click()

    def enter_reports_superAdmin_report_21_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_21_year_option).click()

    def enter_reports_superAdmin_report_21_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_21_graph).click()

    def enter_reports_superAdmin_report_21_fund(self):
        self.driver.find_element('xpath', reports_superAdmin_report_21_fund).click()

    def enter_reports_superAdmin_report_21_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_21_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_superAdmin_value_report_22(self):
        report_22 = self.driver.find_element('xpath', reports_superAdmin_value_report_22).text
        print("مقدار کل سفارشات فروش", report_22, "است.")

    def enter_reports_superAdmin_report_22_month(self):
        self.driver.find_element('xpath', reports_superAdmin_report_22_month).click()

    def enter_reports_superAdmin_report_22_year(self):
        self.driver.find_element('xpath', reports_superAdmin_report_22_year).click()

    def enter_reports_superAdmin_report_22_year_option(self):
        self.driver.find_element('xpath', reports_superAdmin_report_22_year_option).click()

    def enter_reports_superAdmin_report_22_graph(self):
        self.driver.find_element('xpath', reports_superAdmin_report_22_graph).click()

    def enter_reports_superAdmin_report_22_fund(self):
        self.driver.find_element('xpath', reports_superAdmin_report_22_fund).click()

    def enter_reports_superAdmin_report_22_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_superAdmin_report_22_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

# # # reports_providers

    def enter_click_reports_providers(self):
        viewproviders= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_reports_providers)))
        viewproviders.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', click_reports_providers).click()

    def enter_reports_providers_assert(self):
        print("با موفقیت وارد قسمت گزارشات تامین کنندگان شد.")

    def enter_reports_providers_value_report_1(self):
        report_1 = self.driver.find_element('xpath', reports_providers_value_report_1).text
        print("تعداد کل تراکنش های درگاه آنلاین", report_1, "است.")

    def enter_reports_providers_report_1_month(self):
        self.driver.find_element('xpath', reports_providers_report_1_month).click()

    def enter_reports_providers_report_1_year(self):
        self.driver.find_element('xpath', reports_providers_report_1_year).click()

    def enter_reports_providers_report_1_year_option(self):
        self.driver.find_element('xpath', reports_providers_report_1_year_option).click()

    def enter_reports_providers_report_1_graph(self):
        self.driver.find_element('xpath', reports_providers_report_1_graph).click()

    def enter_reports_providers_report_1_fund(self):
        self.driver.find_element('xpath', reports_providers_report_1_fund).click()

    def enter_reports_providers_report_1_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_providers_report_1_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_reports_providers_value_report_2(self):
        report_2 = self.driver.find_element('xpath', reports_providers_value_report_2).text
        print("تعداد کل تراکنش های دایرکت دبیت", report_2, "است.")

    def enter_reports_providers_report_2_month(self):
        self.driver.find_element('xpath', reports_providers_report_2_month).click()

    def enter_reports_providers_report_2_month_option(self):
        self.driver.find_element('xpath', reports_providers_report_2_month_option).click()

    def enter_reports_providers_report_2_year(self):
        self.driver.find_element('xpath', reports_providers_report_2_year).click()

    def enter_reports_providers_report_2_year_option(self):
        self.driver.find_element('xpath', reports_providers_report_2_year_option).click()

    def enter_reports_providers_report_2_graph(self):
        self.driver.find_element('xpath', reports_providers_report_2_graph).click()

    def enter_reports_providers_report_2_fund(self):
        self.driver.find_element('xpath', reports_providers_report_2_fund).click()

    def enter_reports_providers_report_2_fund_result(self):
        table_id = self.driver.find_element('xpath', reports_providers_report_2_fund_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

# # # reports_cards_daily

    def enter_click_reports_cards_daily(self):
        viewcards= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_reports_cards_daily)))
        viewcards.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', click_reports_cards_daily).click()

    def enterreports_cards_daily_assert(self):
        print("با موفقیت وارد قسمت گزارشات روزانه کارت‌ها شد.")

    def enter_reports_cards_daily_date(self):
        self.driver.find_element('xpath', reports_cards_daily_date).click()

    def enter_reports_cards_daily_date_back(self):
        self.driver.find_element('xpath', reports_cards_daily_date_back).click()

    def enter_reports_cards_daily_date_option(self):
        self.driver.find_element('xpath', reports_cards_daily_date_option).click()

    def enter_reports_cards_daily_result(self):
        table_id = self.driver.find_element('xpath', reports_cards_daily_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

# # #reports_users_invited

    def enter_click_reports_users_invited(self):
        viewinvited= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_reports_users_invited)))
        viewinvited.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', click_reports_users_invited).click()

    def enter_reports_users_invited_assert(self):
        print("با موفقیت وارد قسمت گزارش تعداد کاربران دعوت شده شد.")

    def enter_reports_users_invited_from_date(self):
        self.driver.find_element('xpath', reports_users_invited_from_date).click()

    def enter_reports_users_invited_from_date_back(self):
        self.driver.find_element('xpath', reports_users_invited_from_date_back).click()

    def enter_reports_users_invited_from_date_option(self):
        self.driver.find_element('xpath', reports_users_invited_from_date_option).click()

    def enter_reports_users_invited_to_date(self):
        self.driver.find_element('xpath', reports_users_invited_to_date).click()

    def enter_reports_users_invited_to_date_next(self):
        self.driver.find_element('xpath', reports_users_invited_to_date_next).click()

    def enter_reports_users_invited_to_date_option(self):
        self.driver.find_element('xpath', reports_users_invited_to_date_option).click()

    def enter_reports_users_invited_phone_search(self, code):
        self.driver.find_element('xpath', reports_users_invited_phone_search).send_keys(code)

    def enter_reports_users_invited_phone_search_result(self):
        table_id = self.driver.find_element('xpath', reports_users_invited_phone_search_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

# # # reports_users_invited_name_search

    def enter_reports_users_invited_name_search(self, name):
        self.driver.find_element('xpath', reports_users_invited_name_search).send_keys(name)


# # #reports_users_buy_sell_search_phon

    def enter_click_reports_users_buy_sell(self):
        viewbuysell= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_reports_users_buy_sell)))
        viewbuysell.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', click_reports_users_buy_sell).click()

    def enter_reports_users_buy_sell_assert(self):
        print("با موفقیت وارد قسمت گزارش تعداد کاربران دعوت شده شد.")

    def enter_reports_users_buy_sell_from_date(self):
        self.driver.find_element('xpath', reports_users_buy_sell_from_date).click()

    def enter_reports_users_buy_sell_from_date_back(self):
        self.driver.find_element('xpath', reports_users_buy_sell_from_date_back).click()

    def enter_reports_users_buy_sell_from_date_option(self):
        self.driver.find_element('xpath', reports_users_buy_sell_from_date_option).click()

    def enter_reports_users_buy_sell_to_date(self):
        self.driver.find_element('xpath', reports_users_buy_sell_to_date).click()

    def enter_reports_users_buy_sell_to_date_next(self):
        self.driver.find_element('xpath', reports_users_buy_sell_to_date_next).click()

    def enter_reports_users_buy_sell_to_date_option(self):
        self.driver.find_element('xpath', reports_users_buy_sell_to_date_option).click()

    def enter_reports_users_buy_sell_btn_sale(self):
        self.driver.find_element('xpath', reports_users_buy_sell_btn_sale).click()

    def enter_reports_users_buy_sell_phone_search(self, code):
        self.driver.find_element('xpath', reports_users_buy_sell_phone_search).send_keys(code)

    def enter_reports_users_buy_sell_phone_search_result(self):
        table_id = self.driver.find_element('xpath', reports_users_buy_sell_phone_search_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

# # # reports_users_buy_sell_name_search

    def enter_reports_users_buy_sell_name_search(self, name):
        self.driver.find_element('xpath', reports_users_buy_sell_name_search).send_keys(name)

# # #reports_disabled_accounts

    def enter_click_reports_disabled_accounts(self):
        viewaccounts= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_reports_disabled_accounts)))
        viewaccounts.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', click_reports_disabled_accounts).click()

    def enter_reports_disabled_accounts_assert(self):
        print("با موفقیت وارد قسمت حساب های غیرفعال یا حذف شده شد.")

    def enter_reports_disabled_accounts_from_date(self):
        self.driver.find_element('xpath', reports_disabled_accounts_from_date).click()

    def enter_reports_disabled_accounts_from_date_back(self):
        self.driver.find_element('xpath', reports_disabled_accounts_from_date_back).click()

    def enter_reports_disabled_accounts_from_date_option(self):
        self.driver.find_element('xpath', reports_disabled_accounts_from_date_option).click()

    def enter_reports_disabled_accounts_to_date(self):
        self.driver.find_element('xpath', reports_disabled_accounts_to_date).click()

    def enter_reports_disabled_accounts_to_date_next(self):
        self.driver.find_element('xpath', reports_disabled_accounts_to_date_next).click()

    def enter_reports_disabled_accounts_to_date_option(self):
        self.driver.find_element('xpath', reports_disabled_accounts_to_date_option).click()

    def enter_reports_disabled_accounts_phone_search(self, code):
        self.driver.find_element('xpath', reports_disabled_accounts_phone_search).send_keys(code)

    def enter_reports_disabled_accounts_phone_search_result(self):
        table_id = self.driver.find_element('xpath', reports_disabled_accounts_search_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)