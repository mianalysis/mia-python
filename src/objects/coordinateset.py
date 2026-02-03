from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.types.types import Point, Points

import numpy as np

class CoordinateSet():
    def __init__(self):
        self._points: Points = np.empty((0,3)).astype(int)
        self._chunk_size: int = 10000
        self._chunks: list[np.ndarray] = []
        self._current_chunk: Points = np.empty((self._chunk_size, 3), dtype=int)
        self._count: int = 0
        
    def __iter__(self):
        return CoordinateSetIterator(self)
    
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

    def finaliseSlice(self, z: int):
        self._points = np.vstack(self._chunks + [self._current_chunk[:self._count]])

    def duplicate(self) -> CoordinateSet:
        new_points: CoordinateSet = CoordinateSet()

        point: Point
        for point in self._points:
            new_points.add(point)

        return new_points        
    
    def calculateProjected(self):
        raise Exception('CoordinateSet: Implement calculateProjected')
        
    def getSlice(self, slice: int):
        slice_coordinate_set: CoordinateSet = CoordinateSet()
        
        for point in self:
            if point[2] == slice:
                slice_coordinate_set.add(point)
                
        slice_coordinate_set.finalise()
        
        return slice_coordinate_set

    # From Set
    
    def size(self) -> int:
        return len(self._points)

    def iterator(self) -> CoordinateSetIterator:
        return CoordinateSetIterator(self)

    def isEmpty(self) -> bool:
        raise Exception('CoordinateSet: Implement isEmpty')
        
    def toArray(self, array=None): # To do
        raise Exception('CoordinateSet: Implement toArray')

    def contains(self, point: Point) -> bool:
        raise Exception('CoordinateSet: Implement contains')
        
    def containsAll(self, points: Points) -> bool:
        raise Exception('CoordinateSet: Implement containsAll')
    
    def add(self, point: Point) -> bool:
        return self.addCoord(point[0], point[1], point[2])
        
    def addAll(self, points: Points) -> bool:
        raise Exception('CoordinateSet: Implement addAll')

    def retainAll(self, points: Points) -> bool:
        raise Exception('CoordinateSet: Implement retainAll')

    def remove(self, point: Point) -> bool:
        raise Exception('CoordinateSet: Implement remove')
        
    def removeAll(self, points: Points) -> bool:
        raise Exception('CoordinateSet: Implement removeAll')

    def clear(self): # No return
        raise Exception('CoordinateSet: Implement clear')
        
    def equals(self, point: Point) -> bool:
        raise Exception('CoordinateSet: Implement equals')

    def hashCode(self, point: Point) -> int:
        raise Exception('CoordinateSet: Implement hashCode')

    def spliterator(self): # To do
        raise Exception('CoordinateSet: Implement spliterator')


class CoordinateSetIterator:
    def __init__(self, coordinate_set: CoordinateSet):
        self._next_idx: int = 0
        self._coordinate_set: CoordinateSet = coordinate_set

    # def hasNext(self) -> bool:
    #     return self._next_idx < self._coordinate_set.size()
        
    def __next__(self) -> Point:
        if self._next_idx == self._coordinate_set.size():
            raise StopIteration
            
        point: Point = self._coordinate_set.getPointAtIndex(self._next_idx)
        self._next_idx = self._next_idx + 1
        
        return point        

    # def remove(self) -> Point | None:
    #     # Check the iterator has returned a value (i.e. next_idx>0)
    #     if self._next_idx == 0:
    #         return None

    #     return self._coordinate_set.getPointAtIndex(self._next_idx-1)
        
    # def forEachRemaining(self, action): # To do
    #     raise Exception('CoordinateSetIterator: Implement forEachRemaining')
        

class CoordinateSetFactory:
    def getName(self) -> str:
        return "Coordinate set factory"
    
    def createCoordinateSet(self) -> CoordinateSet:
        return CoordinateSet()

    def duplicate(self) -> CoordinateSetFactory:
        return CoordinateSetFactory()
        