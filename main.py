import requests
from datetime import datetime

APP_ID = "1b931bd5"
API_KEY = "2c4d00aab20f4cb2d9e470f27d1a83e2"
USERNAME = "6c0887c27fe16c2892977f767bcbbd82"

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

sheety_endpoint = f"https://api.sheety.co/{USERNAME}/workoutTracking/workouts"

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

    exercise_res = requests.post(url=sheety_endpoint, json=sheety_params)
    print(exercise_res.text)
