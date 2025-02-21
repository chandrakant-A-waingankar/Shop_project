from ..Base import Base
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
import os
import sys
sys.path.append(os.path.abspath(''))

class LoginPage(Base):
    def __init__(self):
        super().__init__()
        self.login_area = "css:.card-body"


    @keyword("User ${USER} logs in to the Shop")
    def login(self, user):
        self.wait_until_element_is_visible(self.login_area,timeout=300)
        self.clear_element_text('id:email')
        self.clear_element_text('id:password')
        self.input_text('id:email', BuiltIn().get_variable_value('${USERNAME}'))
        self.input_text('id:password', BuiltIn().get_variable_value('${PASSWORD}'))
        self.wait_for_and_click_element("//button[contains(text(),'Sign In')]")
        


     