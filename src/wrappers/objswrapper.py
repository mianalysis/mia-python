from __future__ import annotations

from jpype import JImplements, JOverride # type: ignore
from typing import Dict, List
from typing import TYPE_CHECKING

from src.objects.objs import Objs
from src.wrappers.objwrapper import ObjWrapper

if TYPE_CHECKING:
    from src.objects.obj import Obj
    from src.wrappers.imagewrapper import ImageWrapper    
    from src.wrappers.coordinatesetwrapper import CoordinateSetFactoryWrapper
    from src.types.JPointType import JPointType
    from src.types.JSpatioTemporallyCalibrated import JSpatioTemporallyCalibrated

@JImplements('io.github.mianalysis.mia.object.ObjsI') # type: ignore
class ObjsWrapper():
    def __init__(self, name: str, width: int, height: int, n_slices: int, dpp_xy: float, dpp_z: float, spatial_units: str, n_frames: int, frame_interval: float, temporal_unit): # To do
        self._objs: Objs = Objs(name, width, height, n_slices, dpp_xy, dpp_z, spatial_units, n_frames, frame_interval, temporal_unit)
        print("Created")
        
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
        return self._objs.getName()
    
    @JOverride
    def add(self, object: ObjWrapper): # No return
        raise Exception('ObjsWrapper: Implement add')
        
    @JOverride
    def getAndIncrementID(self) -> int:
        print("Incrementing")
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
    def setCalibrationFromExample(self, example: JSpatioTemporallyCalibrated, update_all_objects: bool): # No return
        raise Exception('ObjsWrapper: Implement setCalibrationFromExample')
    
    @JOverride
    def getNFrames(self) -> int:
        raise Exception('ObjsWrapper: Implement getNFrames')
    
    @JOverride
    def setNFrames(self, nFrames: int): # No return
        raise Exception('ObjsWrapper: Implement setNFrames')
    
    @JOverride
    def getFrameInterval(self) -> float:
        raise Exception('ObjsWrapper: Implement getFrameInterval')
    
    @JOverride
    def setFrameInterval(self, frame_interval: float): # No return
        raise Exception('ObjsWrapper: Implement setFrameInterval')
    
    @JOverride
    def getTemporalUnit(self): # To do
        raise Exception('ObjsWrapper: Implement getTemporalUnit')
    
    @JOverride
    def setTemporalUnit(self, temporal_unit): # No return
        raise Exception('ObjsWrapper: Implement setTemporalUnit')
        
    @JOverride
    def duplicate(self, new_objects_name: str, duplicate_relationships: bool, duplicate_measurement: bool,
                  duplicate_metadata: bool, add_original_duplicate_relationship: bool) -> ObjsWrapper:
        raise Exception('ObjsWrapper: Implement duplicate')


    # Default methods

    @JOverride
    def getWidth(self) -> int:
        return self._objs.getWidth()
    
    @JOverride
    def setWidth(self, width: int): # No return
        self._objs.setWidth(width)
    
    @JOverride
    def getHeight(self) -> int:
        return self._objs.getHeight()
    
    @JOverride
    def setHeight(self, height: int): # No return
        self._objs.setHeight(height)
    
    @JOverride
    def getNSlices(self) -> int:
        return self._objs.getNSlices()
    
    @JOverride
    def setNSlices(self, n_slices: int): # No return
        self._objs.setNSlices(n_slices)
    
    @JOverride
    def getDppXY(self) -> float:
        return self._objs.getDppXY()
    
    @JOverride
    def setDppXY(self, dpp_xy: float): # No return
        self._objs.setDppXY(dpp_xy)
    
    @JOverride
    def getDppZ(self) -> float:
        return self._objs.getDppZ()
    
    @JOverride
    def setDppZ(self, dpp_z: float): # No return
        self._objs.setDppZ(dpp_z)
    
    @JOverride
    def getSpatialUnits(self) -> str:
        return self._objs.getSpatialUnits()
    
    @JOverride
    def setSpatialUnits(self, spatial_units: str): # No return
        self._objs.setSpatialUnits(spatial_units)
    
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
        prevObj: Obj = self._objs.get(key)
        prevObjWrapper: ObjWrapper | None = None
        
        if prevObj is not None:
            prevObjWrapper = ObjWrapper(None, None, 1)
            prevObjWrapper.setPythonObj(prevObj)
            
        self._objs.put(key, value.getPythonObj())
        
        return prevObjWrapper
    
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
    def values(self) -> List[ObjWrapper]:
        vals: List[ObjWrapper] = []
        
        for obj in self._objs.values():
            obj_wrapper = ObjWrapper(None, None, 1)
            obj_wrapper.setPythonObj(obj)
            vals.append(obj_wrapper)
        
        return vals
    
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
        
        obj_wrapper = ObjWrapper(None, None, 1)
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
    def createObjs(self, name: str, width: int, height: int, n_slices: int, dpp_xy: float, dpp_z: float, spatial_units: str, n_frames: int, frame_interval: float, temporal_unit) -> ObjsWrapper: # To do
        
        print("Creating from raw values")
        
        return ObjsWrapper(name, width, height, n_slices, dpp_xy, dpp_z, spatial_units, n_frames, frame_interval, temporal_unit)

    @JOverride
    def createFromExample(self, name: str, example_objs: ObjsWrapper) -> ObjsWrapper:
        width: int = example_objs.getWidth()
        height: int = example_objs.getHeight()
        n_slices: int = example_objs.getNSlices()
        dpp_xy: float = example_objs.getDppXY()
        dpp_z: float = example_objs.getDppZ()
        spatial_units: str = example_objs.getSpatialUnits()
        n_frames: int = example_objs.getNFrames()
        frame_interval: float = example_objs.getFrameInterval()
        temporal_unit = example_objs.getTemporalUnit()
        
        return ObjsWrapper(name, width, height, n_slices, dpp_xy, dpp_z, spatial_units, n_frames, frame_interval, temporal_unit)

    @JOverride
    def createFromImage(self, name: str, image_for_calibration: ImageWrapper) -> ObjsWrapper: # To do
        width: int = image_for_calibration.getWidth()
        height: int = image_for_calibration.getHeight()
        n_slices: int = image_for_calibration.getNSlices()
        dpp_xy: float = image_for_calibration.getDppXY()
        dpp_z: float = image_for_calibration.getDppZ()
        spatial_units: str = image_for_calibration.getSpatialUnits()
        n_frames: int = image_for_calibration.getNFrames()
        frame_interval: float = image_for_calibration.getFrameInterval()
        temporal_unit = image_for_calibration.getTemporalUnit()
        
        print("Creating from image")
        output: ObjsWrapper = ObjsWrapper(name, width, height, n_slices, dpp_xy, dpp_z, spatial_units, n_frames, frame_interval, temporal_unit)
        print(output)
        return output
                
    @JOverride
    def duplicate(self) -> ObjsFactoryWrapper:
        return ObjsFactoryWrapper()
        