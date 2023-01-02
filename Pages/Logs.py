from Locators import *


class Logs:
    def __init__(self, driver):
        self.driver = driver

###Logs_login

    def enter_click_logs(self):
        self.driver.find_element('xpath', click_logs).click()

    def enter_logs_assert(self):
        print("با موفقیت وارد قسمت گزارشات ورود و خروج شد.")

    def enter_logs_result(self):
        table_id = self.driver.find_element('xpath', logs_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

