from typing import Dict
from pytest import fixture
from mock_data.response_examples import google_response, postal_response


@fixture
def google() -> Dict[str, str]:
    return google_response


@fixture
def place_id() -> str:
    return "ChIJgUbEo8cfqokR5lP9_Wh_DaM"


@fixture
def address() -> str:
    return "The Boulevard Flat 19, Harbour Reach London SW62SS Spain"


@fixture
def postal() -> Dict[str, str]:
    return postal_response
