from ..lib import *
import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()


def sendHttp(body):
    api_key = os.getenv('SV_API_KEY')
    if not api_key:
        raise Exception('No env variable SV_API_KEY exist, please add key=value in .env file')

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key,
        'Connection': 'close'
    }
    url = 'https://www.camreahome.com/SVgatewayAPI/v1'
    for i in range(10):
        try:
            r = requests.post(url, headers=headers, data=json.dumps(body))
            data = json.loads(r.text)
            break
        except:
            time.sleep(2)
    time.sleep(1)
    return data
