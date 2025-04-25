import scaleapi
from config import API_KEY_TEST

client = scaleapi.ScaleClient(API_KEY_TEST)

try:
    projects = client.get_projects()
    print(f"Successfully connected to Scale API. Found {len(projects)} projects.")
except Exception as e:
    print(f"Error connecting to Scale API: {e}")
