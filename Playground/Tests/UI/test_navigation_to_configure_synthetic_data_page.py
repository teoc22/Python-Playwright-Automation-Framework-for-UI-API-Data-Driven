# test_navigation_to_configure_synthetic_data_page.py

import logging
import pytest
from logger_config import setup_logger
from Engine.UI.Browser.browser_setup import BrowserUtils
from Engine.UI.POM.base_page import BasePage
from Playground.Resources.UI.initial_url_ui import INITIAL_URL

# The integration marker
@pytest.mark.integration
def test_navigation_to_configure_synthetic_data_page():
    setup_logger()
    logger = logging.getLogger(__name__)

    try:
        browser_utils = BrowserUtils()
        page = browser_utils.page

        # Directly navigate to the Configure Synthetic Data page
        configure_synthetic_data_page_url = INITIAL_URL + "/configure-synthetic-data"
        base_page = BasePage(page)
        base_page.navigate_to(configure_synthetic_data_page_url)
        
        page.wait_for_load_state('networkidle')
        
        # Verify the URL or a unique element on the page
        assert "configure-synthetic-data" in page.url, "Failed to navigate to the Configure Synthetic Data Page"
        
        logger.info("Successfully navigated to the Configure Synthetic Data Page")
    except Exception as e:
        logger.error(f"Error encountered during navigation to the Configure Synthetic Data Page: {e}")
        raise
    finally:
        browser_utils.teardown()

if __name__ == "__main__":
    test_navigation_to_configure_synthetic_data_page()