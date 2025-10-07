from jpype import JImplements, JOverride
from scyjava import jimport

from src.wrappers.volume import VolumeWrapper

Point = jimport('io.github.mianalysis.mia.object.coordinates.Point')

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.CoordinateSetI')
class CoordinateSetWrapper():
    def __init__(self):
        self._points = []

    def getPythonPoints(self):
        return self._points

    def getPythonPointAtIndex(self, idx):
        point = self._points[idx]
        return 
        
    def getPointAtIndex(self, idx):
        point = self._points[idx]
        return Point(point[0],point[1],point[2])

    @JOverride
    def getFactory(self):
        return PythonCoordinateSetFactory()

    @JOverride
    def addCoord(self, x, y, z):
        self._points.append((x,y,z))
        
        return True

    @JOverride
    def getNumberOfElements(self):
        return self.size()

    @JOverride
    def createEmptyCoordinateSet(self):
        return getFactory().createCoordinateSet()

    @JOverride
    def finalise(self):
        pass

    @JOverride
    def finaliseSlice(self, z):
        pass

    @JOverride
    def duplicate(self):
        new_points = getFactory().createCoordinateSet()

        for point in self._points:
            new_points.append(point)

        return new_points        
    
    @JOverride
    def calculateProjected(self):
        print('CoordinateSetWrapper: Implement calculateProjected')
        
    @JOverride
    def getSlice(self, slice):
        print('CoordinateSetWrapper: Implement getSlice')


    # From Set
    
    @JOverride
    def size(self):
        return len(self._points)

    @JOverride
    def iterator(self):
        return PythonCoordinateSetIterator(self)

    @JOverride
    def isEmpty(self):
        print('CoordinateSetWrapper: Implement isEmpty')

    @JOverride
    def toArray(self, array=None):
        print('CoordinateSetWrapper: Implement toArray')

    @JOverride
    def contains(self, point):
        print('CoordinateSetWrapper: Implement contains')
        
    @JOverride
    def containsAll(self, points):
        print('CoordinateSetWrapper: Implement containsAll')
    
    @JOverride
    def add(self, point):
        print('CoordinateSetWrapper: Implement add')
        
    @JOverride
    def addAll(self, points):
        print('CoordinateSetWrapper: Implement addAll')

    @JOverride
    def retainAll(self, points):
        print('CoordinateSetWrapper: Implement retainAll')

    @JOverride
    def remove(self, point):
        print('CoordinateSetWrapper: Implement remove')
        
    @JOverride
    def removeAll(self, points):
        print('CoordinateSetWrapper: Implement removeAll')

    @JOverride
    def clear(self):
        print('CoordinateSetWrapper: Implement clear')

    @JOverride
    def extend(self, point):
        print('CoordinateSetWrapper: Implement extend')
        
    @JOverride
    def equals(self, point):
        print('CoordinateSetWrapper: Implement equals')

    @JOverride
    def hashCode(self, point):
        print('CoordinateSetWrapper: Implement hashCode')

    @JOverride
    def spliterator(self):
        print('CoordinateSetWrapper: Implement spliterator')


@JImplements('io.github.mianalysis.mia.object.coordinates.volume.CoordinateSetFactoryI')
class PythonCoordinateSetFactory:
    
    @JOverride
    def getName(self):
        return "Python coordinate set factory"
    
    @JOverride
    def createCoordinateSet(self):
        return CoordinateSetWrapper()

    @JOverride
    def duplicate(self):
        return PythonCoordinateSetFactory()

@JImplements('java.util.Iterator')
class PythonCoordinateSetIterator:
    def __init__(self, coordinate_set):
        self._next_idx = 0
        self._coordinate_set = coordinate_set

    @JOverride
    def hasNext(self):
        return self._next_idx < self._coordinate_set.size()
        
    @JOverride
    def next(self):
        if self._next_idx == self._coordinate_set.size():
            print('No such element: the coordinate set has no more elements')
            return None
            
        point = self._coordinate_set.getPointAtIndex(self._next_idx)
        self._next_idx = self._next_idx + 1
        
        return point        

    @JOverride
    def remove(self, point):
        # Check the iterator has returned a value (i.e. next_idx>0)
        if self._next_idx == 0:
            return

        return self._coordinate_set.getPointAtIndex(self._next_idx-1)
        
    @JOverride
    def forEachRemaining(self, action):
        print('PythonCoordinateSetIterator: Implement forEachRemaining')
        