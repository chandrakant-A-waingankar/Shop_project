import math
from .HomePage import HomePage
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By
import os
import sys
sys.path.append(os.path.abspath(''))
import time
import re


class Quote(HomePage):
    def __init__(self):
        super().__init__()
        self.page_heading = "//h1"
        self.subscription = "//label[contains(@for, '{}')]"
        #self.tenure = "css: input#myRange"
        self.post_paid_msg = "css: p.mb-5"
        self.data_center_dropdown = "css:button[data-id='cloud-datacenter']"
        self.data_center_option = "//a[contains(.,'Mumbai')]"
        self.plans_dropdown = "css:button[title='Plans']"
        self.plans_option = "//a[contains(.,'{}')]"
        self.discount_dropdown = "//button[text()=' Discount ']"
        self.discount_option = "//label[text()=' Discount {} %']"
        self.free_period_dropdown = "//button[text()=' Free period ']"
        self.free_period_option = "//label[text()='{} month FREE']"
        self.trial_period_dropdown = "//button[text()=' Trial (free period) ']"
        self.postponed_billing_dropdown = "//button[text()=' Postponed billing ']"
        self.postponed_billing_option = "//label[text()='{} month FREE']"
        self.quote_expiry_dropdown = "css:#expirationDate"
        self.today_date = "css:.today.day"
        self.customer_data_input_fields = "//*[@name='{}']"
        self.submit_quote_subscription = "//button[contains(.,'Quote subscription')]"
        self.quote_submitted_confirmation = "css:div.alert-success div.alert-text"
        self.quote_submitted_error_alert = "css: div.alert-text ul li"



    @keyword("User ${USER} creates a new ${option} Quote")
    def create_new_quote(self, user, option):
        self.select_new_option(option)
        if option.lower() == "cloud":
            self.element_text_should_be(self.page_heading, f"Create a Cloud Quote")
        else:
            self.element_text_should_be(self.page_heading, f"Create a Saas Quote")

    @keyword("User ${USER} selects subscription: ${subscription}")
    def select_subscription(self, user, subscription):
        if subscription.lower() == "post-paid":
            self.wait_for_and_click_element(self.subscription.format("post_paid"))
            self.element_text_should_be(self.post_paid_msg, "Fees will be determined by the peak number of users as these may change in the monthly subscription.")
        elif subscription.lower() == "pre-paid":
            self.wait_for_and_click_element(self.subscription.format("pre_paid"))
        else:
            print("Subscription not supported, Please select valid subscription or check the spelling")


    @keyword("User ${USER} selects currency: ${currency}")
    def select_currency(self, user, currency):
        if currency.lower()in ["euro", "EUR"]:
            self.wait_for_and_click_element("//option[contains(text(), 'EUR')]")
        elif currency.lower() in ["usd", "dollar","us dollar"]:
            self.wait_for_and_click_element("//option[contains(text(), 'USD')]")
        else:
            print("Currency not supported, System supports only USD and EUR")

    @keyword("User ${USER} selects pre-paid tenure: ${tenure} months (12 <= tenure <= 36)")
    def select_tenure(self, user, tenure: int):
        self.execute_javascript(f"""
                                    let slider = document.getElementById('myRange');
                                    slider.value = {tenure};
                                    slider.dispatchEvent(new Event('input'));
                                """.format(tenure))

    @keyword("User ${USER} selects data center city: ${data_center_city}")
    def select_data_center(self, user, data_center_city):
        self.wait_for_and_click_element(self.data_center_dropdown)
        self.wait_for_and_click_element(self.data_center_option.format(data_center_city))


    @keyword("User ${USER} selects plan: ${plan}")
    def select_plan(self,user, plan):
        self.wait_for_and_click_element(self.plans_dropdown)
        self.wait_for_and_click_element(self.plans_option.format(plan))

        

    @keyword("User ${USER} selects Disocunt: ${discount} %")
    def select_discount(self, user, discount):
        self.wait_for_and_click_element(self.discount_dropdown)
        self.wait_for_and_click_element(self.discount_option.format(discount))

    @keyword("User ${USER} selects Free period: ${free_period} month(s)")
    def select_free_period(self, user, free_period):
        self.wait_for_and_click_element(self.free_period_dropdown)
        self.wait_for_and_click_element(self.free_period_option.format(free_period))

    @keyword("User ${USER} selects  Trial (free period)  period: ${free_period} month(s)")
    def select_trial_period(self, user, free_period):
        self.wait_for_and_click_element(self.trial_period_dropdown)
        self.wait_for_and_click_element(self.free_period_option.format(free_period))

    @keyword("User ${USER} fills his company details")
    def fill_company_details(self,user):
        self.company_data ={
                        "company":"test1_Company",
                        "email":"tester1@icewarp.com",
                        "country":"India",
                        "first_name":"Test1",
                        "last_name":"USER1",
                        "phone":"+911234567892",
                        "address":"TEST_ADDRESS",
                        "city":"TEST_CITY",
                        "zip":"123456",
                        "company_id":"CID_3456",
                        }

        for data_field in self.company_data:
            data_field_element = self.get_webelement(self.customer_data_input_fields.format(data_field))#driver.find_element(By.XPATH,self.customer_data_input_fields.format(data_field))
            if data_field_element.tag_name == "select":
                self.select_from_list_by_label(data_field_element, self.company_data[data_field])
            elif data_field_element.tag_name == "input":
                self.wait_for_and_input_text(self.customer_data_input_fields.format(data_field), self.company_data[data_field])
            else:
                BuiltIn().log("Improper element is found while entering the company details")
        



    @keyword("User ${USER} Selects Expiry as today")
    def select_today_expiry(self,user):
        self.wait_for_and_click_element(self.quote_expiry_dropdown)
        self.wait_for_and_click_element(self.today_date)
        time.sleep(10)

    @keyword("User ${USER} submits the quote")
    def submit_quote(self, user):
        try:
            self.wait_for_and_click_element(self.submit_quote_subscription)
            self.wait_until_element_is_visible(self.quote_submitted_confirmation,timeout=10)
            self.element_text_should_be(self.quote_submitted_confirmation,"Cloud Quote for \""+self.company_data["company"]+"\" has been created.")
            

        except Exception as e:
            ALerts_list = self.get_webelements(self.quote_submitted_error_alert)
            for alert_text in ALerts_list:
                BuiltIn().log(alert_text.text)


    
        




            

        