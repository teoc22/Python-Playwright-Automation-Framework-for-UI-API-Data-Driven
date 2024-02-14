# test_api_get_request.py

import pytest
import logging
from Playground.Resources.API.endpoints_api import GET_DATA_LAYER_ENDPOINT
from Engine.API.api_wrappers import get_request

# Initialize logger for this test
logger = logging.getLogger(__name__)

# The API marker
@pytest.mark.api
def test_get_dataset_info():
    try:
        logger.info(f"Starting GET request test for endpoint: {GET_DATA_LAYER_ENDPOINT}")
        
        # Perform the GET request
        response = get_request(GET_DATA_LAYER_ENDPOINT)

        # Assert and log the result
        assert response.status_code == 200, f"Failed to get dataset info, status code: {response.status_code}"
        logger.info("GET request test passed, received expected status code 200")
    
    except AssertionError as e:
        logger.error(f"Assertion error in test: {e}")
        raise
    except Exception as e:
        logger.error(f"Error in test_get_dataset_info: {e}")
        raise

if __name__ == "__main__":
    pytest.main()
