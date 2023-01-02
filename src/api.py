from typing import Dict
from typing import Union


def get_api_data() -> Dict[str, Union[str, int]]:
    return {
        'name': 'Marcos',
        'age': 25,
        'job': 'Data Engineer'
    }


def get_api_data_v2() -> Dict[str, Union[str, int]]:
    return {
        'name': 'Marcos',
        'age': 25,
        'job': 'Data Engineer',
        'sign': 'Aquarius'
    }
