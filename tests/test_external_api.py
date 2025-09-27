from unittest.mock import patch

from src.external_api import summ_transaction


@patch("requests.request")
def test_summ_transaction(mock_request, data_from_json):
    mock_request.return_value.json.return_value = {"result": 100}
    assert summ_transaction(data_from_json) == 32057.58
