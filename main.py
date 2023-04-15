"""imported requests module"""
import requests

"""variable to store endpoint"""
pixelaEndpoint = "https://pixe.la/v1/users"

"""dictionary to hold the parameters"""
pixelaParameters = {
    "token": "ds2d233kjh44jwkjb23b3kjd2",
    "username": "anshusinha20",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

"""posting the request"""
response = requests.post(url=pixelaEndpoint, json=pixelaParameters)
print(response.text)