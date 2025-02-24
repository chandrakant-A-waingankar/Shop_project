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
        self.deactivate_button= "//a[text()=' Deactivate']"
        self.actions_button= "//button[contains(.,'Actions')]"
        self.partner_name= "//a[text()='{}']"

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
        

    @keyword("User ${USER} deactivates partner with name ${ptnr_name}")
    def _delete_partner(self, user, ptnr_name):
        """
            This keyword is ued to deactivate a specific partner.

            **Arguments**
            - ptnr_name: (str) 

            **Example**
            | User chan deactivates partner with name Mumbai Technologies |
        """
        self.wait_for_and_click_element(self.partner_name.format(ptnr_name))
        self.wait_for_and_click_element(self.actions_button)
        self.wait_for_and_click_element(self.deactivate_button)


    @keyword("User ${USER} searches for partner with ${filter} having value ${value}")
    def search_partner(self, user, filter, value):
        """
            This keyword is used to search partner using filters name /partner_id of the partner

            **Arguments**
            - filter: (str)   options- name | partner_id
            - value: (str)

            **Example**
            | User chan searches for partner with name having value Mumbai Technologies |
            | User chan searches foe partner with partner_id having value 212145 |
        """
        self.wait_until_element_is_visible(self.filter_textbox.format(filter))
        self.clear_element_text(self.filter_textbox.format(filter))
        self.wait_for_and_input_text(self.filter_textbox.format(filter), value)
        self.wait_for_and_click_element(self.search_button)
        self.wait_until_element_is_visible("//table[contains(@class, 'viki-table-partners')]//tbody//tr//td", timeout=10)
        list_of_leads = []
        for element in self.get_webelements("//table[contains(@class, 'viki-table-partners')]//tbody//tr//td"):
            list_of_leads.append(element.text)

        BuiltIn().should_contain(list_of_leads, value, f"The {value} is not present in Partners")
