from __future__ import annotations

from jpype import JImplements, JOverride # type: ignore
from typing import Dict, List, Self, TYPE_CHECKING
from weakref import WeakKeyDictionary

from src.objects.image import Image
from src.objects.measurement import Measurement
from src.objects.objs import Objs
from src.wrappers.objwrapper import ObjFactoryWrapper, wrapObj
from src.wrappers.imagewrapper import wrapImage
from src.wrappers.measurementwrapper import MeasurementWrapper

if TYPE_CHECKING:
    from src.objects.obj import Obj    
    from src.wrappers.coordinatesetwrapper import CoordinateSetFactoryWrapper
    from src.wrappers.imagewrapper import ImageWrapper
    from src.wrappers.objwrapper import ObjWrapper
    from src.types.JPointType import JPointType
    from src.types.JSpatioTemporallyCalibratedType import JSpatioTemporallyCalibrated

_wrapper_cache: WeakKeyDictionary[Objs, ObjsWrapper] = WeakKeyDictionary()
        
@JImplements('java.util.Iterator')
class ObjsWrapperIterator:
    def __init__(self, objs_wrapper: ObjsWrapper):
        self._objs_wrapper = objs_wrapper
        self._items: List[Obj] = self._objs_wrapper._objs.values()
        self._idx = 0
        self._last_idx = -1
        
    @JOverride
    def hasNext(self):
        return self._idx < len(self._items)
    
    @JOverride
    def next(self):
        if not self.hasNext():
            raise jpype.JClass("java.util.NoSuchElementException")() # type: ignore
        
        obj_wrapper: ObjWrapper = wrapObj(self._items[self._idx])
        
        self._last_idx = self._idx
        self._idx += 1        
        
        return obj_wrapper
    
    @JOverride
    def remove(self):
        if self._last_idx == -1:
            raise jpype.JClass("java.lang.IllegalStateException")() # type: ignore
        
        self._objs_wrapper._objs.remove(self._items[self._last_idx].getID())
        self._last_key = None
        
@JImplements('java.util.Collection')
class ObjsWrapperCollection:
    def __init__(self, objs_wrapper: ObjsWrapper):
        self._objs_wrapper: ObjsWrapper = objs_wrapper
            
    @JOverride
    def add(self, obj_wrapper: ObjWrapper) -> bool:
        self._objs_wrapper.add(obj_wrapper)
        return True
            
    @JOverride
    def addAll(self, collection) -> bool:
        obj_wrapper: ObjWrapper
        for obj_wrapper in collection:
            self._objs_wrapper.add(obj_wrapper)
            
        return True
        
    @JOverride
    def clear(self):
        self._objs_wrapper.clear()
    
    @JOverride
    def contains(self, obj_wrapper: ObjWrapper) -> bool:
        return self._objs_wrapper.containsValue(obj_wrapper)
    
    @JOverride
    def containsAll(self, collection) -> bool:
        raise Exception('ValuesCollection: Implement containsAll')
    
    @JOverride
    def equals(self, values_collection: Self) -> bool:
        raise Exception('ValuesCollection: Implement equals')
    
    @JOverride
    def hashCode(self) -> int:
        raise Exception('ValuesCollection: Implement hashCode')
    
    @JOverride
    def isEmpty(self) -> bool:
        return self._objs_wrapper.isEmpty()
    
    @JOverride
    def iterator(self):
        return ObjsWrapperIterator(self._objs_wrapper)
    
    @JOverride
    def remove(self, obj_wrapper: ObjWrapper) -> bool:
        if obj_wrapper:
            self._objs_wrapper.remove(obj_wrapper.getID())
            
        return True
    
    @JOverride
    def removeAll(self, collection) -> bool:
        obj_wrapper: ObjWrapper
        for obj_wrapper in collection:
            self.remove(obj_wrapper)
            
        return True
    
    @JOverride
    def retainAll(self, collection) -> bool:
        raise Exception('ValuesCollection: Implement retainAll')
    
    @JOverride
    def size(self) -> int:
        return self._objs_wrapper._objs.size()
    
    @JOverride
    def toArray(self): # To do
        raise Exception('ValuesCollection: Implement toArray')

        
@JImplements('io.github.mianalysis.mia.object.ObjsI') # type: ignore
class ObjsWrapper():
    def __init__(self, name: str, width: int, height: int, n_slices: int, dpp_xy: float, dpp_z: float, spatial_units: str, n_frames: int, frame_interval: float, temporal_unit): # To do
        self._objs: Objs = Objs(name, width, height, n_slices, dpp_xy, dpp_z, spatial_units, n_frames, frame_interval, temporal_unit)
        
    def getPythonObjs(self) -> Objs:
        return self._objs
    
    def setPythonObjs(self, objs: Objs):
        self._objs = objs
        
    @JOverride
    def createAndAddNewObject(self, coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper) -> ObjWrapper:
        new_obj: Obj = self._objs.createAndAddNewObject(coordinate_set_factory_wrapper.getPythonCoordinateSetFactory())
        return wrapObj(new_obj)
    
    @JOverride
    def createAndAddNewObjectWithID(self, coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper, ID: int) -> ObjWrapper:
        new_obj: Obj = self._objs.createAndAddNewObjectWithID(coordinate_set_factory_wrapper.getPythonCoordinateSetFactory(), ID)
        return wrapObj(new_obj)
        
    @JOverride
    def getName(self) -> str:
        return self._objs.getName()
    
    @JOverride
    def add(self, obj_wrapper: ObjWrapper): # No return
        self._objs.add(obj_wrapper.getPythonObj())
        
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
    def setCalibrationFromExample(self, example: JSpatioTemporallyCalibrated, update_all_objects: bool): # No return
        raise Exception('ObjsWrapper: Implement setCalibrationFromExample')
    
    @JOverride
    def getNFrames(self) -> int:
        return self._objs.getNFrames()
    
    @JOverride
    def setNFrames(self, n_frames: int): # No return
        self._objs.setNFrames(n_frames)
    
    @JOverride
    def getFrameInterval(self) -> float:
        return self._objs.getFrameInterval()
    
    @JOverride
    def setFrameInterval(self, frame_interval: float): # No return
        self._objs.setFrameInterval(frame_interval)
    
    @JOverride
    def getTemporalUnit(self): # To do
        return self._objs.getTemporalUnit()
    
    @JOverride
    def setTemporalUnit(self, temporal_unit): # No return
        self._objs.setTemporalUnit(temporal_unit)
        
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
    def convertToImage(self, outputName: str, hues: Dict[int, float], bitDepth: int, nanBackground: bool, verbose: bool) -> ImageWrapper:
        python_hues: Dict[int, float] = {}
        key: int
        for key in hues.keys():
            python_hues[int(key)] = float(hues[key])
            
        im: Image = self._objs.convertToImage(outputName, python_hues, bitDepth, nanBackground, verbose)
        return wrapImage(im)
    
    @JOverride
    def convertToImageRandomColours(self) -> ImageWrapper:
        im:  Image = self._objs.convertToImageRandomColours()
        return wrapImage(im)
        
    @JOverride
    def convertToImageBinary(self, name: str) -> ImageWrapper:
        im: Image = self._objs.convertToImageBinary(name)
        return wrapImage(im)
    
    @JOverride
    def convertToImageIDColours(self) -> ImageWrapper:
        im: Image = self._objs.convertToImageIDColours()
        return wrapImage(im)
    
    @JOverride
    def convertCentroidsToImage(self, outputName: str, hues: Dict[int, float], bitDepth: int, nanBackground: bool) -> ImageWrapper:
        im: Image = self._objs.convertCentroidsToImage(outputName, hues, bitDepth, nanBackground)
        return wrapImage(im)
    
    @JOverride
    def applyCalibration(self, image: ImageWrapper): # No return
        raise Exception('ObjsWrapper: Implement applyCalibration')
    
    @JOverride
    def applyCalibrationFromImagePlus(self, ipl): # To do
        raise Exception('ObjsWrapper: Implement applyCalibrationFromImagePlus')
    
    @JOverride
    def createImage(self, outputName: str, bitDepth: int) -> ImageWrapper:
        im: Image = self._objs.createImage(outputName, bitDepth)
        return wrapImage(im)
    
    @JOverride
    def setNaNBackground(self, ipl): # To do
        raise Exception('ObjsWrapper: Implement setNaNBackground')
    
    @JOverride
    def getByEqualsIgnoreNameAndID(self, referenceObj: ObjWrapper) -> ObjWrapper:
        raise Exception('ObjsWrapper: Implement getByEqualsIgnoreNameAndID')
    
    @JOverride
    def showMeasurements(self, module, modules): # To do
        measurement_refs = module.updateAndGetObjectMeasurementRefs()
        if measurement_refs is None:
            return
                
        measurement_names: List[str] = [str(ref.getName()) for ref in measurement_refs.values()]
        
        self._objs.showMeasurements(measurement_names)
    
    @JOverride
    def showAllMeasurements(self): # No return
        measurement_names: List[str] = []
        obj: Obj
        for obj in self._objs.values():
            curr_measurements: Dict[str, Measurement] = obj.getMeasurements()
            measurement_name: str
            for measurement_name in curr_measurements.keys():
                if measurement_name not in measurement_names:
                    measurement_names.append(str(measurement_name))
            
        self._objs.showMeasurements(measurement_names)
    
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
    def get(self, key: int) -> ObjWrapper | None:
        obj: Obj | None = self._objs.get(key)
        return None if obj is None else wrapObj(obj)
    
    @JOverride
    def size(self) -> int:
        return self._objs.size()
    
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
    def put(self, key: int, value: ObjWrapper) -> ObjWrapper | None:
        prevObj: Obj | None = self._objs.get(key)
        prevObjWrapper: ObjWrapper | None = None
        
        if prevObj is not None:
            prevObjWrapper = wrapObj(prevObj)
                        
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
    def values(self): # To do
        return ObjsWrapperCollection(self)
    
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
    def putIfAbsent(self, key: int, value: ObjWrapper) -> ObjWrapper | None:
        obj: Obj | None = self._objs.putIfAbsent(key, value.getPythonObj())
        
        obj_wrapper: ObjWrapper| None = None
        if obj is not None:
            obj_wrapper = wrapObj(obj)
        
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
        
        output: ObjsWrapper = ObjsWrapper(name, width, height, n_slices, dpp_xy, dpp_z, spatial_units, n_frames, frame_interval, temporal_unit)

        return output
                
    @JOverride
    def duplicate(self) -> ObjsFactoryWrapper:
        return ObjsFactoryWrapper()
        
def wrapObjs(objs: Objs) -> ObjsWrapper:
    try:
        return _wrapper_cache[objs]
    except:        
        objs_wrapper = ObjsWrapper("", 0, 0, 0, 0.0, 0.0, "", 0, 0.0, None)
        objs_wrapper.setPythonObjs(objs)
        _wrapper_cache[objs]  = objs_wrapper
    
        return objs_wrapper
