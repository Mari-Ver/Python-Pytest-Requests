import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c131ccec3085f458bd51c4e9844684c8'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "dominohkamariia@yandex.ru",
    "password": "Picasso01!"
}

TRAINER_ID = '12068'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == TRAINER_ID