import requests
from datetime import datetime
import os

#https://pixe.la/v1/users/andyvn/graphs/graph1.html

USERNAME = os.getenv("GRAPH_API_USERNAME")
TOKEN = os.getenv("GRAPH_API_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "learn to code graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}"

date_today = datetime.strftime(datetime.now(), format="%Y%m%d")

pixe_config = {
    "date": str(date_today),
    "quantity": "3"
}

# response = requests.post(url=post_pixel_endpoint, json=pixe_config, headers=headers)
# print(response.text)
put_pixel_config = {
    "quantity": "120"
}

# response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{str(date_today)}",
#                         json=put_pixel_config, headers=headers)
# print(response.text)


response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{str(date_today)}", headers=headers)
print(response.text)