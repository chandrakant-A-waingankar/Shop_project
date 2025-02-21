from Main.Pages.Quote import Quote
from Main.Pages.LoginPage import LoginPage
from Main.Pages.Lead import Lead
from Main.Pages.Services import Services
from Main.Pages.Users import Users
from Main.Pages.Partners import Partners


class ShopLibrary(LoginPage, Quote, Lead, Services, Users, Partners):
    def __init__(self):
        super().__init__()