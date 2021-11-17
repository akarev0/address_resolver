
from fastapi import FastAPI, status
from pydash import get
from services.google import GoogleHandler
import services.postal as postal_service
from models.default_model import CombinedAddress

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
def health_check():
    """Simple health check"""


@app.get("/parse", status_code=status.HTTP_200_OK)
def parse(address: str) -> CombinedAddress:
    """Parse provided address with libpostal and details from google API"""
    combined_address = dict()
    # parsed address with libpostal
    combined_address["address_info"] = postal_service.parseAddress(address=address)
    # raw address from request
    combined_address["raw_input"] = address
    # details parsed from google maps
    google_handler = GoogleHandler(address=address)
    google_results = google_handler.parse_address()
    combined_address["coordinates"] = get(google_results, "coordinates")
    combined_address["place_id"] = get(google_results, "place_id")

    return CombinedAddress.parse_obj(combined_address)
