from typing import Dict, List, Tuple
from postal.parser import parse_address


def parseAddress(address: str) -> Dict[str, str]:
    """Parse provided address with libpostal"""

    parsed_address: List[Tuple[str, str]] = parse_address(address)

    converted_address = {
        field[1]: field[0] for field in parsed_address
    }

    return converted_address
