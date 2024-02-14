# test_navigation_to_analyze_statistics_page.py

# Import necessary modules and classes
import logging
import pytest
from logger_config import setup_logger
from Engine.UI.Browser.browser_setup import BrowserUtils
from Engine.UI.POM.base_page import BasePage
from Playground.Resources.UI.initial_url_ui import INITIAL_URL

# The integration marker
@pytest.mark.integration
def test_navigation_to_analyze_statistics_page():
    setup_logger()
    logger = logging.getLogger(__name__)

    try:
        # Initialize the browser utilities and get the page object
        browser_utils = BrowserUtils()
        page = browser_utils.page

        # Navigate directly to the Analyze Statistics page
        analyze_statistics_page_url = INITIAL_URL + "/analyze-statistics"
        base_page = BasePage(page)
        base_page.navigate_to(analyze_statistics_page_url)
        
        # Wait for the page's network activities to idle
        page.wait_for_load_state('networkidle')
        
        # Verify the URL or a unique element on the Analyze Statistics Page
        assert "analyze-statistics" in page.url, "Failed to navigate to the Analyze Statistics Page"
        
        logger.info("Successfully navigated to the Analyze Statistics Page")
    except Exception as e:
        logger.error(f"Error encountered during navigation to the Analyze Statistics Page: {e}")
        raise
    finally:
        # Clean up by closing the browser context
        browser_utils.teardown()

# This allows the script to be run standalone or as part of a test suite
if __name__ == "__main__":
    test_navigation_to_analyze_statistics_page()
