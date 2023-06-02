# utility stuff
import os
from uuid import uuid4

# flask stuff
from flask import (
    Flask, 
    request
)

# oauth stuff
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# my stuff
from auth import get_flow
from config import secrets

app = Flask(__name__)
app.secret_key = uuid4().hex

# Set up the OAuth flow
flow = get_flow()

def valid_api_key(request):
    if ('apikey' not in request.form) or (request.form['apikey'] != secrets['api_key']):
        return False
    return True

@app.errorhandler(404)
def not_found(e):
    return "404: Not Found"

if __name__ == '__main__':
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = 'True'
    if os.environ["ENV"] == "DEV":
        os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    else:
        os.unsetenv('OAUTHLIB_INSECURE_TRANSPORT')
    PORT = int(os.getenv('PORT')) if os.getenv('PORT') else 8080
    app.run('127.0.0.1', PORT, debug=True)