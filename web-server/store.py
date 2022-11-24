import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    categories = r.json()
    
    for categories in categories:
        print(categories['name'])

def get_users():
    r = requests.get('https://api.escuelajs.co/api/v1/users')
    print(r.status_code)
    users = r.json()

    for users in users:
        print(users['name'], users['role'])