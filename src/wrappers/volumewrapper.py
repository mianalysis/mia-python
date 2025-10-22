from jpype import JImplements, JOverride
from scyjava import jimport

from src.wrappers.coordinatesetwrapper import CoordinateSetWrapper
from src.objects.volume import Volume

VolumeAdaptor = jimport('io.github.mianalysis.mia.python.VolumeAdaptor')

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.Volume')
class VolumeWrapper:
    def __init__(self, coordinate_set_factory_wrapper: CoordinateSetWrapper, spat_cal):
        self._volume = Volume(coordinate_set_factory_wrapper.getPythonCoordinateSet(), spat_cal)
        
    def getPythonVolume(self):
        return self._volume
        
    @JOverride
    def getFactory(self):
        return VolumeFactoryWrapper()

    @JOverride
    def getCoordinateSetFactory(self):
        raise Exception('VolumeWrapper: Implement getCoordinateSetFactory')

    @JOverride
    def getSurface(self, ignoreEdgesXY, ignoreEdgesZ):
        raise Exception('VolumeWrapper: Implement getSurface')

    @JOverride
    def hasCalculatedSurface(self):
        raise Exception('VolumeWrapper: Implement hasCalculatedSurface')

    @JOverride
    def getProjected(self):
        raise Exception('VolumeWrapper: Implement getProjected')

    @JOverride
    def hasCalculatedProjection(self):
        raise Exception('VolumeWrapper: Implement hasCalculatedProjection')

    @JOverride
    def getMeanCentroid(self, pixelDistances, matchXY):
        raise Exception('VolumeWrapper: Implement getMeanCentroid')

    @JOverride
    def hasCalculatedCentroid(self):
        raise Exception('VolumeWrapper: Implement hasCalculatedCentroid')

    @JOverride
    def clearAllCoordinates(self):
        raise Exception('VolumeWrapper: Implement clearAllCoordinates')

    @JOverride
    def clearSurface(self):
        raise Exception('VolumeWrapper: Implement clearSurface')

    @JOverride
    def clearPoints(self):
        raise Exception('VolumeWrapper: Implement clearPoints')

    @JOverride
    def clearProjected(self):
        raise Exception('VolumeWrapper: Implement clearProjected')

    @JOverride
    def clearCentroid(self):
        raise Exception('VolumeWrapper: Implement clearCentroid')

    @JOverride
    def hashCode(self):
        raise Exception('VolumeWrapper: Implement hashCode')

    @JOverride
    def equals(self, obj):
        raise Exception('VolumeWrapper: Implement equals')

    @JOverride
    def getSpatialCalibration(self):
        raise Exception('VolumeWrapper: Implement getSpatialCalibration')

    @JOverride
    def setSpatialCalibration(self, spat_cal):
        raise Exception('VolumeWrapper: Implement setSpatialCalibration')

    @JOverride
    def getCoordinateSet(self):
        raise Exception('VolumeWrapper: Implement getCoordinateSet')

    @JOverride
    def setCoordinateSet(self, coordinate_set):
        raise Exception('VolumeWrapper: Implement setCoordinateSet')

    @JOverride
    def createNewVolume(self, factory, spatCal):
        raise Exception('VolumeWrapper: Implement createNewVolume')

    @JOverride
    def getCalibratedIterator(self, pixelDistances, matchXY):
        raise Exception('VolumeWrapper: Implement getCalibratedIterator')

    # Default methods
    def addCoord(self, x, y, z):
        self._volume.addCoord(x,y,z)

    def finalise(self):
        self._volume.finalise()

    def finaliseSlice(self, z):
        self._volume.finaliseSlice(z)

    def getWidth(self):
        self._volume.getWidth()

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.VolumeFactory')
class VolumeFactoryWrapper:
    @JOverride
    def getName(self):
        return "Python volume factory"
    
    @JOverride
    def createVolume(self, coordinate_set_factory, spat_cal):
        return VolumeWrapper(coordinate_set_factory, spat_cal)

    @JOverride
    def duplicate(self):
        return VolumeFactoryWrapper()
    