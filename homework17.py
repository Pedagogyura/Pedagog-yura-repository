import requests


def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        astronauts = [astronaut['name'] for astronaut in data['people']]
        return astronauts
    else:
        return []


if __name__ == "__main__":
    astronauts = get_astronauts()
    print("Астронавты на МКС в данный момент:")
    for astronaut in astronauts:
        print("-", astronaut)
