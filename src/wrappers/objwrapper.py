from __future__ import annotations
from jpype import JImplements, JOverride
from scyjava import jimport
from typing import TYPE_CHECKING

from src.objects.obj import Obj
from src.wrappers.volumewrapper import VolumeWrapper

if TYPE_CHECKING:
    from src.wrappers.coordinatesetwrapper import CoordinateSetFactoryWrapper
    from src.wrappers.objswrapper import ObjsWrapper


JObj = jimport('io.github.mianalysis.mia.object.coordinates.ObjI')
JObjAdaptor = jimport('io.github.mianalysis.mia.python.ObjAdaptor')
JVolumeAdaptor = jimport('io.github.mianalysis.mia.python.VolumeAdaptor')

@JImplements('io.github.mianalysis.mia.object.coordinates.ObjI')
class ObjWrapper(VolumeWrapper):
    
    def __init__(self, obj_collection: ObjsWrapper, coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper, ID: int, spat_cal=None): # To do
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
        return self._j_obj_collection

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
        return super().getCoordinateSetFactory()

    @JOverride
    def getSurface(self, ignoreEdgesXY, ignoreEdgesZ):
        return self._obj.getSurface(ignoreEdgesXY, ignoreEdgesZ)

    @JOverride
    def hasCalculatedSurface(self):
        return self._obj.hasCalculatedSurface()

    @JOverride
    def getProjected(self):
        return self._obj.getProjected()

    @JOverride
    def hasCalculatedProjection(self):
        return self._obj.hasCalculatedProjection()

    @JOverride
    def getMeanCentroid(self, pixelDistances, matchXY):
        return self._obj.getMeanCentroid(pixelDistances, matchXY)

    @JOverride
    def hasCalculatedCentroid(self):
        return self._obj.hasCalculatedCentroid()

    @JOverride
    def clearAllCoordinates(self):
        self._obj.clearAllCoordinates()

    @JOverride
    def clearSurface(self):
        self._obj.clearSurface()

    @JOverride
    def clearPoints(self):
        self._obj.clearPoints()

    @JOverride
    def clearProjected(self):
        self._obj.clearProjected()

    @JOverride
    def clearCentroid(self):
        self._obj.clearCentroid()

    @JOverride
    def hashCode(self):
        self._obj.hashCode()

    @JOverride
    def equals(self, obj):
        self._obj.equals(obj)

    @JOverride
    def getSpatialCalibration(self):
        return self._obj.getSpatialCalibration()

    @JOverride
    def setSpatialCalibration(self, spat_cal):
        self._obj.setSpatialCalibration(spat_cal)

    @JOverride
    def getCoordinateSet(self):
        return self._obj.getCoordinateSet()

    @JOverride
    def setCoordinateSet(self, coordinate_set):
        self._obj.setCoordinateSet(coordinate_set)

    @JOverride
    def createNewVolume(self, factory, spat_cal):
        return self._obj.createNewVolume(factory, spat_cal)

    @JOverride
    def getCalibratedIterator(self, pixelDistances, matchXY):
        return self._obj.getCalibratedIterator(pixelDistances, matchXY)
    
    
    # Obj default methods
    
    def addToImage(self, image, hue):
        self._obj.addToImage(image, hue)
        
        
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
    def getName(self):
        return "Python object factory"
    
    @JOverride
    def createObj(self, obj_collection, factory, ID, spat_cal=None):
        return ObjWrapper(obj_collection, factory, ID, spat_cal)

    @JOverride
    def duplicate(self):
        return ObjFactoryWrapper()