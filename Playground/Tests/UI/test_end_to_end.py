# Import logging
import logging
from logger_config import setup_logger
import pytest

# Set up the logger
setup_logger()
logger = logging.getLogger(__name__)

from Engine.UI.Browser.browser_setup import BrowserUtils
from Engine.UI.POM.base_page import BasePage
from Engine.UI.POM.upload_data_page import UploadDataPage
from Engine.UI.POM.analyse_statistics_page import AnalyseStatisticsPage
from Engine.UI.POM.configure_synthetic_data_page import ConfigureSyntheticDataPage
from Engine.UI.POM.generate_synthetic_data_page import GenerateSyntheticDataPage
from Engine.UI.POM.save_export_project_data_page import SaveSyntheticDataPage
from Playground.Resources.UI.file_path_ui import file_path_ui 
from Playground.Resources.UI.project_name_ui import project_name
from Playground.Resources.UI.initial_url_ui import INITIAL_URL

def test_end_to_end():
    # Start of the end-to-end test
    logger.info("Starting the end-to-end test")

    try:
        # Setup the browser for testing
        browser_utils = BrowserUtils()
        page = browser_utils.page

        # Navigate to the initial page
        logger.info(f"Navigating to initial URL: {INITIAL_URL}")
        base_page = BasePage(page)
        base_page.navigate_to(INITIAL_URL)
        page.wait_for_load_state('networkidle')
        logger.info("Navigation to initial URL completed")

        # Upload data and proceed to generate statistics
        logger.info("Uploading data and navigating to generate statistics")
        upload_data_page = UploadDataPage(page)
        upload_data_page.upload_file(file_path_ui)
        upload_data_page.click_generate_statistics_data()
        page.wait_for_load_state('networkidle')

        # Configure and analyze statistics
        logger.info("Configuring and analyzing statistics")
        analyse_statistics_page = AnalyseStatisticsPage(page)
        analyse_statistics_page.click_configure_outcome()
        page.wait_for_load_state('networkidle')

        # Configure synthetic data
        logger.info("Configuring synthetic data")
        configure_synthetic_data_page = ConfigureSyntheticDataPage(page)
        configure_synthetic_data_page.set_synthetic_records(10)
        configure_synthetic_data_page.click_generate_synthetic_data()
        page.wait_for_load_state('networkidle')

        # Generate synthetic data
        logger.info("Generating synthetic data")
        generate_synthetic_data_page = GenerateSyntheticDataPage(page)
        generate_synthetic_data_page.click_synthetic_data_set()
        page.wait_for_load_state('networkidle')
        generate_synthetic_data_page.click_next_research_project()
        page.wait_for_load_state('networkidle')

        # Save and export the project data
        logger.info("Saving and exporting project data")
        save_synthetic_data_page = SaveSyntheticDataPage(page)
        save_synthetic_data_page.set_research_project_name(project_name)
        save_synthetic_data_page.click_save_research_project()
        page.wait_for_load_state('networkidle')
        save_synthetic_data_page.click_close_research_project()
        page.wait_for_load_state('networkidle')

        logger.info("End-to-end test completed successfully")
    except Exception as e:
        # Log any exceptions encountered during the test
        logger.error(f"Error encountered during end-to-end test: {e}")
        raise
    finally:
        # Teardown the browser and log the completion
        browser_utils.teardown()
        logger.info("Browser teardown completed")

# Run the test
if __name__ == "__main__":
    test_end_to_end()
