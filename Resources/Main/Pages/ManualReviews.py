from .HomePage import HomePage
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn


class ManualReviews(HomePage):
    def __init__(self):
        super().__init__()

    @keyword("User ${USER} verifes the Manual reviews Page")
    def verify_manual_review_page(self, user):
        """ This keyword is used to check and verify that the Manual reviews page is opened correctly or not
        """
        self.element_should_be_visible("h1")
        self.element_text_should_be("h1", "Manual Reviews")
        self.element_should_be_visible("css: #accordion-partner-filters") # checking whether the filter section is visible or not
        self.element_should_be_visible("css: #cloud-filtered-data") # checking whether the data table is displayed or not

    @keyword("User ${USER} searches in the manual reviews by filter ${filter_name} with ${value}")
    def  search_in_manual_reviews(self, user, filter_name: str, value):
        """
            This keyword is used to search in the Manual reviews page by applying the desired filter provided

            **Arguments:**
            - filter_name: (str) name of filter to be applied =  options => company | name | email
            - value: (str) value of that filter

            **Example**
            | User chan searches in the manual reviews by filter company with  | 
        """
        self.wait_until_element_is_visible(self.filter_textbox.format(filter_name.lower()))
        self.clear_element_text(self.filter_textbox.format(filter_name.lower()))
        self.wait_for_and_input_text(self.filter_textbox.format(filter_name.lower()), value)
        self.wait_for_and_click_element(self.search_button)
        self.wait_until_element_is_visible("//table[contains(@class, 'leads-table')]//tbody//tr//td", timeout=10)
        list_of_leads = []
        for element in self.get_webelements("//table[contains(@class, 'leads-table')]//tbody//tr//td"):
            list_of_leads.append(element.text)

        BuiltIn().should_contain(list_of_leads, value, f"The {value} is not present in Manual Reviews")
    
    @keyword("User ${USER} selects all displayed records")
    def select_all_records(self, user):
        self.wait_for_and_select_checkbox(self.select_all_checkbox)

    @keyword("User ${USER} marks ${Reject_or_Ignore} to selected records")
    def mark_records(self, user, Reject_or_Ignore):
        """
            This keyword is used to Reject/ Ignore selected record(s)

            **Arguments**
            - Reject_or_Ignore: (Str) options =>  Reject | Ignore

            **Example**
            | User chan marks Reject to selected records | 
        """
        self.wait_for_and_click_element(self.manage_button)
        self.wait_for_and_click_element("link: {}".format(Reject_or_Ignore))
        self.wait_for_and_click_element("//button[text()='Yes']")

