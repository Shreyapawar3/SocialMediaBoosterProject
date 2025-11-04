from django.conf import settings
import requests

def fetch_data_from_external_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON data from the response
    except requests.exceptions.RequestException as e:
        # Log the error or handle it as needed
        print(f"Error fetching data from API: {e}")
        return None

def send_data_to_external_api(api_url, data):
    try:
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON data from the response
    except requests.exceptions.RequestException as e:
        # Log the error or handle it as needed
        print(f"Error sending data to API: {e}")
        return None

def get_api_url(endpoint):
    return f"{settings.EXTERNAL_API_BASE_URL}/{endpoint}"