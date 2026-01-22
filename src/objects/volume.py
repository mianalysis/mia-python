from __future__ import annotations
from typing import Self, TYPE_CHECKING
from jpype import JImplements, JOverride # type: ignore

if TYPE_CHECKING:
    from src.objects.coordinateset import CoordinateSet, CoordinateSetFactory
    from src.types.types import Point
    from src.types.JSpatiallyCalibrated import JSpatiallyCalibrated

@JImplements('io.github.mianalysis.mia.object.coordinates.SpatiallyCalibrated')
class Volume():
    def __init__(self, coordinate_set_factory: CoordinateSetFactory, width: int, height: int, n_slices: int, dpp_xy: float, dpp_z: float, spatial_units: str):
        self._coordinate_set: CoordinateSet = coordinate_set_factory.createCoordinateSet()
        self._coordinate_set_factory: CoordinateSetFactory = coordinate_set_factory
        self._width: int = width
        self._height: int = height
        self._n_slices: int = n_slices
        self._dpp_xy: float = dpp_xy
        self._dpp_z: float = dpp_z
        self._spatial_units: str = spatial_units

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

    def equals(self, obj: Self) -> bool:
        raise Exception('VolumeWrapper: Implement equals')

    def getCoordinateSet(self) -> CoordinateSet:
        return self._coordinate_set

    def setCoordinateSet(self, coordinate_set: CoordinateSet):
        self._coordinate_set = coordinate_set

    def createNewVolume(self, coordinate_set_factory: CoordinateSetFactory, exampleVolume: Volume) -> Volume:
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
        if x < 0 or x >= self._width:
            print("Coordinate out of bounds! (x: %i)" % x)
            return
        if y < 0 or y >= self._height:
            print("Coordinate out of bounds! (y: %i)" % y)
            return
        if z < 0 or z >= self._n_slices:
            print("Coordinate out of bounds! (z: %i)" % z)
            return

        self._coordinate_set.addCoord(x, y, z)

    def finalise(self): # No return
        self._coordinate_set.finalise()

    def finaliseSlice(self, z: int): # No return
        self._coordinate_set.finaliseSlice(z)

    @JOverride
    def getWidth(self) -> int:
        return self._width

    @JOverride
    def setWidth(self, width: int): # No return
        self._width = width

    @JOverride
    def getHeight(self) -> int:
        return self._height

    @JOverride
    def setHeight(self, height: int): # No return
        self.height = height

    @JOverride
    def getNSlices(self) -> int:
        return self._n_slices

    @JOverride
    def setNSlices(self, n_slices: int): # No return
        self.n_slices = n_slices

    @JOverride
    def getDppXY(self) -> float:
        return self._dpp_xy

    @JOverride
    def setDppXY(self, dpp_xy: float): # No return
        self._dpp_xy = dpp_xy

    @JOverride
    def getDppZ(self) -> float:
        return self._dpp_z

    @JOverride
    def setDppZ(self, dpp_z: float): # No return
        self._dpp_z = dpp_z

    @JOverride
    def getSpatialUnits(self) -> str:
        return self._spatial_units

    @JOverride
    def setSpatialUnits(self, spatial_units: str): # No return
        self._spatial_units = spatial_units

    @JOverride
    def applySpatialCalibrationToImage(self, ipl): # To do
        raise Exception('SpatiallyCalibrated: Implement applySpatialCalibrationToImage')

    @JOverride    
    def setSpatialCalibrationFromExample(self, example: JSpatiallyCalibrated): # To do
        raise Exception('SpatiallyCalibrated: Implement setSpatialCalibrationFromExample')
        