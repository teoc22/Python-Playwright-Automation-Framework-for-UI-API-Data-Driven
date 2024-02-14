# save_synthetic_data_page.py

import logging
from Engine.UI.Browser.browser_actions import BrowserActions

class SaveSyntheticDataPage:

    # Locators
    RESEARCH_PROJECT_INPUT_LOCATOR = 'input[placeholder="Introduce project name"]'
    SAVE_RESEARCH_PROJECT_BUTTON_LOCATOR = "button:has-text('Save research project')"
    CLOSE_RESEARCH_PROJECT_BUTTON_LOCATOR = "button:has-text('Close')"

    def __init__(self, page):
        self.actions = BrowserActions(page)
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def set_research_project_name(self, project_name):
        try:
            self.logger.info(f"Setting research project name to: {project_name}")
            self.actions.fill(self.RESEARCH_PROJECT_INPUT_LOCATOR, project_name)
            self.logger.info("Research project name set successfully")
        except Exception as e:
            self.logger.error(f"Error setting research project name: {e}")
            raise  # Re-raise the exception after logging

    def click_save_research_project(self):
        try:
            self.logger.info("Clicking 'Save research project' button")
            self.actions.click_and_wait_for_load(self.SAVE_RESEARCH_PROJECT_BUTTON_LOCATOR)
            self.logger.info("'Save research project' button clicked successfully")
        except Exception as e:
            self.logger.error(f"Error clicking 'Save research project' button: {e}")
            raise  # Re-raise the exception after logging

    def click_close_research_project(self):
        try:
            self.logger.info("Clicking 'Close' button")
            self.actions.click(self.CLOSE_RESEARCH_PROJECT_BUTTON_LOCATOR)
            self.logger.info("'Close' button clicked successfully")
        except Exception as e:
            self.logger.error(f"Error clicking 'Close' button: {e}")
            raise  # Re-raise the exception after logging


