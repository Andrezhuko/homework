from src.masks import get_mask_account, get_mask_card_number
from src.witget import get_date, mask_account_card

number_cards = "7000792289606361"
number_counts = "73654108430135874305"

cards_name = "Visa Classic 6831982476737228"
count_name = "Счет 35383033474447895560"

data_info = "2024-03-11T02:26:18.671407"

print(get_date(data_info))
print(mask_account_card(cards_name))
print(get_mask_card_number(number_cards))
print(get_mask_account(number_counts))
print(mask_account_card(count_name))
