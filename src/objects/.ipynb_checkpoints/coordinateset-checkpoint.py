import numpy as np

class CoordinateSet():
    def __init__(self):
        self._points = []
        self._chunk_size = 10000
        self._chunks = []
        self._current_chunk = np.empty((self._chunk_size, 3), dtype=np.int32)
        self._count = 0

    def getPoints(self):
        return self._points

    def getPointAtIndex(self, idx):
        return self._points[idx]

    def addCoord(self, x, y, z):
        if self._count == len(self._current_chunk):
            self._chunks.append(self._current_chunk)
            self._current_chunk = np.empty((self._chunk_size, 3), dtype=np.int32)
            self._count = 0
        self._current_chunk[self._count] = [x, y, z]
        self._count += 1
        
        return True

    def getNumberOfElements(self):
        return self.size()

    def createEmptyCoordinateSet(self):
        return CoordinateSet()

    def finalise(self):
        self._points = np.vstack(self._chunks + [self._current_chunk[:self._count]])
        pass

    def finaliseSlice(self, z):
        pass

    def duplicate(self):
        new_points = CoordinateSet()

        for point in self._points:
            new_points.append(point)

        return new_points        
    
    def calculateProjected(self):
        print('CoordinateSetWrapper: Implement calculateProjected')
        
    def getSlice(self, slice):
        print('CoordinateSetWrapper: Implement getSlice')


    # From Set
    
    def size(self):
        return len(self._points)

    def iterator(self):
        return CoordinateSetIterator(self)

    def isEmpty(self):
        print('CoordinateSetWrapper: Implement isEmpty')

    def toArray(self, array=None):
        print('CoordinateSetWrapper: Implement toArray')

    def contains(self, point):
        print('CoordinateSetWrapper: Implement contains')
        
    def containsAll(self, points):
        print('CoordinateSetWrapper: Implement containsAll')
    
    def add(self, point):
        print('CoordinateSetWrapper: Implement add')
        
    def addAll(self, points):
        print('CoordinateSetWrapper: Implement addAll')

    def retainAll(self, points):
        print('CoordinateSetWrapper: Implement retainAll')

    def remove(self, point):
        print('CoordinateSetWrapper: Implement remove')
        
    def removeAll(self, points):
        print('CoordinateSetWrapper: Implement removeAll')

    def clear(self):
        print('CoordinateSetWrapper: Implement clear')

    def extend(self, point):
        print('CoordinateSetWrapper: Implement extend')
        
    def equals(self, point):
        print('CoordinateSetWrapper: Implement equals')

    def hashCode(self, point):
        print('CoordinateSetWrapper: Implement hashCode')

    def spliterator(self):
        print('CoordinateSetWrapper: Implement spliterator')


class CoordinateSetIterator:
    def __init__(self, coordinate_set):
        self._next_idx = 0
        self._coordinate_set = coordinate_set

    def hasNext(self):
        return self._next_idx < self._coordinate_set.size()
        
    def next(self):
        if self._next_idx == self._coordinate_set.size():
            print('No such element: the coordinate set has no more elements')
            return None
            
        point = self._coordinate_set.getPointAtIndex(self._next_idx)
        self._next_idx = self._next_idx + 1
        
        return point        

    def remove(self, point):
        # Check the iterator has returned a value (i.e. next_idx>0)
        if self._next_idx == 0:
            return

        return self._coordinate_set.getPointAtIndex(self._next_idx-1)
        
    def forEachRemaining(self, action):
        print('CoordinateSetIterator: Implement forEachRemaining')
        