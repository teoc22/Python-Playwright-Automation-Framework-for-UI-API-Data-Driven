# test_data_driven.py

import sys
import os

# Import necessary modules
import pytest
import logging
from logger_config import setup_logger
from Engine.UI.Browser.browser_setup import BrowserUtils
from Engine.UI.POM.base_page import BasePage
from Engine.UI.POM.upload_data_page import UploadDataPage
from Engine.UI.POM.analyse_statistics_page import AnalyseStatisticsPage
from Engine.UI.POM.configure_synthetic_data_page import ConfigureSyntheticDataPage
from Engine.UI.POM.generate_synthetic_data_page import GenerateSyntheticDataPage
from Engine.UI.POM.save_export_project_data_page import SaveSyntheticDataPage
from Playground.Resources.UI.initial_url_ui import INITIAL_URL
from Playground.Resources.UI.test_data import test_data_sets

# Set up the logger
setup_logger()

@pytest.mark.parametrize("file_path_ui, project_name, synthetic_records", test_data_sets)
def test_end_to_end(file_path_ui, project_name, synthetic_records):
    logger = logging.getLogger(__name__)
    logger.info(f"Starting the end-to-end test with file path: {file_path_ui}, project name: {project_name}, synthetic records: {synthetic_records}")

    try:
        browser_utils = BrowserUtils()
        page = browser_utils.page

        # Navigate to the initial page
        logger.info(f"Navigating to initial URL: {INITIAL_URL}")
        base_page = BasePage(page)
        base_page.navigate_to(INITIAL_URL)
        page.wait_for_load_state('networkidle')

        # Upload data and proceed to generate statistics
        upload_data_page = UploadDataPage(page)
        upload_data_page.upload_file(file_path_ui)
        upload_data_page.click_generate_statistics_data()

        # Configure and analyze statistics
        analyse_statistics_page = AnalyseStatisticsPage(page)
        analyse_statistics_page.click_configure_outcome()

        # Configure synthetic data
        configure_synthetic_data_page = ConfigureSyntheticDataPage(page)
        configure_synthetic_data_page.set_synthetic_records(synthetic_records)
        configure_synthetic_data_page.click_generate_synthetic_data()

        # Generate synthetic data
        generate_synthetic_data_page = GenerateSyntheticDataPage(page)
        generate_synthetic_data_page.click_synthetic_data_set()
        generate_synthetic_data_page.click_next_research_project()

        # Save and export the project data
        save_synthetic_data_page = SaveSyntheticDataPage(page)
        save_synthetic_data_page.set_research_project_name(project_name)
        save_synthetic_data_page.click_save_research_project()
        save_synthetic_data_page.click_close_research_project()

        logger.info(f"End-to-end test completed successfully for file path: {file_path_ui}, project name: {project_name}, synthetic records: {synthetic_records}")
    except Exception as e:
        logger.error(f"Error encountered during end-to-end test: {e}")
        raise
    finally:
        browser_utils.teardown()
        logger.info("Browser teardown completed")

if __name__ == "__main__":
    pytest.main(["-v", __file__])
