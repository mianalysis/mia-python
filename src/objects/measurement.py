from __future__ import annotations

class Measurement:
    def __init__(self, name: str, value: float):
        # print("Measurement: Implement units conversion in __init__")
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
