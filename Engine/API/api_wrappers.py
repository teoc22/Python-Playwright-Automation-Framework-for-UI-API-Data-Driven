# api_wrappers.py

import logging
import requests

# Initialize logger for this module
logger = logging.getLogger(__name__)

def get_request(endpoint):
    # GET request wrapper: Sends a GET request to the specified endpoint.
    try:
        logger.info(f"Sending GET request to {endpoint}")
        response = requests.get(endpoint)
        logger.info(f"Received response with status code {response.status_code} for GET request to {endpoint}")
        return response
    except Exception as e:
        logger.error(f"Error during GET request to {endpoint}: {e}")
        raise

def post_request(endpoint, payload, files, headers):
    # POST request wrapper: Sends a POST request to the specified endpoint with payload, files, and headers.
    try:
        logger.info(f"Sending POST request to {endpoint} with payload: {payload}")
        response = requests.post(endpoint, data=payload, files=files, headers=headers)
        logger.info(f"Received response with status code {response.status_code} for POST request to {endpoint}")
        return response
    except Exception as e:
        logger.error(f"Error during POST request to {endpoint}: {e}")
        raise

def put_request(endpoint, files):
    # PUT request wrapper: Sends a PUT request to the specified endpoint with the provided files.
    try:
        logger.info(f"Sending PUT request to {endpoint}")
        response = requests.put(endpoint, files=files)
        logger.info(f"Received response with status code {response.status_code} for PUT request to {endpoint}")
        return response
    except Exception as e:
        logger.error(f"Error during PUT request to {endpoint}: {e}")
        raise

def delete_request(endpoint):
    # DELETE request wrapper: Sends a DELETE request to the specified endpoint.
    try:
        logger.info(f"Sending DELETE request to {endpoint}")
        response = requests.delete(endpoint)
        logger.info(f"Received response with status code {response.status_code} for DELETE request to {endpoint}")
        return response
    except Exception as e:
        logger.error(f"Error during DELETE request to {endpoint}: {e}")
        raise

