import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ['API_KEY']

exercises_done = input("Tell me which exercises you did: ")
current_datetime = datetime.now()

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

exercise_params = {
    "query": exercises_done
}

res = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
exercise_data = res.json()

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

USERNAME = os.environ["USERNAME"]
PASS = os.environ["PASS"]

basic = HTTPBasicAuth(USERNAME, PASS)

for exercise in exercise_data['exercises']:
    sheety_params = {
        "workout": {
            "date": current_datetime.strftime("%d/%m/%Y"),
            "time": current_datetime.strftime("%H:%M:%S"),
            "exercise": exercise['user_input'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }

    exercise_res = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, auth=basic)
    print(exercise_res.text)
