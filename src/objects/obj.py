from __future__ import annotations
from typing import Dict
from typing import TYPE_CHECKING

from src.objects.volume import Volume

import numpy as np

if TYPE_CHECKING:
    from src.objects.objs import Objs
    from src.objects.coordinateset import CoordinateSetFactory
    from src.objects.image import Image  
    from src.types.types import Point


class Obj(Volume):
    def __init__(self, coordinate_set_factory: CoordinateSetFactory, obj_collection: Objs, ID: int):
        super().__init__(coordinate_set_factory, obj_collection.getWidth(),obj_collection.getHeight(), 
                         obj_collection.getNSlices(), obj_collection.getDppXY(), obj_collection.getDppZ(), 
                         obj_collection.getSpatialUnits())
        
        self._ID: int = ID
        self._obj_collection: Objs = obj_collection
        
        self._n_frames: int = obj_collection.getNFrames()    
        self._frame_interval: float = obj_collection.getFrameInterval()
        self._temporal_unit = obj_collection.getTemporalUnit()
        
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
        self._ID = ID # type: ignore
        
        return self

    def getT(self) -> int:
        return self._T

    def setT(self, T: int) -> Obj:
        self._T = T # type: ignore
        
        return self

    def getAllParents(self) -> Dict[str, Obj]:
        raise Exception('Obj: Implement getAllParents')

    def setAllParents(self, parents: Dict[str, Obj]):
        raise Exception('Obj: Implement setAllParents')

    def getAllChildren(self) -> Dict[str, Objs]:
        raise Exception('Obj: Implement getAllChildren')

    def setAllChildren(self, children: Dict[str, Objs]):
        raise Exception('Obj: Implement setAllChildren')

    def getAllPartners(self) -> Dict[str, Objs]:
        raise Exception('Obj: Implement getAllPartners')

    def setAllPartners(self, partners: Dict[str, Objs]):
        raise Exception('Obj: Implement setAllPartners')

    def removeRelationships(self): # No return
        raise Exception('Obj: Implement removeRelationships')

    def getMeasurements(self): # To do
        raise Exception('Obj: Implement getMeasurements')

    def setMeasurements(self, measurements): # To do
        raise Exception('Obj: Implement setMeasurements')

    def getMetadata(self): # To do
        raise Exception('Obj: Implement getMetadata')

    def setMetadata(self, metadata): # To do
        raise Exception('Obj: Implement setMetadata')

    def getRoi(self, z_slice: int): # To do
        raise Exception('Obj: Implement getRoi')

    def getRois(self): # To do
        raise Exception('Obj: Implement getRois')

    def clearROIs(self): # No return
        raise Exception('Obj: Implement clearROIs')

    def duplicate(self, new_collection: Objs, duplicate_relationships: bool, duplicate_measurements: bool, duplicate_metadata: bool) -> Obj:
        raise Exception('Obj: Implement duplicate')

    def equalsIgnoreNameAndID(self, obj: Obj) -> bool:
        raise Exception('Obj: Implement equalsIgnoreNameAndID')

    def toString(self) -> str:
        return f"Object \"{self.getName()}\", ID = {self.getID()}, frame = {self.getT()}"


    # From SpatioTemporallyCalibrated

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
    
    def applySpatioTemporalCalibrationToImage(self, ipl): # To do
        raise Exception('Obj: Implement applySpatioTemporalCalibrationToImage')
    
    def setSpatioTemporalCalibrationFromExample(self, example): # To do
        # This should just use Python objects
        raise Exception('Obj: Implement setSpatioTemporalCalibrationFromExample')


    # Obj default methods
    
    def addToImage(self, image: Image, hue: float): # No return
        np_img: np.ndarray = image.getRawImage()
        
        point: Point | None
        for point in self.getCoordinateSet():
            if point is None:
                continue
            
            x: int = point[0]
            y: int = point[1]
            z: int = point[2]
            
            np_img[y,x,0] = hue
        
        if self.getNSlices() > 1 or self.getNFrames() > 1:
            raise Exception('Obj: Add multidimensional objects to addToImage')
        
    # Volume default methods
    
    def addCoord(self, x: int, y: int, z: int): # No return
        super().addCoord(x,y,z)
