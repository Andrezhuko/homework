import re

def fucntion_by_seach(data: list[dict], seach: str) -> list[dict]:
    """функция которая принимает список словарей а возвращает список категорий операций"""
    pattern = re.compile(seach, re.IGNORECASE)
    return [transaction for transaction in data if pattern.findall(transaction["description"])]

