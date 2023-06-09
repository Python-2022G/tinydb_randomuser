import requests

base_url = "https://randomuser.me/api/"

def get_users(n: int) -> list:
    payload = {
        "results": n
    }
    response = requests.get(base_url, params=payload)

    users = []
    for user in response.json()['results']:
        user_data = {
            "first_name": user['name']['first'],
            "last_name": user['name']['last'],
            "age": user['dob']['age'],
            "phone": user['phone'],
            "country": user['location']['country'],
            "email": user['email'],
        }
        users.append(user_data)

    return users