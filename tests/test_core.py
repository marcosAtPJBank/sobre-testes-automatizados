import pytest

from src.core import convert_to_uppercase
from src.core import cube_number


def test_core_assert_convert_to_uppercase_returns_uppercased_text():
    retorno = convert_to_uppercase(text='datalake')

    assert retorno == 'DATALAKE'


def test_core_assert_convert_to_uppercase_int_type_raises_AttributeError():
    with pytest.raises(AttributeError):
        convert_to_uppercase(text=1)


def test_core_asserts_cube_number_2_is_8():
    retorno = cube_number(number=2)

    assert retorno == 8
