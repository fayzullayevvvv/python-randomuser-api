import json
import requests


def get_randomuser_full_data():
    url = 'https://randomuser.me/api/'

    response = requests.get(url)
    data = response.json()

    return data['results'][0]


def get_user_data(user: dict):
    full_name = user['name']['first'] + ' ' + user['name']['last']
    phone = user['phone']
    email = user['email']
    age = user['dob']['age']
    nat = user['nat']
    gender = user['gender']
    country = user['location']['country']

    result = {
        "full_name": full_name,
        "phone": phone,
        "email": email,
        "age": age,
        "nat": nat,
        "gender": gender,
        "country": country
    }

    return result


def main() -> None:
    male_users = []
    female_users = []
    for i in range(30):
        user = get_randomuser_full_data()
        user_data = get_user_data(user)
    
        if user_data['gender'] == 'male':
            male_users.append(user_data)
        else:
            female_users.append(user_data)

    users = {
        'male': male_users,
        'female': female_users
    }

    with open('users.json', 'w') as f:
        f.write(json.dumps(users, indent=4))

main()
