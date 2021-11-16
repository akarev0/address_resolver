from typing import Dict, List, Tuple
from postal.parser import parse_address
from fastapi import APIRouter, status
from models.default_model import DefaultAddressModel

router = APIRouter(
    prefix="/postal",
    tags=["postal"]
)


@router.get("/parse", status_code=status.HTTP_200_OK)
def parse(address: str) -> Dict[str, str]:
    """Parse provided addres with libpostal"""
    parsed_address: List[Tuple[str, str]] = parse_address(address)
    converted_to_dict: Dict[str, str] = {
        field[1]: field[0] for field in parsed_address}
    return DefaultAddressModel.parse_obj(converted_to_dict)
