import requests
import pydantic_models
from config import settings

form_headers = {'Content-Type': 'application/x-www-form-urlencoded'}

payload = 'username=admin&password=secret'
raw_token = requests.post(settings.API_URL + "/token",
                          headers=form_headers,
                          data=payload)
token = raw_token.json()
sesh = requests.Session()
sesh.headers = {
    'accept': 'application/json',
    'Authorization': "Bearer " + token['access_token']
}


def update_user(user: dict):
    user = pydantic_models.User_to_update.validate(user)
    responce = sesh.put(f'{settings.API_URL}/user/{user.id}', data=user.json())
    try:
        return responce.json()
    except:
        return responce.text


def delete_user(user_id: int):
    return sesh.delete(f'{settings.API_URL}/user/{user_id}').json()


def create_user(user: pydantic_models.User_to_create):
    user = pydantic_models.User_to_create.validate(user)
    return sesh.post(f'{settings.API_URL}/user/create', data=user.json()).json()


def get_info_about_user(user_id):
    return sesh.get(f'{settings.API_URL}/get_info_by_user_id/{user_id}').json()


def get_user_balance_by_id(user_id):
    responce = sesh.get(f'{settings.API_URL}/get_user_balance_by_id/{user_id}')
    try:
        return float(responce.text)
    except:
        return f'Error: Not a Number\nResponce: {responce.text}'


def get_total_balance():
    responce = sesh.get(f'{settings.API_URL}/get_total_balance')
    try:
        return float(responce.text)
    except:
        return f'Error: Not a Number\nResponce: {responce.text}'


def get_users():
    return sesh.get(f"{settings.API_URL}/users").json()


def get_user_by_tg_id(tg_id):
    return sesh.get(f"{settings.API_URL}/user_by_tg_id/{tg_id}").json()


def get_user_transactions(user_id):
    responce = sesh.get(f"{settings.API_URL}/get_user_transactions/{user_id}")
    try:
        return responce.json()
    except Exception as E:
        return f"{responce.text} \n" \
               f"Exception: {E.args, E.__traceback__}"


def create_transaction(tg_id, receiver_address: str, amount_btc_without_fee: float):
    user_dict = get_user_by_tg_id(tg_id)
    payload = {'receiver_address': receiver_address,
               'amount_btc_without_fee': amount_btc_without_fee}
    responce = sesh.post(f"{settings.API_URL}/create_transaction/{user_dict['id']}", json=payload)
    return responce.text


def get_user_wallet_by_tg_id(tg_id):
    user_dict = get_user_by_tg_id(tg_id)
    return sesh.get(f"{settings.API_URL}/get_user_wallet/{user_dict['id']}").json()
