import requests
from datetime import datetime as dt
from exercise_data import api_response


def current_datetime():
    """Returns current date and time string using datetime module"""
    current_date = dt.today()
    return current_date.strftime('%d/%m/%Y'), current_date.strftime('%H:%M:%S')


def sheety_datasheet_api(data):
    """Accepts data as the parameters and adds it to the list"""
    sheety_api = '#----YOUR SHEETY API HERE----#'
    # Parameters for sheety sheets
    parameters = {"sheet1": data}
    # Authentication header for sheety
    sheety_headers = {'Authorization': '#----YOUR SHEETY AUTHENTICATION HEADER---#'}
    # post requests for sheety api
    response2 = requests.post(sheety_api, json=parameters, headers=sheety_headers)
    response2.raise_for_status()
    if 200 <= response2.status_code < 300:
        print("Record added successfully")


# Getting current date and time string from the function
date_string, time_string = current_datetime()

# getting the api_response from exercise data and iterating over the json file to get the data for Google sheet
for exercises in api_response['exercises']:
    name_of_exercise = exercises['name'].title()
    duration = exercises['duration_min']
    calories_burnt = exercises['nf_calories']
    data_for_excel = {'date': date_string,
                      'time': time_string,
                      'exercise': name_of_exercise,
                      'duration': duration,
                      'calories': calories_burnt
                      }
    sheety_datasheet_api(data_for_excel)
