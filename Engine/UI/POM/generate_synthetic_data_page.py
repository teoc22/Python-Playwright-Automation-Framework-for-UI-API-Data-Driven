# generate_synthetic_data_page.py

import logging
from Engine.UI.Browser.browser_actions import BrowserActions

class GenerateSyntheticDataPage:

    # Locators
    SYNTHETIC_DATA_SET_BUTTON_LOCATOR = "text='Synthetic data set'"
    NEXT_RESEARCH_PROJECT_BUTTON_LOCATOR = "button:has-text('Next: Save research project')"

    def __init__(self, page):
        self.actions = BrowserActions(page)
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def click_synthetic_data_set(self):
        try:
            self.logger.info("Clicking on 'Synthetic data set' button")
            self.actions.click(self.SYNTHETIC_DATA_SET_BUTTON_LOCATOR)
            self.logger.info("'Synthetic data set' button clicked successfully")
        except Exception as e:
            self.logger.error(f"Error occurred while clicking 'Synthetic data set' button: {e}")
            raise  # Re-raise the exception after logging

    def click_next_research_project(self):
        try:
            self.logger.info("Clicking on 'Next: Save research project' button")
            self.actions.click_and_wait_for_load(self.NEXT_RESEARCH_PROJECT_BUTTON_LOCATOR)
            self.logger.info("'Next: Save research project' button clicked successfully")
        except Exception as e:
            self.logger.error(f"Error occurred while clicking 'Next: Save research project' button: {e}")
            raise  # Re-raise the exception after logging
