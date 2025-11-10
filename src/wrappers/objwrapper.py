from __future__ import annotations
from jpype import JImplements, JOverride # type: ignore
from scyjava import jimport # type: ignore
from typing import TYPE_CHECKING

from src.objects.obj import Obj
from src.objects.volume import Volume
from src.wrappers.volumewrapper import VolumeWrapper

if TYPE_CHECKING:
    from src.objects.coordinateset import CoordinateSet
    from src.wrappers.coordinatesetwrapper import CoordinateSetWrapper, CoordinateSetFactoryWrapper
    from src.wrappers.imagewrapper import ImageWrapper
    from src.wrappers.objswrapper import ObjsWrapper
    from src.types.JPointType import JPointType

JObj = jimport('io.github.mianalysis.mia.object.coordinates.ObjI') # type: ignore
JObjAdaptor = jimport('io.github.mianalysis.mia.python.ObjAdaptor') # type: ignore
JVolumeAdaptor = jimport('io.github.mianalysis.mia.python.VolumeAdaptor') # type: ignore

@JImplements('io.github.mianalysis.mia.object.coordinates.ObjI')
class ObjWrapper(VolumeWrapper):
    
    def __init__(self, obj_collection: ObjsWrapper | None, coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper, ID: int, spat_cal=None): # To do
        if obj_collection is not None:
            self._obj: Obj = Obj(obj_collection.getPythonObjs(), coordinate_set_factory_wrapper.getPythonCoordinateSetFactory(), ID, spat_cal)

    def getPythonObj(self) -> Obj:
        return self._obj

    def setPythonObj(self, obj: Obj):
        self._obj = obj
            
    @JOverride
    def getFactory(self) -> ObjFactoryWrapper:
        return ObjFactoryWrapper()
    
    @JOverride
    def getObjectCollection(self) -> ObjsWrapper:
        objs_wrapper: ObjsWrapper = ObjsWrapper()
        objs_wrapper.setPythonObjs(self._obj.getObjectCollection())

        return objs_wrapper

    @JOverride
    def setObjectCollection(self, obj_collection: ObjsWrapper): # No return
        self._obj.setObjectCollection(obj_collection.getPythonObjs())

    @JOverride
    def getName(self) -> str:
        return self._obj.getName()

    @JOverride
    def getID(self) -> int:
        return self._obj.getID()

    @JOverride
    def setID(self, ID: int) -> ObjWrapper:
        self._obj.setID(ID)
        return self

    @JOverride
    def getT(self) -> int:
        return self._obj.getT()

    @JOverride
    def setT(self, T: int) -> ObjWrapper:
        self._obj.setT(T)
        return self

    @JOverride
    def getAllParents(self): # To do
        raise Exception('ObjWrapper: Implement getAllParents')

    @JOverride
    def setAllParents(self, parents): # To do
        raise Exception('ObjWrapper: Implement setAllParents')

    @JOverride
    def getAllChildren(self): # To do
        raise Exception('ObjWrapper: Implement getAllChildren')

    @JOverride
    def setAllChildren(self, children): # To do
        raise Exception('ObjWrapper: Implement setAllChildren')

    @JOverride
    def getAllPartners(self): # To do
        raise Exception('ObjWrapper: Implement getAllPartners')

    @JOverride
    def setAllPartners(self, partners): # To do
        raise Exception('ObjWrapper: Implement setAllPartners')

    @JOverride
    def removeRelationships(self): # To do
        raise Exception('ObjWrapper: Implement removeRelationships')

    @JOverride
    def getMeasurements(self): # To do
        raise Exception('ObjWrapper: Implement getMeasurements')

    @JOverride
    def setMeasurements(self, measurements): # To do
        raise Exception('ObjWrapper: Implement setMeasurements')

    @JOverride
    def getMetadata(self): # To do
        raise Exception('ObjWrapper: Implement getMetadata')

    @JOverride
    def setMetadata(self, metadata): # To do
        raise Exception('ObjWrapper: Implement setMetadata')

    @JOverride
    def getRoi(self, z_slice: int): # To do
        raise Exception('ObjWrapper: Implement getRoi')

    @JOverride
    def getRois(self): # To do
        raise Exception('ObjWrapper: Implement getRois')

    @JOverride
    def clearROIs(self): # No return
        raise Exception('ObjWrapper: Implement clearROIs')

    @JOverride
    def duplicate(self, new_collection: ObjsWrapper, duplicate_relationships: bool, duplicate_measurements: bool, duplicate_metadata: bool) -> ObjWrapper:
        raise Exception('ObjWrapper: Implement duplicate')

    @JOverride
    def equalsIgnoreNameAndID(self, obj: ObjWrapper) -> bool:
        raise Exception('ObjWrapper: Implement equalsIgnoreNameAndID')

    @JOverride
    def toString(self) -> str:
        return self._obj.toString()


    ## Inherited from VolumeWrapper

    @JOverride
    def getCoordinateSetFactory(self) -> CoordinateSetFactoryWrapper:
        coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper = CoordinateSetFactoryWrapper()
        coordinate_set_factory_wrapper.setPythonCoordinateSetFactory(self._obj.getCoordinateSetFactory())
        
        return coordinate_set_factory_wrapper

    @JOverride
    def getSurface(self, ignoreEdgesXY: bool, ignoreEdgesZ: bool) -> VolumeWrapper:
        volume: Volume = self._obj.getSurface(ignoreEdgesXY, ignoreEdgesZ)
        return VolumeWrapper.wrapVolume(volume, self._obj.getSpatialCalibration())

    @JOverride
    def hasCalculatedSurface(self) -> bool:
        return self._obj.hasCalculatedSurface()

    @JOverride
    def getProjected(self) -> VolumeWrapper:
        volume: Volume = self._obj.getProjected()
        return VolumeWrapper.wrapVolume(volume, self._obj.getSpatialCalibration())

    @JOverride
    def hasCalculatedProjection(self) -> bool:
        return self._obj.hasCalculatedProjection()

    @JOverride
    def getMeanCentroid(self, pixelDistances: bool, matchXY: bool) -> JPointType[float]:
        raise Exception('ObjWrapper: Implement getMeanCentroid')

    @JOverride
    def hasCalculatedCentroid(self) -> bool:
        return self._obj.hasCalculatedCentroid()

    @JOverride
    def clearAllCoordinates(self): # No return
        self._obj.clearAllCoordinates()

    @JOverride
    def clearSurface(self): # No return
        self._obj.clearSurface()

    @JOverride
    def clearPoints(self): # No return
        self._obj.clearPoints()

    @JOverride
    def clearProjected(self): # No return
        self._obj.clearProjected()

    @JOverride
    def clearCentroid(self): # No return
        self._obj.clearCentroid()

    @JOverride
    def hashCode(self) -> int:
        raise Exception('ObjWrapper: Implement hashCode')

    @JOverride
    def equals(self, obj: ObjWrapper) -> bool:
        raise Exception('ObjWrapper: Implement equals')

    @JOverride
    def getSpatialCalibration(self): # To do
        raise Exception('ObjWrapper: Implement getSpatialCalibration')

    @JOverride
    def setSpatialCalibration(self, spat_cal): # To do
        raise Exception('ObjWrapper: Implement setSpatialCalibration')

    @JOverride
    def getCoordinateSet(self) -> CoordinateSetWrapper:
        coordinate_set: CoordinateSet = self._obj.getCoordinateSet()
        coordinate_set_wrapper: CoordinateSetWrapper = CoordinateSetWrapper()
        coordinate_set_wrapper.setPythonCoordinateSet(coordinate_set)
        
        return coordinate_set_wrapper

    @JOverride
    def setCoordinateSet(self, coordinate_set: CoordinateSetWrapper):
        raise Exception('ObjWrapper: Implement setCoordinateSet')

    @JOverride
    def createNewVolume(self, factory, spat_cal): # To do
        return self._obj.createNewVolume(factory, spat_cal)

    @JOverride
    def getCalibratedIterator(self, pixelDistances: bool, matchXY: bool): # To do
        raise Exception('ObjWrapper: Implement getCalibratedIterator')
    
    
    # Obj default methods
    
    def addToImage(self, image: ImageWrapper, hue: float):
        raise Exception('ObjWrapper: Implement addToImage')
        
        
    # Volume default methods
    
    def addCoord(self, x: int, y: int, z: int): # No return
        self._obj.addCoord(x,y,z)
        
    def finalise(self): # No return
        self._obj.finalise()

    def finaliseSlice(self, z: int): # No return
        self._obj.finaliseSlice(z)

    def getWidth(self) -> int:
        return self._obj.getWidth()


@JImplements('io.github.mianalysis.mia.object.coordinates.ObjFactoryI')
class ObjFactoryWrapper:
    
    @JOverride
    def getName(self) -> str:
        return "Python object factory"
    
    @JOverride
    def createObj(self, obj_collection: ObjsWrapper, factory: CoordinateSetFactoryWrapper, ID: int, spat_cal=None) -> ObjWrapper: # To do
        return ObjWrapper(obj_collection, factory, ID, spat_cal)

    @JOverride
    def duplicate(self) -> ObjFactoryWrapper:
        return ObjFactoryWrapper()
    