import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)

API_KEY = os.getenv('KRX_API_KEY')

def request_stock() -> str | None:
    url = 'https://openapi.krx.co.kr/svc/sample/apis/sto/stk_bydd_trd'
    headers = {
        'Accept': 'application/json',
        'Host': 'openapi.krx.co.kr',
        'AUTH_KEY': API_KEY,
    }
    params = {
       'baseDd': 20250625
    }
   
    try:
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()  # This will raise an HTTPError for bad responses (4xx, 5xx)
        data = res.json()
        return data
    except Exception as e:
        print(f"request_stock error: {e}")
        return None

print(request_stock())










