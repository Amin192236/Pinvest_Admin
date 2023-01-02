from Locators import *


class Blog:
    def __init__(self, driver):
        self.driver = driver

###Blog

    def enter_click_blog(self):
        self.driver.find_element('xpath', click_blog).click()

    def enter_blog_assert(self):
        print("با موفقیت وارد قسمت بلاگ پینوست شد.")

    def enter_blog_category(self):
        self.driver.find_element('xpath', blog_category).click()

    def enter_blog_category_option(self):
        self.driver.find_element('xpath', blog_category_option).click()

    def enter_blog_search(self, name):
        self.driver.find_element('xpath', blog_search).send_keys(name)

    def enter_blog_result(self):
        table_id = self.driver.find_element('xpath', blog_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)


###Blog_add

    def enter_blog_add(self):
        self.driver.find_element('xpath', blog_add).click()

    def enter_blog_add_title(self, name):
        self.driver.find_element('xpath', blog_add_title).send_keys(name)

    def enter_blog_add_category(self):
        self.driver.find_element('xpath', blog_add_category).click()

    def enter_blog_add_category_option(self):
        self.driver.find_element('xpath', blog_add_category_option).click()

    def enter_blog_add_description(self, description):
        self.driver.find_element('xpath', blog_add_description).send_keys(description)

    def enter_blog_add_content(self, content):
        self.driver.find_element('xpath', blog_add_content).send_keys(content)

    def enter_blog_add_submit_form(self):
        self.driver.find_element('xpath', blog_add_submit_form).click()

###Blog_edit

    def enter_blog_edit(self):
        self.driver.find_element('xpath', blog_edit).click()

    def enter_blog_edit_title(self, name):
        self.driver.find_element('xpath', blog_edit_title).send_keys(name)

    def enter_blog_edit_category(self):
        self.driver.find_element('xpath', blog_edit_category).click()

    def enter_blog_edit_description(self, description):
        self.driver.find_element('xpath', blog_edit_description).send_keys(description)

    def enter_blog_edit_content(self, content):
        self.driver.find_element('xpath', blog_edit_content).send_keys(content)

    def enter_blog_edit_submit_form(self):
        self.driver.find_element('xpath', blog_edit_submit_form).click()

###Blog_categories

    def enter_click_blog_categories(self):
        self.driver.find_element('xpath', click_blog_categories).click()

    def enter_blog_categories_assert(self):
        print("با موفقیت وارد قسمت بلاگ پینوست شد.")

    def enter_blog_categories_result(self):
        table_id = self.driver.find_element('xpath', blog_categories_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_blog_categories_name(self, name):
        self.driver.find_element('xpath', blog_categories_name).send_keys(name)

    def enter_blog_categories_fa_name(self, name):
        self.driver.find_element('xpath', blog_categories_fa_name).send_keys(name)

    def enter_blog_categories_submit(self):
        self.driver.find_element('xpath', blog_categories_submit).click()

###Blog_categories_edit

    def enter_blog_categories_edit(self):
        self.driver.find_element('xpath', blog_categories_edit).click()

    def enter_blog_categories_edit_name_update(self, name):
        self.driver.find_element('xpath', blog_categories_edit_name_update).send_keys(name)

    def enter_blog_categories_edit_fa_name_update(self, name):
        self.driver.find_element('xpath', blog_categories_edit_fa_name_update).send_keys(name)

    def enter_blog_categories_edit_update_no(self):
        self.driver.find_element('xpath', blog_categories_edit_update_no).click()

###Blog_categories_delete

    def enter_blog_categories_delete(self):
        self.driver.find_element('xpath', blog_categories_delete).click()

    def enter_blog_categories_delete_no(self):
        self.driver.find_element('xpath', blog_categories_delete_no).click()
