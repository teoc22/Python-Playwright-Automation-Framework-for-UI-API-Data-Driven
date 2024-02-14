# base_page.py

import logging
from Engine.UI.Browser.browser_actions import BrowserActions

class BasePage:
    def __init__(self, page):
        self.actions = BrowserActions(page)
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def navigate_to(self, url):
        # Log the action of navigating to a URL
        self.logger.info(f"Attempting to navigate to URL: {url}")
        try:
            self.actions.navigate_to(url)
            # Log a message after successful navigation
            self.logger.info(f"Successfully navigated to {url}")
        except Exception as e:
            # Log any exceptions that occur during navigation
            self.logger.error(f"Error navigating to {url}: {e}")
            raise  # Re-raise the exception after logging