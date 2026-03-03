from abc import ABC, abstractmethod

class Ref(ABC):
    def __init__(self, name: str):
        self._name = name
        self._nickname = name
        self._description = ""
        
    def getName(self) -> str:
        return self._name
    
    def getDescription(self) -> str:
        return self._description
    
    def setDescription(self, description: str):
        self._description = description
        
    def getNickname(self) -> str:
        return self._nickname
    
    def setNickname(self, nickname: str):
        self._nickname = nickname
    
    @abstractmethod
    def appendXMLAttributes(self, element): ...
    
    @abstractmethod
    def setAttributesFromXML(self, node): ...
    