from typing import Union

from src.masks import get_mask_account, get_mask_card_n


def mask_account_card(count: Union[int, str]) -> Union[int, str]:
    """функция которая принимает номер счета или карты и маскирует его"""
    list_numbers = []
    list_names = []
    for i in count:
        if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            list_numbers.append(i)
        else:
            list_names.append(i)

    if len(list_numbers) == 20:
        return f'{"".join(list_names)}{(get_mask_account("".join(list_numbers)))}'

    else:
        return f'{"".join(list_names)}{(get_mask_card_number("".join(list_numbers)))}'


def get_date(dats: Union[int, str]) -> Union[int, str]:
   data, time = dats.split("T")
   return ".".join(data.split("-"))


