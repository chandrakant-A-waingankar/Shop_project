from Zoomba.GUILibrary import GUILibrary
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import sys
from time import sleep, time
sys.path.append(os.path.abspath(''))
import json


class Base(GUILibrary):
    def __init__(self):
        super().__init__()
        self.filter_textbox = "css: input[name={}]"
        self.search_button = "//button[text()='Search']"
        self.error_alert= "css: div.alert-text ul li"
        self.success_alert= "css: div.alert-text"
        self.select_all_checkbox= "\"input[name='select-all']\""
        self.manage_button= "css: button.btn-manage"

    @keyword("User ${USER} opens the browser")
    def open_window(self, user):
        browser:str = BuiltIn().get_variable_value('${BROWSER}')        

        if browser.lower() == 'chrome':
            chromeoptions =  webdriver.ChromeOptions()          
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
    

    def load_json(self, file_path):
        """
            Loads a JSON file and returns the data as a Python dictionary.
            
            :param file_path: Path to the JSON file.
            :return: Dictionary containing JSON data.
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading JSON file: {e}")
            return None  # Return None if there's an error
        

            

        