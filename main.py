"""imported requests module"""
import requests

"""contants"""
USERNAME = "anshusinha20"
TOKEN = "ds2d233kjh44jwkjb23b3kjd2"

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
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graphEndpoint, json=graphParameters, headers=headers)
print(response.text)