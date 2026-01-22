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
        return VolumeFactory()

    @JOverride
    def getCoordinateSetFactory(self):
        print('VolumeWrapper: Implement getCoordinateSetFactory')

    @JOverride
    def getSurface(self, ignoreEdgesXY, ignoreEdgesZ):
        print('VolumeWrapper: Implement getSurface')

    @JOverride
    def hasCalculatedSurface(self):
        print('VolumeWrapper: Implement hasCalculatedSurface')

    @JOverride
    def getProjected(self):
        print('VolumeWrapper: Implement getProjected')

    @JOverride
    def hasCalculatedProjection(self):
        print('VolumeWrapper: Implement hasCalculatedProjection')

    @JOverride
    def getMeanCentroid(self, pixelDistances, matchXY):
        print('VolumeWrapper: Implement getMeanCentroid')

    @JOverride
    def hasCalculatedCentroid(self):
        print('VolumeWrapper: Implement hasCalculatedCentroid')

    @JOverride
    def clearAllCoordinates(self):
        print('VolumeWrapper: Implement clearAllCoordinates')

    @JOverride
    def clearSurface(self):
        print('VolumeWrapper: Implement clearSurface')

    @JOverride
    def clearPoints(self):
        print('VolumeWrapper: Implement clearPoints')

    @JOverride
    def clearProjected(self):
        print('VolumeWrapper: Implement clearProjected')

    @JOverride
    def clearCentroid(self):
        print('VolumeWrapper: Implement clearCentroid')

    @JOverride
    def hashCode(self):
        print('VolumeWrapper: Implement hashCode')

    @JOverride
    def equals(self, obj):
        print('VolumeWrapper: Implement equals')

    @JOverride
    def getSpatialCalibration(self):
        print('VolumeWrapper: Implement getSpatialCalibration')

    @JOverride
    def setSpatialCalibration(self, spat_cal):
        print('VolumeWrapper: Implement setSpatialCalibration')

    @JOverride
    def getCoordinateSet(self):
        print('VolumeWrapper: Implement getCoordinateSet')

    @JOverride
    def setCoordinateSet(self, coordinate_set):
        print('VolumeWrapper: Implement setCoordinateSet')

    @JOverride
    def createNewVolume(self, factory, spatCal):
        print('VolumeWrapper: Implement createNewVolume')

    @JOverride
    def getCalibratedIterator(self, pixelDistances, matchXY):
        print('VolumeWrapper: Implement getCalibratedIterator')

    # Default methods
    def addCoord(self, x, y, z):
        print('VolumeWrapper: Implement addCoord')

    def finalise(self):
        print('VolumeWrapper: Implement finalise')

    def finaliseSlice(self, z):
        print('VolumeWrapper: Implement finaliseSlice')

    def getWidth(self):
        print('VolumeWrapper: Implement getWidth')

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.VolumeFactory')
class VolumeFactory:
    
    @JOverride
    def getName(self):
        return "Python volume factory"
    
    @JOverride
    def createVolume(self, coordinate_set_factory, spat_cal):
        return VolumeWrapper(coordinate_set_factory, spat_cal)

    @JOverride
    def duplicate(self):
        return VolumeFactory()
    