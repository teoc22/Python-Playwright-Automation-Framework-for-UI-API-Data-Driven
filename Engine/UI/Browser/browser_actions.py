# browser_actions.py

import logging

class BrowserActions:
    def __init__(self, page):
        self.page = page
        self.logger = logging.getLogger(__name__)

    def navigate_to(self, url):
        try:
            self.logger.info(f"Navigating to URL: {url}")
            self.page.goto(url)
            self.logger.info(f"Successfully navigated to URL: {url}")
        except Exception as e:
            self.logger.error(f"Error navigating to URL {url}: {e}")
            raise

    def set_input_files(self, locator, file_path):
        try:
            self.logger.info(f"Setting input files at {locator} with {file_path}")
            self.page.locator(locator).set_input_files(file_path)
            self.logger.info("Input file set successfully")
        except Exception as e:
            self.logger.error(f"Error setting input files: {e}")
            raise

    def click(self, locator):
        try:
            self.logger.info(f"Clicking on locator: {locator}")
            self.page.locator(locator).click()
            self.logger.info(f"Clicked on locator: {locator}")
        except Exception as e:
            self.logger.error(f"Error clicking on locator {locator}: {e}")
            raise

    def wait_for_selector_and_fill(self, locator, text):
        try:
            self.logger.info(f"Waiting for selector and filling text at {locator}")
            element = self.page.wait_for_selector(locator)
            element.click()
            element.fill(text)
            self.logger.info(f"Filled text at {locator}")
        except Exception as e:
            self.logger.error(f"Error in wait_for_selector_and_fill at {locator}: {e}")
            raise

    def click_and_wait_for_load(self, locator):
        try:
            self.logger.info(f"Clicking and waiting for load at {locator}")
            self.page.locator(locator).click()
            self.page.wait_for_load_state('load')
            self.logger.info(f"Completed click and wait at {locator}")
        except Exception as e:
            self.logger.error(f"Error in click_and_wait_for_load at {locator}: {e}")
            raise

    def fill(self, locator, value):
        try:
            self.logger.info(f"Filling {value} at {locator}")
            input_field = self.page.locator(locator)
            input_field.fill(value)
            self.logger.info(f"Filled {value} at {locator}")
        except Exception as e:
            self.logger.error(f"Error filling {value} at {locator}: {e}")
            raise