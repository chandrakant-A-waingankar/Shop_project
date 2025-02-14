from .HomePage import HomePage
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class Services(HomePage):
    def __init__(self):
        super().__init__()
        self.service_item = "css: select[title='Select Service item']"
        self.billing_country = "css: select[title='Select billing country']"
        self.input_name_description = "css: input[name*='{}'][placeholder*='{}']"
        self.discount_box = "css: button[data-target='#discountBox']"
        self.discount_item = "//div[@class='row align-items-center' and contains(.,'{}')]/descendant::select"
        self.customer_data_input_fields= "css: div#new_customer [id={}]"
        self.submit_service_order = "css: input[value='Create Service order']"
        self.service_order_alert_text = "css: div.alert-text ul li"
        self.service_order_submitted_confirmation = "css: div.alert-text"


    @keyword("User ${USER} selects service item as ${item}")
    def select_service_item(self, user, item):
        """ This keyword is used to select service items

        **Arguments:**
        -   item: String

        **Options**
        - Custom service | Poc service | Consultancy | Emergency | HealthCheck | Migration | SSL Certificate | Partner Certification | Development | SentinelOne | Implementation | Implementation of HA | SLA Subscription | Upgrade - old | Upgrade | Training


        **Example:**
        | User Chan selects service item as Custome service |
        | User Chan selects service item as Poc service | 
        """
        self.select_from_list_by_label(self.service_item, item)

    @keyword("User ${USER} selects billing country as ${country}")
    def select_billing_country(self, user, country):
        """ This keyword is used to select the desired country

        **Arguments:**
        - country: String

        **Example:**
        | User Chan selects billing country as China |
        """
        self.select_from_list_by_label(self.billing_country, country)

    @keyword("User ${USER} enters ${item} item ${item_input_field} as ${value}")
    def enter_cert_name(self, user, item, item_input_field, value):
        """ This keyword is ued to enter certificate name 

        **Arguments:**
        - item: (String)
        - item_input_field: (String) Name | Description
        - content: 

        **Example:**
        | User Chan enters certificate name as MyCertificate |
        | User Chan enters emergency name as GreatEmergency |
        | User Chan entes certificate description as This is certificate bearing cert No. 12345 |
        """
        self.wait_for_and_input_text(self.input_name_description.format(item, item_input_field), value)

    @keyword("User ${USER} selects discount for item ${item} as ${discount} %")
    def select_discount_for_item(self, user, item, discount):
        """ This Keyword is used to select discount against the desired service item

        **Arguments**
        - item: String
        - discount: integer

        **Example**
        | User chan selects discount for item SSL certificate as 5 % |
        """
        
        self.wait_for_and_click_element(self.discount_box)
        self.wait_until_element_is_visible("css: button[title='+ Add discount']")
        self.select_from_list_by_label(self.discount_item.format(item), discount+" %")

    @keyword("User ${USER} fills his company details on Service order")
    def fill_company_details_on_service_order(self,user):
        self.company_data ={
                        "customer_company":"test1_Company",
                        "customer_email":"tester1@icewarp.com",
                        "customer_country":"India",
                        "customer_first_name":"Test1",
                        "customer_last_name":"USER1",
                        "customer_phone":"+911234567892",
                        "customer_address":"TEST_ADDRESS",
                        "customer_city":"TEST_CITY",
                        "customer_zip":"123456",
                        "customer_company_id":"CID_3456",
                        }

        for data_field in self.company_data:
            data_field_element = self.get_webelement(self.customer_data_input_fields.format(data_field))#driver.find_element(By.XPATH,self.customer_data_input_fields.format(data_field))
            if data_field_element.tag_name == "select":
                self.select_from_list_by_label(data_field_element, self.company_data[data_field])
            elif data_field_element.tag_name == "input":
                self.wait_for_and_input_text(self.customer_data_input_fields.format(data_field), self.company_data[data_field])
            else:
                BuiltIn().log("Improper element is found while entering the company details")

    @keyword("User ${USER} submits the service order ")
    def submits_service_order(self, user):
        try:
            self.wait_for_and_click_element(self.submit_service_order)
            self.wait_until_element_is_visible(self.service_order_submitted_confirmation,timeout=10)
            self.element_text_should_be(self.service_order_submitted_confirmation,"Services Order has been successfully created.")

        except Exception as e:
            ALerts_list = self.get_webelements(self.service_order_alert_text)
            for alert_text in ALerts_list:
                BuiltIn().log(alert_text.text)     

