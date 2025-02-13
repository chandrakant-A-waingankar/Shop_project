from ..Base import Base
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
import os
import sys
sys.path.append(os.path.abspath(''))


class HomePage(Base):
    """This Class is used to handle the elements and functionalities present on Home Page"""
    def __init__(self):
        super().__init__()
        self.homepage_header_element = "//header[@class='staging-environment']"
        self.menu_button = "css:button.sidebar-expand"
        self.left_menu_panel = "css: nav#sidebar"
        self.page_link = "//nav[@id='sidebar']/ul/li/a[contains(text(),'{}')]"
        self.page_link_under_dropdown = "//nav[@id='sidebar']/ul/li/a[contains(text(),'{}')]/following-sibling::ul/li/a[contains(text(),'{}')]"
        self.new_button = "css:button.btn.create-new-item-btn"
        self.shop_logo = "css:div.header-logo"
        self.user_button = "css:span.user-button"
        self.user_btn_dropdown = "css:span.user-button + div.dropdown-menu"
        self.manual_reviews_info_area = "css:div.k-portlet"
        self.sign_out = "//a[contains(text(),'Sign Out')]"
        self.new_option = "//h3[text()='{}']/following-sibling::a"
        

    @keyword("User ${USER} verifies Homepage")
    def verify_homepage(self, user):
        """
            This keyword verifies whether the Home page is opened properly or not.
            It verifies that Home page header contains Menu button, New button, Shop logo(that too in center), 
            user button, Manual reviews information window
        """
        self.element_should_be_visible(self.homepage_header_element)
        self.element_should_be_visible(self.menu_button)
        self.element_should_be_visible(self.new_button)
        self.element_should_be_visible(self.shop_logo)        
        BuiltIn().should_contain(self.get_element_attribute(self.shop_logo,"class"),"text-center")
        self.element_should_be_visible(self.user_button)
        self.element_should_be_visible(self.manual_reviews_info_area)


    @keyword("User ${USER} Logs out the Shop")
    def logout(self, user):
        """ This keyword is used for logging out of application
        """
        self.wait_for_and_click_element(self.user_button)
        self.wait_until_element_is_visible(self.user_btn_dropdown)
        self.wait_for_and_click_element(self.sign_out)
        self.wait_until_element_is_not_visible(self.shop_logo)

    def select_new_option(self, option):
        self.wait_for_and_click_element(self.new_button)
        if option.lower() == "cloud":
            self.wait_for_and_click_element(self.new_option.format("Cloud"))
        elif option.lower() == "saas":
            self.wait_for_and_click_element(self.new_option.format("SaaS"))
        elif option.lower() == "leads":
            self.wait_for_and_click_element(self.new_option.format("Leads"))
        else:
            print("Option not supported, Please select valid option")


    def open_left_menu(self):
        """
        This function is used to open the left Menu 
        """
        self.wait_for_and_click_element(self.menu_button)
        self.wait_until_element_is_visible(self.left_menu_panel)

    @keyword("User ${USER} Opens ${page_name} Page from left menu")
    def open_page_from_leftmenu(self,user, page_name):
        """
            This keyword is used to open desired page from left menu (which is not under any dropdown)

            **args:**
            - user: str
            - page_name: str

            **Example:**
                | User Chan opens Royalties Page from left menu |
                | User Chan opens Documents Page from left menu | 

        """
        if not page_name in ["Leads", "Services", "Partners", "Pricelist", "Extras", "Users"]:
            self.open_left_menu()
            self.wait_for_and_click_element(self.page_link.format(page_name))
        else:
            BuiltIn().log("Please refer another keyword \"User $user Opens page $new under $Leads dropdown from left menu\"")

    @keyword("User ${USER} Opens page ${page_name} under ${dropdown} dropdown from left menu")
    def open_page_under_dropdown(self,user, page_name, dropdown):
        """
            This keyword is used to open desired page from left menu (which is under dropdown)

            **args:**
            - user: str = users name 
            - page_name: str = Name of page to be opened
            - dropdown: str = dropdown name under which the page to be opened is present

            **Example:**
                | User Chan opens Page New under Services from left menu |
                | User Chan opens Page Overview under Leads from left menu | 

        """
        if dropdown in ["Leads", "Services", "Partners", "Pricelist", "Extras", "Users"]:
            self.open_left_menu()
            self.wait_for_and_click_element(self.page_link.format(dropdown))
            self.wait_for_and_click_element(self.page_link_under_dropdown.format(dropdown,page_name))
        else:
            BuiltIn().log("Please refer another keyword \"User $user Opens page $Leads from left menu\"")
