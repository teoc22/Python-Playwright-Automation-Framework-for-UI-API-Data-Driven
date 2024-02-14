# test_api_put_request.py

import pytest
import logging
from Playground.Resources.API.endpoints_api import PUT_DATA_LAYER_ENDPOINT
from Playground.Resources.API.file_path_api import file_path_api
from Engine.API.api_wrappers import put_request

# Initialize logger for this test
logger = logging.getLogger(__name__)

# The API marker
@pytest.mark.api
def test_update_dataset():
    try:
        logger.info("Starting PUT request test for dataset update")

        # Open the file and prepare it for the PUT request
        with open(file_path_api, 'rb') as file:
            files = {'file': (file_path_api, file, 'text/csv')}

            # Perform the PUT request
            response = put_request(PUT_DATA_LAYER_ENDPOINT, files)
            logger.info("PUT request sent")

        # Assert and log the result
        assert response.status_code == 200, f"Failed to update the dataset, status code: {response.status_code}"
        logger.info("PUT request test for dataset update passed, received status code 200")

    except AssertionError as e:
        logger.error(f"Assertion error in PUT request test: {e}")
        raise
    except Exception as e:
        logger.error(f"Error in test_update_dataset: {e}")
        raise

if __name__ == "__main__":
    pytest.main()


