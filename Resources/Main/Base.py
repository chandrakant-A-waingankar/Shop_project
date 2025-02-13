from Zoomba.GUILibrary import GUILibrary
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import sys
import time
sys.path.append(os.path.abspath(''))


class Base(GUILibrary):
    def __init__(self):
        super().__init__()

    @keyword("User ${USER} opens the browser")
    def open_window(self, user):
        browser:str = BuiltIn().get_variable_value('${BROWSER}')

        if browser.lower() == 'chrome':
            chromeoptions = webdriver.ChromeOptions()
            service = Service(BuiltIn().get_variable_value('${PATH_TO_DRIVER}'))
            self.open_browser(url="https://google.com",browser="chrome",service=service,options=chromeoptions)
            self.maximize_browser_window()

        elif browser.lower() == 'firefox':
            ffoptions = webdriver.FirefoxOptions()
            executable_path = BuiltIn().get_variable_value('${PATH_TO_DRIVER}')
            self.open_browser(browser='firefox',options=chromeoptions,executable_path=executable_path)
            self.maximize_browser_window()

        else:
            print('Browser not supported')


    @keyword("User ${USER} navigates to the url")
    def navigate_to_url(self, user):
        url = BuiltIn().get_variable_value('${URL}')
        self.go_to(url)
        self.go_to(url)

    @keyword('Get Unit Timestamp')
    def unix_timestamp(self):
        """ Returns current unix timestamp.
        """
        unix_timestamp = int(time())
        return unix_timestamp
        

            

        