import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)

def auth_token():
    user = post_new_user(data.user_body)
    user_json = user.json()

    return user_json['authToken']
def post_new_client_kit(kit_body_key):
    token = auth_token()
    headers = data.headers.copy()
    headers['Authorization'] = f'Bearer {token}'

    kit_body = kit_body_key
    return requests.post(cofiguration.URL_SERVICE + configuration.KITS_PAHT,
                         json=kit_body,
                         headers=headers,
    )

response = post_new_client_kit(data.kit_bodies["one_character"])