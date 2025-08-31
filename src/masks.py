from typing import Union


def get_mask_card_number(number_cards: Union[int, str]) -> Union[str, int]:
    """фунция которая маскирует номер карты"""
    if number_cards.isdigit() and len(number_cards) == 16:
        return f"{number_cards[:4]} {number_cards[4:6]}** **** {number_cards[-4:]}"
    else:
        return "неверный номер карты"


def get_mask_account(number_counts: Union[int, str]) -> Union[str, int]:
    """фунция которая маскирует номер счета"""
    if number_counts.isdigit() and len(number_counts) == 20:
        return f"**{number_counts[-4:]}"
    else:
        return "неверный номер счета"

