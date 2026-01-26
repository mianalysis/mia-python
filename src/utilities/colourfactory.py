from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Dict

if TYPE_CHECKING:
    from src.objects.objs import Objs
    
def getIDHues(objects: Objs,normalised: bool = True) -> Dict[int, float]:
    hues: Dict[int, float] = {}
    if objects is None:
        return hues
    
    for object in objects.values():
        ID: int = object.getID()
        
        # Default hue value in case none is assigned
        H: float = float(object.getID())
        if normalised:
            H = (H * 1048576 % 255) / 255
        
        hues[ID] = H
        
    return hues
