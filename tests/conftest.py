import pytest

@pytest.fixture
def numbers_card():
    return "1215454845466546"

@pytest.fixture
def incorrect_numbers_card():
    return "15454845466546"

@pytest.fixture
def numbers_account():
    return "15644546464448644684"

@pytest.fixture
def incorrect_numbers_account():
    return "934823"

@pytest.fixture
def name_cards():
    return "Visa 1215454845466546"

@pytest.fixture
def incorrect_name_cards():
    return "Visa 5454845466546"

@pytest.fixture
def name_account():
    return "Счет 15644546464448644684"

@pytest.fixture
def incorrect_name_account():
    return "Счет 1564454646444864468"

@pytest.fixture
def date_time():
    return "2024-03-11T02:26:18.671407"


