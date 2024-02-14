# test_navigation_to_upload_data_page.py

import logging
import pytest
from logger_config import setup_logger
from Engine.UI.Browser.browser_setup import BrowserUtils
from Engine.UI.POM.base_page import BasePage
from Playground.Resources.UI.initial_url_ui import INITIAL_URL

# The integration marker
@pytest.mark.integration
def test_navigation_to_upload_data_page():
    setup_logger()
    logger = logging.getLogger(__name__)

    try:
        browser_utils = BrowserUtils()
        page = browser_utils.page

        # Navigate to the initial URL
        base_page = BasePage(page)
        base_page.navigate_to(INITIAL_URL)
        
        # Assume there's a button or link to go to the Upload Data Page
        upload_data_link_locator = "text='Upload Data'"
        page.click(upload_data_link_locator)
        
        # Wait for the upload data page to load
        page.wait_for_load_state('networkidle')

        # Verify the URL or a unique element on the Upload Data Page
        assert "upload-data" in page.url, "Failed to navigate to the Upload Data Page"
        
        logger.info("Successfully navigated to the Upload Data Page")
    except Exception as e:
        logger.error(f"Error encountered during navigation to the Upload Data Page: {e}")
        raise
    finally:
        browser_utils.teardown()

# Remember to call this function or set it up to run with your test suite
if __name__ == "__main__":
    test_navigation_to_upload_data_page()