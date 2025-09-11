from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(numbers_card: str, incorrect_numbers_card: str) -> None:
    assert get_mask_card_number(numbers_card) == "1215 45** **** 6546"
    assert get_mask_card_number(incorrect_numbers_card) == "неверный номер карты"


def test_get_mask_account(numbers_account: str, incorrect_numbers_account: str) -> None:
    assert get_mask_account(numbers_account) == "**4684"
    assert get_mask_account(incorrect_numbers_account) == "неверный номер счета"
