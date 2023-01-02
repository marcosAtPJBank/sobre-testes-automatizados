import pytest

from src.api import get_api_data


def test_api_assert_get_api_data_name_is_marcos():
    api_response = get_api_data()

    assert api_response['name'] == 'Marcos'


def test_api_assert_get_api_data_get_nonexistent_key_raises_KeyError():
    api_response = get_api_data()

    with pytest.raises(KeyError):
        print(api_response['sign'])
