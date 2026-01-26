# Note: Can this extend Dict (e.g. class Objs(Dict[int, Obj])) and have the objswrapper just convert 
# the methods?

from __future__ import annotations
from typing import Dict, List, Tuple
from typing import TYPE_CHECKING

from src.objects.image import Image
from src.utilities.colourfactory import getIDHues

import numpy as np

if TYPE_CHECKING:
    from src.objects.coordinateset import CoordinateSetFactory
    
    from src.objects.obj import Obj
    from src.types.types import Point

class Objs():
    def __init__(self, name: str, width: int, height: int, n_slices: int, dpp_xy: float, dpp_z: float, spatial_units: str, n_frames: int, frame_interval: float, temporal_unit): # To do
        self._objs: Dict[int, Obj] = {}
        self._max_ID: int = 0
        
        self._name: str = name
        self._width: int = width
        self._height: int = height
        self._n_slices: int = n_slices
        self._dpp_xy: float = dpp_xy
        self._dpp_z: float = dpp_z
        self._spatial_units: str = spatial_units
        
        self._n_frames: int = n_frames
        self._frame_interval: float = frame_interval
        self._temporal_unit = temporal_unit
                
    def createAndAddNewObject(self, factory: CoordinateSetFactory) -> Obj:
        raise Exception('Objs: Implement createAndAddNewObject')
    
    def createAndAddNewObjectWithID(self, factory: CoordinateSetFactory, ID: int) -> Obj:
        raise Exception('Objs: Implement createAndAddNewObjectWithID')
        
    def getName(self) -> str:
        return self._name
    
    def add(self, object: Obj): # No return
        raise Exception('Objs: Implement add')
        
    def getAndIncrementID(self) -> int:
        self._max_ID = self._max_ID + 1
        return self._max_ID
    
    def resetCollection(self): # No return
        raise Exception('Objs: Implement resetCollection')
    
    def recalculateMaxID(self): # No return
        raise Exception('Objs: Implement recalculateMaxID')
    
    def getAsSingleObject(self) -> Obj:
        raise Exception('Objs: Implement getAsSingleObject')
    
    def getObjectsInFrame(self, output_objects_name: str, frame: int) -> Objs:
        raise Exception('Objs: Implement getObjectsInFrame')
    
    def getNFrames(self) -> int:
        return self._n_frames
    
    def setNFrames(self, n_frames: int): # No return
        self._n_frames = n_frames
    
    def getFrameInterval(self) -> float:
        return self._frame_interval
    
    def setFrameInterval(self, frame_interval: float): # No return
        self._frame_interval = frame_interval
    
    def getTemporalUnit(self): # To do
        return self._temporal_unit
    
    def setTemporalUnit(self, temporal_unit): # To do
        self._temporal_unit = temporal_unit
        
    def duplicate(self, new_objects_name: str, duplicate_relationships: bool, duplicate_measurement: bool,
                  duplicate_metadata: bool, add_original_duplicate_relationship: bool) -> Objs:
        raise Exception('Objs: Implement duplicate')


    # Default methods

    def getWidth(self) -> int:
        return self._width
    
    def setWidth(self, width: int): # No return
        self._width = width
    
    def getHeight(self) -> int:
        return self._height
    
    def setHeight(self, height: int): # No return
        self._height = height
    
    def getNSlices(self) -> int:
        return self._n_slices

    def setNSlices(self, n_slices: int): # No return
        self._n_slices = n_slices
    
    def getDppXY(self) -> float:
        return self._dpp_xy
    
    def setDppXY(self, dpp_xy: float): # No return
        self._dpp_xy = dpp_xy

    def getDppZ(self) -> float:
        return self._dpp_z

    def setDppZ(self, dpp_z: float): # No return
        self._dpp_z = dpp_z
    
    def getSpatialUnits(self) -> str:
        return self._spatial_units

    def setSpatialUnits(self, spatial_units: str): # No return
        self._spatial_units = spatial_units

    def getFirst(self) -> Obj:
        raise Exception('Objs: Implement getFirst')
    
    def getSpatialExtents(self) -> List[List[int]]:
        raise Exception('Objs: Implement getSpatialExtents')
    
    def getSpatialLimits(self) -> List[List[int]]:
        raise Exception('Objs: Implement getSpatialLimits')
    
    def getTemporalLimits(self) -> List[int]:
        raise Exception('Objs: Implement getTemporalLimits')
    
    def getLargestID(self) -> int:
        raise Exception('Objs: Implement getLargestID')
        
    def convertToImage(self, output_name: str, hues: Dict[int, float], bit_depth: int, nanBackground: bool, verbose: bool) -> Image:
        im: Image = self.createImage(output_name, bit_depth)
        
        if nanBackground:
            np_img = im.getRawImage()
            np_img.fill(np.nan)
                   
        object: Obj
        for object in self.values(): 
            object.addToImage(im, hues.get(object.getID(),0.0))
            
        print('Objs: Add applySpatioTemporalCalibration to created image (convertToImage)')
        
        return im
    
    def convertToImageRandomColours(self) -> Image:
        raise Exception('Objs: Implement convertToImageRandomColours')
        
    def convertToImageBinary(self, name: str) -> Image:
        raise Exception('Objs: Implement convertToImageBinary')
    
    def convertToImageIDColours(self) -> Image:
        hues: Dict[int, float] = getIDHues(self, False)
        return self.convertToImage(self.getName(), hues, 32, False, False)
    
    def convertCentroidsToImage(self, output_name: str, hues: Dict[int, float], bit_bepth: int, nan_background: bool) -> Image:
        raise Exception('Objs: Implement convertCentroidsToImage')
    
    def applyCalibration(self, image: Image): # No return
        raise Exception('Objs: Implement applyCalibration')
    
    def applyCalibrationFromImagePlus(self, ipl): # To do
        raise Exception('Objs: Implement applyCalibrationFromImagePlus')
    
    def createImage(self, output_name: str, bit_depth: int) -> Image:
        dtype = None
        if bit_depth == 8:
            dtype = np.uint8
        elif bit_depth == 16:
            dtype = np.uint16
        elif bit_depth == 32:
            dtype = np.float32
        else:
            raise Exception('Objs: Unsupported bit depth')
        
        print("IMPORTANT: Find out dimension order for np_img in Image class, but for now assuming XYCZT")
        np_img = np.zeros((self._width, self._height, 1, self._n_slices, self._n_frames), dtype=dtype)
        
        return Image(output_name, np_img)
    
    def setNaNBackground(self, ipl): # To do
        raise Exception('Objs: Implement setNaNBackground')
    
    def getByEqualsIgnoreNameAndID(self, reference_obj: Obj) -> Obj:
        raise Exception('Objs: Implement getByEqualsIgnoreNameAndID')
    
    def showMeasurements(self, module, modules): # To do
        raise Exception('Objs: Implement showMeasurements')
    
    def showAllMeasurements(self): # No return
        raise Exception('Objs: Implement showAllMeasurements')
    
    def showMetadata(self, module, modules): # To do
        raise Exception('Objs: Implement showMetadata')
    
    def showAllMetadata(self): # No return
        raise Exception('Objs: Implement showAllMetadata')
    
    def removeParents(self, parent_objects_name: str): # No return
        raise Exception('Objs: Implement removeParents')
    
    def removeChildren(self, child_objects_name: str): # No return
        raise Exception('Objs: Implement removeChildren')
    
    def removePartners(self, partner_objects_name: str): # No return
        raise Exception('Objs: Implement removePartners')
    
    def containsPoint(self, point: Point) -> bool:
        raise Exception('Objs: Implement containsPoint')
    
    def containsCoord(self, x: int, y: int, z: int) -> bool:
        raise Exception('Objs: Implement containsCoord')
    
    def getLargestObject(self, t: int) -> Obj:
        raise Exception('Objs: Implement getLargestObject')
    
    def getSmallestObject(self, t: int) -> Obj:
        raise Exception('Objs: Implement getSmallestObject')


    # From Map

    def size(self) -> int:
        return len(self._objs)
    
    def isEmpty(self) -> bool:
        raise Exception('MapWrapper: Implement isEmpty')
    
    def containsKey(self, key: int) -> bool:
        raise Exception('MapWrapper: Implement containsKey')
    
    def containsValue(self, value: Obj) -> bool:
        raise Exception('MapWrapper: Implement containsValue')
        
    def get(self, key: int) -> Obj | None:
        return self._objs.get(key)
    
    def put(self, key: int, value: Obj) -> Obj | None:
        prevObj: Obj | None = self._objs.get(key)
        self._objs[key] = value
        
        return prevObj
    
    def remove(self, key: int) -> Obj:
        raise Exception('MapWrapper: Implement remove')
    
    def putAll(self, m: Dict[int, Obj]): # No return
        raise Exception('MapWrapper: Implement putAll')
    
    def clear(self): # No return
        raise Exception('MapWrapper: Implement clear')
    
    def keySet(self) -> List[int]:
        raise Exception('MapWrapper: Implement keySet')
    
    def values(self) -> List[Obj]:
        return [obj for obj in self._objs.values()]
    
    def entrySet(self) -> List[Tuple[int,Obj]]:
        raise Exception('MapWrapper: Implement values')
        # entry_set: List[Tuple[int,Obj]] = []
        # for key, value in self._objs.items():
        #     entry_set.append((key, value))
            
        # return entry_set

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
    
    def putIfAbsent(self, key: int, value: Obj) -> Obj|None:
        if self._objs.get(key) is None:
            self._objs[key] = value
            return None
        else:
            return self._objs[key]
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
