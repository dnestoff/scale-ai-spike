import scaleapi
from config import API_KEY_TEST, API_KEY_PROD
import os

def verify_api_key(api_key):
    """
    Verify if the API key is valid.
    A test API key should start with 'test' and a prod API key should start with 'live'.
    """
    if api_key.startswith('test') or api_key.startswith('live'):
        return True
    return False

print(os.environ)

def set_api_key():
    # Set the API key based on the environment
    API_KEY = API_KEY_TEST  # Default to test key

    # Conditional logic to switch to production key if needed
    if 'PRODUCTION' in os.environ:
        API_KEY = API_KEY_PROD
    return API_KEY

API_KEY = set_api_key()

# Verify the API key before proceeding
if verify_api_key(API_KEY):
    client = scaleapi.ScaleClient(API_KEY)
    try:
        projects = client.get_projects()
        print(f"Successfully connected to Scale API. Found {len(projects)} projects.")
    except Exception as e:
        print(f"Error connecting to Scale API: {e}")
else:
    print("Invalid API key. Please use a valid test or production API key.")
