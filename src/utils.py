import json


def by_process_json(link_by_json_file: str) -> list[dict]:
    """функция, которая принимает путь до файла и возвращает список словарей с информацией о транзакциях"""
    if type(link_by_json_file) == str:
        with open(link_by_json_file, "r", encoding="utf-8") as file_json:
            data = json.load(file_json)
        return data
    else:
        return "Invalid input data type"
