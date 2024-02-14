# configure_synthetic_data_page.py

import logging
from .base_page import BasePage
from Engine.UI.Browser.browser_actions import BrowserActions

class ConfigureSyntheticDataPage(BasePage):

    # Locators
    SYNTHETIC_RECORDS_INPUT_LOCATOR = 'input[placeholder="0"]'
    GENERATE_SYNTHETIC_DATA_BUTTON_LOCATOR = "button:has-text('Next: Generate synthetic data')"

    def __init__(self, page):
        super().__init__(page)
        self.actions = BrowserActions(page)
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def set_synthetic_records(self, num_records):
        try:
            self.logger.info(f"Setting synthetic records to {num_records}")
            self.actions.wait_for_selector_and_fill(self.SYNTHETIC_RECORDS_INPUT_LOCATOR, str(num_records))
            self.logger.info("Synthetic records set successfully")
        except Exception as e:
            self.logger.error(f"Error setting synthetic records: {e}")
            raise  # Re-raise the exception after logging
        
    def click_generate_synthetic_data(self):
        try:
            self.logger.info("Clicking 'Next: Generate synthetic data' button")
            self.actions.click(self.GENERATE_SYNTHETIC_DATA_BUTTON_LOCATOR)
            self.logger.info("'Next: Generate synthetic data' button clicked")
        except Exception as e:
            self.logger.error(f"Error clicking 'Next: Generate synthetic data' button: {e}")
            raise  # Re-raise the exception after logging

