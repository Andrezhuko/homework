import pytest

from src.utils import by_process_json


def test_by_process_json(data_from_json):
    assert by_process_json("data/test.json") == data_from_json
    assert by_process_json(1) == "Invalid input data type"
    with pytest.raises(Exception):
        by_process_json()
