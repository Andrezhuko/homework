from typing import Any

import pandas as pd


def by_processing_csv(link_by_csv_file: str) -> Any:
    """функция которая принимает файл csv а возвращает список словарей"""
    if isinstance(link_by_csv_file, str):
        raise FileNotFoundError("неверный формат файла или файл отсутсвует")
    else:
        return (pd.read_csv(link_by_csv_file)).to_dict(orient="records")



def by_processing_exe(link_by_exe_file: str) -> Any:
    """фукнция которая принмает exe а возвращает список словарей"""
    if isinstance(link_by_exe_file, str):
        raise FileNotFoundError("неверный формат файла или файл отсутсвует")
    else:
        return (pd.read_excel(link_by_exe_file)).to_dict(orient="records")
