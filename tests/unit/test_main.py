from main import parse
from models.default_model import CombinedAddress, DefaultAddressModel, Coordinates


def test_parse(mocker, place_id, address, google, postal):
    mocker.patch("services.google.GoogleHandler._call", return_value=google)
    mocker.patch("services.postal.parseAddress", return_value=postal)

    response = parse(address)

    assert isinstance(response, CombinedAddress)
    assert response.place_id is None
    assert isinstance(response.raw_input, str)
    assert isinstance(response.address_info, DefaultAddressModel)
    assert response.coordinates is None
