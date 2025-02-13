from Main.Pages.Quote import Quote
from Main.Pages.LoginPage import LoginPage
from Main.Pages.Lead import Lead


class ShopLibrary(LoginPage, Quote, Lead):
    def __init__(self):
        super().__init__()