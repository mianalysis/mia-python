class Volume:
    def __init__(self, coordinate_set_factory, spat_cal):
        self._coordinate_set = coordinate_set_factory.createCoordinateSet()
        self._coordinate_set_factory = coordinate_set_factory
        self._spat_cal = spat_cal

        # Storing these for access speed
        self._width = spat_cal.getWidth()
        self._height = spat_cal.getHeight()
        self._nSlices = spat_cal.getNSlices()

    def getCoordinateSetFactory(self):
        return self._coordinate_set_factory

    def getSurface(self, ignoreEdgesXY, ignoreEdgesZ):
        print('VolumeWrapper: Implement getSurface')

    def hasCalculatedSurface(self):
        print('VolumeWrapper: Implement hasCalculatedSurface')

    def getProjected(self):
        print('VolumeWrapper: Implement getProjected')

    def hasCalculatedProjection(self):
        print('VolumeWrapper: Implement hasCalculatedProjection')

    def getMeanCentroid(self, pixelDistances, matchXY):
        print('VolumeWrapper: Implement getMeanCentroid')

    def hasCalculatedCentroid(self):
        print('VolumeWrapper: Implement hasCalculatedCentroid')

    def clearAllCoordinates(self):
        print('VolumeWrapper: Implement clearAllCoordinates')

    def clearSurface(self):
        print('VolumeWrapper: Implement clearSurface')

    def clearPoints(self):
        print('VolumeWrapper: Implement clearPoints')

    def clearProjected(self):
        print('VolumeWrapper: Implement clearProjected')

    def clearCentroid(self):
        print('VolumeWrapper: Implement clearCentroid')

    def hashCode(self):
        print('VolumeWrapper: Implement hashCode')

    def equals(self, obj):
        print('VolumeWrapper: Implement equals')

    def getSpatialCalibration(self):
        return self._spat_cal

    def setSpatialCalibration(self, spat_cal):
        self._spat_cal = spat_cal

    def getCoordinateSet(self):
        return self._coordinate_set

    def setCoordinateSet(self, coordinate_set):
        self._coordinate_set = coordinate_set

    def createNewVolume(self, factory, spatCal):
        print('VolumeWrapper: Implement createNewVolume')

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

    # Default methods
    def addCoord(self, x, y, z):
        if self._spat_cal is not None:
            if x < 0 or x >= self._width:
                print("Coordinate out of bounds! (x: " + x + ")")
                return
            if y < 0 or y >= self._height:
                print("Coordinate out of bounds! (y: " + y + ")")
                return
            if z < 0 or z >= self._nSlices:
                print("Coordinate out of bounds! (z: " + z + ")")
                return

        self._coordinate_set.addCoord(x, y, z)

    def finalise(self):
        VolumeAdaptor.finalise(self)

    def finaliseSlice(self, z):
        VolumeAdaptor.finaliseSlice(self, z)

    def getWidth(self):
        return VolumeAdaptor.getWidth(self)
    