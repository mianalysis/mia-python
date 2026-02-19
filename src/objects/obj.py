from __future__ import annotations
from typing import Dict, List, TYPE_CHECKING
from xarray import DataArray

from src.objects.measurement import Measurement
from src.objects.units import replaceSpatialUnits, replaceTemporalUnits
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
        
        self._measurements: Dict[str, Measurement] = {}
        # To do: Create ObjMetadata class
        
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
        return self._parents

    def setAllParents(self, parents: Dict[str, Obj]):
        raise Exception('Obj: Implement setAllParents')

    def getAllChildren(self) -> Dict[str, Objs]:
        return self._children

    def setAllChildren(self, children: Dict[str, Objs]):
        raise Exception('Obj: Implement setAllChildren')

    def getAllPartners(self) -> Dict[str, Objs]:
        return self._partners

    def setAllPartners(self, partners: Dict[str, Objs]):
        raise Exception('Obj: Implement setAllPartners')

    def removeRelationships(self): # No return
        # Removing itself as a child from its parent
        if self._parents is not None:
            parent: Obj
            for parent in self._parents.values():
                if parent is not None:
                    parent.removeChild(self)
        
        # Removing itself as a parent from any children
        if self._children is not None:
            child_set: Objs
            for child_set in self._children.values():
                child: Obj
                for child in child_set.values():
                    if child.getParent(self.getName()) == self:
                        child.removeParent(self.getName())

        # Removing itself as a partner from any partners
        if self._partners is not None:
            partner_set: Objs
            for partner_set in self._partners.values():
                partner: Obj
                for partner in partner_set.values():
                    partner.removePartner(self)

        # Clearing children and parents
        children = {}
        parents = {}
        partners = {}

    def getMeasurements(self) -> Dict[str, Measurement]:
        return self._measurements

    def setMeasurements(self, measurements: Dict[str, Measurement]):
        self._measurements = measurements
    
    def getMetadata(self): # To do
        raise Exception('Obj: Implement getMetadata')

    def setMetadata(self, metadata): # To do
        raise Exception('Obj: Implement setMetadata')

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
            
    def getParents(self, use_full_hierarchy: bool) -> Dict[str, Obj]:
        if not use_full_hierarchy:
            return self.getAllParents()

        # Adding each parent and then the parent of that
        parent_hierarchy: Dict[str, Obj] = {}
        parent: Obj
        for parent in self.getAllParents().values():
            parent_hierarchy[parent.getName()] = parent

        # Going through each parent, adding the parents of that.
        for parent in self.getAllParents().values():
            if parent is None:
                continue
            
            current_parents: Dict[str, Obj] = parent.getParents(True)
            if current_parents is None:
                continue
            
            current_parent: Obj
            for current_parent in current_parents.values():
                parent_hierarchy[current_parent.getName()] = current_parent
    
        return parent_hierarchy

    def getParent(self, name: str) -> Obj:
        # Split name down by " // " tokenizer
        elements: List[str] = name.split(" // ")
        
        # Getting the first parent
        parent: Obj = self._parents[elements[0]]
        
        if len(elements) == 1:
            return parent
        
        new_name: str = ""
        for i in range(1,len(elements)):
            new_name = new_name + elements[i]
            if i != len(elements)-1:
                new_name = new_name + " // "
                
        if parent is None:
            return None
        
        return parent.getParent(new_name)

    def addParent(self, parent: Obj):
        if parent:
            self._parents[parent.getName()] = parent

    def removeParent(self, name: str):
        self._parents.pop(name)

    def getChildren(self, name: str) -> Objs:
        raise Exception('Obj: Implement getChildren')

    def addChildren(self, child_set: Objs):
        raise Exception('Obj: Implement addChildren')

    def removeChildren(self, name: str):
        raise Exception('Obj: Implement removeChildren')

    def addChild(self, child: Obj):
        if child is None:
            return
        
        child_name: str = child.getName()
        if child_name not in self._children:
            self._children[child_name] = child.getObjectCollection().createNewObjsFromThis(child_name)
            
        self._children[child_name].add(child)

    def removeChild(self, child: Obj):
        raise Exception('Obj: Implement removeChild')

    def getPartners(self, name: str) -> Objs:
        raise Exception('Obj: Implement getPartners')

    def addPartners(self, partner_set: Objs):
        raise Exception('Obj: Implement addPartners')

    def addPartner(self, partner: Obj):
        raise Exception('Obj: Implement addPartner')

    def removePartner(self, partner: Obj):
        raise Exception('Obj: Implement removePartner')

    def removePartners(self, name: str):
        raise Exception('Obj: Implement removePartners')

    def getPreviousPartners(self, name: str) -> Objs:
        raise Exception('Obj: Implement getPreviousPartners')

    def getSimultaneousPartners(self, name: str) -> Objs:
        raise Exception('Obj: Implement getSimultaneousPartners')

    def getNextPartners(self, name: str) -> Objs:
        raise Exception('Obj: Implement getNextPartners')

    def addMetadataItem(self, metadata_item): # To do
        raise Exception('Obj: Implement addMetadataItem')

    def getMetadataItem(self, name: str): # To do
        raise Exception('Obj: Implement getMetadataItem')

    def removeMetadataItem(self, name: str):
        raise Exception('Obj: Implement removeMetadataItem')

    def addMeasurement(self, measurement: Measurement):
        self._measurements[measurement.getName()] = measurement

    def getMeasurement(self, name: str) -> Measurement | None:
        name = replaceSpatialUnits(name)
        name = replaceTemporalUnits(name)
        
        return self._measurements.get(name)

    def removeMeasurement(self, name: str):
        raise Exception('Obj: Implement removeMeasurement')

    def getAsImage(self, imageName: str, single_timepoint: bool) -> Image:
        raise Exception('Obj: Implement getAsImage')
    
    def getCentroidAsImage(self, imageName: str, single_timepoint: bool) -> Image:
        raise Exception('Obj: Implement getCentroidAsImage')

    def addToImage(self, image: Image, hue: float): # No return
        # np_img: DataArray = image.getRawImage()
        
        point: Point | None
        for point in self.getCoordinateSet():
            if point is None:
                continue
            
            image.putPixel(hue, point[0], point[1], z=point[2], t=self.getT())
            # x: int = point[0]
            # y: int = point[1]
            # z: int = point[2]
            
            # np_img[y,x,0] = hue

    def addCentroidToImage(self, image: Image, hue: float):
        raise Exception('Obj: Implement addCentroidToImage')

    def removeOutOfBoundsCoords(self):
        raise Exception('Obj: Implement removeOutOfBoundsCoords')

    def getImgPlusCoordinateIterator(self): # To do
        raise Exception('Obj: Implement getImgPlusCoordinateIterator')

        
    # Volume default methods
    
    def addCoord(self, x: int, y: int, z: int): # No return
        super().addCoord(x,y,z)
