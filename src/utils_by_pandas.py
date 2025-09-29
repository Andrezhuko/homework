from typing import Any

import pandas as pd
import csv


def by_prossering_csv(link_by_csv_file: str) -> Any:
    """функция которая принимает файл ссв а возвращает список словарей"""
    return (pd.read_csv(link_by_csv_file)).to_dict(orient='records')

def by_prossering_exe(link_by_exe_file: str) -> Any:
    """фукнция которая принмает эксэль а возвращает список словарей"""
    return (pd.read_excel(link_by_exe_file)).to_dict(orient='records')

