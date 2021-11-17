from pydantic import BaseModel, validator, Field
from typing import Optional


class DefaultAddressModel(BaseModel):

    # venue name e.g. "Brooklyn Academy of Music", and building names e.g. "Empire State Building"
    house: Optional[str]
    # for category queries like "restaurants", etc.
    category: Optional[str]
    # phrases like "in", "near", etc. used after a category phrase to help with parsing queries like
    # "restaurants in Brooklyn"
    near: Optional[str]
    # usually refers to the external (street-facing) building number. In some countries this may be a compount,
    # hyphenated number which also includes an apartment number, or a block number (a la Japan),
    # but libpostal will just call it the house_number for simplicity.
    house_number: Optional[str]
    # street name(s)
    road: Optional[str]
    # an apartment, unit, office, lot, or other secondary unit designator
    unit: Optional[str]
    # expressions indicating a floor number e.g. "3rd Floor", "Ground Floor", etc.
    level: Optional[str]
    # numbered / lettered staircase
    staircase: Optional[str]
    # numbered / lettered entrance
    entrance: Optional[str]
    # post office
    po_box: Optional[str]
    # typically found in non - physical(mail - only) addresses
    box: Optional[str]
    # postalcodes used for mail sorting
    postcode: Optional[str]
    # usually an unofficial neighborhood name like "Harlem", "South Bronx", or "Crown Heights"
    suburb: Optional[str]
    # these are usually boroughs or districts within a city that serve some official purpose e.g. "Brooklyn"
    # or "Hackney" or "Bratislava IV"
    city_district: Optional[str]
    # any human settlement including cities, towns, villages,
    # hamlets, localities, etc. island: named islands e.g. "Maui"
    city: Optional[str]
    # usually a second - level administrative division or county.
    state_district: Optional[str]
    # a first - level administrative division.Scotland, Northern Ireland, Wales, and England in the UK are mapped to
    # "state" as well(convention used in OSM, GeoPlanet, etc.)
    state: Optional[str]
    # informal subdivision of a country without any political status
    country_region: Optional[str]
    # sovereign nations and their dependent territories, anything with an ISO-3166 code.
    country: Optional[str]
    # currently only used for appending “West Indies” after the country name, a pattern frequently used in the
    # English-speaking Caribbean e.g.“Jamaica, West Indies”
    world_region: Optional[str]

    @validator("city", "country", always=True)
    def capitalizeValues(cls, value) -> str:
        return value.capitalize()

    @validator("postcode", always=True)
    def toUpperCase(cls, value) -> str:
        return value.upper()


class Coordinates(BaseModel):
    latitude: float = Field(alias="lat")
    longitude: float = Field(alias="lng")


class CombinedAddress(BaseModel):
    address_info: DefaultAddressModel
    raw_input: str
    coordinates: Coordinates
    place_id: str
