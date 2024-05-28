import requests
import json

# Global constant variables including details of the API and the personal details
APP_ID = '#----YOUR NUTRITIONIX APP ID----#'
API_KEY = '#----YOUR NUTRITIONIX API KEY----#'
API_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
AGE = "#----YOUR AGE----#"
HEIGHT = "#----YOUR HEIGHT IN CM----#"
WEIGHT = "#----YOUR WEIGHT IN KG----#"

# Taking the user response about the activity
user_response = input("Tell me what exercises you did? ")
# Parameters and headers to go to the API post request
params = {
    'query': user_response,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
# Getting the response from the API link
response = requests.post(url=API_ENDPOINT, json=params, headers=headers)
# Raise exceptions while trying to get the data from API
response.raise_for_status()
# Converting the string into a dictionary using json module
api_response = json.loads(response.text)