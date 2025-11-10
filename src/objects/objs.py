# Note: Can this extend Dict (e.g. class Objs(Dict[int, Obj])) and have the objswrapper just convert 
# the methods?

from __future__ import annotations
from typing import Dict, List, Tuple
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.objects.coordinateset import CoordinateSetFactory
    from src.objects.image import Image
    from src.objects.obj import Obj
    from src.types.types import Point

class Objs():
    def __init__(self):
        self._objs: Dict[int, Obj] = {}
        self._max_ID: int = 0
        
    def createAndAddNewObject(self, factory: CoordinateSetFactory) -> Obj:
        raise Exception('ObjsWrapper: Implement createAndAddNewObject')
    
    def createAndAddNewObjectWithID(self, factory: CoordinateSetFactory, ID: int) -> Obj:
        raise Exception('ObjsWrapper: Implement createAndAddNewObjectWithID')
        
    def getName(self) -> str:
        raise Exception('ObjsWrapper: Implement getName')
    
    def add(self, object: Obj): # No return
        raise Exception('ObjsWrapper: Implement add')
    
    def getSpatialCalibration(self): # To do
        raise Exception('ObjsWrapper: Implement getSpatialCalibration')
    
    def setSpatialCalibration(self, spat_cal, update_all_objects: bool): # To do
        raise Exception('ObjsWrapper: Implement setSpatialCalibration')
    
    def getAndIncrementID(self) -> int:
        self._max_ID = self._max_ID + 1
        return self._max_ID
    
    def resetCollection(self): # No return
        raise Exception('ObjsWrapper: Implement resetCollection')
    
    def recalculateMaxID(self): # No return
        raise Exception('ObjsWrapper: Implement recalculateMaxID')
    
    def getAsSingleObject(self) -> Obj:
        raise Exception('ObjsWrapper: Implement getAsSingleObject')
    
    def getObjectsInFrame(self, output_objects_name: str, frame: int) -> Objs:
        raise Exception('ObjsWrapper: Implement getObjectsInFrame')
    
    def getNFrames(self) -> int:
        raise Exception('ObjsWrapper: Implement getNFrames')
    
    def getFrameInterval(self) -> float:
        raise Exception('ObjsWrapper: Implement getFrameInterval')
    
    def getTemporalUnit(self): # To do
        raise Exception('ObjsWrapper: Implement getTemporalUnit')
    
    def setNFrames(self, nFrames: int): # No return
        raise Exception('ObjsWrapper: Implement setNFrames')
    
    def duplicate(self, new_objects_name: str, duplicate_relationships: bool, duplicate_measurement: bool,
                  duplicate_metadata: bool, add_original_duplicate_relationship: bool) -> Objs:
        raise Exception('ObjsWrapper: Implement duplicate')


    # Default methods

    def getWidth(self) -> int:
        raise Exception('ObjsWrapper: Implement getWidth')
    
    def getHeight(self) -> int:
        raise Exception('ObjsWrapper: Implement getHeight')
    
    def getNSlices(self) -> int:
        raise Exception('ObjsWrapper: Implement getNSlices')
    
    def getDppXY(self) -> float:
        raise Exception('ObjsWrapper: Implement getDppXY')
    
    def getDppZ(self) -> float:
        raise Exception('ObjsWrapper: Implement getDppZ')
    
    def getSpatialUnits(self) -> str:
        raise Exception('ObjsWrapper: Implement getSpatialUnits')
    
    def getFirst(self) -> Obj:
        raise Exception('ObjsWrapper: Implement getFirst')
    
    def getSpatialExtents(self) -> List[List[int]]:
        raise Exception('ObjsWrapper: Implement getSpatialExtents')
    
    def getSpatialLimits(self) -> List[List[int]]:
        raise Exception('ObjsWrapper: Implement getSpatialLimits')
    
    def getTemporalLimits(self) -> List[int]:
        raise Exception('ObjsWrapper: Implement getTemporalLimits')
    
    def getLargestID(self) -> int:
        raise Exception('ObjsWrapper: Implement getLargestID')
        
    def convertToImage(self, output_name: str, hues: Dict[int, float], bit_depth: int, nanBackground: bool, verbose: bool) -> Image:
        raise Exception('ObjsWrapper: Implement convertToImage')
    
    def convertToImageRandomColours(self) -> Image:
        raise Exception('ObjsWrapper: Implement convertToImageRandomColours')
        
    def convertToImageBinary(self, name: str) -> Image:
        raise Exception('ObjsWrapper: Implement convertToImageBinary')
    
    def convertToImageIDColours(self) -> Image:
        raise Exception('ObjsWrapper: Implement convertToImageIDColours')
    
    def convertCentroidsToImage(self, output_name: str, hues: Dict[int, float], bit_bepth: int, nan_background: bool) -> Image:
        raise Exception('ObjsWrapper: Implement convertCentroidsToImage')
    
    def applyCalibration(self, image: Image): # No return
        raise Exception('ObjsWrapper: Implement applyCalibration')
    
    def applyCalibrationFromImagePlus(self, ipl): # To do
        raise Exception('ObjsWrapper: Implement applyCalibrationFromImagePlus')
    
    def createImage(self, output_name: str, bit_depth: int) -> Image:
        raise Exception('ObjsWrapper: Implement createImage')
    
    def setNaNBackground(self, ipl): # To do
        raise Exception('ObjsWrapper: Implement setNaNBackground')
    
    def getByEqualsIgnoreNameAndID(self, reference_obj: Obj) -> Obj:
        raise Exception('ObjsWrapper: Implement getByEqualsIgnoreNameAndID')
    
    def showMeasurements(self, module, modules): # To do
        raise Exception('ObjsWrapper: Implement showMeasurements')
    
    def showAllMeasurements(self): # No return
        raise Exception('ObjsWrapper: Implement showAllMeasurements')
    
    def showMetadata(self, module, modules): # To do
        raise Exception('ObjsWrapper: Implement showMetadata')
    
    def showAllMetadata(self): # No return
        raise Exception('ObjsWrapper: Implement showAllMetadata')
    
    def removeParents(self, parent_objects_name: str): # No return
        raise Exception('ObjsWrapper: Implement removeParents')
    
    def removeChildren(self, child_objects_name: str): # No return
        raise Exception('ObjsWrapper: Implement removeChildren')
    
    def removePartners(self, partner_objects_name: str): # No return
        raise Exception('ObjsWrapper: Implement removePartners')
    
    def containsPoint(self, point: Point) -> bool:
        raise Exception('ObjsWrapper: Implement containsPoint')
    
    def containsCoord(self, x: int, y: int, z: int) -> bool:
        raise Exception('ObjsWrapper: Implement containsCoord')
    
    def getLargestObject(self, t: int) -> Obj:
        raise Exception('ObjsWrapper: Implement getLargestObject')
    
    def getSmallestObject(self, t: int) -> Obj:
        raise Exception('ObjsWrapper: Implement getSmallestObject')


    # From Map

    def size(self) -> int:
        raise Exception('MapWrapper: Implement size')
    
    def isEmpty(self) -> bool:
        raise Exception('MapWrapper: Implement isEmpty')
    
    def containsKey(self, key: int) -> bool:
        raise Exception('MapWrapper: Implement containsKey')
    
    def containsValue(self, value: Obj) -> bool:
        raise Exception('MapWrapper: Implement containsValue')
        
    def put(self, key: int, value: Obj) -> Obj:
        raise Exception('MapWrapper: Implement put')
    
    def remove(self, key: int) -> Obj:
        raise Exception('MapWrapper: Implement remove')
    
    def putAll(self, m: Dict[int, Obj]): # No return
        raise Exception('MapWrapper: Implement putAll')
    
    def clear(self): # No return
        raise Exception('MapWrapper: Implement clear')
    
    def keySet(self) -> List[int]:
        raise Exception('MapWrapper: Implement keySet')
    
    def values(self) -> List[int]:
        raise Exception('MapWrapper: Implement values')
    
    def entrySet(self) -> List[Tuple[int,Obj]]:
        raise Exception('MapWrapper: Implement entrySet')

    def equals(self, o: Objs) -> bool:
        raise Exception('MapWrapper: Implement equals')
    
    def hashCode(self) -> int:
        raise Exception('MapWrapper: Implement hashCode')
    
    def getOrDefault(self, key: int, defaultValue: Obj) -> Obj:
        raise Exception('MapWrapper: Implement getOrDefault')
    
    def forEach(self, action): # To do
        raise Exception('MapWrapper: Implement forEach')
    
    def replaceAll(self, function): # To do
        raise Exception('MapWrapper: Implement replaceAll')
    
    def putIfAbsent(self, key: int, value: Obj) -> Obj:
        raise Exception('MapWrapper: Implement putIfAbsent')
    
    def replace(self, key: int, value: Obj) -> Obj:
        raise Exception('MapWrapper: Implement replace (key, value)')
    
    def computeIfAbsent(self, key, mappingFunction): # To do
        raise Exception('MapWrapper: Implement computeIfAbsent')
    
    def computeIfPresent(self, key, remappingFunction): # To do
        raise Exception('MapWrapper: Implement computeIfPresent')
    
    def compute(self, key, remappingFunction): # To do
        raise Exception('MapWrapper: Implement compute')
    
    def merge(self, key, value, remappingFunction): # To do
        raise Exception('MapWrapper: Implement merge')

    # Note: May also need to implement the Entry interface:

    # # def getKey(self):
    #     raise Exception('EntryWrapper: Implement getKey')
    
    # # def getValue(self):
    #     raise Exception('EntryWrapper: Implement getValue')
    
    # # def setValue(self, value):
    #     raise Exception('EntryWrapper: Implement setValue')
    
    # # def equals(self, o):
    #     raise Exception('EntryWrapper: Implement equals')
    
    # # def hashCode(self):
    #     raise Exception('EntryWrapper: Implement hashCode')
    
    # # Static comparator methods (if relevant to expose)
    
    # @staticmethod
    # def comparingByKey():
    #     raise Exception('EntryWrapper: Implement comparingByKey')
    
    # @staticmethod
    # def comparingByValue():
    #     raise Exception('EntryWrapper: Implement comparingByValue')
    
    # @staticmethod
    # def comparingByKeyWithComparator(cmp):
    #     raise Exception('EntryWrapper: Implement comparingByKey with comparator')
    
    # @staticmethod
    # def comparingByValueWithComparator(cmp):
    #     raise Exception('EntryWrapper: Implement comparingByValue with comparator')
