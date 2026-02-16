from typing import Dict

PIXELS: str = "Pixels"
METRE: str = "Metres"
CENTIMETRE: str = "Centimetres"
MILLIMETRE: str = "Millimetres"
MICROMETRE: str = "Micrometres"
NANOMETRE: str = "Nanometres"
ANGSTROM: str = "Angstroms"

FRAMES: str = "Frames"
NANOSECOND: str = "Nanoseconds"
MILLISECOND: str = "Milliseconds"
SECOND: str = "Seconds"
MINUTE: str = "Minutes"
HOUR: str = "Hours"
DAY: str = "Days"

class Units:
    spatial_units: str = PIXELS
    temporal_units: str = FRAMES
    
def replaceSpatialUnits(input_string: str) -> str:
    return input_string.replace("${SCAL}", getSpatialSymbol())

def getSpatialSymbol() -> str:
    symbol_map: Dict[str, str] = {
        PIXELS: "px",
        METRE: "m",
        CENTIMETRE: "cm",
        MILLIMETRE: "mm",
        MICROMETRE: "μm",
        NANOMETRE: "nm",
        ANGSTROM: "Å"
    }
    
    if Units.spatial_units in symbol_map:
        return symbol_map[Units.spatial_units]
    
    return ""         

def replaceTemporalUnits(input_string: str) -> str:
    return input_string.replace("${TCAL}", getTemporalSymbol())

def getTemporalSymbol() -> str:
    symbol_map: Dict[str, str] = {
        FRAMES: "fr",
        NANOSECOND: "ns",
        MILLISECOND: "ms",
        SECOND: "s",
        MINUTE: "min",
        HOUR: "h",
        DAY: "days"
    }
    
    if Units.temporal_units in symbol_map:
        return symbol_map[Units.temporal_units]

    return ""
