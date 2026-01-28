from __future__ import annotations
from jpype import JImplements, JOverride # type: ignore
from scyjava import jimport # type: ignore
from typing import Dict
from typing import TYPE_CHECKING, Self

from src.objects.measurement import Measurement
from src.objects.obj import Obj
from src.objects.volume import Volume
from src.wrappers.volumewrapper import VolumeFactoryWrapper, VolumeWrapper, wrapVolume
from src.types.JSpatioTemporallyCalibrated import JSpatioTemporallyCalibrated
from src.wrappers.measurementwrapper import MeasurementWrapper, wrapMeasurement

import src.wrappers.objswrapper as osw

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
class ObjWrapper:
    
    def __init__(self, coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper | None, obj_collection: ObjsWrapper | None, ID: int):
        if coordinate_set_factory_wrapper is not None and obj_collection is not None:
            self._obj: Obj = Obj(coordinate_set_factory_wrapper.getPythonCoordinateSetFactory(), obj_collection.getPythonObjs(), ID)

    def getPythonObj(self) -> Obj:
        return self._obj

    def setPythonObj(self, obj: Obj):
        self._obj = obj
            
    @JOverride
    def getFactory(self) -> VolumeFactoryWrapper:
        return VolumeFactoryWrapper()
    
    @JOverride
    def getObjectCollection(self) -> ObjsWrapper:
        objs_wrapper: ObjsWrapper = osw.wrapObjs(self._obj.getObjectCollection())

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
    def setID(self, ID: int) -> Self:
        self._obj.setID(ID)
        return self

    @JOverride
    def getT(self) -> int:
        return self._obj.getT()

    @JOverride
    def setT(self, T: int) -> Self:
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
    def getMeasurements(self) -> Dict[str, MeasurementWrapper]:
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
    def getRoi(self, slice: int): # To do
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
    def createNewVolume(self, coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper, example_volume: VolumeWrapper) -> VolumeWrapper:
        volume: Volume = self._obj.createNewVolume(coordinate_set_factory_wrapper.getPythonCoordinateSetFactory(), example_volume.getPythonVolume())
        return wrapVolume(volume)

    @JOverride
    def getCoordinateSetFactory(self) -> CoordinateSetFactoryWrapper:
        coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper = CoordinateSetFactoryWrapper()
        coordinate_set_factory_wrapper.setPythonCoordinateSetFactory(self._obj.getCoordinateSetFactory())
        
        return coordinate_set_factory_wrapper

    @JOverride
    def getSurface(self, ignore_edges_xy: bool, ignore_edges_z: bool) -> VolumeWrapper:
        volume: Volume = self._obj.getSurface(ignore_edges_xy, ignore_edges_z)
        return wrapVolume(volume)

    @JOverride
    def hasCalculatedSurface(self) -> bool:
        return self._obj.hasCalculatedSurface()

    @JOverride
    def getProjected(self) -> VolumeWrapper:
        volume: Volume = self._obj.getProjected()
        return wrapVolume(volume)

    @JOverride
    def hasCalculatedProjection(self) -> bool:
        return self._obj.hasCalculatedProjection()

    @JOverride
    def getMeanCentroid(self, pixel_distances: bool, match_xy: bool) -> JPointType[float]:
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
    def getCoordinateSet(self) -> CoordinateSetWrapper:
        coordinate_set: CoordinateSet = self._obj.getCoordinateSet()
        coordinate_set_wrapper: CoordinateSetWrapper = CoordinateSetWrapper()
        coordinate_set_wrapper.setPythonCoordinateSet(coordinate_set)
        
        return coordinate_set_wrapper

    @JOverride
    def setCoordinateSet(self, coordinate_set: CoordinateSetWrapper):
        raise Exception('ObjWrapper: Implement setCoordinateSet')

    @JOverride
    def getCalibratedIterator(self, pixel_distances: bool, match_xy: bool): # To do
        raise Exception('ObjWrapper: Implement getCalibratedIterator')
    

    # From SpatiallyCalibrated

    @JOverride
    def getWidth(self) -> int:
        return self._obj.getWidth()

    @JOverride
    def setWidth(self, width: int): # No return
        self._obj.setWidth(width)

    @JOverride
    def getHeight(self) -> int:
        return self._obj.getHeight()

    @JOverride
    def setHeight(self, height: int): # No return
        self._obj.setHeight(height)
        
    @JOverride
    def getNSlices(self) -> int:
        return self._obj.getNSlices()

    @JOverride
    def setNSlices(self, n_slices: int): # No return
        self._obj.setNSlices(n_slices)
        
    @JOverride
    def getDppXY(self) -> float:
        return self._obj.getDppXY()

    @JOverride
    def setDppXY(self, dpp_xy: float): # No return
        self._obj.setDppXY(dpp_xy)

    @JOverride
    def getDppZ(self) -> float:
        return self._obj.getDppZ()

    @JOverride
    def setDppZ(self, dpp_z: float): # No return
        self._obj.setDppZ(dpp_z)

    @JOverride
    def getSpatialUnits(self) -> str:
        return self._obj.getSpatialUnits()

    @JOverride
    def setSpatialUnits(self, spatial_units: str): # No return
        self._obj.setSpatialUnits(spatial_units)


    # From SpatioTemporallyCalibrated

    @JOverride
    def getNFrames(self) -> int:
        return self._obj.getNFrames()

    @JOverride
    def setNFrames(self, n_frames: int): # No return
        self._obj.setNFrames(n_frames)

    @JOverride
    def getFrameInterval(self) -> float:
        return self._obj.getFrameInterval()

    @JOverride
    def setFrameInterval(self, frame_interval: float): # No return
        self._obj.setFrameInterval(frame_interval)  

    @JOverride
    def getTemporalUnit(self): # To do
        return self._obj.getTemporalUnit()

    @JOverride
    def setTemporalUnit(self, time_unit): # To do
        self._obj.setTemporalUnit(time_unit)

    @JOverride
    def applySpatioTemporalCalibrationToImage(self, ipl): # To do
        raise Exception('ObjWrapper: Implement applySpatioTemporalCalibrationToImage')

    @JOverride
    def setSpatioTemporalCalibrationFromExample(self, example: JSpatioTemporallyCalibrated): # No return
        raise Exception('ObjWrapper: Implement setSpatioTemporalCalibrationFromExample')


    # Obj default methods
    
    def getParents(self, use_full_hierarchy: bool) -> Dict[str, ObjWrapper]:
        raise Exception('ObjWrapper: Implement getParents')

    def getParent(self, name: str) -> ObjWrapper:
        raise Exception('ObjWrapper: Implement getParent')

    def addParent(self, parent: ObjWrapper):
        raise Exception('ObjWrapper: Implement addParent')

    def removeParent(self, name: str):
        raise Exception('ObjWrapper: Implement removeParent')

    def getChildren(self, name: str) -> ObjsWrapper:
        raise Exception('ObjWrapper: Implement getChildren')

    def addChildren(self, child_set: ObjsWrapper):
        raise Exception('ObjWrapper: Implement addChildren')

    def removeChildren(self, name: str):
        raise Exception('ObjWrapper: Implement removeChildren')

    def addChild(self, child: ObjWrapper):
        raise Exception('ObjWrapper: Implement addChild')

    def removeChild(self, child: ObjWrapper):
        raise Exception('ObjWrapper: Implement removeChild')

    def getPartners(self, name: str) -> ObjsWrapper:
        raise Exception('ObjWrapper: Implement getPartners')

    def addPartners(self, partner_set: ObjsWrapper):
        raise Exception('ObjWrapper: Implement addPartners')

    def addPartner(self, partner: ObjWrapper):
        raise Exception('ObjWrapper: Implement addPartner')

    def removePartner(self, partner: ObjWrapper):
        raise Exception('ObjWrapper: Implement removePartner')

    def removePartners(self, name: str):
        raise Exception('ObjWrapper: Implement removePartners')

    def getPreviousPartners(self, name: str) -> ObjsWrapper:
        raise Exception('ObjWrapper: Implement getPreviousPartners')

    def getSimultaneousPartners(self, name: str) -> ObjsWrapper:
        raise Exception('ObjWrapper: Implement getSimultaneousPartners')

    def getNextPartners(self, name: str) -> ObjsWrapper:
        raise Exception('ObjWrapper: Implement getNextPartners')

    def addMetadataItem(self, metadata_item): # To do
        raise Exception('ObjWrapper: Implement addMetadataItem')

    def getMetadataItem(self, name: str): # To do
        raise Exception('ObjWrapper: Implement getMetadataItem')

    def removeMetadataItem(self, name: str):
        raise Exception('ObjWrapper: Implement removeMetadataItem')

    def addMeasurement(self, measurement: MeasurementWrapper):
        self._obj.addMeasurement(measurement.getPythonMeasurement())

    def getMeasurement(self, name: str) -> MeasurementWrapper | None:
        measurement: Measurement | None = self._obj.getMeasurement(name)
        return None if measurement is None else wrapMeasurement(measurement)

    def removeMeasurement(self, name: str):
        raise Exception('ObjWrapper: Implement removeMeasurement')

    def getAsImage(self, imageName: str, single_timepoint: bool) -> ImageWrapper:
        raise Exception('ObjWrapper: Implement getAsImage')

    def getCentroidAsImage(self, imageName: str, single_timepoint: bool) -> ImageWrapper:
        raise Exception('ObjWrapper: Implement getCentroidAsImage')

    def addToImage(self, image: ImageWrapper, hue: float):
        raise Exception('ObjWrapper: Implement addToImage')

    def addCentroidToImage(self, image: ImageWrapper, hue: float):
        raise Exception('ObjWrapper: Implement addCentroidToImage')

    def removeOutOfBoundsCoords(self):
        raise Exception('ObjWrapper: Implement removeOutOfBoundsCoords')

    def getImgPlusCoordinateIterator(self): # To do
        raise Exception('ObjWrapper: Implement getImgPlusCoordinateIterator')


    # Volume default methods
            
    def getCoordinateIterator(self): # To do
        raise Exception('ObjWrapper: Implement getCoordinateIterator')

    def addCoord(self, x: int, y: int, z: int): # No return
        self._obj.addCoord(x,y,z)
        
    def addPoint(self, point): # To do
        raise Exception('ObjWrapper: Implement addPoint')

    def addPointsFromRoi(self, roi, z: int): # To do
        raise Exception('ObjWrapper: Implement addPointsFromRoi')

    def addPointsFromPolygon(self, polygon, z: int): # To do
        raise Exception('ObjWrapper: Implement addPointsFromPolygon')

    def addPointsFromShape(self, polygon, z: int): # To do
        raise Exception('ObjWrapper: Implement addPointsFromShape')

    def translateCoords(self, x_offs: int, y_offs: int, zOffs: int):
        raise Exception('ObjWrapper: Implement translateCoords')

    def finalise(self): # No return
        self._obj.finalise()

    def finaliseSlice(self, z: int): # No return
        self._obj.finaliseSlice(z)

    def getPoints(self): # To do
        raise Exception('ObjWrapper: Implement getPoints')

    def getProjectedArea(self, pixel_distances: bool) -> float:
        raise Exception('ObjWrapper: Implement getProjectedArea')

    def size(self) -> int:
        return self._obj.size()

    def setPoints(self, points): # To do
        raise Exception('ObjWrapper: Implement setPoints')

    def isOnEdgeXY(self, p) -> bool: # To do
        raise Exception('ObjWrapper: Implement isOnEdgeXY')

    def isOnEdgeZ(self, p) -> bool: # To do
        raise Exception('ObjWrapper: Implement isOnEdgeZ')

    def contains(self, point1) -> bool: # To do
        raise Exception('ObjWrapper: Implement contains')

    def getNumberOfElements(self) -> int:
        raise Exception('ObjWrapper: Implement getNumberOfElements')

    def is2D(self) -> bool:
        return self._obj.is2D()

    def getCalibratedX(self, point) -> float: # To do
        raise Exception('ObjWrapper: Implement getCalibratedX')

    def getCalibratedY(self, point) -> float: # To do
        raise Exception('ObjWrapper: Implement getCalibratedY')

    def getXYScaledZ(self, z: float) -> float:
        raise Exception('ObjWrapper: Implement getXYScaledZ')

    def getCalibratedZ(self, point, match_xy: bool) -> float: # To do
        raise Exception('ObjWrapper: Implement getCalibratedZ')

    def getExtents(self, pixel_distances: bool, match_xy: bool): # To do
        self._obj.getExtents(pixel_distances, match_xy)

    def getAsImage(self, imageName: str, t: int, nFrames: int) -> ImageWrapper:
        raise Exception('ObjWrapper: Implement getAsImage')

    def getAsTightImage(self, imageName: str) -> ImageWrapper:
        raise Exception('ObjWrapper: Implement getAsTightImage')

    def getAsTightImageWithBorders(self, imageName: str, border_widths) -> ImageWrapper: # To do
        raise Exception('ObjWrapper: Implement getAsTightImageWithBorders')

    def getContainedVolume(self, pixel_distances: bool) -> float:
        return self._obj.getContainedVolume(pixel_distances)

    def getOverlap(self, volume2: VolumeWrapper) -> int:
        raise Exception('ObjWrapper: Implement getOverlap')

    def getX(self, pixel_distances: bool): # To do
        raise Exception('ObjWrapper: Implement getX')

    def getY(self, pixel_distances: bool): # To do
        raise Exception('ObjWrapper: Implement getY')

    def getZ(self, pixel_distances: bool, match_xy: bool): # To do
        raise Exception('ObjWrapper: Implement getZ')

    def getSurfaceXCoords(self): # To do
        raise Exception('ObjWrapper: Implement getSurfaceXCoords')

    def getSurfaceYCoords(self): # To do
        raise Exception('ObjWrapper: Implement getSurfaceYCoords')

    def getSurfaceZCoords(self): # To do
        raise Exception('ObjWrapper: Implement getSurfaceZCoords')

    def getSurfaceX(self, pixel_distances: bool): # To do
        raise Exception('ObjWrapper: Implement getSurfaceX')

    def getSurfaceY(self, pixel_distances: bool): # To do
        raise Exception('ObjWrapper: Implement getSurfaceY')

    def getSurfaceZ(self, pixel_distances: bool, match_xy: bool): # To do
        raise Exception('ObjWrapper: Implement getSurfaceZ')

    def getXMean(self, pixel_distances: bool) -> float:
        raise Exception('ObjWrapper: Implement getXMean')

    def getYMean(self, pixel_distances: bool) -> float:
        raise Exception('ObjWrapper: Implement getYMean')

    def getZMean(self, pixel_distances: bool, match_xy: bool) -> float:
        raise Exception('ObjWrapper: Implement getZMean')

    def getVolumeHeight(self, pixel_distances: bool, match_xy: bool) -> float:
        raise Exception('ObjWrapper: Implement getVolumeHeight')

    def hasVolume(self) -> bool:
        raise Exception('ObjWrapper: Implement hasVolume')

    def hasArea(self) -> bool:
        raise Exception('ObjWrapper: Implement hasArea')

    def calculateAngle2D(self, volume2: VolumeWrapper) -> float:
        raise Exception('ObjWrapper: Implement calculateAngle2D')

    def calculateAngleToPoint2D(self, point) -> float: # To do
        raise Exception('ObjWrapper: Implement calculateAngleToPoint2D')

    def calculatePointPointSeparation(self, point1, point2, pixel_distances: bool) -> float: # To do
        raise Exception('ObjWrapper: Implement calculatePointPointSeparation')

    def getSurfaceSeparation(self, volume2, pixel_distances: bool, force2D: bool, ignore_edges_xy: bool, ignore_edges_z: bool) -> float: # To do
        raise Exception('ObjWrapper: Implement getSurfaceSeparation')

    def getPointSurfaceSeparation(self, point, pixel_distances: bool, force2D: bool, ignore_edges_xy: bool, ignore_edges_z: bool) -> float: # To do
        raise Exception('ObjWrapper: Implement getPointSurfaceSeparation')

    def getCentroidSeparation(self, volume2: VolumeWrapper, pixel_distances: bool, force2D: bool) -> float: # To do
        raise Exception('ObjWrapper: Implement getCentroidSeparation')

    def getOverlappingPoints(self, volume2: VolumeWrapper) -> VolumeWrapper:
        raise Exception('ObjWrapper: Implement getOverlappingPoints')

    def getSlice(self, slice: int) -> VolumeWrapper:
        raise Exception('ObjWrapper: Implement getSlice')

    def getRoi(self, slice: int): # To do
        raise Exception('ObjWrapper: Implement getRoi')
        

@JImplements('io.github.mianalysis.mia.object.coordinates.ObjFactoryI')
class ObjFactoryWrapper:
    
    @JOverride
    def getName(self) -> str:
        return "Python object factory"
    
    @JOverride
    def duplicate(self) -> ObjFactoryWrapper:
        return ObjFactoryWrapper()

    @JOverride
    def createObj(self, factory: CoordinateSetFactoryWrapper, obj_collection: ObjsWrapper) -> ObjWrapper: # To do
        return ObjWrapper(factory, obj_collection, obj_collection.getAndIncrementID())

    @JOverride
    def createObjWithID(self, factory: CoordinateSetFactoryWrapper, obj_collection: ObjsWrapper, ID: int) -> ObjWrapper: # To do
        return ObjWrapper(factory, obj_collection, ID)

def wrapObj(obj: Obj) -> ObjWrapper:
    obj_wrapper = ObjWrapper(None, None, 0)
    obj_wrapper.setPythonObj(obj)
    
    return obj_wrapper