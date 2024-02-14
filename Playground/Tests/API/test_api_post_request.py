# test_api_post_request.py

import pytest
import logging
from Playground.Resources.API.endpoints_api import POST_DATA_LAYER_ENDPOINT
from Playground.Resources.API.file_path_api import file_path_api
from Engine.API.api_wrappers import post_request

# Initialize logger for this test
logger = logging.getLogger(__name__)

def test_upload_dataset():
    try:
        logger.info("Starting POST request test for dataset upload")

        payload = {'data-set-name': 'ag_test_01_11_1730.csv'}
        # Ensure file is properly closed after its use
        with open(file_path_api, 'rb') as file:
            files = [('data-set', ('ag_test_01_11_1730.csv', file, 'text/csv'))]
            headers = {'Content-Type': 'multipart/form-data; boundary=<calculated when request is sent>', 'Accept': 'csv'}

            # Perform the POST request
            response = post_request(POST_DATA_LAYER_ENDPOINT, payload, files, headers)
            logger.info("POST request sent")

        # Assert and log the result
        assert response.status_code == 200, f"Failed to upload the dataset, status code: {response.status_code}"
        logger.info("POST request test for dataset upload passed, received status code 200")

    except AssertionError as e:
        logger.error(f"Assertion error in POST request test: {e}")
        raise
    except Exception as e:
        logger.error(f"Error in test_upload_dataset: {e}")
        raise

if __name__ == "__main__":
    pytest.main()


