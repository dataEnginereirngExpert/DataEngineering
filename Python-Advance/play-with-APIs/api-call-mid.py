import requests


## PAGINATION EXAMPLE 

all_posts = []

for page in range(1, 4):
    url = f"https://jsonplaceholder.typicode.com/posts?_limit=5&_page={page}"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        print(F"--------------{page}-------------------")
        print(posts)
        all_posts.extend(posts)
    else:
        print("Error on page", page)

print("Total posts fetched:", len(all_posts))

## Header passing while calling 
headers = {
    "Accept": "application/json",
    "User-Agent": "Python-Workshop"
}


url1 = "https://jsonplaceholder.typicode.com/posts/1"  
response = requests.get(url1,headers=headers)
print(response.status_code)
print(response.text) 