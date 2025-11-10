from __future__ import annotations
from jpype import JImplements, JOverride # type: ignore
from typing import Dict
from typing import TYPE_CHECKING

from src.objects.objs import Objs

if TYPE_CHECKING:
    from src.objects.obj import Obj
    from src.wrappers.imagewrapper import ImageWrapper
    from src.wrappers.objwrapper import ObjWrapper
    from src.wrappers.coordinatesetwrapper import CoordinateSetFactoryWrapper
    from types.JPointType import JPointType
    from types.JPype import *


# @JImplements('io.github.mianalysis.mia.object.ObjsI') # type: ignore
class ObjsWrapper():      
    def __init__(self):
        self._objs: Objs = Objs()
        
    def getPythonObjs(self) -> Objs:
        return self._objs
    
    def setPythonObjs(self, objs: Objs):
        self._objs = objs
        
    @JOverride
    def createAndAddNewObject(self, factory: CoordinateSetFactoryWrapper) -> ObjWrapper:
        raise Exception('ObjsWrapper: Implement createAndAddNewObject')
    
    @JOverride
    def createAndAddNewObjectWithID(self, factory: CoordinateSetFactoryWrapper, ID: int) -> ObjWrapper:
        raise Exception('ObjsWrapper: Implement createAndAddNewObjectWithID')
        
    @JOverride
    def getName(self) -> str:
        raise Exception('ObjsWrapper: Implement getName')
    
    @JOverride
    def add(self, object: ObjWrapper): # No return
        raise Exception('ObjsWrapper: Implement add')
    
    @JOverride
    def getSpatialCalibration(self): # To do
        raise Exception('ObjsWrapper: Implement getSpatialCalibration')
    
    @JOverride
    def setSpatialCalibration(self, spat_cal, update_all_objects: bool): # To do
        raise Exception('ObjsWrapper: Implement setSpatialCalibration')
    
    @JOverride
    def getAndIncrementID(self) -> int:
        return self._objs.getAndIncrementID()
    
    @JOverride
    def resetCollection(self): # No return
        raise Exception('ObjsWrapper: Implement resetCollection')
    
    @JOverride
    def recalculateMaxID(self): # No return
        raise Exception('ObjsWrapper: Implement recalculateMaxID')
    
    @JOverride
    def getAsSingleObject(self) -> ObjWrapper:
        raise Exception('ObjsWrapper: Implement getAsSingleObject')
    
    @JOverride
    def getObjectsInFrame(self, output_objects_name: str, frame: int) -> ObjsWrapper:
        raise Exception('ObjsWrapper: Implement getObjectsInFrame')
    
    @JOverride
    def getNFrames(self) -> int:
        raise Exception('ObjsWrapper: Implement getNFrames')
    
    @JOverride
    def getFrameInterval(self) -> float:
        raise Exception('ObjsWrapper: Implement getFrameInterval')
    
    @JOverride
    def getTemporalUnit(self): # To do
        raise Exception('ObjsWrapper: Implement getTemporalUnit')
    
    @JOverride
    def setNFrames(self, nFrames: int): # No return
        raise Exception('ObjsWrapper: Implement setNFrames')
    
    @JOverride
    def duplicate(self, new_objects_name: str, duplicate_relationships: bool, duplicate_measurement: bool,
                  duplicate_metadata: bool, add_original_duplicate_relationship: bool) -> ObjsWrapper:
        raise Exception('ObjsWrapper: Implement duplicate')


    # Default methods

    @JOverride
    def getWidth(self) -> int:
        raise Exception('ObjsWrapper: Implement getWidth')
    
    @JOverride
    def getHeight(self) -> int:
        raise Exception('ObjsWrapper: Implement getHeight')
    
    @JOverride
    def getNSlices(self) -> int:
        raise Exception('ObjsWrapper: Implement getNSlices')
    
    @JOverride
    def getDppXY(self) -> float:
        raise Exception('ObjsWrapper: Implement getDppXY')
    
    @JOverride
    def getDppZ(self) -> float:
        raise Exception('ObjsWrapper: Implement getDppZ')
    
    @JOverride
    def getSpatialUnits(self) -> str:
        raise Exception('ObjsWrapper: Implement getSpatialUnits')
    
    @JOverride
    def getFirst(self) -> ObjWrapper:
        raise Exception('ObjsWrapper: Implement getFirst')
    
    @JOverride
    def getSpatialExtents(self): # To do
        raise Exception('ObjsWrapper: Implement getSpatialExtents')
    
    @JOverride
    def getSpatialLimits(self): # To do
        raise Exception('ObjsWrapper: Implement getSpatialLimits')
    
    @JOverride
    def getTemporalLimits(self): # To do
        raise Exception('ObjsWrapper: Implement getTemporalLimits')
    
    @JOverride
    def getLargestID(self) -> int:
        raise Exception('ObjsWrapper: Implement getLargestID')
        
    @JOverride
    def convertToImage(self, outputName: str, hues, bitDepth: int, nanBackground: bool, verbose: bool) -> ImageWrapper: # To do
        raise Exception('ObjsWrapper: Implement convertToImage')
    
    @JOverride
    def convertToImageRandomColours(self) -> ImageWrapper:
        raise Exception('ObjsWrapper: Implement convertToImageRandomColours')
        
    @JOverride
    def convertToImageBinary(self, name: str) -> ImageWrapper:
        raise Exception('ObjsWrapper: Implement convertToImageBinary')
    
    @JOverride
    def convertToImageIDColours(self) -> ImageWrapper:
        raise Exception('ObjsWrapper: Implement convertToImageIDColours')
    
    @JOverride
    def convertCentroidsToImage(self, outputName: str, hues, bitDepth: int, nanBackground: bool) -> ImageWrapper: # To do
        raise Exception('ObjsWrapper: Implement convertCentroidsToImage')
    
    @JOverride
    def applyCalibration(self, image: ImageWrapper): # No return
        raise Exception('ObjsWrapper: Implement applyCalibration')
    
    @JOverride
    def applyCalibrationFromImagePlus(self, ipl): # To do
        raise Exception('ObjsWrapper: Implement applyCalibrationFromImagePlus')
    
    @JOverride
    def createImage(self, outputName: str, bitDepth: int) -> ImageWrapper:
        raise Exception('ObjsWrapper: Implement createImage')
    
    @JOverride
    def setNaNBackground(self, ipl): # To do
        raise Exception('ObjsWrapper: Implement setNaNBackground')
    
    @JOverride
    def getByEqualsIgnoreNameAndID(self, referenceObj: ObjWrapper) -> ObjWrapper:
        raise Exception('ObjsWrapper: Implement getByEqualsIgnoreNameAndID')
    
    @JOverride
    def showMeasurements(self, module, modules): # To do
        raise Exception('ObjsWrapper: Implement showMeasurements')
    
    @JOverride
    def showAllMeasurements(self): # No return
        raise Exception('ObjsWrapper: Implement showAllMeasurements')
    
    @JOverride
    def showMetadata(self, module, modules): # To do
        raise Exception('ObjsWrapper: Implement showMetadata')
    
    @JOverride
    def showAllMetadata(self): # No return
        raise Exception('ObjsWrapper: Implement showAllMetadata')
    
    @JOverride
    def removeParents(self, parentObjectsName: str): # No return
        raise Exception('ObjsWrapper: Implement removeParents')
    
    @JOverride
    def removeChildren(self, childObjectsName: str): # No return
        raise Exception('ObjsWrapper: Implement removeChildren')
    
    @JOverride
    def removePartners(self, partnerObjectsName: str): # No return
        raise Exception('ObjsWrapper: Implement removePartners')
    
    @JOverride
    def containsPoint(self, point: JPointType[int]) -> bool:
        raise Exception('ObjsWrapper: Implement containsPoint')
    
    @JOverride
    def containsCoord(self, x: int, y: int, z: int) -> bool:
        raise Exception('ObjsWrapper: Implement containsCoord')
    
    @JOverride
    def getLargestObject(self, t: int) -> ObjWrapper:
        raise Exception('ObjsWrapper: Implement getLargestObject')
    
    @JOverride
    def getSmallestObject(self, t: int) -> ObjWrapper:
        raise Exception('ObjsWrapper: Implement getSmallestObject')


    # From Map

    @JOverride
    def get(self, key: int) -> ObjWrapper:
        raise Exception('MapWrapper: Implement size')
    
    @JOverride
    def size(self) -> int:
        raise Exception('MapWrapper: Implement size')
    
    @JOverride
    def isEmpty(self) -> bool:
        raise Exception('MapWrapper: Implement isEmpty')
    
    @JOverride
    def containsKey(self, key: int) -> bool:
        raise Exception('MapWrapper: Implement containsKey')
    
    @JOverride
    def containsValue(self, value: ObjWrapper) -> bool:
        raise Exception('MapWrapper: Implement containsValue')
        
    @JOverride
    def put(self, key: int, value: ObjWrapper) -> ObjWrapper:
        raise Exception('MapWrapper: Implement put')
    
    @JOverride
    def remove(self, key: int) -> ObjWrapper:
        raise Exception('MapWrapper: Implement remove')
    
    @JOverride
    def putAll(self, m: Dict[int, Obj]): # No return
        raise Exception('MapWrapper: Implement putAll')
    
    @JOverride
    def clear(self): # No return
        raise Exception('MapWrapper: Implement clear')
    
    @JOverride
    def keySet(self): # To do
        raise Exception('MapWrapper: Implement keySet')
    
    @JOverride
    def values(self): # To do
        raise Exception('MapWrapper: Implement values')
    
    @JOverride
    def entrySet(self): # To do
        raise Exception('MapWrapper: Implement entrySet')

    @JOverride
    def equals(self, o: ObjsWrapper) -> bool:
        raise Exception('MapWrapper: Implement equals')
    
    @JOverride
    def hashCode(self) -> int:
        raise Exception('MapWrapper: Implement hashCode')
    
    @JOverride
    def getOrDefault(self, key: int, defaultValue: ObjWrapper) -> ObjWrapper:
        raise Exception('MapWrapper: Implement getOrDefault')
    
    @JOverride
    def forEach(self, action): # To do
        raise Exception('MapWrapper: Implement forEach')
    
    @JOverride
    def replaceAll(self, function): # To do
        raise Exception('MapWrapper: Implement replaceAll')
    
    @JOverride
    def putIfAbsent(self, key: int, value: ObjWrapper) -> ObjWrapper:
        obj: Obj = self._objs.putIfAbsent(key, value.getPythonObj())
        
        obj_wrapper = ObjWrapper()
        obj_wrapper.setPythonObj(obj)
        
        return obj_wrapper
    
    # @JOverride
    # def removeKeyValue(self, key, value):
    #     raise Exception('MapWrapper: Implement remove (key, value)')
    
    # @JOverride
    # def replaceKeyValue(self, key, oldValue, newValue):
    #     raise Exception('MapWrapper: Implement replace (key, oldValue, newValue)')
    
    @JOverride
    def replace(self, key: int, value: ObjWrapper) -> bool:
        raise Exception('MapWrapper: Implement replace (key, value)')
    
    @JOverride
    def computeIfAbsent(self, key, mapping_function): # To do
        raise Exception('MapWrapper: Implement computeIfAbsent')
    
    @JOverride
    def computeIfPresent(self, key, remappingFunction): # To do
        raise Exception('MapWrapper: Implement computeIfPresent')
    
    @JOverride
    def compute(self, key, remappingFunction): # To do
        raise Exception('MapWrapper: Implement compute')
    
    @JOverride
    def merge(self, key, value, remappingFunction): # To do
        raise Exception('MapWrapper: Implement merge')

    # Note: May also need to implement the Entry interface:

    # @JOverride
    # def getKey(self):
    #     raise Exception('EntryWrapper: Implement getKey')
    
    # @JOverride
    # def getValue(self):
    #     raise Exception('EntryWrapper: Implement getValue')
    
    # @JOverride
    # def setValue(self, value):
    #     raise Exception('EntryWrapper: Implement setValue')
    
    # @JOverride
    # def equals(self, o):
    #     raise Exception('EntryWrapper: Implement equals')
    
    # @JOverride
    # def hashCode(self):
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



@JImplements('io.github.mianalysis.mia.object.ObjsFactoryI')
class ObjsFactoryWrapper:
    
    @JOverride
    def getName(self) -> str:
        return "Python objects factory"
    
    @JOverride
    def createObjs(self, name: str, dppXY: float, dppZ: float, units: str, width: int, height: int, nSlices: int, nFrames: int, frameInterval: float, temporalUnit) -> ObjsWrapper: # To do
        raise Exception('ObjsFactoryWrapper: Implement createObjs 1')
        return ObjsWrapper()
        # return ObjsWrapper(name, dppXY, dppZ, units, width, height, nSlices, nFrames, frameInterval, temporalUnit)

    @JOverride
    def createFromExampleObjs(self, name: str, example_objs: ObjsWrapper) -> ObjsWrapper:
        raise Exception('ObjsFactoryWrapper: Implement createObjs 2')
        return ObjsWrapper()
        # return ObjsWrapper(name, name, imageForCalibration)

    @JOverride
    def createFromImage(self, name: str, imageForCalibration) -> ObjsWrapper: # To do
        raise Exception('ObjsFactoryWrapper: Implement createObjs 3')
        return ObjsWrapper()
        # return ObjsWrapper(name, name, imageForCalibration)
        
    @JOverride
    def createFromSpatCal(self, name: str, spat_cal, nFrames: int, frameInterval: float, temporalUnit) -> ObjsWrapper: # To do
        # raise Exception('ObjsFactoryWrapper: Implement createObjs 4')
        return ObjsWrapper()
        # return ObjsWrapper(name, cal, nFrames, frameInterval, temporalUnit)
        
    @JOverride
    def duplicate(self) -> ObjsFactoryWrapper:
        return ObjsFactoryWrapper()
        