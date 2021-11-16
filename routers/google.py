import requests
from typing import Dict
from fastapi import APIRouter
from googlemaps import Client

from constants import GOOGLE_BASE_URL, GOOGLE_API_KEY

router = APIRouter(
    prefix="/google",
    tags=["google"]
)


@router.get("/geocode")
def geocode_from_address(address: str) -> Dict[str, str]:
    gclient = get_google_client()
    return gclient.geocode(address=address)


@router.get("/coordinates")
def address_from_coordinates(longitude: float, latitude: float):
    gclient = get_google_client()
    return gclient.reverse_geocode((longitude, latitude))


@router.get("/place_id")
def address_by_place_id(place_id: str):
    url: str = f"{GOOGLE_BASE_URL}?placeid={place_id}&key={GOOGLE_API_KEY}"
    return requests.get(url=url)


def get_google_client():
    return Client(key=GOOGLE_API_KEY)
