from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.objects.coordinateset import CoordinateSet, CoordinateSetFactory
    from src.types.types import Point

class Volume:
    def __init__(self, coordinate_set_factory: CoordinateSetFactory, spat_cal): # To do
        self._coordinate_set: CoordinateSet = coordinate_set_factory.createCoordinateSet()
        self._coordinate_set_factory: CoordinateSetFactory = coordinate_set_factory
        self._spat_cal = spat_cal

        # Storing these for access speed
        self._width: int = spat_cal.getWidth()
        self._height: int = spat_cal.getHeight()
        self._nSlices: int = spat_cal.getNSlices()

    def getCoordinateSetFactory(self) -> CoordinateSetFactory:
        return self._coordinate_set_factory
    
    def getSurface(self, ignore_edges_XY: bool, ignore_edges_Z: bool) -> Volume:
        raise Exception('VolumeWrapper: Implement getSurface')

    def hasCalculatedSurface(self) -> bool:
        raise Exception('VolumeWrapper: Implement hasCalculatedSurface')

    def getProjected(self) -> Volume:
        raise Exception('VolumeWrapper: Implement getProjected')

    def hasCalculatedProjection(self) -> bool:
        raise Exception('VolumeWrapper: Implement hasCalculatedProjection')

    def getMeanCentroid(self, pixel_distances: bool, match_XY: bool) -> Point:
        raise Exception('VolumeWrapper: Implement getMeanCentroid')

    def hasCalculatedCentroid(self) -> bool:
        raise Exception('VolumeWrapper: Implement hasCalculatedCentroid')

    def clearAllCoordinates(self): # No return
        raise Exception('VolumeWrapper: Implement clearAllCoordinates')

    def clearSurface(self): # No return
        raise Exception('VolumeWrapper: Implement clearSurface')

    def clearPoints(self): # No return
        raise Exception('VolumeWrapper: Implement clearPoints')

    def clearProjected(self): # No return
        raise Exception('VolumeWrapper: Implement clearProjected')

    def clearCentroid(self): # No return
        raise Exception('VolumeWrapper: Implement clearCentroid')

    def hashCode(self) -> int:
        raise Exception('VolumeWrapper: Implement hashCode')

    def equals(self, obj: Volume) -> bool:
        raise Exception('VolumeWrapper: Implement equals')

    def getSpatialCalibration(self): # To do
        return self._spat_cal

    def setSpatialCalibration(self, spat_cal): # To do
        self._spat_cal = spat_cal

    def getCoordinateSet(self) -> CoordinateSet:
        return self._coordinate_set

    def setCoordinateSet(self, coordinate_set: CoordinateSet):
        self._coordinate_set = coordinate_set

    def createNewVolume(self, coordinate_set_factory: CoordinateSetFactory, spatCal) -> Volume:
        raise Exception('VolumeWrapper: Implement createNewVolume')

    def getCalibratedIterator(self, pixel_distances: bool, match_XY: bool): # To do
        raise Exception('VolumeWrapper: Implement getCalibratedIterator')

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
    def addCoord(self, x: int, y: int, z: int): # No return
        if self._spat_cal is not None:
            if x < 0 or x >= self._width:
                print("Coordinate out of bounds! (x: %i)" % x)
                return
            if y < 0 or y >= self._height:
                print("Coordinate out of bounds! (y: %i)" % y)
                return
            if z < 0 or z >= self._nSlices:
                print("Coordinate out of bounds! (z: %i)" % z)
                return

        self._coordinate_set.addCoord(x, y, z)

    def finalise(self): # No return
        pass

    def finaliseSlice(self, z: int): # No return
        pass

    def getWidth(self) -> int:
        return self._width
        