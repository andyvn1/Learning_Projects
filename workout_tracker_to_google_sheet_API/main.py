import requests as r
from datetime import datetime
import os

#User would input type of exercise and this one with information of the user will be posed into track api
#the that response will be used to have more information like calories used to post on sheety


APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
nl_syndigo_api = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

syndigo_config = {
    "query": "",
    "age": 32,
    "height_cm": 170.18,
    "weight_kg": 91
}

sheety_auth_header = {
    "Authorization": os.environ["Authorization"]
}

sheety_api = "https://api.sheety.co/6490ff7bf89c54a07966ace22c35403d/myWorkouts/workouts"


def post_exercise():
    answer = input(str("Tell me which exercises you did "))
    syndigo_config["query"] = answer

    #Posting
    response_post = r.post(url=nl_syndigo_api, json=syndigo_config, headers=header)
    data = response_post.json()

    for exercise in data["exercises"]:
        sheet_input = {
            "workout": {
                "date": datetime.strftime(datetime.now(), "%d/%m/%Y"),
                "time": datetime.strftime(datetime.now(), "%X"),
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }

        # print(response_post.json())
        response_post_sheety = r.post(url=sheety_api, json=sheet_input, headers=sheety_auth_header)
        print(response_post_sheety.text)


post_exercise()
