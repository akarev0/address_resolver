import requests
from typing import Dict, Optional
from pydash import get
import services.mongo as mongo_services
from constants import GOOGLE_MAPS_BASE_URL, GOOGLE_API_KEY, GOOGLE_GEO_BASE_URL


class GoogleHandler:
    def __init__(self, address: str) -> None:
        self.address = address
        self.api_key = GOOGLE_API_KEY
        self.base_maps_url = GOOGLE_MAPS_BASE_URL
        self.base_geocode_url = GOOGLE_GEO_BASE_URL

    def parse_address(self) -> Dict[str, str]:
        if existing_address := mongo_services.check_mongo_for_address(self.address):
            # do we need to return existing address or pick up place_id and call google with it
            # url: str = f"{self.base_maps_url}?placeid={existing_address}&key={self.api_key}"
            return self.standardize_google_response(existing_address)
        else:
            url: str = f"{self.base_geocode_url}?address={self.address}key={self.api_key}"
        response: Dict = self._call(url=url)
        return self.standardize_google_response(response)

    def address_from_coordinates(self, longitude: float, latitude: float):
        url: str = f"{GOOGLE_GEO_BASE_URL}?latlng={longitude, latitude}key={self.api_key}"
        response: Dict = self._call(url=url)
        return self.standardize_google_response(response)

    @staticmethod
    def _call(url: str, params: Dict = None) -> Optional[Dict[str, str]]:
        """call to provided url"""
        if not url:
            raise ValueError("Missed URL for call")

        response = requests.get(url)
        if response.ok:
            return response.json()
        raise ValueError(f"Incorrect response status_code: {response.status_code}")

    @staticmethod
    def standardize_google_response(raw_response: Dict) -> Dict:
        result = dict()
        result["coordinates"] = get(raw_response, "result.geometry.location")
        result["place_id"] = get(raw_response, "result.place_id")

        return result
