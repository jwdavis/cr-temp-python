# flask stuff
from flask import session

# google stuff
from google.auth import default
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials

# my stuff
from config import scopes, secrets

# python stuff
import json
import requests

def get_app_creds():
    credentials = {}
    creds, project_id = default(scopes=scopes)
    credentials['app'] = creds
    # credentials['delegated'] = creds.with_subject("<account>")
    return credentials

def get_flow():
    client_config = json.loads(secrets['oauth_client_secret'])
    flow = Flow.from_client_config(
        client_config=client_config,
        scopes=[],
    )
    return flow
 
def revoke_creds():
    ui = json.loads(session['creds'])
    ui['refresh_token'] = None
    creds = Credentials.from_authorized_user_info(info=ui)
    result = requests.post('https://accounts.google.com/o/oauth2/revoke',
                    params={'token': creds.token},
                    headers={'content-type': 'application/x-www-form-urlencoded'})
    session.clear()