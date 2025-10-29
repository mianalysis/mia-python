from __future__ import annotations
from typing import Dict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.objects.objs import Objs
    from src.objects.coordinateset import CoordinateSetFactory
    from src.objects.image import Image
    
from src.objects.volume import Volume

class Obj(Volume):
    # private LinkedHashMap<String, Measurement> measurements = new LinkedHashMap<>();
    # private LinkedHashMap<String, ObjMetadata> metadata = new LinkedHashMap<>();
    # private HashMap<Integer, Roi> rois = new HashMap<>();
    
    def __init__(self, obj_collection: Objs, coordinate_set_factory: CoordinateSetFactory, ID: int, spat_cal=None):        
        if spat_cal is None:
            spat_cal = obj_collection.getSpatialCalibration()
            
        super().__init__(coordinate_set_factory, spat_cal=spat_cal)
        
        self._ID: int = ID
        self._obj_collection: Objs = obj_collection
        self._T: int = 0
        self._parents: Dict[str, Obj] = {}
        self._children: Dict[str, Objs] = {}
        self._partners: Dict[str, Objs] = {}

    def getObjectCollection(self) -> Objs:
        return self._obj_collection

    def setObjectCollection(self, obj_collection: Objs):
        self._obj_collection = obj_collection

    def getName(self) -> str:
        return self._obj_collection.getName()

    def getID(self) -> int:
        return self._ID

    def setID(self, ID: int) -> Obj:
        self._ID = ID
        
        return self

    def getT(self) -> int:
        return self._T

    def setT(self, T: int) -> Obj:
        self._T = T
        
        return self

    def getAllParents(self) -> Dict[str, Obj]:
        raise Exception('ObjWrapper: Implement getAllParents')

    def setAllParents(self, parents: Dict[str, Obj]):
        raise Exception('ObjWrapper: Implement setAllParents')

    def getAllChildren(self) -> Dict[str, Objs]:
        raise Exception('ObjWrapper: Implement getAllChildren')

    def setAllChildren(self, children: Dict[str, Objs]):
        raise Exception('ObjWrapper: Implement setAllChildren')

    def getAllPartners(self) -> Dict[str, Objs]:
        raise Exception('ObjWrapper: Implement getAllPartners')

    def setAllPartners(self, partners: Dict[str, Objs]):
        raise Exception('ObjWrapper: Implement setAllPartners')

    def removeRelationships(self): # No return
        raise Exception('ObjWrapper: Implement removeRelationships')

    def getMeasurements(self): # To do
        raise Exception('ObjWrapper: Implement getMeasurements')

    def setMeasurements(self, measurements): # To do
        raise Exception('ObjWrapper: Implement setMeasurements')

    def getMetadata(self): # To do
        raise Exception('ObjWrapper: Implement getMetadata')

    def setMetadata(self, metadata): # To do
        raise Exception('ObjWrapper: Implement setMetadata')

    def getRoi(self, z_slice): # To do
        raise Exception('ObjWrapper: Implement getRoi')

    def getRois(self): # To do
        raise Exception('ObjWrapper: Implement getRois')

    def clearROIs(self): # No return
        raise Exception('ObjWrapper: Implement clearROIs')

    def duplicate(self, new_collection: Objs, duplicate_relationships: bool, duplicate_measurements: bool, duplicate_metadata: bool) -> Obj:
        raise Exception('ObjWrapper: Implement duplicate')

    def equalsIgnoreNameAndID(self, obj: Obj) -> bool:
        raise Exception('ObjWrapper: Implement equalsIgnoreNameAndID')

    def toString(self) -> str:
        return f"Object \"{self.getName()}\", ID = {self.getID()}, frame = {self.getT()}"
    
    
    # Obj default methods
    
    def addToImage(self, image: Image, hue: float): # No return
        raise Exception('ObjWrapper: Implement addToImage')
        
    # Volume default methods
    
    def addCoord(self, x: int, y: int, z: int): # No return
        super().addCoord(x,y,z)