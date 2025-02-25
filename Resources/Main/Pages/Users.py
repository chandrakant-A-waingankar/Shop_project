from .HomePage import HomePage
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
import os

class Users(HomePage):
    def __init__(self):
        super().__init__()
        self.avatar_img= "css: input[name=avatar_upload]"
        self.basic_info_field= "css: input[name={}]"
        self.roles = "//label[contains(.,'{}')]"
        self.permission = "//div[label[contains(text(), '{}')]]/descendant::label[contains(., '{}')]"
        self.create_button = "//button[text()='Create']"
        


    @keyword("User ${USER} uploads avatar image ${path_to_avatar_img}")
    def upload_avatar(self, user, path_to_avatar_img):
        """ This keyword is used to upload avatar image while creating new user

        **Argumnets**
        - path to avatar image:  String

        **Note**
        Accepted files: .png, .jpg, .jpeg, .svg, .gif
        
        **Example**
        | user chan uploads avatar image test_data/MyImage.png |
        """
        self.wait_until_element_is_visible("css: div#imagePreview")
        absolute_path = os.path.abspath(path_to_avatar_img)
        self.choose_file(self.avatar_img, absolute_path)


    @keyword("User ${USER} enters ${info_field} as ${info_field_value}")
    def enter_basic_details(self, user, info_field, info_field_value):
        """ 
        This keyword is used to fill the basic information details of the user

        **Arguments**
        - info_field: String - options: name | email | position | password | password_confirmation | 
        """
        self.wait_for_and_input_text(self.basic_info_field.format(info_field), info_field_value)

    @keyword("User ${USER} assigns the role ${role_name} to the new user")
    def assign_role(self, user, role_name):
        """ This keyword is ued to assign the roles to the new user while creating it

            **Arguments**
            - role_name: String - options: | Admin | Manager | Partner | Sales | Support | Human Relations (HR) |

            **Example**
            | User chan assigns the role Admin to the new user |
        """
        self.wait_for_and_click_element(self.roles.format(role_name))

    @keyword("User ${USER} assigns permission for ${permission_for} to ${permission_to}")
    def assign_permission(self, user, permission_for, permission_to):
        """ This keyword is used to assign permissions to the new user 

            **Arguments**
            - permisssion_for: String 
            - permission_to: String

            ***Note**
            - write the exact word which are present on front-end considering case-sensitive nature of this method

            **Example**
            | User chan assigns permission for Clouds to Overiview |
        """
        self.wait_for_and_click_element(self.permission.format(permission_for, permission_to))


    @keyword("User ${USER} submits the new user data ")
    def submits_new_user_data(self, user):
        try:
            self.wait_for_and_click_element(self.create_button)
            self.wait_until_element_is_visible(self.success_alert,timeout=10)
            self.element_text_should_be(self.success_alert,r"User \w+ successfully created.")

        except Exception as e:
            ALerts_list = self.get_webelements(self.error_alert)
            for alert_text in ALerts_list:
                BuiltIn().log(alert_text.text)     


    @keyword("User ${USER} searches the Users by ${filter_name} as ${value}")
    def search_in_leads(self, USER=None, filter_name=None, value=None):
        """ This keyword is used to search desired record using filter Name/email/position 

            **Arguments**
            - filter_name: name | email | position
            - value: String 

            **Example**
            | User chan searches the Users by name as Marco Polo |
            | User Chan searches the Users by email as tester@gemail.com |
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

    