import requests

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
    base_url = "https://api.api-ninjas.com/v1/animals"
    api_key = "YEiSpPfWxYSunop1KCSRuQ==dEWrGUmi4uMKU5Jr"
    
    params = {'name': animal_name}
    headers = {'X-Api-Key': api_key}
    
    try:
        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"API Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None