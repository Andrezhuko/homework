def filter_by_state(list_dicts: list[dict], state: str='EXECUTED') -> list[dict]:
    """функция которая принмает список словорей и возвращает список словарей с указанным параметром"""
    new_list_dicts = []
    for dicts in list_dicts:
        if dicts['state'] == state:
            new_list_dicts.append(dicts)
    return new_list_dicts