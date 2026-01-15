from __future__ import annotations
from jpype import JImplements, JOverride # type: ignore
from scyjava import jimport # type: ignore
from typing import TYPE_CHECKING

from src.wrappers.coordinatesetwrapper import CoordinateSetWrapper, CoordinateSetFactoryWrapper
from src.objects.volume import Volume
from src.types.JSpatiallyCalibrated import JSpatiallyCalibrated

if TYPE_CHECKING:
    from types.JPointType import JPointType
    from types.JPype import *

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
    def getSurface(self, ignoreEdgesXY: bool, ignoreEdgesZ: bool) -> VolumeWrapper:
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
    def getMeanCentroid(self, pixelDistances: bool, matchXY: bool) -> JPointType[float]:
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
    def getCoordinateSet(self: VolumeWrapper) -> CoordinateSetWrapper:
        coordinate_set_wrapper: CoordinateSetWrapper = CoordinateSetWrapper()
        coordinate_set_wrapper.setPythonCoordinateSet(self._volume.getCoordinateSet())

        return coordinate_set_wrapper

    @JOverride
    def setCoordinateSet(self, coordinate_set: CoordinateSetWrapper): # No return
        raise Exception('VolumeWrapper: Implement setCoordinateSet')

    @JOverride
    def createNewVolume(self, factory: CoordinateSetFactoryWrapper, example_volume: VolumeWrapper):
        raise Exception('VolumeWrapper: Implement createNewVolume')

    @JOverride
    def getCalibratedIterator(self, pixelDistances: bool, matchXY: bool): # To do
        raise Exception('VolumeWrapper: Implement getCalibratedIterator')

    # Default methods
    def addCoord(self, x: int, y: int, z: int): # No return
        self._volume.addCoord(x,y,z)

    def finalise(self): # No return
        self._volume.finalise()

    def finaliseSlice(self, z: int): # No return
        self._volume.finaliseSlice(z)


    # From SpatiallyCalibrated

    @JOverride
    def getWidth(self: VolumeWrapper) -> int:
        return self._volume.getWidth()

    @JOverride
    def setWidth(self: VolumeWrapper, width: int): # No return
        self._volume.setWidth(width)

    @JOverride
    def getHeight(self: VolumeWrapper) -> int:
        return self._volume.getHeight()

    @JOverride
    def setHeight(self: VolumeWrapper, height: int): # No return
        self.height = height

    @JOverride
    def getNSlices(self: VolumeWrapper) -> int:
        return self._volume.getNSlices()

    @JOverride
    def setNSlices(self: VolumeWrapper, n_slices: int): # No return
        self.n_slices = n_slices

    @JOverride
    def getDppXY(self: VolumeWrapper) -> float:
        return self._volume.getDppXY()

    @JOverride
    def setDppXY(self: VolumeWrapper, dpp_xy: float): # No return
        self._dpp_xy = dpp_xy

    @JOverride
    def getDppZ(self: VolumeWrapper) -> float:
        return self._volume.getDppZ()

    @JOverride
    def setDppZ(self: VolumeWrapper, dpp_z: float): # No return
        self._dpp_z = dpp_z

    @JOverride
    def getSpatialUnits(self: VolumeWrapper) -> str:
        return self._volume.getSpatialUnits()

    @JOverride
    def setSpatialUnits(self: VolumeWrapper, spatial_units: str): # No return
        self._spatial_units = spatial_units

    @JOverride
    def applySpatialCalibrationToImage(self: VolumeWrapper, ipl): # To do
        self._volume.applySpatialCalibrationToImage(ipl)
        
    @JOverride
    def setSpatialCalibrationFromExample(self: VolumeWrapper, example: JSpatiallyCalibrated): # To do
        self._volume.setSpatialCalibrationFromExample(example)
    

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
    # Setting empty wrapper, as it will be repopulated immediately with real volume
    volume_wrapper: VolumeWrapper = VolumeWrapper(None,0,0,0,1,1,"px")

    volume_wrapper.setPythonVolume(volume)
    
    return volume_wrapper
    