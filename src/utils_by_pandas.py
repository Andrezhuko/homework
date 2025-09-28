from typing import Any

import pandas as pd
import csv


def by_prossering_csv(link_by_csv_file: str) -> Any:
    """функция которая принимает файл ссв а возвращает список словарей"""
    if type(link_by_csv_file) == str:
        with open(link_by_csv_file, "r", encoding="utf-8") as file:
            return [a for a in csv.DictReader(file, delimiter=';')]
    else:
        return "неправильный формат ссылки"

def by_prossering_exe(link_by_exe_file: str) -> Any:
    """фукнция которая принмает эксэль а возвращает список словарей"""
    if type(link_by_exe_file) == str:
            return [a for a in pd.read_excel(link_by_exe_file)]
    else:
        return "неправильный формат ссылки"

fkld = by_prossering_exe("../data/transactions_excel.xlsx")
print(fkld.head())