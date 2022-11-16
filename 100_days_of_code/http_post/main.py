import requests
import datetime

USERNAME = "istoc"
TOKEN = "5V5m7NLjmByc68xP"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

pixela_endpoint = "https://pixe.la/v1/users"

# response = requests.post(url=pixela_endpoint, json=user_params, verify=False)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Russian Language graph",
    "unit": "session",
    "type": "int",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers, verify=False)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers, verify=False)
# print(response.text)

