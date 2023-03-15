import requests


headers = {'Authorization': 'Bearer fe2b63b3e90faf220743ba2811014c31f13d4f3b'}
endpoint = "http://localhost:8000/api/products/"


data = {
    'title':"this field is done :*"
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())