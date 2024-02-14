# test_api_delete_request.py

import pytest
import logging
from Playground.Resources.API.endpoints_api import DELETE_DATA_LAYER_ENDPOINT
from Engine.API.api_wrappers import delete_request

# Initialize logger for this test
logger = logging.getLogger(__name__)

# The API marker
@pytest.mark.api
def test_delete_dataset():
    try:
        logger.info(f"Starting DELETE request test for endpoint: {DELETE_DATA_LAYER_ENDPOINT}")

        # Perform the DELETE request
        response = delete_request(DELETE_DATA_LAYER_ENDPOINT)
        logger.info("DELETE request sent")

        # Assert and log the result
        assert response.status_code == 204, f"Failed to delete the dataset, status code: {response.status_code}"
        logger.info("DELETE request test passed, received expected status code 204")

    except AssertionError as e:
        logger.error(f"Assertion error in DELETE request test: {e}")
        raise
    except Exception as e:
        logger.error(f"Error in test_delete_dataset: {e}")
        raise

if __name__ == "__main__":
    pytest.main()


