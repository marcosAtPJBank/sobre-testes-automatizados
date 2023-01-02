from typing import Union


def convert_to_uppercase(text: str) -> str:
    if not isinstance(text, str):
        raise AttributeError

    retorno = text.upper()

    return retorno


def convert_to_lowercase(text: str) -> str:
    return text.lower()


def convert_to_capitalcase(text: str) -> str:
    return text.capitalize()


def cube_number(number: Union[int, float]) -> Union[int, float]:
    return number ** 3
