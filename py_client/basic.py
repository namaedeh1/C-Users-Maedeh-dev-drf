import requests


# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "ABC", "content": "hello world"})
print(get_response.json())
#print(get_response.json()['message'])
#print(get_response.text)
#print(get_response.status_code)