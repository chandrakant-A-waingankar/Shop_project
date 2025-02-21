import builtins
from .HomePage import HomePage
from robot.api.deco import keyword
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from Zoomba.GUILibrary import BuiltIn
from typing import List



class Lead(HomePage):
    """ This class is used to handle the elements and function present on Lead page and its subpages """
    def __init__(self):
        super().__init__()
        self.page_heading = "//h1"
        self.assign_to_radio_button = "//label[text()='{}']"
        self.basic_info_dropdown = "//select[@title='{}']"
        self.lead_description = "css:textarea#description"
        self.select_a_field_button = "css: button[title='Select a Field']"
        self._field_input_textbox = ""
        self.fields_container = "css: div#fields-container>div"
        #self.filter_textbox = "css: input[name={}]"
        #self.search_button = "//button[text()='Search']"

    @keyword("User ${USER} creates new Lead")
    def create_new_lead(self, user):
        """" Here this keyword actually opens up the New Lead creation page """
        self.select_new_option("Leads")
        self.element_text_should_be(self.page_heading, f"Create a Lead")

    @keyword("User ${USER} selects Assigns To radio option as: ${option}")
    def select_assign_to_option(self, user, option):
        """
        This keyword is used to select the radio buttons regarding "Assign To" on Leads creation page

        **Arguments:**
        - option: Direct | Partner

        Example: 
        | User Bravo selects option as: Partner |
        """
        self.wait_for_and_click_element(self.assign_to_radio_button.format(option))

    @keyword("User ${USER} selects ${field} option as: ${option}")
    def select_value_from_dropdown(self, user, field, option):
        """
        This keyword is used to select the values in vaious basic info details fields such as Source, Stage and Country

        Arguments:
                    field: str
                    option: str
        Note:
                    for Source = Website | Shop | Sales | representative | Business card | Email
                    for Stage = Open | Qualification | Proposal sent | Proposal and Contract Closing | Closed Won | Closed Lost | Finished | Refunded Order
                    for Country = Country names as on application.


        Example:    User Bravo selects Source option as: Website
                    User Bravo selects Stage option as: Open
                    user Bravo select Country option as: India   
        """
        self.select_from_list_by_label(self.basic_info_dropdown.format(field),option)

        
    @keyword("User ${USER} enters description: ${description_text}")
    def enter_description(self, user, description_text):
        """
        This keyword is used to enter any description regarding the Lead. However it is not mandatory. 
        """
        self.wait_for_and_input_text(self.lead_description,description_text)

    @keyword("User ${USER} selects ${field_option} on field ${row_number} and enters value as: ${value_in_textbox}")
    def select_field_and_enter_value(self, user, field_option, row_number: int, value_in_textbox):

        list_of_fields: List[WebElement] = self.get_webelements(self.fields_container)
        field_dropdown = list_of_fields[row_number-1].find_element(By.CSS_SELECTOR,"select")
        value_textbox = list_of_fields[row_number-1].find_element(By.CSS_SELECTOR,"input")
        
        self.select_from_list_by_label(field_dropdown, field_option)
        self.wait_for_and_input_text(value_textbox, value_in_textbox)

    @keyword("User ${USER} Adds item to user details")
    def add_item(self,user):
        self.wait_for_and_click_element("css: button.create-field")


    @keyword("User ${USER} Submits the Lead creation form")
    def submit_form(self, user):
        try:
            self.wait_for_and_click_element("css: .card-footer button")
            self.wait_until_element_is_visible("css: div.alert-success div.alert-text")
            self.element_text_should_be("css: div.alert-text","Lead has been created.")

        except Exception as e:
            Alert_list = self.get_webelements("css: div.alert-text ul li")
            for alert_text in Alert_list:
                BuiltIn().log(alert_text.text)

    @keyword("User ${USER} searches the leads by ${filter_name} as ${value}")
    def search_in_leads(self, USER=None, filter_name=None, value=None):
        """ This keyword is used to search desired record using filter company/email 

            **Arguments**
            - filter_name: company | email
            - value: String 

            **Example**
            | User chan searches the leads by company as United Computer pvt ltd. |
            | User Chan searches the leads by email as tester@gemail.com |
        """
        self.wait_until_element_is_visible(self.filter_textbox.format(filter_name.lower()))
        self.clear_element_text(self.filter_textbox.format(filter_name.lower()))
        self.wait_for_and_input_text(self.filter_textbox.format(filter_name.lower()), value)
        self.wait_for_and_click_element(self.search_button)
        self.wait_until_element_is_visible("//table[contains(@class, 'leads-table')]//tbody//tr//td", timeout=10)
        list_of_leads = []
        for element in self.get_webelements("//table[contains(@class, 'leads-table')]//tbody//tr//td"):
            list_of_leads.append(element.text)

        BuiltIn().should_contain(list_of_leads, value, f"The {value} is not present in Leads")


    @keyword("User ${USER} selects the displayed record(s) in leads")
    def select_displayed_records_in_leads(self, user):
        """ This keyword selects all the displayed records
        """
        
        self.execute_javascript("document.querySelector({}).click();".format(self.select_all_checkbox))

    @keyword("User ${USER} deletes the selected records in leads")
    def delete_selected_records_in_leads(self, user):
        """ This keyword is used to delete the selected records
        """
        self.wait_for_and_click_element(self.manage_button)
        self.wait_for_and_click_element("link: Delete")

        
        



    

        