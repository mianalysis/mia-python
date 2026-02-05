from __future__ import annotations
from jpype import JImplements, JOverride # type: ignore
from scyjava import jimport # type: ignore
from typing import List, TYPE_CHECKING
from weakref import WeakKeyDictionary

from src.wrappers.coordinatesetwrapper import CoordinateSetWrapper, CoordinateSetFactoryWrapper
from src.wrappers.imagewrapper import ImageWrapper
from src.objects.image import Image
from src.objects.volume import Volume
from src.types.JSpatiallyCalibrated import JSpatiallyCalibrated
from src.utilities.rois import getRoi

if TYPE_CHECKING:
    from src.types.JPointType import JPointType

_wrapper_cache: WeakKeyDictionary[Volume, VolumeWrapper] = WeakKeyDictionary() 

JVolumeAdaptor = jimport('io.github.mianalysis.mia.python.VolumeAdaptor') # type: ignore

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.VolumeI','io.github.mianalysis.mia.object.coordinates.SpatiallyCalibrated')
class VolumeWrapper:
    def __init__(self, coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper|None, width: int, height: int, n_slices: int, dpp_xy: float, dpp_z: float, spatial_units: str):
        if coordinate_set_factory_wrapper is not None:
            self._volume: Volume = Volume(coordinate_set_factory_wrapper.getPythonCoordinateSetFactory(), width, height, n_slices, dpp_xy, dpp_z, spatial_units)
        
    def getPythonVolume(self) -> Volume:
        return self._volume
    
    def setPythonVolume(self, volume: Volume): # No return
        self._volume = volume
        
    @JOverride
    def getFactory(self) -> VolumeFactoryWrapper:
        return VolumeFactoryWrapper()

    @JOverride
    def getCoordinateSetFactory(self) -> CoordinateSetFactoryWrapper:
        raise Exception('VolumeWrapper: Implement getCoordinateSetFactory')

    @JOverride
    def getSurface(self, ignore_edges_xy: bool, ignore_edge_eZ: bool) -> VolumeWrapper:
        raise Exception('VolumeWrapper: Implement getSurface')

    @JOverride
    def hasCalculatedSurface(self) -> bool:
        raise Exception('VolumeWrapper: Implement hasCalculatedSurface')

    @JOverride
    def getProjected(self) -> VolumeWrapper:
        raise Exception('VolumeWrapper: Implement getProjected')

    @JOverride
    def hasCalculatedProjection(self) -> bool:
        raise Exception('VolumeWrapper: Implement hasCalculatedProjection')

    @JOverride
    def getMeanCentroid(self, pixel_distances: bool, match_xy: bool) -> JPointType[float]:
        raise Exception('VolumeWrapper: Implement getMeanCentroid')

    @JOverride
    def hasCalculatedCentroid(self) -> bool:
        raise Exception('VolumeWrapper: Implement hasCalculatedCentroid')

    @JOverride
    def clearAllCoordinates(self): # No return
        raise Exception('VolumeWrapper: Implement clearAllCoordinates')

    @JOverride
    def clearSurface(self): # No return
        raise Exception('VolumeWrapper: Implement clearSurface')

    @JOverride
    def clearPoints(self): # No return
        raise Exception('VolumeWrapper: Implement clearPoints')

    @JOverride
    def clearProjected(self): # No return
        raise Exception('VolumeWrapper: Implement clearProjected')

    @JOverride
    def clearCentroid(self): # No return
        raise Exception('VolumeWrapper: Implement clearCentroid')

    @JOverride
    def hashCode(self) -> int:
        raise Exception('VolumeWrapper: Implement hashCode')

    @JOverride
    def equals(self, obj: VolumeWrapper) -> bool:
        raise Exception('VolumeWrapper: Implement equals')

    @JOverride
    def getCoordinateSet(self) -> CoordinateSetWrapper:
        coordinate_set_wrapper: CoordinateSetWrapper = CoordinateSetWrapper()
        coordinate_set_wrapper.setPythonCoordinateSet(self._volume.getCoordinateSet())

        return coordinate_set_wrapper

    @JOverride
    def setCoordinateSet(self, coordinate_set: CoordinateSetWrapper): # No return
        raise Exception('VolumeWrapper: Implement setCoordinateSet')

    @JOverride
    def createNewVolume(self, coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper, example_volume: VolumeWrapper) -> VolumeWrapper:
        raise Exception('VolumeWrapper: Implement createNewVolume')

    @JOverride
    def getCalibratedIterator(self, pixel_distances: bool, match_xy: bool): # To do
        raise Exception('VolumeWrapper: Implement getCalibratedIterator')


    # Default methods
        
    def getCoordinateIterator(self): # To do
        raise Exception('VolumeWrapper: Implement getCoordinateIterator')

    def addCoord(self, x: int, y: int, z: int): # No return
        self._volume.addCoord(x,y,z)

    def addPoint(self, point): # To do
        raise Exception('VolumeWrapper: Implement addPoint')

    def addPointsFromRoi(self, roi, z: int): # To do
        raise Exception('VolumeWrapper: Implement addPointsFromRoi')

    def addPointsFromPolygon(self, polygon, z: int): # To do
        raise Exception('VolumeWrapper: Implement addPointsFromPolygon')

    def addPointsFromShape(self, polygon, z: int): # To do
        raise Exception('VolumeWrapper: Implement addPointsFromShape')

    def translateCoords(self, x_offs: int, y_offs: int, z_offs: int):
        raise Exception('VolumeWrapper: Implement translateCoords')

    def finalise(self): # No return
        self._volume.finalise()

    def finaliseSlice(self, z: int): # No return
        self._volume.finaliseSlice(z)

    def getPoints(self): # To do
        raise Exception('VolumeWrapper: Implement getPoints')

    def getProjectedArea(self, pixel_distances: bool) -> float:
        raise Exception('VolumeWrapper: Implement getProjectedArea')

    def size(self) -> int:
        print("No size!")
        raise Exception('VolumeWrapper: Implement size')

    def setPoints(self, points): # To do
        raise Exception('VolumeWrapper: Implement setPoints')

    def isOnEdgeXY(self, p) -> bool: # To do
        raise Exception('VolumeWrapper: Implement isOnEdgeXY')

    def isOnEdgeZ(self, p) -> bool: # To do
        raise Exception('VolumeWrapper: Implement isOnEdgeZ')

    def contains(self, point1) -> bool: # To do
        raise Exception('VolumeWrapper: Implement contains')

    def getNumberOfElements(self) -> int:
        raise Exception('VolumeWrapper: Implement getNumberOfElements')

    def is2D(self) -> bool:
        raise Exception('VolumeWrapper: Implement is2D')

    def getCalibratedX(self, point) -> float: # To do
        raise Exception('VolumeWrapper: Implement getCalibratedX')

    def getCalibratedY(self, point) -> float: # To do
        raise Exception('VolumeWrapper: Implement getCalibratedY')

    def getXYScaledZ(self, z: float) -> float:
        return self._volume.getXYScaledZ(z)

    def getCalibratedZ(self, point, match_xy: bool) -> float: # To do
        raise Exception('VolumeWrapper: Implement getCalibratedZ')

    def getExtents(self, pixel_distances: bool, match_xy: bool) -> List[List[float]]:
        return self._volume.getExtents(pixel_distances, match_xy)

    def getAsImage(self, imageName: str, t: int, nFrames: int) -> ImageWrapper:
        raise Exception('VolumeWrapper: Implement getAsImage')

    def getAsTightImage(self, imageName: str) -> ImageWrapper:
        raise Exception('VolumeWrapper: Implement getAsTightImage')

    def getAsTightImageWithBorders(self, imageName: str, borderWidths) -> ImageWrapper: # To do
        raise Exception('VolumeWrapper: Implement getAsTightImageWithBorders')

    def getContainedVolume(self, pixel_distances: bool) -> float:
        raise Exception('VolumeWrapper: Implement getContainedVolume')

    def getOverlap(self, volume2: VolumeWrapper) -> int:
        raise Exception('VolumeWrapper: Implement getOverlap')

    def getX(self, pixel_distances: bool): # To do
        raise Exception('VolumeWrapper: Implement getX')

    def getY(self, pixel_distances: bool): # To do
        raise Exception('VolumeWrapper: Implement getY')

    def getZ(self, pixel_distances: bool, match_xy: bool): # To do
        raise Exception('VolumeWrapper: Implement getZ')

    def getSurfaceXCoords(self): # To do
        raise Exception('VolumeWrapper: Implement getSurfaceXCoords')

    def getSurfaceYCoords(self): # To do
        raise Exception('VolumeWrapper: Implement getSurfaceYCoords')

    def getSurfaceZCoords(self): # To do
        raise Exception('VolumeWrapper: Implement getSurfaceZCoords')

    def getSurfaceX(self, pixel_distances: bool): # To do
        raise Exception('VolumeWrapper: Implement getSurfaceX')

    def getSurfaceY(self, pixel_distances: bool): # To do
        raise Exception('VolumeWrapper: Implement getSurfaceY')

    def getSurfaceZ(self, pixel_distances: bool, match_xy: bool): # To do
        raise Exception('VolumeWrapper: Implement getSurfaceZ')

    def getXMean(self, pixel_distances: bool) -> float:
        return self.getXMean(pixel_distances)

    def getYMean(self, pixel_distances: bool) -> float:
        return self.getYMean(pixel_distances)

    def getZMean(self, pixel_distances: bool, match_xy: bool) -> float:
        return self.getZMean(pixel_distances, match_xy)

    def calculateBaseAreaPx(self) -> float:
        return self._volume.calculateBaseAreaPx()
    
    def getVolumeHeight(self, pixel_distances: bool, match_xy: bool) -> float:
        return self._volume.getVolumeHeight(pixel_distances, match_xy)

    def hasVolume(self) -> bool:
        raise Exception('VolumeWrapper: Implement hasVolume')

    def hasArea(self) -> bool:
        raise Exception('VolumeWrapper: Implement hasArea')

    def calculateAngle2D(self, volume2: VolumeWrapper) -> float:
        raise Exception('VolumeWrapper: Implement calculateAngle2D')

    def calculateAngleToPoint2D(self, point) -> float: # To do
        raise Exception('VolumeWrapper: Implement calculateAngleToPoint2D')

    def calculatePointPointSeparation(self, point1, point2, pixel_distances: bool) -> float: # To do
        raise Exception('VolumeWrapper: Implement calculatePointPointSeparation')

    def getSurfaceSeparation(self, volume2, pixel_distances: bool, force_2D: bool, ignore_edges_xy: bool, ignore_edges_z: bool) -> float: # To do
        raise Exception('VolumeWrapper: Implement getSurfaceSeparation')

    def getPointSurfaceSeparation(self, point, pixel_distances: bool, force_2D: bool, ignore_edges_xy: bool, ignore_edges_z: bool) -> float: # To do
        raise Exception('VolumeWrapper: Implement getPointSurfaceSeparation')

    def getCentroidSeparation(self, volume2: VolumeWrapper, pixel_distances: bool, force_2D: bool) -> float: # To do
        raise Exception('VolumeWrapper: Implement getCentroidSeparation')

    def getOverlappingPoints(self, volume2: VolumeWrapper) -> VolumeWrapper:
        raise Exception('VolumeWrapper: Implement getOverlappingPoints')

    def getSlice(self, slice: int) -> VolumeWrapper:
        return wrapVolume(self._volume.getSlice(slice))

    def getRoi(self, slice: int): # To do
        return getRoi(self._volume, slice)
        

    # From SpatiallyCalibrated

    @JOverride
    def getWidth(self) -> int:
        return self._volume.getWidth()

    @JOverride
    def setWidth(self, width: int): # No return
        self._volume.setWidth(width)

    @JOverride
    def getHeight(self) -> int:
        return self._volume.getHeight()

    @JOverride
    def setHeight(self, height: int): # No return
        self.height = height

    @JOverride
    def getNSlices(self) -> int:
        return self._volume.getNSlices()

    @JOverride
    def setNSlices(self, n_slices: int): # No return
        self.n_slices = n_slices

    @JOverride
    def getDppXY(self) -> float:
        return self._volume.getDppXY()

    @JOverride
    def setDppXY(self, dpp_xy: float): # No return
        self._dpp_xy = dpp_xy

    @JOverride
    def getDppZ(self) -> float:
        return self._volume.getDppZ()

    @JOverride
    def setDppZ(self, dpp_z: float): # No return
        self._dpp_z = dpp_z

    @JOverride
    def getSpatialUnits(self) -> str:
        return self._volume.getSpatialUnits()

    @JOverride
    def setSpatialUnits(self, spatial_units: str): # No return
        self._spatial_units = spatial_units

    @JOverride
    def applySpatialCalibrationToImage(self, ipl): # To do
        raise Exception('VolumeWrapper: Implement applySpatialCalibrationToImage')
        
    @JOverride
    def setSpatialCalibrationFromExample(self, example: JSpatiallyCalibrated): # To do
        raise Exception('VolumeWrapper: Implement setSpatialCalibrationFromExample')
    

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.VolumeFactoryI')
class VolumeFactoryWrapper:
    @JOverride
    def getName(self) -> str:
        return "Python volume factory"

    @JOverride
    def duplicate(self) -> VolumeFactoryWrapper:
        return VolumeFactoryWrapper()

    @JOverride
    def createVolume(self, coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper,  width: int, height: int, n_slices: int, dpp_xy: float, dpp_z: float, spatial_units: str) -> VolumeWrapper:
        return VolumeWrapper(coordinate_set_factory_wrapper, width, height, n_slices, dpp_xy, dpp_z, spatial_units)

    @JOverride
    def createVolumeFromExample(self, coordinate_set_factory_wrapper: CoordinateSetFactoryWrapper, example: JSpatiallyCalibrated) -> VolumeWrapper:
        return VolumeWrapper(coordinate_set_factory_wrapper, example.getWidth(), example.getHeight(), example.getNSlices(), example.getDppXY(), example.getDppZ(), example.getSpatialUnits())


def wrapVolume(volume: Volume) -> VolumeWrapper:    
    try:
        return _wrapper_cache[volume]
    except:        
        volume_wrapper: VolumeWrapper = VolumeWrapper(None,0,0,0,1,1,"px")
        volume_wrapper.setPythonVolume(volume)
        _wrapper_cache[volume]  = volume_wrapper
    
        return volume_wrapper