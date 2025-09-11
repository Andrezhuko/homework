from src.witget import get_date, mask_account_card


def test_mask_account_card(
    name_cards: str, incorrect_name_cards: str, name_account: str, incorrect_name_account: str
) -> None:
    assert mask_account_card(name_cards) == "Visa 1215 45** **** 6546"
    assert mask_account_card(incorrect_name_cards) == "Visa неверный номер карты"
    assert mask_account_card(name_account) == "Счет **4684"
    assert mask_account_card(incorrect_name_account) == "Счет неверный номер счета"


def test_get_date(date_time: str) -> None:
    assert get_date(date_time) == "11.03.2024"
