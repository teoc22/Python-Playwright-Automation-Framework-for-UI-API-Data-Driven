# upload_data_page.py

import logging
from Engine.UI.Browser.browser_actions import BrowserActions

class UploadDataPage:

    # Locators
    FILE_INPUT_LOCATOR = 'input[type="file"]'
    GENERATE_STATISTICS_DATA_BUTTON_LOCATOR = "button:has-text('Next: Generate statistics data')"

    def __init__(self, page):
        self.actions = BrowserActions(page)
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def upload_file(self, file_path):
        try:
            self.logger.info(f"Uploading file from path: {file_path}")
            self.actions.set_input_files(self.FILE_INPUT_LOCATOR, file_path)
            self.logger.info("File upload successful")
        except Exception as e:
            self.logger.error(f"Error during file upload: {e}")
            raise  # Re-raise the exception after logging

    def click_generate_statistics_data(self):
        try:
            self.logger.info("Clicking 'Next: Generate Statistics Data' button")
            self.actions.click(self.GENERATE_STATISTICS_DATA_BUTTON_LOCATOR)
            self.logger.info("'Next: Generate Statistics Data' button clicked")
        except Exception as e:
            self.logger.error(f"Error clicking 'Next: Generate Statistics Data' button: {e}")
            raise  # Re-raise the exception after logging

