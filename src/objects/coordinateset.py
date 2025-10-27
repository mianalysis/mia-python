from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.utilities.types import Point, Points

import numpy as np

class CoordinateSet():
    def __init__(self):
        self._points: Points = np.empty((0,3)).astype(int)
        self._chunk_size: int = 10000
        self._chunks: list[np.ndarray] = []
        self._current_chunk: Points = np.empty((self._chunk_size, 3), dtype=int)
        self._count: int = 0

    def getPoints(self) -> Points:
        return self._points

    def getPointAtIndex(self, idx: int) -> Point:
        return self._points[idx]

    def addCoord(self, x: int, y: int, z: int) -> bool:        
        if self._count == len(self._current_chunk):
            self._chunks.append(self._current_chunk)
            self._current_chunk = np.empty((self._chunk_size, 3), dtype=int)
            self._count = 0
        self._current_chunk[self._count] = [x, y, z]
        self._count += 1
        
        return True

    def getNumberOfElements(self) -> int:
        return self.size()

    def createEmptyCoordinateSet(self) -> CoordinateSet:
        return CoordinateSet()

    def finalise(self):
        self._points = np.vstack(self._chunks + [self._current_chunk[:self._count]])
        pass

    def finaliseSlice(self, z: int):
        pass

    def duplicate(self) -> CoordinateSet:
        new_points: CoordinateSet = CoordinateSet()

        point: Point
        for point in self._points:
            new_points.add(point)

        return new_points        
    
    def calculateProjected(self):
        raise Exception('CoordinateSetWrapper: Implement calculateProjected')
        
    def getSlice(self, slice):
        raise Exception('CoordinateSetWrapper: Implement getSlice')


    # From Set
    
    def size(self) -> int:
        return len(self._points)

    def iterator(self) -> CoordinateSetIterator:
        return CoordinateSetIterator(self)

    def isEmpty(self) -> bool:
        raise Exception('CoordinateSetWrapper: Implement isEmpty')
        
    def toArray(self, array=None): # To do
        raise Exception('CoordinateSetWrapper: Implement toArray')

    def contains(self, point: Point) -> bool:
        raise Exception('CoordinateSetWrapper: Implement contains')
        
    def containsAll(self, points: Points) -> bool:
        raise Exception('CoordinateSetWrapper: Implement containsAll')
    
    def add(self, point: Point) -> bool:
        raise Exception('CoordinateSetWrapper: Implement add')
        
    def addAll(self, points: Points) -> bool:
        raise Exception('CoordinateSetWrapper: Implement addAll')

    def retainAll(self, points: Points) -> bool:
        raise Exception('CoordinateSetWrapper: Implement retainAll')

    def remove(self, point: Point) -> bool:
        raise Exception('CoordinateSetWrapper: Implement remove')
        
    def removeAll(self, points: Points) -> bool:
        raise Exception('CoordinateSetWrapper: Implement removeAll')

    def clear(self): # No return
        raise Exception('CoordinateSetWrapper: Implement clear')
        
    def equals(self, point: Point) -> bool:
        raise Exception('CoordinateSetWrapper: Implement equals')

    def hashCode(self, point: Point) -> int:
        raise Exception('CoordinateSetWrapper: Implement hashCode')

    def spliterator(self): # To do
        raise Exception('CoordinateSetWrapper: Implement spliterator')


class CoordinateSetIterator:
    def __init__(self, coordinate_set: CoordinateSet):
        self._next_idx: int = 0
        self._coordinate_set: CoordinateSet = coordinate_set

    def hasNext(self) -> bool:
        return self._next_idx < self._coordinate_set.size()
        
    def next(self) -> Point | None:
        if self._next_idx == self._coordinate_set.size():
            print('No such element: the coordinate set has no more elements')
            return None
            
        point: Point = self._coordinate_set.getPointAtIndex(self._next_idx)
        self._next_idx = self._next_idx + 1
        
        return point        

    def remove(self) -> Point | None:
        # Check the iterator has returned a value (i.e. next_idx>0)
        if self._next_idx == 0:
            return None

        return self._coordinate_set.getPointAtIndex(self._next_idx-1)
        
    def forEachRemaining(self, action):
        raise Exception('CoordinateSetIterator: Implement forEachRemaining')
        

class CoordinateSetFactory:
    def getName(self) -> str:
        return "Coordinate set factory"
    
    def createCoordinateSet(self) -> CoordinateSet:
        return CoordinateSet()

    def duplicate(self) -> CoordinateSetFactory:
        return CoordinateSetFactory()
        