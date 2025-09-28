import json

import logging

from typing import Any

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/utils.log', 'w', 'utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def by_process_json(link_by_json_file: str) -> Any:
    """функция, которая принимает путь до файла и возвращает список словарей с информацией о транзакциях"""
    try:
        if type(link_by_json_file) == str:
            with open(link_by_json_file, "r", encoding="utf-8") as file_json:
                data = json.load(file_json)
            logger.info("файл найден")
            return data
        else:
            logger.warning("файл не найден")
            return "Invalid input data type"
    except Exception as error:
        logger.error(f"произошла ошибка {error}")