import os

import requests
from dotenv import load_dotenv

load_dotenv()


def summ_transaction(list_transactions: list[dict]) -> float:
    """функция которая принимает транзакцию а возвращает сумму транзакций в рублях"""
    amount = []
    for transaction in list_transactions:
        trans_code = transaction["operationAmount"]["currency"]["code"]
        if trans_code == "RUB":
            amount.append(float(transaction["operationAmount"]["amount"]))

        else:
            carrensy_from = transaction["operationAmount"]["currency"]["code"]
            basa_url = "https://api.apilayer.com/exchangerates_data/convert"
            url = f"{basa_url}?to={"RUB"}&from={carrensy_from}&amount={transaction["operationAmount"]["amount"]}"

            token_api = os.getenv("API_KEY")
            headers = {"apikey": token_api}

            response = requests.request("GET", url, headers=headers)
            result = response.json()
            amount.append(float(result["result"]))
    return sum(amount)
