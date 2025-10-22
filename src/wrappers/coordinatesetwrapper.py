from jpype import JImplements, JOverride
from scyjava import jimport

from src.objects.coordinateset import CoordinateSet
from src.objects.coordinateset import CoordinateSetFactory

Point = jimport('io.github.mianalysis.mia.object.coordinates.Point')

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.CoordinateSetI')
class CoordinateSetWrapper():
    def __init__(self):
        self._coordinate_set: CoordinateSet = CoordinateSet()
        
    def getPythonCoordinateSet(self):
        return self._coordinate_set

    def getPythonPoints(self):
        return self._coordinate_set.getPoints()

    def getPythonPointAtIndex(self, idx):
        return self._coordinate_set.getPointAtIndex(idx)
        
    def getPointAtIndex(self, idx):
        point = self._coordinate_set.getPointAtIndex(idx)
        return Point(point[idx,0],point[idx,1],point[idx,2])

    @JOverride
    def getFactory(self):
        return CoordinateSetFactoryWrapper()

    @JOverride
    def addCoord(self, x, y, z):
        return self._coordinate_set.addCoord(x,y,z)

    @JOverride
    def getNumberOfElements(self):
        return self._coordinate_set.getNumberOfElements()

    @JOverride
    def createEmptyCoordinateSet(self):
        return self.getFactory().createCoordinateSet()

    @JOverride
    def finalise(self):
        self._coordinate_set.finalise()

    @JOverride
    def finaliseSlice(self, z):
        self._coordinate_set.finaliseSlice(z)

    @JOverride
    def duplicate(self):
        new_coordinate_set_wrapper = self.getFactory().createCoordinateSet()
        new_coordinate_set_wrapper._coordinate_set = self._coordinate_set.duplicate()

        return new_coordinate_set_wrapper        
    
    @JOverride
    def calculateProjected(self):
        raise Exception('CoordinateSetWrapper: Implement calculateProjected')
        
    @JOverride
    def getSlice(self, slice):
        raise Exception('CoordinateSetWrapper: Implement getSlice')


    # From Set
    
    @JOverride
    def size(self):
        return self._coordinate_set.size()

    @JOverride
    def iterator(self):
        return self._coordinate_set.iterator()

    @JOverride
    def isEmpty(self):
        raise Exception('CoordinateSetWrapper: Implement isEmpty')

    @JOverride
    def toArray(self, array=None):
        raise Exception('CoordinateSetWrapper: Implement toArray')

    @JOverride
    def contains(self, point):
        raise Exception('CoordinateSetWrapper: Implement contains')
        
    @JOverride
    def containsAll(self, points):
        raise Exception('CoordinateSetWrapper: Implement containsAll')
    
    @JOverride
    def add(self, point):
        raise Exception('CoordinateSetWrapper: Implement add')
        
    @JOverride
    def addAll(self, points):
        raise Exception('CoordinateSetWrapper: Implement addAll')

    @JOverride
    def retainAll(self, points):
        raise Exception('CoordinateSetWrapper: Implement retainAll')

    @JOverride
    def remove(self, point):
        raise Exception('CoordinateSetWrapper: Implement remove')
        
    @JOverride
    def removeAll(self, points):
        raise Exception('CoordinateSetWrapper: Implement removeAll')

    @JOverride
    def clear(self):
        raise Exception('CoordinateSetWrapper: Implement clear')
        
    @JOverride
    def equals(self, point):
        raise Exception('CoordinateSetWrapper: Implement equals')

    @JOverride
    def hashCode(self, point):
        raise Exception('CoordinateSetWrapper: Implement hashCode')

    @JOverride
    def spliterator(self):
        raise Exception('CoordinateSetWrapper: Implement spliterator')


@JImplements('io.github.mianalysis.mia.object.coordinates.volume.CoordinateSetFactoryI')
class CoordinateSetFactoryWrapper:
    
    def __init__(self):
        self._coordinate_set_factory = CoordinateSetFactory()
        
    def getPythonCoordinateSetFactory(self):
        return self._coordinate_set_factory
    
    @JOverride
    def getName(self):
        return "Python coordinate set factory"
    
    @JOverride
    def createCoordinateSet(self):
        return CoordinateSetWrapper()

    @JOverride
    def duplicate(self):
        return CoordinateSetFactoryWrapper()
        