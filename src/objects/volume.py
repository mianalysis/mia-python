from __future__ import annotations
from typing import Self, TYPE_CHECKING

from src.objects.image import Image

if TYPE_CHECKING:
    from src.objects.coordinateset import CoordinateSet, CoordinateSetFactory
    from src.types.types import Point

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
        raise Exception('Volume: Implement getSurface')

    def hasCalculatedSurface(self) -> bool:
        raise Exception('Volume: Implement hasCalculatedSurface')

    def getProjected(self) -> Volume:
        raise Exception('Volume: Implement getProjected')

    def hasCalculatedProjection(self) -> bool:
        raise Exception('Volume: Implement hasCalculatedProjection')

    def getMeanCentroid(self, pixel_distances: bool, match_XY: bool) -> Point:
        raise Exception('Volume: Implement getMeanCentroid')

    def hasCalculatedCentroid(self) -> bool:
        raise Exception('Volume: Implement hasCalculatedCentroid')

    def clearAllCoordinates(self): # No return
        raise Exception('Volume: Implement clearAllCoordinates')

    def clearSurface(self): # No return
        raise Exception('Volume: Implement clearSurface')

    def clearPoints(self): # No return
        raise Exception('Volume: Implement clearPoints')

    def clearProjected(self): # No return
        raise Exception('Volume: Implement clearProjected')

    def clearCentroid(self): # No return
        raise Exception('Volume: Implement clearCentroid')

    def hashCode(self) -> int:
        raise Exception('Volume: Implement hashCode')

    def equals(self, obj: Self) -> bool:
        raise Exception('Volume: Implement equals')

    def getCoordinateSet(self) -> CoordinateSet:
        return self._coordinate_set

    def setCoordinateSet(self, coordinate_set: CoordinateSet):
        self._coordinate_set = coordinate_set

    def createNewVolume(self, coordinate_set_factory: CoordinateSetFactory, exampleVolume: Volume) -> Volume:
        raise Exception('Volume: Implement createNewVolume')

    def getCalibratedIterator(self, pixel_distances: bool, match_XY: bool): # To do
        raise Exception('Volume: Implement getCalibratedIterator')

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

    # From SpatiallyCalibrated
    
    def getWidth(self) -> int:
        return self._width

    def setWidth(self, width: int): # No return
        self._width = width

    def getHeight(self) -> int:
        return self._height

    def setHeight(self, height: int): # No return
        self.height = height

    def getNSlices(self) -> int:
        return self._n_slices

    def setNSlices(self, n_slices: int): # No return
        self.n_slices = n_slices

    def getDppXY(self) -> float:
        return self._dpp_xy

    def setDppXY(self, dpp_xy: float): # No return
        self._dpp_xy = dpp_xy

    def getDppZ(self) -> float:
        return self._dpp_z

    def setDppZ(self, dpp_z: float): # No return
        self._dpp_z = dpp_z

    def getSpatialUnits(self) -> str:
        return self._spatial_units

    def setSpatialUnits(self, spatial_units: str): # No return
        self._spatial_units = spatial_units
        
        
    # Default methods

    def getCoordinateIterator(self): # To do
        raise Exception('Volume: Implement getCoordinateIterator')

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

    def addPoint(self, point): # To do
        raise Exception('Volume: Implement addPoint')

    def addPointsFromRoi(self, roi, z: int): # To do
        raise Exception('Volume: Implement addPointsFromRoi')

    def addPointsFromPolygon(self, polygon, z: int): # To do
        raise Exception('Volume: Implement addPointsFromPolygon')

    def addPointsFromShape(self, polygon, z: int): # To do
        raise Exception('Volume: Implement addPointsFromShape')

    def translateCoords(self, xOffs: int, yOffs: int, zOffs: int):
        raise Exception('Volume: Implement translateCoords')

    def finalise(self): # No return
        self._coordinate_set.finalise()

    def finaliseSlice(self, z: int): # No return
        self._coordinate_set.finaliseSlice(z)

    def getPoints(self): # To do
        raise Exception('Volume: Implement getPoints')

    def getProjectedArea(self, pixelDistances: bool) -> float:
        raise Exception('Volume: Implement getProjectedArea')

    def size(self) -> int:
        return self._coordinate_set.size()

    def setPoints(self, points): # To do
        raise Exception('Volume: Implement setPoints')

    def isOnEdgeXY(self, p) -> bool: # To do
        raise Exception('Volume: Implement isOnEdgeXY')

    def isOnEdgeZ(self, p) -> bool: # To do
        raise Exception('Volume: Implement isOnEdgeZ')

    def contains(self, point1) -> bool: # To do
        raise Exception('Volume: Implement contains')

    def getNumberOfElements(self) -> int:
        raise Exception('Volume: Implement getNumberOfElements')

    def is2D(self) -> bool:
        return self.getNSlices() == 1

    def getCalibratedX(self, point) -> float: # To do
        raise Exception('Volume: Implement getCalibratedX')

    def getCalibratedY(self, point) -> float: # To do
        raise Exception('Volume: Implement getCalibratedY')

    def getXYScaledZ(self, z: float) -> float:
        raise Exception('Volume: Implement getXYScaledZ')

    def getCalibratedZ(self, point, matchXY: bool) -> float: # To do
        raise Exception('Volume: Implement getCalibratedZ')

    def getExtents(self, pixelDistances: bool, matchXY: bool): # To do
        raise Exception('Volume: Implement getExtents')

    def getAsImage(self, imageName: str, t: int, nFrames: int) -> Image:
        raise Exception('Volume: Implement getAsImage')

    def getAsTightImage(self, imageName: str) -> Image:
        raise Exception('Volume: Implement getAsTightImage')

    def getAsTightImageWithBorders(self, imageName: str, borderWidths) -> Image: # To do
        raise Exception('Volume: Implement getAsTightImageWithBorders')

    def getContainedVolume(self, pixelDistances: bool) -> float:
        if pixelDistances:
            return self.size() * self.getDppZ() / self.getDppXY()
        else:
            return self.size() * self.getDppXY() * self.getDppXY() * self.getDppZ()
        
    def getOverlap(self, volume2: Volume) -> int:
        raise Exception('Volume: Implement getOverlap')

    def getX(self, pixelDistances: bool): # To do
        raise Exception('Volume: Implement getX')

    def getY(self, pixelDistances: bool): # To do
        raise Exception('Volume: Implement getY')

    def getZ(self, pixelDistances: bool, matchXY: bool): # To do
        raise Exception('Volume: Implement getZ')

    def getSurfaceXCoords(self): # To do
        raise Exception('Volume: Implement getSurfaceXCoords')

    def getSurfaceYCoords(self): # To do
        raise Exception('Volume: Implement getSurfaceYCoords')

    def getSurfaceZCoords(self): # To do
        raise Exception('Volume: Implement getSurfaceZCoords')

    def getSurfaceX(self, pixelDistances: bool): # To do
        raise Exception('Volume: Implement getSurfaceX')

    def getSurfaceY(self, pixelDistances: bool): # To do
        raise Exception('Volume: Implement getSurfaceY')

    def getSurfaceZ(self, pixelDistances: bool, matchXY: bool): # To do
        raise Exception('Volume: Implement getSurfaceZ')

    def getXMean(self, pixelDistances: bool) -> float:
        raise Exception('Volume: Implement getXMean')

    def getYMean(self, pixelDistances: bool) -> float:
        raise Exception('Volume: Implement getYMean')

    def getZMean(self, pixelDistances: bool, matchXY: bool) -> float:
        raise Exception('Volume: Implement getZMean')

    def getVolumeHeight(self, pixelDistances: bool, matchXY: bool) -> float:
        raise Exception('Volume: Implement getVolumeHeight')

    def hasVolume(self) -> bool:
        raise Exception('Volume: Implement hasVolume')

    def hasArea(self) -> bool:
        raise Exception('Volume: Implement hasArea')

    def calculateAngle2D(self, volume2: Volume) -> float:
        raise Exception('Volume: Implement calculateAngle2D')

    def calculateAngleToPoint2D(self, point) -> float: # To do
        raise Exception('Volume: Implement calculateAngleToPoint2D')

    def calculatePointPointSeparation(self, point1, point2, pixelDistances: bool) -> float: # To do
        raise Exception('Volume: Implement calculatePointPointSeparation')

    def getSurfaceSeparation(self, volume2, pixelDistances: bool, force2D: bool, ignoreEdgesXY: bool, ignoreEdgesZ: bool) -> float: # To do
        raise Exception('Volume: Implement getSurfaceSeparation')

    def getPointSurfaceSeparation(self, point, pixelDistances: bool, force2D: bool, ignoreEdgesXY: bool, ignoreEdgesZ: bool) -> float: # To do
        raise Exception('Volume: Implement getPointSurfaceSeparation')

    def getCentroidSeparation(self, volume2: Volume, pixelDistances: bool, force2D: bool) -> float: # To do
        raise Exception('Volume: Implement getCentroidSeparation')

    def getOverlappingPoints(self, volume2: Volume) -> Volume:
        raise Exception('Volume: Implement getOverlappingPoints')

    def getSlice(self, slice: int) -> Volume:
        raise Exception('Volume: Implement getSlice')

    def getRoi(self, slice: int): # To do
        raise Exception('Volume: Implement getRoi')

    