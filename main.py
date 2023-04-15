"""imported requests module"""
import requests

"""imported datetime module as dt"""
import datetime as dt

"""contants"""
USERNAME = "anshusinha20"
TOKEN = "ds2d233kjh44jwkjb23b3kjd2"
GRAPH_ID = "graph1"

"""variable to store endpoint"""
pixelaEndpoint = "https://pixe.la/v1/users"

"""dictionary to hold the parameters"""
pixelaParameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# """posting the request"""
# response = requests.post(url=pixelaEndpoint, json=pixelaParameters)
# print(response.text)

"""variable to store the graph endpoint"""
graphEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs"

"""dictionary to hold the graph parameters"""
graphParameters = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graphEndpoint, json=graphParameters, headers=headers)
# print(response.text)

"""variable to hold dates"""
today = dt.datetime.today().strftime("%Y%m%d")

"""variable to store the data creation endpoint"""
pixelDataCreationEndpoint = f"{pixelaEndpoint}/{USERNAME}/graphs/{GRAPH_ID}"

"""dictionary to hold the data creation parameters"""
pixelDataCreationParameters = {
    "date": today,
    "quantity": "10.5",
}

response = requests.post(url=pixelDataCreationEndpoint, json=pixelDataCreationParameters, headers=headers)
print(response.text)

