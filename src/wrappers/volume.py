from jpype import JImplements, JOverride
from scyjava import jimport

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.Volume')
class VolumeWrapper:
    # protected Volume surface = null;
    # protected Volume projection = null;
    # protected Point<Double> meanCentroidPx = null;

    def __init__(self, coordinate_set_factory, spat_cal=None):
        self._coordinate_set = coordinate_set_factory.createCoordinateSet()
        self._coordinate_set_factory = coordinate_set_factory
        self._spat_cal = spat_cal

    # def __init__(self, factory, width, height, nSlices, dppXY, dppZ, units):
    #     print('VolumeWrapper: Implement constructor')

    @JOverride
    def getFactory(self):
        return PythonVolumeFactory()

    @JOverride
    def getCoordinateSetFactory(self):
        return self._coordinate_set_factory

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
        return self._spat_cal

    @JOverride
    def setSpatialCalibration(self, spat_cal):
        self._spat_cal = spat_cal

    @JOverride
    def getCoordinateSet(self):
        return self._coordinate_set

    @JOverride
    def setCoordinateSet(self, coordinate_set):
        self._coordinate_set = coordinate_set

    @JOverride
    def createNewVolume(self, factory, spatCal):
        print('VolumeWrapper: Implement createNewVolume')

    @JOverride
    def getCalibratedIterator(self, pixelDistances, matchXY):
        print('VolumeWrapper: Implement getCalibratedIterator')

    # private class VolumeIterator implements Iterator<Point<Double>> {
    #     private Iterator<Point<Integer>> iterator;
    #     private boolean pixelDistances;
    #     private boolean matchXY;

    #     public VolumeIterator(boolean pixelDistances, boolean matchXY) {
    #         this.pixelDistances = pixelDistances;
    #         this.iterator = coordinateSet.iterator();
    #         this.matchXY = matchXY;
    #     }

    #     @Override
    #     public boolean hasNext() {
    #         return iterator.hasNext();
    #     }

    #     @Override
    #     public Point<Double> next() {
    #         Point<Integer> nextPoint = iterator.next();
    #         int x = nextPoint.x;
    #         int y = nextPoint.y;
    #         int z = nextPoint.z;

    #         if (pixelDistances && matchXY) {
    #             return new Point<>((double) x, (double) y, (double) z * spatCal.dppZ / spatCal.dppXY);
    #         } else if (pixelDistances & !matchXY) {
    #             return new Point<>((double) x, (double) y, (double) z);
    #         } else {
    #             return new Point<>((double) x * spatCal.dppXY, (double) y * spatCal.dppXY, (double) z * spatCal.dppZ);
    #         }
    #     }
    # }

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.VolumeFactory')
class PythonVolumeFactory:
    
    @JOverride
    def getName(self):
        return "Python volume factory"
    
    @JOverride
    def createVolume(self, coordinate_set_factory, spat_cal):
        return VolumeWrapper(coordinate_set_factory, spat_cal)

    @JOverride
    def duplicate(self):
        return PythonVolumeFactory()
    