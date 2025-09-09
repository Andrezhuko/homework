from src.witget import mask_account_card, get_date

def test_mask_account_card(name_cards, incorrect_name_cards, name_account, incorrect_name_account):
    assert mask_account_card(name_cards) == "Visa 1215 45** **** 6546"
    assert mask_account_card(incorrect_name_cards) == "Visa неверный номер карты"
    assert mask_account_card(name_account) == "Счет **4684"
    assert mask_account_card(incorrect_name_account) == "Счет неверный номер счета"

def test_get_date(date_time):
    assert get_date(date_time) == "11.03.2024"
