from .HomePage import HomePage
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn



class Partners(HomePage):
    def __init__(self):
        super().__init__()
        self.create_button= "//button[text()='Create']"
        self.toggle_button= "//div[@class='form-group row' and contains(.,'{}')]//label[contains(.,'{}')]"
        self.dropdown_box= "//div[contains(@class, 'col-md-8') and contains(.,'{}')]/following-sibling::div[1]//select[contains(@title,'{}')]"
        self.input_box = "//div[contains(@class, 'col-md-8') and contains(.,'{}')]/following-sibling::div[1]//input[@placeholder='{}']"
        

    @keyword("User ${USER} verifies the create new partner page")
    def verify_create_new_partner_page(self, user):
        self.element_text_should_be("css: h1", "Create a Partner", "Page Header is Invalid")
        list_of_subheaders= []
        for element in self.get_webelements("css: h4"):
            list_of_subheaders.append(element.text)
            if '' in list_of_subheaders:
                list_of_subheaders.remove('')
        BuiltIn().should_be_equal(list_of_subheaders, ["Basics","Vendor pricelists","Price margins","Billing details"])
        self.element_should_be_visible(self.create_button, "Create Button is not visible on Create new Partner Page")
        
    @keyword("User ${USER} fills in the new partner data")
    def fill_new_Partner_details(self, user):
        """ This keyword is used to fill the new partner data in one go as the required data to be filled is picked from new_partner_info.json
        """
        unique_string= str(self.unix_timestamp()) 
        partner_data = self.load_json("test_data\\new_partner_info.json")
        for section in ["Basics", "Vendor pricelists", "Price margins", "Billing details"]:
            for field in partner_data[section]:
                if field in ["Type", "Status", "Plan Quotes"]:
                    self.wait_for_and_click_element(self.toggle_button.format(field, partner_data[section][field]))
                elif field in ["Parent Partner", "Country", "Business Countries", "On-premises", ""]:
                    self.select_from_list_by_label(self.dropdown_box.format(section, field), partner_data[section][field])
                elif field in ["Cloud margin", "Cloud vendor margin", "Saas margin"]:
                    self.wait_for_and_input_text(self.input_box.format(section, field), partner_data[section][field])
                else:
                    self.wait_for_and_input_text(self.input_box.format(section, field), partner_data[section][field]+unique_string)
    
    @keyword("User ${USER} submits the new partner data")
    def submit_new_partner_data(self, user):
        try:
            self.wait_for_and_click_element(self.create_button)
            self.wait_until_element_is_visible(self.success_alert,timeout=10)
            BuiltIn().log(self.get_webelement(self.success_alert).text)
            BuiltIn().should_contain(self.get_webelement(self.success_alert).text, "Partner has been created.", "The text is not matching")
        except Exception as e:
            ALerts_list = self.get_webelements(self.error_alert)
            for alert_text in ALerts_list:
                BuiltIn().log(alert_text.text)
        

        
