import requests
import os 


API_KEY = os.environ['API']
headers = {
    'X-Api-Key': API_KEY,
}
base_url ='https://randommer.io/api/Card/Types'

response = requests.get(base_url, headers=headers)
print(response.json())
