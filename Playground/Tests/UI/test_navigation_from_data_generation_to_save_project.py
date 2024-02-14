# test_navigation_from_data_generation_to_save_project.py

import logging
import pytest
from logger_config import setup_logger
from Engine.UI.Browser.browser_setup import BrowserUtils
from Engine.UI.POM.base_page import BasePage
from Playground.Resources.UI.initial_url_ui import INITIAL_URL

# The integration marker
@pytest.mark.integration
def test_navigation_from_data_generation_to_save_project():
    setup_logger()
    logger = logging.getLogger(__name__)

    try:
        browser_utils = BrowserUtils()
        page = browser_utils.page

        # Navigate to the Data Generation page
        data_generation_page_url = INITIAL_URL + "/data-generation"
        base_page = BasePage(page)
        base_page.navigate_to(data_generation_page_url)
        
        page.wait_for_load_state('networkidle')

        # Simulate action that leads to the Project Save page
        page.click("text='Generate and Save Data'")
        page.wait_for_load_state('networkidle')

        # Verify successful navigation
        assert "save-project" in page.url, "Failed to navigate from Data Generation to Project Save"
        
        logger.info("Successfully navigated from Data Generation to Project Save")
    except Exception as e:
        logger.error(f"Error encountered during navigation from Data Generation to Project Save: {e}")
        raise
    finally:
        browser_utils.teardown()

if __name__ == "__main__":
    test_navigation_from_data_generation_to_save_project()