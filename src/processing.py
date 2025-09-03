def filter_by_state(list_dicts: list[dict], state: str='EXECUTED') -> list[dict]:
    """функция которая принмает список словорей и возвращает список словарей с указанным параметром"""
    new_list_dicts = []
    for dicts in list_dicts:
        if dicts['state'] == state:
            new_list_dicts.append(dicts)
    return new_list_dicts

def sort_by_date(list_dicts: list[dict], ascending: bool=True) -> list[dict]:
    """функция которая сортирует список словарей по дате"""
    new_list_dicts = sorted(list_dicts, key=lambda x: x['date'], reverse=ascending)
    return new_list_dicts