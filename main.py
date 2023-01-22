import requests

base_host = 'https://akabab.github.io/superhero-api/api'

def get_int_by_name(name, responce):
    heroes_list = responce.json()
    flag = False
    for elem in heroes_list:
        if elem.get('name') == name:
            flag = True
            return elem.get('powerstats').get('intelligence')
    if flag == False:
        return 0

def find_max_int(h_dict):
    max_val = max(h_dict.values())
    for k, v in h_dict.items():
        if v == max_val:
            return k

if __name__ == "__main__":
    heroes_list=['Hulk', 'Captain America', 'Thanos']
    heroes_dict = {}

    uri = '/all.json'
    request_url = base_host + uri
    responce = requests.get(request_url)

    for hero in heroes_list:
        heroes_dict[hero] = get_int_by_name(hero, responce)

    print(f'Самый умный герой - {find_max_int(heroes_dict)}')


