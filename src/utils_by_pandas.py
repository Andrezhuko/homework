from typing import Any

import pandas as pd


def by_processing_csv(link_by_csv_file: str) -> Any:
    """функция которая принимает файл ссв а возвращает список словарей"""
    try:
        if isinstance(link_by_csv_file, str):
            return "неверный формат файла или файл отсутсвует"
        else:
            return (pd.read_csv(link_by_csv_file)).to_dict(orient="records")
    except Exception as error:
        return f"ошибка {error}"


def by_processing_exe(link_by_exe_file: str) -> Any:
    """фукнция которая принмает эксэль а возвращает список словарей"""
    try:
        if isinstance(link_by_exe_file, str):
            return "неверный формат файла или файл отсутсвует"
        else:
            return (pd.read_excel(link_by_exe_file)).to_dict(orient="records")
    except Exception as error:
        return f"ошибка {error}"
