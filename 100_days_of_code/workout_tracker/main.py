import requests
from datetime import datetime

APP_ID = "720b732c"
API_KEY = "a8ac4017b13bb86387469b5a48aadfc8"
MY_WEIGHT = 80
MY_HEIGHT = 178
MY_AGE = 31

query_text = input("What exercise did you do?: ").lower()

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

workout_params = {
    "query": query_text,
    "gender": "male",
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE
}

headers = {
    "X-APP-ID": APP_ID,
    "X-APP-KEY": API_KEY,
}

exercise_response = requests.post(url=exercise_endpoint, json=workout_params, headers=headers, verify=False)

result = exercise_response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_endpoint = "https://api.sheety.co/14a50286cbf0a4097606b4436b42adad/myWorkouts/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, verify=False)