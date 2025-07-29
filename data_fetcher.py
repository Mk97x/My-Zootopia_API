import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    }
    """
    BASE_URL = "https://api.api-ninjas.com/v1/animals"
    API_KEY = os.getenv("API_KEY")
    
    PARAMS = {'name': animal_name}
    HEADERS = {'X-Api-Key': API_KEY}
    
    try:
        response = requests.get(BASE_URL, headers=HEADERS, params=PARAMS)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"API Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None