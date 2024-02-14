# analyse_statistics_page.py

import logging
from Engine.UI.Browser.browser_actions import BrowserActions

class AnalyseStatisticsPage:

    # Locators
    CONFIGURE_OUTCOME_BUTTON_LOCATOR = "button:has-text('Next: Configure Outcome')"

    def __init__(self, page):
        self.actions = BrowserActions(page)
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def click_configure_outcome(self):
        try:
            self.logger.info("Attempting to click 'Next: Configure Outcome' button")
            self.actions.click(self.CONFIGURE_OUTCOME_BUTTON_LOCATOR)
            self.logger.info("'Next: Configure Outcome' button clicked")
        except Exception as e:
            self.logger.error(f"Error clicking 'Next: Configure Outcome' button: {e}")
            raise  # Re-raise the exception after logging


