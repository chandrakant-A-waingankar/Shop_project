from.HomePage import HomePage
from robot.api.deco import keyword


class Royalties(HomePage):
    def __init__(self):
        super().__init__()
        self.reporting_id = "css: "

    @keyword("User ${USER} verifies the Royalties page")
    def verify_Royalties_page(self, user):
        self.element_should_be_visible("h1")
        self.element_text_should_be("h1", "Royalties")
        self.element_should_be_visible("css: #accordion-partner-filters")
        self.element_should_be_visible("css: #cloud-filtered-data")

    @keyword("User ${USER} searches and opens the reporting ID: ${reporting_ID} in Royalties")
    def search_in_Royalties(self, user, reporting_ID):
        """
            This keyword is used to search and open desired reporting Id directly on the Royalties page

            **Arguments**
            - reporting_ID: (str)

            **Example**
            | User chan searches and opens the reporting ID: 602_CONVERSION_30 in Royalties |

        """
        self.wait_until_element_is_visible(self.reporting_id.format(reporting_ID))
        


