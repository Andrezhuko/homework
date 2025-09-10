import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(list_dict_transaction):
    test_one = filter_by_currency(list_dict_transaction)
    assert next(test_one) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(test_one) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    test_two = filter_by_currency(list_dict_transaction, "RUB")
    assert next(test_two) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(test_two) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }
    test_three = filter_by_currency([])
    test_four = filter_by_currency(list_dict_transaction, "EU")
    with pytest.raises(StopIteration):
        assert next(test_three)
        assert next(test_four)


def test_transaction_descriptions(list_dict_transaction):
    assert next(transaction_descriptions(list_dict_transaction)) == "Перевод организации"
    assert next(transaction_descriptions([])) == "пустой список"


def test_card_number_generator():
    assert next(card_number_generator(1, 4)) == "0000 0000 0000 0001"
    assert next(card_number_generator()) == "0000 0000 0000 0001"
    assert next(card_number_generator("213121313131313213123")) == "слишком большой диапозон"
