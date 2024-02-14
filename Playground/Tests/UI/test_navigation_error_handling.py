# test_navigation_error_handling.py

import logging
import pytest
from logger_config import setup_logger
from Engine.UI.Browser.browser_setup import BrowserUtils
from Engine.UI.POM.base_page import BasePage
from Playground.Resources.UI.initial_url_ui import INITIAL_URL

def test_navigation_error_handling():
    setup_logger()
    logger = logging.getLogger(__name__)

    try:
        browser_utils = BrowserUtils()
        page = browser_utils.page

        # Attempt to navigate to a non-existent page to simulate a failure
        faulty_page_url = INITIAL_URL + "/non-existent-page"
        base_page = BasePage(page)
        base_page.navigate_to(faulty_page_url)
        
        # Optionally, wait for a specific error message or element indicating failure
        error_indicator_locator = "text='Error message or Page Not Found text'"
        page.wait_for_selector(error_indicator_locator, timeout=5000)
        
        # Verify that the error indicator is indeed present
        assert page.is_visible(error_indicator_locator), "Expected error indicator not found on the page"
        
        logger.info("Navigation error handling verified successfully")
    except Exception as e:
        logger.error(f"Error encountered during navigation error handling test: {e}")
        raise
    finally:
        browser_utils.teardown()

if __name__ == "__main__":
    test_navigation_error_handling()
