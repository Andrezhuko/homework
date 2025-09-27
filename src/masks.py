import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/masks.log', 'w', 'utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_cards: str) -> str:
    """фунция которая маскирует номер карты"""
    try:
        if number_cards.isdigit() and len(number_cards) == 16:
            logger.info("функция успешно отработала")
            return f"{number_cards[:4]} {number_cards[4:6]}** **** {number_cards[-4:]}"
        else:
            logger.warning("ошибка с номером карты")
            return "неверный номер карты"
    except Exception as error:
        logger.error(f"произошла ошибка {error}")

def get_mask_account(number_counts: str) -> str:
    """фунция которая маскирует номер счета"""
    try:
        if number_counts.isdigit() and len(number_counts) == 20:
            logger.info("функция успешно отработала")
            return f"**{number_counts[-4:]}"
        else:
            logger.warning("ошибка с номером счета")
            return "неверный номер счета"
    except Exception as error:
        logger.error(f"произошла ошибка {error}")