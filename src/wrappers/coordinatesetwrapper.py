from __future__ import annotations
from jpype import JImplements, JOverride
from scyjava import jimport
from typing import TYPE_CHECKING

from src.objects.coordinateset import CoordinateSet, CoordinateSetIterator
from src.objects.coordinateset import CoordinateSetFactory

if TYPE_CHECKING:
    from types.JPointType import JPointType

from src.utilities.types import Point, Points    

JPoint = jimport('io.github.mianalysis.mia.object.coordinates.Point')

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.CoordinateSetI')
class CoordinateSetWrapper():
    def __init__(self):
        self._coordinate_set: CoordinateSet = CoordinateSet()
        
    def getPythonCoordinateSet(self) -> CoordinateSet:
        return self._coordinate_set

    def getPythonPoints(self) -> Points:
        return self._coordinate_set.getPoints()

    def getPythonPointAtIndex(self, idx:int) -> Point:
        return self._coordinate_set.getPointAtIndex(idx)
        
    def getPointAtIndex(self, idx: int) -> JPointType[int]:
        point: Point = self._coordinate_set.getPointAtIndex(idx)
        return JPoint[int](point[idx,0],point[idx,1],point[idx,2])

    @JOverride
    def getFactory(self) -> CoordinateSetFactoryWrapper:
        return CoordinateSetFactoryWrapper()

    @JOverride
    def addCoord(self, x: int, y: int, z: int) -> bool:
        return self._coordinate_set.addCoord(x,y,z)

    @JOverride
    def getNumberOfElements(self) -> int:
        return self._coordinate_set.getNumberOfElements()

    @JOverride
    def createEmptyCoordinateSet(self) -> CoordinateSetWrapper:
        return self.getFactory().createCoordinateSet()

    @JOverride
    def finalise(self): # No return
        self._coordinate_set.finalise()

    @JOverride
    def finaliseSlice(self, z: int): # No return
        self._coordinate_set.finaliseSlice(z)

    @JOverride
    def duplicate(self) -> CoordinateSetWrapper:
        new_coordinate_set_wrapper: CoordinateSetWrapper = self.getFactory().createCoordinateSet()
        
        point: Point
        for point in self._coordinate_set.getPoints():
            new_coordinate_set_wrapper.addCoord(point[0], point[1], point[2])

        return new_coordinate_set_wrapper        
    
    @JOverride
    def calculateProjected(self) -> CoordinateSetWrapper:
        raise Exception('CoordinateSetWrapper: Implement calculateProjected')
        
    @JOverride
    def getSlice(self, slice: int) -> CoordinateSetWrapper:
        raise Exception('CoordinateSetWrapper: Implement getSlice')


    # From Set
    
    @JOverride
    def size(self) -> int:
        return self._coordinate_set.size()

    @JOverride
    def iterator(self) -> CoordinateSetIterator:
        return self._coordinate_set.iterator()

    @JOverride
    def isEmpty(self) -> bool:
        return self._coordinate_set.isEmpty()

    @JOverride
    def toArray(self, array=None): # To do
        return self._coordinate_set.toArray(array)

    @JOverride
    def contains(self, point: Point) -> bool:
        return self._coordinate_set.contains(point)
        
    @JOverride
    def containsAll(self, points: Points) -> bool:
        return self._coordinate_set.containsAll(points)
    
    @JOverride
    def add(self, point: Point) -> bool:
        return self._coordinate_set.add(point)
        
    @JOverride
    def addAll(self, points: Points) -> bool:
        return self._coordinate_set.addAll(points)

    @JOverride
    def retainAll(self, points: Points) -> bool:
        return self._coordinate_set.retainAll(points)

    @JOverride
    def remove(self, point: Point) -> bool:
        return self._coordinate_set.remove(point)
        
    @JOverride
    def removeAll(self, points: Points) -> bool:
        return self._coordinate_set.removeAll(points)

    @JOverride
    def clear(self): # No return
        return self._coordinate_set.clear()
        
    @JOverride
    def equals(self, point: Point) -> bool:
        return self._coordinate_set.equals(point)

    @JOverride
    def hashCode(self, point: Point) -> int:
        return self._coordinate_set.hashCode(point)

    @JOverride
    def spliterator(self): # To do
        raise Exception('CoordinateSetWrapper: Implement spliterator')


@JImplements('io.github.mianalysis.mia.object.coordinates.volume.CoordinateSetFactoryI')
class CoordinateSetFactoryWrapper():
    
    def __init__(self):
        self._coordinate_set_factory: CoordinateSetFactory = CoordinateSetFactory()
        
    def getPythonCoordinateSetFactory(self) -> CoordinateSetFactory:
        return self._coordinate_set_factory
    
    @JOverride
    def getName(self) -> str:
        return "Python coordinate set factory"
    
    @JOverride
    def createCoordinateSet(self) -> CoordinateSetWrapper:
        return CoordinateSetWrapper()

    @JOverride
    def duplicate(self) -> CoordinateSetFactoryWrapper:
        return CoordinateSetFactoryWrapper()
        