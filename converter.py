import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_URL")

model_data = {}


def convert_currency(select, target, amount):
    api_url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"
    querystring = {"from": select, "to": target, "amount": str(amount)}
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }
    try:
        response = requests.get(api_url, headers=headers, params=querystring)
        if response.status_code == requests.codes.ok:
            model_data = {
                "target": response.json()["query"]["to"],
                "amount": response.json()["result"]
            }
            return model_data
    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == '__main__':
    result = convert_currency("EUR", "USD", 700)
    print(result)
