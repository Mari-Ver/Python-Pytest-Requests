import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c131ccec3085f458bd51c4e9844684c8'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "dominohkamariia@yandex.ru",
    "password": "*******"
}

body_confirmation = {"trainer_token": TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_knockout = {
    "pokemon_id": "162733"
}

body_change_name = {
    "pokemon_id": "183928",
    "name": "Lola1",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "183928"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers= HEADER, json= body_registration)
print(response.text)'''


# создать покемона
response_create = requests.post(url= f'{URL}/pokemons', headers=HEADER, json= body_create)
print(response_create.text)

# отправить покемона в нокаут
response_knockout = requests.post(url= f'{URL}/pokemons/knockout', headers=HEADER, json= body_knockout)
print(response_knockout.text)

# изменить имя покемона
response_change_name = requests.put(url= f'{URL}/pokemons', headers=HEADER, json= body_change_name)
print(response_change_name.json())

# поймать покемона в покебол
response_add_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers=HEADER, json= body_add_pokeball)
print(response_add_pokeball.json())