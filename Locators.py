#Login

username="//*[@id='username']"
password="//*[@id='password']"
show_password="//*[@id='signin_form']/div/div[1]/div/div[2]/div/div/div[1]/i[2]"
btn_submit="//*[@id='btn_submit']"
site_header="//*[@id='app']/div/div[2]/div[2]/div[1]/div/div/span[1]"
logout="//*[@id='logout_btn']"
logout_no="//*[@id='confirm_logout_modal']/div/div/div[2]/button[1]"
logout_yes="//*[@id='confirm_logout_modal']/div/div/div[2]/button[2]"

# desktop

click_desktop= "//*[@id='desktop_sidebar']/ul/li[1]"
desktop_show= "//*[@id='app']/div/div[2]/div[2]/div[1]/div/div/span[1]"
desktop_fund= "//*[@id='fund']"
desktop_fund_option= "//*[@id='fund']/option[2]"
desktop_sub_percent= "//*[@id='sub_percent']"
desktop_sub_value= "//*[@id='sub_value']"
desktop_sub_active_units= "//*[@id='sub_active_units']"
desktop_sub_price_unit= "//*[@id='sub_price_unit']"
desktop_all_users= "//*[@id='all_users']"
desktop_direct_customers= "//*[@id='direct_customers']"
desktop_indirect_customers= "//*[@id='indirect_customers']"

# customers_search

click_customers= "//*[@id='desktop_sidebar']/ul/li[2]"
customers_show= "//*[@id='fund']/option[1]"
customers_fund= "//*[@id='fund']"
customers_fund_option= "//*[@id='fund']/option[2]"
customers_from_date= "//*[@id='filter_from_date_dp']"
# customers_from_date= "//*[@id='app']/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/label"
customers_from_date_before= "//*[@id='plotId']/div[1]/div[3]"
# customers_from_date_before= "/html/body/div[6]/div/div[1]/div[3]"
customers_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[3]/td[4]"
customers_to_date= "//*[@id='filter_to_date_dp']"
customers_to_date_next= "/html/body/div[7]/div/div[1]/div[1]"
customers_to_date_option= "/html/body/div[7]/div/div[2]/div/div/table/tbody/tr[5]/td[1]"
customers_phone_search= "//*[@id='search']"
customers_name_search= "//*[@id='name_search']"
customers_phone_search_result= "//table[@class='responsive dataTable no-footer']"
customers_search_direct= "//*[@id='app']/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/label[2]"
customers_search_indirect= "//*[@id='app']/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/label[1]"

# customers_show_account

customers_referral= "//*[@id='referral']"
customers_referral_option= "//*[@value='qYw7EXOvolWRApNmaZ0P']"
customers_show_account= "//*[@id='customers_table']/tbody/tr[2]/td[6]/a"
customers_show_account_name= "//*[@id='customer_name']"

# customers_show_funds

customers_show_funds= "//*[@id='customers_table']/tbody/tr[2]/td[6]/a"
customers_show_funds_name= "//*[@id='customer_name']"

# # # Roles_Add

click_roles= "//*[@id='desktop_sidebar']/ul/li[3]"
roles_add= "//*[@id='app']/div/div[2]/div[2]/div[1]/div/div/div/div[2]/a"
roles_add_name= "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div[1]/div/div/input"
roles_add_permission_all= "//*[@id='permissions_table']/thead/tr/th[1]/a"
roles_add_permission1= "//*[@id='permissions_table']/tbody/tr[1]/td[1]/div/input"
roles_add_permission2= "//*[@id='permissions_table']/tbody/tr[6]/td[1]/div/input"
roles_add_access_role_id= "//*[@id='access_role_id']/option[1]"
roles_add_permission3= "//*[@id='permissions_table']/tbody/tr[129]/td[1]/div/input"
roles_add_donat_save= "//*[@id='save_role_form']/div[2]/div/div/div/div/div/a"
roles_add_save_role_button= "//*[@id='save_role_button']"

# # # Roles_edit

# roles_table= "//*[@id='roles_table']/tbody/tr/td[text()='Test']"
roles_edit= "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr/td[3]/a"
roles_edit_button= "//*[@id='edit_role_button']"

# # # Roles_delete

roles_delete= "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[4]/a"
roles_delete_no= "//*[@id='deleteRole']/div/div/div[2]/button[1]"
roles_delete_button= "//*[@id='delete_role_button']"

# # # users_add

click_users= "//*[@id='desktop_sidebar']/ul/li[4]/a"
users_add= "//*[@id='app']/div/div[2]/div[2]/div[1]/div/div/div/div[2]/a"
users_type= "//*[@id='type']"
users_type_option= "//*[@id='type']/option[2]"
users_first_name= "//*[@id='first_name']"
users_last_name= "//*[@id='last_name']"
users_national_code= "//*[@id='national_code']"
users_phone_number= "//*[@id='msisdn']"
users_username= "//*[@id='username']"
users_password= "//*[@id='password']"
users_password_confirmation= "//*[@id='password_confirmation']"
users_role_id= "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div[1]/div/div[9]/div/select"
users_role_option= "//*[@id='role_id']/option[12]"
users_parent= "//*[@id='parent']"
users_shaba_number= "//*[@id='shaba_number']"
users_bank_id= "//*[@id='bank_id']"
# users_bank_id= "//*[@id='save_user_form']/div[1]/div/div/div[2]/div[1]/div/div[12]/div/div"
users_bank_option= "//*[@id='bank_id']/option[6]"
users_cac= "//*[@id='cac']"
users_address= "//*[@id='address']"
users_save_no= "//*[@id='save_user_form']/div[2]/div/div/div/div/div/a"
users_save_user_button= "//*[@id='save_user_button']"

# # # users_edit

# users_edit= "//*[@id='users_table']/tbody/tr[1]/td[7]/a"
users_edit= "//*[@id='users_table']/tbody/tr[1]/td[7]/a/i"
users_edit_assert= "//*[@id='save_user_form']/div[1]/div/div/div[1]"
users_edit_national_code= "//*[@id='national_code']"
users_edit_username= "//*[@id='username']"
users_edit_first_name= "//*[@id='first_name']"
users_edit_last_name= "//*[@id='last_name']"
users_edit_phone_number= "//*[@id='msisdn']"
users_edit_parent= "//*[@id='parent']"
users_edit_role= "//*[@id='role']"
users_edit_role_option= "//*[@id='role']/option[2]"
users_edit_shaba= "//*[@id='shaba']"
users_edit_bank= "//*[@id='bank']"
users_edit_bank_option= "//*[@id='bank']/option[4]"
users_edit_address= "//*[@id='address']"
users_edit_save_no= "//*[@id='save_user_form']/div[2]/div/div/div/div/div/a"
users_edit_save_user_button= "//*[@id='save_user_button']"

# # # change_password

users_change_password= "//*[@id='users_table']/tbody/tr[1]/td[8]"
# users_change_password= "/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div[1]/div[3]/div/div/div/table/tbody/tr[1]/td[8]"
users_change_password_assert= "//*[@id='change_password_modal']/div/div/div/span"
users_change_password_new= "//*[@id='new_password']"
users_change_password_show= "//*[@id='change_password_form']/div[1]/div/div/div[1]/div/div/div[1]/i[2]"
users_change_password_confirmation= "//*[@id='new_password_confirmation']"
users_change_password_confirmation_show= "//*[@id='change_password_form']/div[1]/div/div/div[2]/div/div/div/i[2]"
users_change_password_no= "//*[@id='change_password_form']/div[2]/button[1]"
users_change_password_yes= "//*[@id='change_password_confirm']"

# # # users_deactivation_activation

# users_deactivation= "//*[@id='users_table']/tbody/tr[1]/td[9]"
users_deactivation= "/html/body/div[1]/div/div[2]/div[2]/div[3]/div/div[1]/div[3]/div/div/div/table/tbody/tr[1]/td[7]"
users_deactivation_assert= "//*[@id='id_text_modal']"
users_deactivation_no= "/html/body/div[3]/div/div/div[2]/button[1]"
users_deactivation_yes= "//*[@id='delete_user_button']"

# # # users_search

users_search_role= "//*[@id='role']"
users_search_role_option= "//*[@id='role']/option[1]"
users_search_from_date= "//*[@id='filter_from_date_dp']"
users_search_from_date_back= "//*[@id='plotId']/div[1]/div[3]"
users_search_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[2]/td[4]"
users_search_to_date= "//*[@id='filter_to_date_dp']"
users_search_to_date_next= "/html/body/div[8]/div/div[1]/div[1]"
users_search_to_date_option= "/html/body/div[8]/div/div[2]/div/div/table/tbody/tr[5]/td[1]"
users_search_code= "//*[@id='search']"
users_search_result= "//*[@id='users_table']"
users_search_direct= "//*[@id='app']/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/label[2]"
users_search_indirect= "//*[@id='app']/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div/label[1]"
users_search_name= "//*[@id='name_search']"

# # # transactions

click_transactions= "//*[@id='desktop_sidebar']/ul/li[5]"
transactions_from_date= "//*[@id='filter_from_date_dp']"
transactions_from_date_back= "//*[@id='plotId']/div[1]/div[3]"
transactions_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[2]/td[4]"
transactions_to_date= "//*[@id='filter_to_date_dp']"
transactions_to_date_next= "/html/body/div[6]/div/div[1]/div[1]"
transactions_to_date_option= "/html/body/div[6]/div/div[2]/div/div/table/tbody/tr[5]/td[1]"
transactions_status= "//*[@id='status']"
transactions_status_option= "//*[@id='status']/option[1]"
transactions_fund= "//*[@id='fund_select']"
transactions_fund_option= "//*[@id='fund_select']/option[1]"
transactions_method= "//*[@id='method']"
transactions_method_option= "//*[@id='method']/option[1]"
transactions_trace_id_search= "//*[@id='trace_id_search']"
transactions_select_all= "//*[@id='app']/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div/div"
transactions_result= "//*[@id='transactions_table']/thead/tr/th[1]/input"
# transactions_select_option= "//*[@id='transactions_table']/tbody/tr[1]/td[1]/input"
transactions_select_option= "/html/body/div[1]/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div/div/div/table/tbody/tr[1]/td[1]/input"
transactions_approve= "//*[@id='approve_multi_select']"
transactions_reject= "//*[@id='reject_multi_select']"

# # # transactions_reject_reason

transactions_reject_reason= "//*[@id='reject_reason']"
transactions_reject_reason_option= "//*[@id='reject_reason']/option[2]"
transactions_reject_reason_yes= "//*[@id='confirm_reject']"
transactions_reject_reason_no= "//*[@id='reason_modal']/div/div/div[3]/button[1]"

# # # orders_search

click_orders= "//*[@id='desktop_sidebar']/ul/li[6]"
orders_code_search= "//*[@id='search']"
orders_name_search= "//*[@id='name_search']"
orders_from_date= "//*[@id='filter_from_date_dp']"
orders_from_date_back= "//*[@id='plotId']/div[1]/div[3]"
orders_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[4]/td[1]"
orders_to_date= "//*[@id='filter_to_date_dp']"
orders_to_date_next= "/html/body/div[5]/div/div[1]/div[1]"
orders_to_date_option= "/html/body/div[5]/div/div[2]/div/div/table/tbody/tr[5]/td[4]"
orders_direct= "//*[@id='app']/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/label[2]"
orders_indirect= "//*[@id='app']/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/label[1]"
orders_fund= "//*[@id='fund_id']"
orders_fund_option= "//*[@id='fund_id']/option[1]"
orders_status= "//*[@id='status']"
orders_status_option= "//*[@id='status']/option[1]"
orders_type= "//*[@id='order_type']"
orders_type_option= "//*[@id='order_type']/option[2]"
orders_method= "//*[@id='method']"
orders_method_option= "//*[@id='method']/option[1]"
orders_referral= "//*[@id='referral']"
orders_result= "//*[@id='orders_table']"

# # # reinvesting

click_reinvesting= "//*[@id='desktop_sidebar']/ul/li[9]/a[1]"
reinvesting_search= "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/input"
reinvesting_result= "//*[@id='users_table']"
reinvesting_funds= "//*[@id='users_table']/tbody/tr[1]/td[4]/button"
reinvesting_investment= "//*[@id='users_table']/tbody/tr[2]/td/table/tbody/tr/td[2]/div/select"
reinvesting_investment_option= "//*[@id='users_table']/tbody/tr[2]/td/table/tbody/tr/td[2]/div/select/option[1]"
reinvesting_hide= "//*[@id='users_table']/tbody/tr[1]/td[4]/button"
reinvesting_funds_name= "//*[@id='users_table']/tbody/tr[2]/td/table/tbody/tr/td[1]"

# # # deposit_pose

# click_deposit= "//*[@id='desktop_sidebar']/ul/li[10]/a"
click_deposit= "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/ul/li[10]/a"
deposit_assert= "//*[@id='app']/div/div[2]/div[2]/div/div/div[1]/div[1]"
deposit_method= "//*[@id='method']"
deposit_pose= "//*[@id='method']/option[2]"
deposit_pose_bank= "//*[@id='pinvest_bank_account_id']"
deposit_pose_bank_option= "//*[@id='pinvest_bank_account_id']/option[3]"
deposit_pose_fund= "//*[@id='fund_id']"
deposit_pose_fund_option= "//*[@id='fund_id']/option"
deposit_pose_submit_btn= "//*[@id='submit_btn']"

# # # deposit_receipt

deposit_receipt= "//*[@id='method']/option[3]"
deposit_receipt_code= "//*[@id='user_id']"
deposit_receipt_fund= "//*[@id='fund_select']"
deposit_receipt_fund_option= "//*[@id='fund_select']/option"
deposit_receipt_amount= "//*[@id='amount']"
deposit_receipt_date= "//*[@id='transaction_date_dp']"
deposit_receipt_date_back= "//*[@id='plotId']/div[1]/div[3]"
deposit_receipt_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[1]/td[6]"
deposit_receipt_bank= "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[3]/form/div[5]/select"
deposit_receipt_bank_option= "/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[3]/form/div[5]/select/option[3]"
deposit_receipt_number= "//*[@id='receipt_number']"
deposit_receipt_description= "//*[@id='description']"
deposit_receipt_submit_btn= "//*[@id='submit_btn']"

# # # cashout

click_cashout= "//*[@id='desktop_sidebar']/ul/li[11]/a[1]"
cashout_assert= "//*[@id='app']/div/div[2]/div[2]/form/div/div[1]/div/div/div[1]"
cashout_user_id= "//*[@id='user_id']"
cashout_fund= "//*[@id='fund_id']"
cashout_unit= "//*[@id='unit']"
cashout_date= "//*[@id='schedule_date_dp']"
cashout_date_next= "//*[@id='plotId']/div[1]/div[1]"
cashout_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[3]/td[4]"
cashout_value= "//*[@id='value']"
cashout_submit_btn= "//*[@id='show_confirm_modal']"

# # # jobs

click_jobs= "//*[@id='desktop_sidebar']/ul/li[15]/a"
# click_jobs= "/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/ul/li[16]/span[1]"
jobs_fund= "//*[@id='fund_select']"
jobs_fund_option= "//*[@id='fund_select']/option"
jobs_config_rayanBuy= "//*[@id='config_rayanBuy']/div/div/button"
jobs_config_WithdrawJob= "//*[@id='config_WithdrawJob']/div/div/button"
jobs_config_updatesOrdersStatus= "//*[@id='config_updatesOrdersStatus']/div/div/button"
jobs_national= "//*[@id='national_code']"
jobs_config_withdrawWithNationalCode= "//*[@id='config_withdrawWithNationalCode']/div/div/button"

# # # invite

click_invite= "//*[@id='desktop_sidebar']/ul/li[16]/a"
invite_assert= "//*[@id='send_invite_link_form']/div/div/div/div[1]"
invite_msisdn= "//*[@id='msisdn']"
invite_send_link= "//*[@id='send_link_btn']"
invite_send_card= "//*[@id='send_bcard_btn']"
invite_show_link= "//*[@id='app']/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/label[2]"
invite_show_card= "//*[@id='app']/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/label[1]"
invite_result= "//*[@id='invites_table']"

# # # consultations

click_consultations= "//*[@id='desktop_sidebar']/ul/li[18]/a"
consultations_from_date= "//*[@id='filter_from_date_dp']"
consultations_from_date_back= "//*[@id='plotId']/div[1]/div[3]"
consultations_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[2]/td[4]"
consultations_to_date= "//*[@id='filter_to_date_dp']"
consultations_to_date_next= "/html/body/div[5]/div/div[1]/div[1]"
consultations_to_date_option= "/html/body/div[5]/div/div[2]/div/div/table/tbody/tr[3]/td[2]"
consultations_result= "//*[@id='report_table']"
consultations_switching= "//*[@id='report_table']/tbody/tr[1]/td[6]/button"

# # # payment

click_payment= "//*[@id='desktop_sidebar']/ul/li[17]/a"
payment_search= "//*[@id='search']"
payment_coefficient_fee= "//*[@id='coefficient_fee']"
payment_payment_link_name= "//*[@id='payment_link_name']"
payment_send= "//*[@id='send_pay_link_form']/div/div/div/div[2]/div[3]/div[2]/button"

# # # payment_graph

payment_from_date= "//*[@id='filter_from_date_dp']"
payment_from_date_back= "//*[@id='plotId']/div[1]/div[3]"
payment_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[3]/td[4]"
payment_to_date= "//*[@id='filter_to_date_dp']"
payment_to_date_next= "/html/body/div[8]/div/div[1]/div[1]"
payment_to_date_option= "/html/body/div[8]/div/div[2]/div/div/table/tbody/tr[4]/td[3]"

# # # payment_actions

payment_table_search= "//*[@id='table_search']"
payment_referral= "//*[@id='referral']"
payment_send_to_link= "//*[@id='links_table']/tbody/tr[1]/td[5]/a"
payment_copy= "/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[6]/div/i[1]"
payment_qr= "//*[@id='links_table']/tbody/tr[1]/td[6]/div/i[2]"
payment_resend= "//*[@id='links_table']/tbody/tr[1]/td[6]/div/i[3]"
payment_resend_no= "/html/body/div[5]/div/div/div[3]/button[1]"
payment_resend_yes= "//*[@id='resend_link_modal']/div/div/div[3]/button[1]"
payment_edit= "//*[@id='links_table']/tbody/tr[1]/td[6]/div/i[4]"
# payment_delete= "//*[@id='links_table']/tbody/tr[1]/td[6]/div/i[5]"
payment_delete= "/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[6]/div/i[5]"

# # # payment_edit

payment_update_coefficient_fee= "//*[@id='update_coefficient_fee']"
payment_update_payment_link_name= "//*[@id='update_payment_link_name']"
payment_update_link_modal= "/html/body/div[4]/div/div/div[3]/button[1]"
payment_update_link_confirm= "//*[@id='update_link_confirm']"

# # # payment_delete

payment_delete_link_modal= "//*[@id='delete_link_modal']/div/div/div[3]/button[1]"
payment_delete_link_confirm= "//*[@id='delete_link_confirm']"

# # # reports

click_reports= "//*[@id='desktop_sidebar']/ul/li[7]/a"

# # # reports_sell_orders

click_reports_sell_orders= "//*[@id='desktop_sidebar']/ul/li[8]/ul/li[1]/a"
reports_sell_orders_from_date= "//*[@id='filter_from_date_dp']"
reports_sell_orders_from_date_back= "//*[@id='plotId']/div[1]/div[3]"
reports_sell_orders_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[3]/td[4]"
reports_sell_orders_to_date= "//*[@id='filter_to_date_dp']"
reports_sell_orders_to_date_next= "/html/body/div[6]/div/div[1]/div[1]"
reports_sell_orders_to_date_option= "/html/body/div[6]/div/div[2]/div/div/table/tbody/tr[3]/td[4]"
reports_sell_orders_type= "//*[@id='type']"
reports_sell_orders_type_option= "//*[@id='type']/option[1]"
reports_sell_orders_fund= "//*[@id='fund_id']"
reports_sell_orders_fund_option= "//*[@id='fund_id']/option[1]"
reports_sell_orders_status= "//*[@id='status']"
reports_sell_orders_status_option= "//*[@id='status']/option[1]"
reports_sell_orders_search= "//*[@id='search']"
reports_sell_orders_method= "//*[@id='method']"
reports_sell_orders_method_option= "//*[@id='method']/option[1]"
reports_sell_orders_result= "//*[@id='report_table']"

# # # reports_cms_sell_orders

click_reports_cms_sell_orders= "//*[@id='desktop_sidebar']/ul/li[8]/ul/li[2]/a"
reports_cms_sell_orders_from_date= "//*[@id='filter_from_date_dp']"
reports_cms_sell_orders_from_date_back= "//*[@id='plotId']/div[1]/div[3]"
reports_cms_sell_orders_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[3]/td[4]"
reports_cms_sell_orders_to_date= "//*[@id='filter_to_date_dp']"
reports_cms_sell_orders_to_date_next= "/html/body/div[5]/div/div[1]/div[1]"
reports_cms_sell_orders_to_date_option= "/html/body/div[5]/div/div[2]/div/div/table/tbody/tr[4]/td[5]"
reports_cms_sell_orders_type= "//*[@id='type']"
reports_cms_sell_orders_type_option= "//*[@id='type']/option[1]"
reports_cms_sell_orders_search= "//*[@id='search']"
reports_cms_sell_orders_status= "//*[@id='status']"
reports_cms_sell_orders_status_option= "//*[@id='status']/option[1]"
reports_cms_sell_orders_result= "//*[@id='report_table']"
reports_cms_sell_orders_shaba= "//*[@id='report_table']/tbody/tr[1]/td[8]/button"
reports_cms_sell_orders_shaba_result= "//*[@id='report_table']/tbody/tr[2]/td/table"

# # # reports_superAdmin

# click_reports_superAdmin= "//*[@id='desktop_sidebar']/ul/li[8]/ul/li[3]"
click_reports_superAdmin= "//*[@id='desktop_sidebar']/ul/li[8]/ul/li[3]/a"
reports_superAdmin_value_report_1= "//*[@id='value_report_1']"
reports_superAdmin_value_report_2= "//*[@id='value_report_2']"
reports_superAdmin_value_report_3= "//*[@id='value_report_3']"
reports_superAdmin_value_report_4= "//*[@id='value_report_4']"
reports_superAdmin_report_4_month= "//*[@id='report_4']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_4_month_option= "//*[@id='report_4']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_4_year= "//*[@id='report_4']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_4_year_option= "//*[@id='report_4']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_4_graph= "//*[@id='report_4']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_value_report_5= "//*[@id='value_report_5']"
reports_superAdmin_report_5_month= "//*[@id='report_5']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_5_month_option= "//*[@id='report_5']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_5_year= "//*[@id='report_5']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_5_year_option= "//*[@id='report_5']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_5_graph= "//*[@id='report_5']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_value_report_6= "//*[@id='value_report_6']"
reports_superAdmin_report_6_month= "//*[@id='report_6']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_6_month_option= "//*[@id='report_6']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_6_year= "//*[@id='report_6']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_6_year_option= "//*[@id='report_6']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_6_graph= "//*[@id='report_6']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_value_report_7= "//*[@id='value_report_7']"
reports_superAdmin_report_7_month= "//*[@id='report_7']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_7_month_option= "//*[@id='report_7']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_7_year= "//*[@id='report_7']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_7_year_option= "//*[@id='report_7']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_7_graph= "//*[@id='report_7']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_value_report_8= "//*[@id='value_report_8']"
reports_superAdmin_report_8_month= "//*[@id='report_8']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_8_month_option= "//*[@id='report_8']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_8_year= "//*[@id='report_8']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_8_year_option= "//*[@id='report_8']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_8_graph= "//*[@id='report_8']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_value_report_9= "//*[@id='value_report_9']"
reports_superAdmin_report_9_month= "//*[@id='report_9']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_9_month_option= "//*[@id='report_9']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_9_year= "//*[@id='report_9']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_9_year_option= "//*[@id='report_9']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_9_graph= "//*[@id='report_9']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_value_report_10= "//*[@id='value_report_10']"
reports_superAdmin_report_10_month= "//*[@id='report_10']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_10_month_option= "//*[@id='report_10']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_10_year= "//*[@id='report_10']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_10_year_option= "//*[@id='report_10']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_10_graph= "//*[@id='report_10']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_11_fund= "//*[@id='report_11']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_11_fund_result= "//*[@id='table_report_11']"
reports_superAdmin_value_report_11= "//*[@id='value_report_11']"
reports_superAdmin_report_11_month= "//*[@id='report_11']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_11_month_option= "//*[@id='report_11']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_11_year= "//*[@id='report_11']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_11_year_option= "//*[@id='report_11']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_11_graph= "//*[@id='report_11']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_value_report_12= "//*[@id='value_report_12']"
reports_superAdmin_report_12_month= "//*[@id='report_12']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_12_month_option= "//*[@id='report_12']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_12_year= "//*[@id='report_12']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_12_year_option= "//*[@id='report_12']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_12_graph= "//*[@id='report_12']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_12_fund= "//*[@id='report_12']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_12_fund_result= "//*[@id='table_report_12']"
reports_superAdmin_value_report_13= "//*[@id='value_report_13']"
reports_superAdmin_report_13_month= "//*[@id='report_13']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_13_month_option= "//*[@id='report_13']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_13_year= "//*[@id='report_13']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_13_year_option= "//*[@id='report_13']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_13_graph= "//*[@id='report_13']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_13_fund= "//*[@id='report_13']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_13_fund_result= "//*[@id='table_report_13']"
reports_superAdmin_value_report_14= "//*[@id='value_report_14']"
reports_superAdmin_report_14_month= "//*[@id='report_14']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_14_month_option= "//*[@id='report_14']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_14_year= "//*[@id='report_14']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_14_year_option= "//*[@id='report_14']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_14_graph= "//*[@id='report_14']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_14_fund= "//*[@id='report_14']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_14_fund_result= "//*[@id='table_report_14']"
reports_superAdmin_value_report_15= "//*[@id='value_report_15']"
reports_superAdmin_report_15_month= "//*[@id='report_15']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_15_month_option= "//*[@id='report_15']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_15_year= "//*[@id='report_15']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_15_year_option= "//*[@id='report_15']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_15_graph= "//*[@id='report_15']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_15_fund= "//*[@id='report_15']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_15_fund_result= "//*[@id='table_report_15']"
reports_superAdmin_value_report_16= "//*[@id='value_report_16']"
reports_superAdmin_report_16_month= "//*[@id='report_16']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_16_month_option= "//*[@id='report_16']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_16_year= "//*[@id='report_16']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_16_year_option= "//*[@id='report_16']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_16_graph= "//*[@id='report_16']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_16_fund= "//*[@id='report_16']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_16_fund_result= "//*[@id='table_report_16']"
reports_superAdmin_value_report_17= "//*[@id='value_report_17']"
reports_superAdmin_report_17_month= "//*[@id='report_17']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_17_month_option= "//*[@id='report_17']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_17_year= "//*[@id='report_17']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_17_year_option= "//*[@id='report_17']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_17_graph= "//*[@id='report_17']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_17_fund= "//*[@id='report_17']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_17_fund_result= "//*[@id='table_report_17']"
reports_superAdmin_value_report_18= "//*[@id='value_report_18']"
reports_superAdmin_report_18_month= "//*[@id='report_18']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_18_month_option= "//*[@id='report_18']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_18_year= "//*[@id='report_18']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_18_year_option= "//*[@id='report_18']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_18_graph= "//*[@id='report_18']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_18_fund= "//*[@id='report_18']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_18_fund_result= "//*[@id='table_report_18']"
reports_superAdmin_value_report_19= "//*[@id='value_report_19']"
reports_superAdmin_report_19_month= "//*[@id='report_19']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_19_month_option= "//*[@id='report_19']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_19_year= "//*[@id='report_19']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_19_year_option= "//*[@id='report_19']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_19_graph= "//*[@id='report_19']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_19_fund= "//*[@id='report_19']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_19_fund_result= "//*[@id='table_report_19']"
reports_superAdmin_value_report_20= "//*[@id='value_report_20']"
reports_superAdmin_report_20_month= "//*[@id='report_20']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_20_month_option= "//*[@id='report_20']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_20_year= "//*[@id='report_20']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_20_year_option= "//*[@id='report_20']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_20_graph= "//*[@id='report_20']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_20_fund= "//*[@id='report_20']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_20_fund_result= "//*[@id='table_report_20']"
reports_superAdmin_value_report_21= "//*[@id='value_report_21']"
reports_superAdmin_report_21_month= "//*[@id='report_21']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_21_month_option= "//*[@id='report_21']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_21_year= "//*[@id='report_21']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_21_year_option= "//*[@id='report_21']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_21_graph= "//*[@id='report_21']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_21_fund= "//*[@id='report_21']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_21_fund_result= "//*[@id='table_report_21']"
reports_superAdmin_value_report_22= "//*[@id='value_report_22']"
reports_superAdmin_report_22_month= "//*[@id='report_22']/div[1]/div[3]/div[1]/select[1]"
reports_superAdmin_report_22_month_option= "//*[@id='report_22']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_superAdmin_report_22_year= "//*[@id='report_22']/div[1]/div[3]/div[1]/select[2]"
reports_superAdmin_report_22_year_option= "//*[@id='report_22']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_superAdmin_report_22_graph= "//*[@id='report_22']/div[1]/div[3]/div[2]/i[2]"
reports_superAdmin_report_22_fund= "//*[@id='report_22']/div[1]/div[3]/div[2]/i[1]"
reports_superAdmin_report_22_fund_result= "//*[@id='table_report_22']"


# # # reports_providers

click_reports_providers= "//*[@id='desktop_sidebar']/ul/li[8]/ul/li[4]/a"
reports_providers_value_report_1= "//*[@id='value_report_1']"
reports_providers_report_1_month= "//*[@id='report_1']/div[1]/div[3]/div[1]/select[1]"
reports_providers_report_1_month_option= "//*[@id='report_1']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_providers_report_1_year= "//*[@id='report_1']/div[1]/div[3]/div[1]/select[2]"
reports_providers_report_1_year_option= "//*[@id='report_1']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_providers_report_1_graph= "//*[@id='report_1']/div[1]/div[3]/div[2]/i[2]"
reports_providers_report_1_fund= "//*[@id='report_1']/div[1]/div[3]/div[2]/i[1]"
reports_providers_report_1_fund_result= "//*[@id='table_report_1']"
reports_providers_value_report_2= "//*[@id='value_report_2']"
reports_providers_report_2_month= "//*[@id='report_2']/div[1]/div[3]/div[1]/select[1]"
reports_providers_report_2_month_option= "//*[@id='report_2']/div[1]/div[3]/div[1]/select[1]/option[1]"
reports_providers_report_2_year= "//*[@id='report_2']/div[1]/div[3]/div[1]/select[2]"
reports_providers_report_2_year_option= "//*[@id='report_2']/div[1]/div[3]/div[1]/select[2]/option[1]"
reports_providers_report_2_graph= "//*[@id='report_2']/div[1]/div[3]/div[2]/i[2]"
reports_providers_report_2_fund= "//*[@id='report_2']/div[1]/div[3]/div[2]/i[1]"
reports_providers_report_2_fund_result= "//*[@id='table_report_2']"

# # # reports_cards_daily

click_reports_cards_daily= "//*[@id='desktop_sidebar']/ul/li[8]/ul/li[5]/a"
reports_cards_daily_date= "//*[@id='date_dp']"
reports_cards_daily_date_back= "//*[@id='plotId']/div[1]/div[3]"
reports_cards_daily_date_option= "//html/body/div[4]/div/div[2]/div/div/table/tbody/tr[2]/td[3]"
reports_cards_daily_result= "//*[@id='report_table']"

# # # reports_users_invited

click_reports_users_invited= "//*[@id='desktop_sidebar']/ul/li[8]/ul/li[6]/a"
reports_users_invited_phone_search= "//*[@id='search']"
reports_users_invited_name_search= "//*[@id='username_search']"
reports_users_invited_from_date= "//*[@id='filter_from_date_dp']"
reports_users_invited_from_date_back= "//*[@id='plotId']/div[1]/div[3]"
reports_users_invited_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[3]/td[4]"
reports_users_invited_to_date= "//*[@id='filter_to_date_dp']"
reports_users_invited_to_date_next= "/html/body/div[5]/div/div[1]/div[1]"
reports_users_invited_to_date_option= "/html/body/div[5]/div/div[2]/div/div/table/tbody/tr[3]/td[3]"
reports_users_invited_phone_search_result= "//*[@id='report_table']"

# # # reports_users_buy_sell

click_reports_users_buy_sell= "//*[@id='desktop_sidebar']/ul/li[8]/ul/li[7]/a"
reports_users_buy_sell_phone_search= "//*[@id='search']"
reports_users_buy_sell_name_search= "//*[@id='username_search']"
reports_users_buy_sell_from_date= "//*[@id='filter_from_date_dp']"
reports_users_buy_sell_from_date_back= "//*[@id='plotId']/div[1]/div[3]"
reports_users_buy_sell_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[3]/td[4]"
reports_users_buy_sell_to_date= "//*[@id='filter_to_date_dp']"
reports_users_buy_sell_to_date_next= "/html/body/div[5]/div/div[1]/div[1]"
reports_users_buy_sell_to_date_option= "/html/body/div[5]/div/div[2]/div/div/table/tbody/tr[3]/td[3]"
reports_users_buy_sell_btn_sale= "//*[@id='app']/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/label[1]"
reports_users_buy_sell_phone_search_result= "//*[@id='report_table']"

# # # reports_disabled_accounts

click_reports_disabled_accounts= "//*[@id='desktop_sidebar']/ul/li[8]/ul/li[8]/a"
reports_disabled_accounts_phone_search= "//*[@id='search']"
reports_disabled_accounts_from_date= "//*[@id='filter_from_date_dp']"
reports_disabled_accounts_from_date_back= "//*[@id='plotId']/div[1]/div[3]"
reports_disabled_accounts_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[3]/td[4]"
reports_disabled_accounts_to_date= "//*[@id='filter_to_date_dp']"
reports_disabled_accounts_to_date_next= "/html/body/div[5]/div/div[1]/div[1]"
reports_disabled_accounts_to_date_option= "/html/body/div[5]/div/div[2]/div/div/table/tbody/tr[3]/td[3]"
reports_disabled_accounts_search_result= "//*[@id='report_table']"












# my_pinvest_desktop_quick_cashout

desktop_cashout_unit= "//*[@id='quick_cashout_unit']"
desktop_cashout_modal= "//*[@id='show_cashout_modal']"
desktop_cashout_modal_show= "/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/div[2]/div/div/form/div[3]/div/button"

# my_pinvest_funds

click_funds= "//*[@id='desktop_sidebar']/ul/li[2]"
funds_show= "//*[@id='funds_container']/div/div/div/div[1]/div/div[1]/span"
funds_profit_calculator= "//*[@id='amount2']"
funds_container= "//*[@id='funds_container']/div/div/div/div[2]/div[3]/div[2]/div/span[2]"
funds_monthly_profit= "//*[@id='funds_container']/div/div/div/div[2]/div[3]/div[3]/div/span[2]"

# my_pinvest_funds_report

click_report= "//*[@id='desktop_sidebar']/ul/li[3]"
report_show= "//*[@id='refund_link']"
report_fund_select= "//*[@id='fund_select']"
report_fund_select_option= "//*[@id='fund_select']/option"
report_refund_link= "//*[@id='refund_link']"
report_refund_link_show= "//*[@id='app']/div/div[2]/div[2]/div/div[1]/div/div/div[1]/span[1]"
report_refund_link_fund_select= "//*[@id='fund_select']"
report_refund_link_fund_option= "//*[@id='fund_select']/option"
report_refund_link_amount= "//*[@id='amount']"
report_refund_link_refund_paytype= "//*[@id='refund_paytype']"
report_refund_link_refund_paytype_option= "//*[@id='refund_paytype']/option[4]"
report_refund_link_transaction_date_dp= "//*[@id='transaction_date_dp']"
report_refund_link_transaction_date_dp_plotId= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[3]/td[6]/span"
report_refund_link_pinvest_bank_account_id= "//*[@id='pinvest_bank_account_id']"
report_refund_link_pinvest_bank_account_id_option= "//*[@id='pinvest_bank_account_id']/option[3]"
report_refund_link_receipt_number= "//*[@id='receipt_number']"
report_refund_link_description= "//*[@id='description']"
report_refund_link_opt_out= "//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/a"
report_refund_link_submit_refund= "//*[@id='submit_refund']"
report_cashout_link= "//*[@id='cashout_link']"
report_cashout_link_fund_select= "//*[@id='fund_select']"
report_cashout_link_fund_select_option= "//*[@id='fund_select']/option"
report_cashout_link_cashout_unit= "//*[@id='cashout_unit']"
report_cashout_link_schedule_date_dp= "//*[@id='schedule_date_dp']"
report_cashout_link_schedule_date_dp_next= "//*[@id='plotId']/div[1]/div[1]"
report_cashout_link_schedule_date_dp_plotId= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[4]/td[5]/span"
report_cashout_link_opt_out= "//*[@id='app']/div/div[2]/div[2]/form/div/div[2]/div/div/div/div/div/a"
report_cashout_link_show_confirm_modal= "//*[@id='show_confirm_modal']"
report_unit_price_tab= "//*[@id='unit_price_tab']"
report_profit_tab= "//*[@id='profit_tab']"
report_table_report_container_successful= "//*[@id='table_report_container']/div/div/div/div[2]/div[1]/div/div/label[2]"
report_table_report_container_unsuccessful= "//*[@id='table_report_container']/div/div/div/div[2]/div[1]/div/div/label[1]"



# my_pinvest_accounts

click_accounts= "//*[@id='desktop_sidebar']/ul/li[4]"
accounts_show= "//*[@id='add_account_btn']"
accounts_add_account_btn= "//*[@id='add_account_btn']"
accounts_add_account_bank= "//*[@id='bank']"
accounts_add_account_bank_option= "//*[@id='bank']/option[3]"
accounts_add_account_period= "//*[@id='period']"
accounts_add_account_period_daily= "//*[@id='period']/option[2]"
accounts_add_account_period_daily_next= "//*[@id='plotId']/div[1]/div[1]"
accounts_add_account_period_daily_option1= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[5]/td[1]/span"
accounts_add_account_period_daily_option2= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[5]/td[2]/span"
accounts_add_account_period_daily_option3= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[6]/td[1]/span"
accounts_add_account_period_weekly= "//*[@id='period']/option[3]"
accounts_add_account_period_weekly_option1= "//*[@id='saturday_check']"
accounts_add_account_period_weekly_option2= "//*[@id='monday_check']"
accounts_add_account_period_weekly_option3= "//*[@id='thursday_check']"
accounts_add_account_period_weekly_daily_next= "//*[@id='weekly_exceptions_calendar']/div[1]/div[1]/div[1]/div"
# accounts_add_account_period_weekly_daily_option1= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[5]/td[3]/span"
accounts_add_account_period_weekly_daily_option1= "//*[@id='weekly_exceptions']/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr[3]/td[1]/span"
accounts_add_account_period_weekly_daily_option2= "//*[@id='weekly_exceptions']/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr[3]/td[5]/span"
accounts_add_account_period_weekly_daily_option3= "//*[@id='weekly_exceptions']/div[2]/div[1]/div/div/div[2]/div/div/table/tbody/tr[4]/td[1]/span"


accounts_add_account_period_monthly= "//*[@id='period']/option[4]"
accounts_add_account_period_monthly_option1= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/span"
accounts_add_account_period_monthly_option2= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/span"
accounts_add_account_period_monthly_option3= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[3]/td[3]/span"
accounts_add_account_period_monthly_option4= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[4]/td[4]/span"
accounts_add_account_period_max_withdraw= "//*[@id='max_withdraw']"
accounts_add_account_period_accept= "//*[@id='accept']"
accounts_add_account_period_opt_out= "//*[@id='add_bank_account_form']/div[2]/div/div/div/div/div/a"
accounts_add_account_period_submit_form= "//*[@id='submit_form']"
accounts_add_account_period_detail= "//*[@id='refundDetailModalLabel']"
accounts_add_account_period_detail_modal_bank= "//*[@id='detail_modal_bank']"
accounts_add_account_period_detail_modal_max= "//*[@id='detail_modal_max']"
accounts_add_account_period_detail_opt_out= "//*[@id='refundDetailModal']/div/div/div[3]/button[1]"

# accounts_show_graph

accounts_show_graph= "//*[@id='card_E4LvMKQG91PLr5lN3nDY']/div[1]/div/div/div[1]/div/div[2]/div[1]/a[2]"
accounts_show_graph_from_date= "//*[@id='filter_from_date_dp']"
accounts_show_graph_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[1]/td[2]"
accounts_show_graph_to_date= "//*[@id='filter_to_date_dp']"
accounts_show_graph_to_date_next= "/html/body/div[5]/div/div[1]/div[1]"
accounts_show_graph_to_date_option= "/html/body/div[5]/div/div[2]/div/div/table/tbody/tr[4]/td[3]"

# accounts_edit

accounts_edit= "//*[@id='card_E4LvMKQG91PLr5lN3nDY']/div[1]/div/div/div[1]/div/div[2]/div[1]/a[1]"
accounts_edit_name= "//*[@id='name']"
accounts_edit_period= "//*[@id='period']"
accounts_edit_period_monthly= "//*[@id='period']/option[4]"
accounts_edit_period_monthly_option1= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/span"
accounts_edit_period_monthly_option2= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/span"
accounts_edit_period_monthly_option3= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[3]/td[3]/span"
accounts_edit_period_monthly_option4= "//*[@id='monthly_exceptions']/div/div/div/div/div/div/div/table/tbody/tr[4]/td[4]/span"
accounts_edit_interval_withdraw_amount= "//*[@id='interval_withdraw_amount']"
accounts_edit_max_withdraw= "//*[@id='max_withdraw']"
accounts_edit_save_changes= "//*[@id='add_bank_account_form']/div[2]/div/div/div/div/div/button"
accounts_edit_detail_opt_out= "//*[@id='refundDetailModal']/div/div/div[3]/button[1]"
accounts_edit_opt_out= "//*[@id='add_bank_account_form']/div[2]/div/div/div/div/div/a"

# accounts_delete

accounts_delete= "//*[@id='card_bkMX4ezvWy2rnpKLED0Z']/div[1]/div/div/div[1]/div/div[2]/div[1]/span/i"
accounts_delete_no= "//*[@id='delete_modal']/div/div/div[3]/button[1]"
accounts_delete_yes= "//*[@id='delete_modal_confirm']"

# accounts_status

accounts_status= "//*[@id='activeSwitchE4LvMKQG91PLr5lN3nDY']"

# my_pinvest_statement_report

click_statement= "//*[@id='desktop_sidebar']/ul/li[5]"
statement_show= "//*[@id='statement_report_table']/thead/tr/th[4]"
statement_fund_select= "//*[@id='fund_select']"
statement_fund_select_option= "//*[@id='fund_select']/option"
statement_from_date= "//*[@id='filter_from_date_dp']"
statement_from_date_back= "//*[@id='plotId']/div[1]/div[3]"
statement_from_date_option= "//*[@id='plotId']/div[2]/div/div/table/tbody/tr[4]/td[1]"
statement_to_date= "//*[@id='filter_to_date_dp']"
statement_to_date_next= "/html/body/div[5]/div/div[1]/div[1]"
statement_to_date_option= "/html/body/div[5]/div/div[2]/div/div/table/tbody/tr[3]/td[6]"

# my_pinvest_nexo_card

click_card= "//*[@id='desktop_sidebar']/ul/li[6]"
card_show= "//*[@id='checking_status']"


# my_pinvest_contact-us

click_contact= "//*[@id='desktop_sidebar']/ul/li[10]"
contact_show= "//*[@id='ways_container']/p"

# my_pinvest_Profile

click_profile= "//*[@id='peofile_btn']"
profile_full_name= "//*[@id='full_name']"
profile_national_code= "//*[@id='national_code']"
profile_sejam= "//*[@id='sejam_shaba_number']"
profile_sejam_edit= "//*[@id='edit_profile_form']/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div/a"
profile_bank= "//*[@id='sejam_bank']"
profile_birthday= "//*[@id='birthday']"
profile_phone_number= "//*[@id='main_msisdn']"
profile_phone_number_edit= "//*[@id='edit_profile_form']/div[1]/div/div/div[2]/div/div[1]/div[6]/div/div/a"
profile_phone_number_new= "//*[@id='msisdn']"
profile_phone_number_btn= "//*[@id='edit_msisdn_button']"
profile_education= "//*[@id='education']"
profile_education_option= "//*[@id='education']/option[7]"
profile_change_password= "//*[@id='edit_profile_form']/div[2]/div/div/div/div/div/a"
profile_change_password_previous= "//*[@id='password']"
profile_change_password_previous_show= "//*[@id='change_password_form']/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div[1]/i[2]"
profile_change_password_new= "//*[@id='new_password']"
profile_change_password_new_show= "//*[@id='change_password_form']/div/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/i[2]"
profile_change_password_confirmation= "//*[@id='new_password_confirmation']"
profile_change_password_confirmation_show= "//*[@id='change_password_form']/div/div[1]/div/div/div[2]/div/div/div[3]/div/div/div/i[2]"
profile_change_password_opt_out= "//*[@id='change_password_form']/div/div[2]/div/div/div/div/div/a"
profile_change_password_btn= "//*[@id='change_password_button']"
profile_btn= "//*[@id='edit_profile_button']"

# # # settings

click_settings= "//*[@id='desktop_sidebar']/ul/li[12]/a"
settings_add= "//*[@id='app']/div/div[2]/div[2]/div[1]/div[1]/button"
settings_name= "//*[@id='name']"
settings_trans= "//*[@id='trans']"
settings_add_config_form= "//*[@id='add_config_form']/div/div/div[3]/div/tags/span"
settings_value= "//*[@id='value']"
settings_value_option= "//*[@id='value']/option[2]"
settings_save= "//*[@id='add_config_form']/div/div/div[5]/div/button"
settings_no_save= "//*[@id='modal_create']/div/div/div[1]/button"
settings_version= "//*[@id='7vbMQGAgR7GR8BEmVX60']"
settings_version_option= "//*[@id='7vbMQGAgR7GR8BEmVX60']/option[2]"
settings_transactions_daily= "//*[@id='J5E7A8WgolXor4nxQPae']"
settings_transactions_daily_option= "//*[@id='J5E7A8WgolXor4nxQPae']/option"
settings_transactions_monthly= "//*[@id='OXAaB4kloGdy5M8QxWzG']"
settings_transactions_monthly_option= "//*[@id='OXAaB4kloGdy5M8QxWzG']/option"
settings_FARABOOM_PAYMAN_API_MAX_CONTRACT_EXPIRATION_YEARS= "//*[@id='3wdeQV25yWQ9v8NpkWaY']"
settings_FARABOOM_PAYMAN_API_MAX_CONTRACT_EXPIRATION_YEARS_option= "//*[@id='3wdeQV25yWQ9v8NpkWaY']/option[1]"
settings_POD_API_MAX_COUNT= "//*[@id='3LwkKxzD9p49M2rNJOGE']"
settings_POD_API_MAX_COUNT_option= "//*[@id='3LwkKxzD9p49M2rNJOGE']/option"
settings_FINNOTECH_API_MAX_MONTHLY_TRANSACTION_COUNT= "//*[@id='NnM0PgJ8RVPoADZ4eX1O']"
settings_FINNOTECH_API_MAX_MONTHLY_TRANSACTION_COUNT_option= "//*[@id='NnM0PgJ8RVPoADZ4eX1O']/option"
settings_CAPTCHA= "//*[@id='JK6vajwWo3ARd0ge35xm']"
settings_CAPTCHA_option= "//*[@id='JK6vajwWo3ARd0ge35xm']/option[1]"
settings_SMS_PANEL= "//*[@id='VpPleg48o2GyawqXn6Bd']"
settings_SMS_PANEL_option= "//*[@id='VpPleg48o2GyawqXn6Bd']/option[1]"
settings_OTP_EXPIRE= "//*[@id='qJLQmPxKoa6ykjVdYGB3']"
settings_OTP_EXPIRE_option= "//*[@id='qJLQmPxKoa6ykjVdYGB3']/option"
settings_TEST_MODE= "//*[@id='NvjKLPVJRjpokzgb7B8p']"
settings_MAX_OTP_CHECK= "//*[@id='EK5vdDZbRAb9j0mBGWnJ']"
settings_MAX_OTP_CHECK_option= "//*[@id='EK5vdDZbRAb9j0mBGWnJ']/option[1]"
settings_TIME_SCOPE_EXPIRE= "//*[@id='z4v6mAK1oNkygxMVDaGe']"
settings_TIME_SCOPE_EXPIRE_option= "//*[@id='z4v6mAK1oNkygxMVDaGe']/option"
settings_LOGIN_TIME_EXPIRE= "//*[@id='a1pDG3zkRg3RBreOvgL0']"
settings_LOGIN_TIME_EXPIRE_option= "//*[@id='a1pDG3zkRg3RBreOvgL0']/option"
settings_MAX_RETRY_SCOPE= "//*[@id='z405mb2woL4oBkVn3qYK']"
settings_MAX_RETRY_SCOPE_option= "//*[@id='z405mb2woL4oBkVn3qYK']/option[1]"
settings_GOOGLE_CAPTCHA_PAGES= "//*[@id='WlkBevDX9zqRjg2MAE4w']"
settings_REQUIREMENT_BANK_ACCOUNT_REGISTRATION= "//*[@id='KW7lw5DO9E2omGPr8Aqj']"
settings_INCREASE_COEFFICIENT= "//*[@id='AwKVdBLQ94kRZP5Y7la0']"
settings_INCREASE_COEFFICIENT_option= "//*[@id='AwKVdBLQ94kRZP5Y7la0']/option[1]"
settings_GOOGLE_2F_AUTH= "//*[@id='pZr63KjNR6JRd0vg2xV8']"
settings_WRAPPER_SEND_MESSAGE_BY_SMS= "//*[@id='wmbZ12pEydmRzNkgBAe3']"
settings_WRAPPER_SEND_MESSAGE_BY_SMS_option= "//*[@id='wmbZ12pEydmRzNkgBAe3']/option[1]"
settings_WRAPPER_SEND_PATTERN_BY_SMS= "//*[@id='DLQvBwYZywq9W0OnaXdx']"
settings_WRAPPER_SEND_PATTERN_BY_SMS_option= "//*[@id='DLQvBwYZywq9W0OnaXdx']/option[1]"
settings_SHAHKAR_PANEL= "//*[@id='q1eXGpx0o589M2Ljv35d']"
settings_SHAHKAR_PANEL_option= "//*[@id='q1eXGpx0o589M2Ljv35d']/option[1]"
settings_WRAPPER_SHAHKAR= "//*[@id='jqnG7DQwyeNR4b0zKXxr']"
settings_WRAPPER_SHAHKAR_option= "//*[@id='jqnG7DQwyeNR4b0zKXxr']/option[1]"
settings_IPG_JIBIMO_CHECK_NATIONAL_CODE= "//*[@id='eg7pJ8EbR1GonQBaPLA0']"
settings_CARD_SERVICE_MENU= "//*[@id='GnwlZzrJR0No860YBOaq']"
settings_CARD_SERVICE_MENU_option= "//*[@id='GnwlZzrJR0No860YBOaq']/option[1]"
settings_RAYAN_REQUEST_TIMEOUT= "//*[@id='4rYmpaXvyZnyLqkgJ0K5']"
settings_RAYAN_REQUEST_TIMEOUT_option= "//*[@id='4rYmpaXvyZnyLqkgJ0K5']/option[1]"
settings_DOMAIN_SEND_SMS= "//*[@id='NWrlEGz5yM79KdQ07J2x']"
settings_DOMAIN_SEND_SMS_option= "//*[@id='NWrlEGz5yM79KdQ07J2x']/option[1]"
settings_MIN_NAV= "//*[@id='GQ5DkWlnyX8y8E2Y4zVp']"
settings_MIN_NAV_option= "//*[@id='GQ5DkWlnyX8y8E2Y4zVp']/option[1]"
settings_MAX_NAV= "//*[@id='wJWQVnzOyKwyvK218Em5']"
settings_MAX_NAV_option= "//*[@id='wJWQVnzOyKwyvK218Em5']/option[1]"
settings_SEJAM_DEFAULT= "//*[@id='GkQNLlMAyn1oWgr1b6mp']"
settings_SEJAM_DEFAULT_option= "//*[@id='GkQNLlMAyn1oWgr1b6mp']/option[1]"
settings_WRAPPER_SEJAM= "//*[@id='OZp7XQWqokb93rJvB6ME']"
settings_WRAPPER_SEJAM_option= "//*[@id='OZp7XQWqokb93rJvB6ME']/option[1]"
settings_WRAPPER_FUND_REGISTER= "//*[@id='Kjzd0QJ3oJa9eLYEqANk']"
settings_WRAPPER_FUND_REGISTER_option= "//*[@id='Kjzd0QJ3oJa9eLYEqANk']/option[1]"
settings_IPG_SEP= "//*[@id='lVb8nPmjoml9QBqJxkgd']"
settings_IPG_PEP= "//*[@id='QDeBlYAbyYMy73rMZa5m']"
settings_EXPIRE_FUND_LICENSE_AFTER_DAY= "//*[@id='N5jdbEn09BmReKDx3kzQ']"
settings_EXPIRE_FUND_LICENSE_AFTER_DAY_option= "//*[@id='N5jdbEn09BmReKDx3kzQ']/option[1]"
settings_PROFIT_CALCULATION_DAY= "//*[@id='rvbAJYw3obq9E0XxNje4']"
settings_PROFIT_CALCULATION_DAY_option= "//*[@id='rvbAJYw3obq9E0XxNje4']/option[1]"
settings_IPG_SEPEHR= "//*[@id='53OrDpaL982y4gePWYmE']"
settings_PAYMENT_LINK_GATEWAY= "//*[@id='ZBkJ3gEl9Oay4razN127']"
settings_PAYMENT_LINK_GATEWAY_option= "//*[@id='ZBkJ3gEl9Oay4razN127']/option[1]"
settings_IPG_JIBIMO= "//*[@id='13Yl2ZGLyDXya4OqMVpX']"
settings_BASE_NAV= "//*[@id='QMvePB6AoxnRj1rdGWJl']"
settings_BASE_NAV_option= "//*[@id='QMvePB6AoxnRj1rdGWJl']/option[1]"
settings_IPG_SADAD= "//*[@id='2NnVLK5D9v5R1OAxvkrY']"

###Accounting
click_accounting= "//*[@id='desktop_sidebar']/ul/li[13]/a"
accounting_referral= "//*[@id='referral']"
accounting_referral_btn= "//*[@id='search_form']/div/div[2]/button"

###Compass

click_compass= "//*[@id='desktop_sidebar']/ul/li[14]/a"
compass_fund= "//*[@id='fund']"
compass_fund_option= "//*[@id='fund']/option[1]"
compass_from_date= "//*[@id='filter_from_date_dp']"
compass_from_date_option= "/html/body/div[4]/div/div[2]/div/div/table/tbody/tr[2]/td[2]"
compass_to_date= "//*[@id='filter_to_date_dp']"
compass_to_date_option= "/html/body/div[5]/div/div[2]/div/div/table/tbody/tr[4]/td[4]"
compass_chart= "//*[@id='chart']"

###Blog

click_blog="//*[@id='desktop_sidebar']/ul/li[19]/a"
blog_category="//*[@id='category']"
blog_category_option="//*[@id='category']/option[1]"
blog_search="//*[@id='search']"
blog_result="//*[@id='posts_table']"

###Blog_add

blog_add="//*[@id='app']/div/div[2]/div[2]/div[1]/div/div/div/div[2]/a"
blog_add_title="//*[@id='title']"
blog_add_category="//*[@id='addPostForm']/div[2]/div/div[1]/span/span[1]/span"
blog_add_category_option="//*[@id='select2-category-result-5shx-23ngkn']"
blog_add_description="//*[@id='description']"
blog_add_content="//*[@id='content_ifr']"
blog_add_submit_form="//*[@id='submit_form']"

###Blog_edit

blog_edit="//*[@id='posts_table']/tbody/tr[1]/td[4]/a"
blog_edit_title="//*[@id='title']"
blog_edit_category="//*[@id='addPostForm']/div[2]/div/div[1]/span/span[1]/span"
blog_edit_description="//*[@id='description']"
blog_edit_content="//*[@id='tinymce']/p[1]"
blog_edit_submit_form="//*[@id='submit_form']"

###Blog_categories

click_blog_categories="//*[@id='desktop_sidebar']/ul/li[20]/a"
blog_categories_result="//*[@id='cats_table']"
blog_categories_name="//*[@id='name']"
blog_categories_fa_name="//*[@id='fa_name']"
blog_categories_submit="//*[@id='create_category_form']/div/div/div/div[2]/div[2]/div[2]/button"

###Blog_categories_edit

blog_categories_edit="//*[@id='cats_table']/tbody/tr[1]/td[3]/i[1]"
blog_categories_edit_name_update="//*[@id='name_update']"
blog_categories_edit_fa_name_update="//*[@id='fa_name_update']"
blog_categories_edit_update_no="/html/body/div[4]/div/div/div[3]/button[1]"

###Blog_categories_delete

blog_categories_delete="//*[@id='cats_table']/tbody/tr[1]/td[3]/i[2]"
blog_categories_delete_no="/html/body/div[3]/div/div/div[3]/button[1]"

###Logs_login

click_logs="//*[@id='desktop_sidebar']/ul/li[21]/a"
logs_result="//*[@id='report_table']"

###nps

click_nps="//*[@id='desktop_sidebar']/ul/li[22]/a"
nps_from_date="//*[@id='filter_from_date_dp']"
nps_from_date_option="/html/body/div[4]/div/div[2]/div/div/table/tbody/tr[3]/td[3]"
nps_to_date="//*[@id='filter_to_date_dp']"
nps_to_date_option="/html/body/div[5]/div/div[2]/div/div/table/tbody/tr[4]/td[2]"
nps_from_score= "//*[@id='from_score']"
nps_from_score_option="//*[@id='from_score']/option[2]"
nps_to_score= "//*[@id='to_score']"
nps_to_score_option="//*[@id='to_score']/option[9]"
nps_search="//*[@id='search']"
nps_result="//*[@id='report_table']"
nps_description="//*[@id='report_table']/tbody/tr[1]/td[3]/button"


###policy

click_policy= "//*[@id='desktop_sidebar']/ul/li[24]/a"
policy_show= "//*[@id='app']/div/div[2]/div[2]/div/div/div/div[3]/div/div/ul"

###faq

click_faq= "//*[@id='desktop_sidebar']/ul/li[25]/a"
faq_pinvest= "//*[@id='faq_section']/div[2]/div/div[1]/div/ul/li[1]"
faq_account= "//*[@id='faq_section']/div[2]/div/div[1]/div/ul/li[2]"
faq_deposit= "//*[@id='faq_section']/div[2]/div/div[1]/div/ul/li[3]"
faq_investment= "//*[@id='faq_section']/div[2]/div/div[1]/div/ul/li[4]"
faq_funds= "//*[@id='faq_section']/div[2]/div/div[1]/div/ul/li[5]"
faq_messages= "//*[@id='faq_section']/div[2]/div/div[1]/div/ul/li[6]"