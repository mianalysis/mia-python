from __future__ import annotations
from jpype import JImplements, JOverride
from scyjava import jimport
from typing import TYPE_CHECKING

from src.wrappers.coordinatesetwrapper import CoordinateSetWrapper, CoordinateSetFactoryWrapper
from src.objects.volume import Volume

if TYPE_CHECKING:
    from types.JPointType import JPointType

JVolumeAdaptor = jimport('io.github.mianalysis.mia.python.VolumeAdaptor')

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.VolumeI')
class VolumeWrapper:
    def __init__(self, coordinate_set_factory_wrapper: CoordinateSetWrapper, spat_cal):
        self._volume: Volume = Volume(coordinate_set_factory_wrapper.getPythonCoordinateSet(), spat_cal)
        
    def getPythonVolume(self) -> Volume:
        return self._volume
        
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
    def getSpatialCalibration(self): # To do
        raise Exception('VolumeWrapper: Implement getSpatialCalibration')

    @JOverride
    def setSpatialCalibration(self, spat_cal): # To do
        raise Exception('VolumeWrapper: Implement setSpatialCalibration')

    @JOverride
    def getCoordinateSet(self) -> CoordinateSetWrapper:
        raise Exception('VolumeWrapper: Implement getCoordinateSet')

    @JOverride
    def setCoordinateSet(self, coordinate_set: CoordinateSetWrapper): # No return
        raise Exception('VolumeWrapper: Implement setCoordinateSet')

    @JOverride
    def createNewVolume(self, factory: CoordinateSetFactoryWrapper, spatCal): # To do
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

    def getWidth(self) -> int:
        return self._volume.getWidth()

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.VolumeFactory')
class VolumeFactoryWrapper:
    @JOverride
    def getName(self) -> str:
        return "Python volume factory"
    
    @JOverride
    def createVolume(self, coordinate_set_factory: CoordinateSetFactoryWrapper, spat_cal): # To do
        return VolumeWrapper(coordinate_set_factory, spat_cal)

    @JOverride
    def duplicate(self) -> VolumeFactoryWrapper:
        return VolumeFactoryWrapper()
    