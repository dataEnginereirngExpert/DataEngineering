import requests

url = "https://fake-json-api.mock.beeceptor.com/users/1"  # Public sample API
response = requests.get(url)

print(response.status_code)
print(response.text)  # raw response

##JSON Parsing 
response_body = response.json()

data = response.json()
print("-----------------------------------") 
print(response_body)
print("-----------------------------------") 
print(type(response_body))  # usually dict or list

##Accessing JSON fields:
print("-----------------------------------") 
print(response_body["name"])
print(response_body["email"])

## Error handling 

def safe_get(endpoint):
    try:
        response = requests.get(endpoint, timeout=5)
        ##print(response.status_code)
        response.raise_for_status()  # raises error for 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print("API Error:", e)
        return None

#Calling function 
print("-----------------------------------") 
wrongURl="https://jsonplaceholder.typicode.co/posts/1" 
safe_get(wrongURl)
