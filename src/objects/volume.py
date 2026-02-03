from __future__ import annotations
from typing import List, Self, TYPE_CHECKING

import numpy as np

from src.objects.image import Image, createImage

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
    #     private boolean pixel_distances;
    #     private boolean match_xy;

    #     public VolumeIterator(boolean pixel_distances, boolean match_xy) {
    #         this.pixel_distances = pixel_distances;
    #         this.iterator = coordinateSet.iterator();
    #         this.match_xy = match_xy;
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

    #         if (pixel_distances && match_xy) {
    #             return new Point<>((double) x, (double) y, (double) z * spatCal.dppZ / spatCal.dppXY);
    #         } else if (pixel_distances & !match_xy) {
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

    def translateCoords(self, x_offs: int, y_offs: int, z_offs: int):
        raise Exception('Volume: Implement translateCoords')

    def finalise(self): # No return
        self._coordinate_set.finalise()

    def finaliseSlice(self, z: int): # No return
        self._coordinate_set.finaliseSlice(z)

    def getPoints(self): # To do
        raise Exception('Volume: Implement getPoints')

    def getProjectedArea(self, pixel_distances: bool) -> float:
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

    def getCalibratedZ(self, point, match_xy: bool) -> float: # To do
        raise Exception('Volume: Implement getCalibratedZ')

    def getExtents(self, pixel_distances: bool, match_xy: bool) -> List[List[float]]:
        if self.size() == 0:
            return [[0,0],[0,0],[0,0]]
        
        minX: float = float('inf')
        maxX: float = -float('inf')
        minY: float = float('inf')
        maxY: float = -float('inf')
        minZ: float = float('inf')
        maxZ: float = -float('inf')
        
        # Getting XY ranges
        point: Point
        for point in self.getCoordinateSet():
            minX = float(min(minX, point[0]))
            maxX = float(max(maxX, point[0]))
            minY = float(min(minY, point[1]))
            maxY = float(max(maxY, point[1]))
            minZ = float(min(minZ, point[2]))
            maxZ = float(max(maxZ, point[2]))
            
        # Getting XY ranges
        if pixel_distances:
            if match_xy:
                minZ = self.getXYScaledZ(minZ)
                maxZ = self.getXYScaledZ(maxZ)
        else:
            minX = minX * self.getDppXY()
            maxX = maxX * self.getDppXY()
            minY = minY * self.getDppXY()
            maxY = maxY * self.getDppXY()
            minZ = minZ * self.getDppZ()
            maxZ = maxZ * self.getDppZ()

        if self.is2D():
            minZ = 0
            maxZ = 0
                
        return [[minX, maxX],[minY, maxY],[minZ, maxZ]]
       
    def getAsImage(self, image_name: str, t: int, n_frames: int) -> Image:
        raise Exception('Volume: Implement getAsImage')

    def getAsTightImage(self, image_name: str) -> Image:
        border_widths: List[List[int]] = [[0,0],[0,0],[0,0]]
        return self.getAsTightImageWithBorders(image_name, border_widths)

    def getAsTightImageWithBorders(self, image_name: str, border_widths: List[List[int]]) -> Image:
        if border_widths is None:
            return self.getAsImage(image_name, 0, 1)
        
        extents: List[List[float]] = self.getExtents(True, False)
        x_offs: int = round(extents[0][0] - border_widths[0][0])
        y_offs: int = round(extents[1][0] - border_widths[1][0])
        z_offs: int = round(extents[2][0] - border_widths[2][0])
        
        width: int = round(extents[0][1]) - round(extents[0][0]) + border_widths[0][0] + border_widths[0][1] + 1
        height: int = round(extents[1][1]) - round(extents[1][0]) + border_widths[1][0] + border_widths[1][1] + 1
        n_slices: int = round(extents[2][1]) - round(extents[2][0]) + border_widths[2][0] + border_widths[2][1] + 1
        
        tight_im: Image = createImage(image_name, width=width, height=height, n_slices=n_slices, d_type=np.uint8, dpp_xy=self.getDppXY(), dpp_z=self.getDppZ(), spatial_units=self.getSpatialUnits())
        
        for point in self.getCoordinateSet():
            tight_im.putPixel(255, x=point[0] - x_offs, y=point[1] - y_offs, z=point[2]-z_offs)
        
        tight_im.showAsIs()
        
        return tight_im

    def getContainedVolume(self, pixel_distances: bool) -> float:
        if pixel_distances:
            return self.size() * self.getDppZ() / self.getDppXY()
        else:
            return self.size() * self.getDppXY() * self.getDppXY() * self.getDppZ()
        
    def getOverlap(self, volume2: Volume) -> int:
        raise Exception('Volume: Implement getOverlap')

    def getX(self, pixel_distances: bool): # To do
        raise Exception('Volume: Implement getX')

    def getY(self, pixel_distances: bool): # To do
        raise Exception('Volume: Implement getY')

    def getZ(self, pixel_distances: bool, match_xy: bool): # To do
        raise Exception('Volume: Implement getZ')

    def getSurfaceXCoords(self): # To do
        raise Exception('Volume: Implement getSurfaceXCoords')

    def getSurfaceYCoords(self): # To do
        raise Exception('Volume: Implement getSurfaceYCoords')

    def getSurfaceZCoords(self): # To do
        raise Exception('Volume: Implement getSurfaceZCoords')

    def getSurfaceX(self, pixel_distances: bool): # To do
        raise Exception('Volume: Implement getSurfaceX')

    def getSurfaceY(self, pixel_distances: bool): # To do
        raise Exception('Volume: Implement getSurfaceY')

    def getSurfaceZ(self, pixel_distances: bool, match_xy: bool): # To do
        raise Exception('Volume: Implement getSurfaceZ')

    def getXMean(self, pixel_distances: bool) -> float:
        raise Exception('Volume: Implement getXMean')

    def getYMean(self, pixel_distances: bool) -> float:
        raise Exception('Volume: Implement getYMean')

    def getZMean(self, pixel_distances: bool, match_xy: bool) -> float:
        raise Exception('Volume: Implement getZMean')

    def calculateBaseAreaPx(self) -> float:
        # Getting the lowest slice
        base_z: int = round(self.getExtents(True, False)[2][0])
        
        # Counting the number of pixels in this slice
        count: int = 0
        point: Point
        for point in self.getCoordinateSet():
            if point[2] == base_z:
                count = count + 1
        
        return count
    
    def getVolumeHeight(self, pixel_distances: bool, match_xy: bool) -> float:
        minZ: float = float('inf')
        maxZ: float = -float('inf')
        
        point: Point
        for point in self.getCoordinateSet():
            minZ = min(minZ, point[2])
            maxZ = max(maxZ, point[2])
            
        height: float = maxZ - minZ
        
        if pixel_distances:
            return self.getXYScaledZ(height) if match_xy else height
        
        return height * self.getDppZ()

    def hasVolume(self) -> bool:
        raise Exception('Volume: Implement hasVolume')

    def hasArea(self) -> bool:
        raise Exception('Volume: Implement hasArea')

    def calculateAngle2D(self, volume2: Volume) -> float:
        raise Exception('Volume: Implement calculateAngle2D')

    def calculateAngleToPoint2D(self, point) -> float: # To do
        raise Exception('Volume: Implement calculateAngleToPoint2D')

    def calculatePointPointSeparation(self, point1, point2, pixel_distances: bool) -> float: # To do
        raise Exception('Volume: Implement calculatePointPointSeparation')

    def getSurfaceSeparation(self, volume2, pixel_distances: bool, force2D: bool, ignore_edges_xy: bool, ignore_edges_z: bool) -> float: # To do
        raise Exception('Volume: Implement getSurfaceSeparation')

    def getPointSurfaceSeparation(self, point, pixel_distances: bool, force2D: bool, ignore_edges_xy: bool, ignore_edges_z: bool) -> float: # To do
        raise Exception('Volume: Implement getPointSurfaceSeparation')

    def getCentroidSeparation(self, volume2: Volume, pixel_distances: bool, force_2D: bool) -> float: # To do
        raise Exception('Volume: Implement getCentroidSeparation')

    def getOverlappingPoints(self, volume2: Volume) -> Volume:
        raise Exception('Volume: Implement getOverlappingPoints')

    def getSlice(self, slice: int) -> Volume:
        width: int = self.getWidth()
        height: int = self.getHeight()
        n_slices: int = self.getNSlices()
        dpp_xy: float = self.getDppXY()
        dpp_z: float = self.getDppZ()
        spatial_units: str = self.getSpatialUnits()
        
        slice_volume: Volume = Volume(self.getCoordinateSetFactory(), width, height, n_slices, dpp_xy, dpp_z, spatial_units)
        slice_volume.setCoordinateSet(self.getCoordinateSet().getSlice(slice))
        
        return slice_volume
    