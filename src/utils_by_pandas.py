from typing import Any

import pandas as pd


def by_processing_csv(link_by_csv_file: str) -> Any:
    """функция которая принимает файл csv а возвращает список словарей"""
    if not isinstance(link_by_csv_file, str):
        raise FileNotFoundError("неверный формат файла или файл отсутсвует")
    else:
        df = pd.read_csv(link_by_csv_file, delimiter=";")
        new_list = []
        for x in df.to_dict(orient="records"):
            x["operationAmount"] = {
                "amount": x["amount"],
                "currency": {"code": x["currency_name"], "name": x["currency_name"]},
            }
            new_list.append(x)
        return new_list


def by_processing_exe(link_by_exe_file: str) -> Any:
    """фукнция которая принмает exe а возвращает список словарей"""
    if not isinstance(link_by_exe_file, str):
        raise FileNotFoundError("неверный формат файла или файл отсутсвует")
    else:
        new_list = []
        for x in pd.read_excel(link_by_exe_file).to_dict(orient="records"):
            x["operationAmount"] = {
                "amount": x["amount"],
                "currency": {"code": x["currency_name"], "name": x["currency_name"]},
            }
            new_list.append(x)
        return new_list
