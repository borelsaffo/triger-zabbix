import requests
import json

# Remplacez les informations de connexion ci-dessous par vos propres informations d'identification Zabbix
url = 'http://<IP_address>/zabbix/api_jsonrpc.php'
username = 'admin'
password = 'password'

# Créez une session Zabbix en utilisant l'API
def zabbix_login(url, username, password):
    payload = {
        'jsonrpc': '2.0',
        'method': 'user.login',
        'params': {
            'user': username,
            'password': password
        },
        'id': 1,
        'auth': None
    }

    response = requests.post(url, json=payload)
    return json.loads(response.content)['result']

# Récupérez tous les triggers Zabbix en utilisant l'API
def get_triggers(url, auth_token):
    payload = {
        'jsonrpc': '2.0',
        'method': 'trigger.get',
        'params': {
            'output': [
                'triggerid',
                'description',
                'priority',
                'status'
            ],
            'expandDescription': True,
            'sortfield': 'priority',
            'sortorder': 'DESC',
            'filter': {
                'value': 1,
                'status': 0
            }
        },
        'auth': auth_token,
        'id': 1
    }

    response = requests.post(url, json=payload)
    return json.loads(response.content)['result']

# Connectez-vous à Zabbix et récupérez tous les triggers
auth_token = zabbix_login(url, username, password)
triggers = get_triggers(url, auth_token)

# Affichez tous les triggers
for trigger in triggers:
    print(trigger)
