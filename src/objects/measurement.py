from __future__ import annotations
from src.objects.units import replaceSpatialUnits, replaceTemporalUnits

class Measurement:
    def __init__(self, name: str, value: float):
        name = replaceSpatialUnits(name)
        name = replaceTemporalUnits(name)
        
        self._name: str = name
        self._value: float = value
        
    def duplicate(self) -> Measurement:
        return Measurement(self._name, self._value)

    def getName(self) -> str:
        return self._name
    
    def getValue(self) -> float:
        return self._value
    
    def setValue(self, value: float):
        self._value =value
