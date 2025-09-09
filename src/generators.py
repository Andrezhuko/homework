from typing import Generator

def filter_by_currency(list_dicts: list[dict], currency: str="USD") -> Generator:
    """функция которая принимает список словарей и валюту а возвращает итератор"""
    yield [i for i in list_dicts if i["operationAmount"]["currency"]["code"] == currency]


def transaction_descriptions(list_dicts: list[dict]) -> Generator:
    """генератор который возвращает описание операций клиента"""
    if list_dicts == []:
        yield "пустой список"
    else:
        for x in list_dicts:
            yield x["description"]



def card_number_generator(start: int=1, stop: int=5) -> Generator:
    """генератор который создает номера банковских карт"""
    stop += 1
    for i in range(start, stop):
        number_card = str(i).zfill(16)
        yield f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}"


print(next(card_number_generator()))
print(next(card_number_generator()))
print(next(card_number_generator()))
