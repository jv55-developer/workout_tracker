import requests

APP_ID = "1b931bd5"
API_KEY = "2c4d00aab20f4cb2d9e470f27d1a83e2"

exercises_done = input("Tell me which exercises you did: ")

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
print(res.text)
