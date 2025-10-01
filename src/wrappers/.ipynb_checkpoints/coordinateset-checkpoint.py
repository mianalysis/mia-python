from jpype import JImplements, JOverride
from scyjava import jimport

from src.wrappers.volume import VolumeWrapper

@JImplements('io.github.mianalysis.mia.object.coordinates.volume.CoordinateSetI','io.github.mianalysis.mia.TestIter')
class CoordinateSetWrapper():
    def __init__(self):
        self._points = []

    @JOverride
    def getFactory(self):
        print('CoordinateSetWrapper: Implement getFactory')

    @JOverride
    def add(self, x, y, z):
        self.points.append((x,y,z))

    @JOverride
    def getNumberOfElements(self):
        print('CoordinateSetWrapper: Implement getNumberOfElements')

    @JOverride
    def createEmptyCoordinateSet(self):
        print('CoordinateSetWrapper: Implement createEmptyCoordinateSet')

    @JOverride
    def finalise(self):
        print('CoordinateSetWrapper: Implement finalise')

    @JOverride
    def finalise(self, z):
        print('CoordinateSetWrapper: Implement finalise')

    @JOverride
    def duplicate(self):
        print('CoordinateSetWrapper: Implement duplicate')
    
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
        print('CoordinateSetWrapper: Implement iterator')

    @JOverride
    def isEmpty(self):
        print('CoordinateSetWrapper: Implement isEmpty')

    @JOverride
    def toArray(self):
        print('CoordinateSetWrapper: Implement toArray')

    @JOverride
    def toArray(self, a):
        print('CoordinateSetWrapper: Implement toArray')

    @JOverride
    def contains(self, o):
        print('CoordinateSetWrapper: Implement contains')
        
    @JOverride
    def containsAll(self, c):
        print('CoordinateSetWrapper: Implement containsAll')
    
    @JOverride
    def add(self, point):
        print('CoordinateSetWrapper: Implement add')
        
    @JOverride
    def addAll(self, c):
        print('CoordinateSetWrapper: Implement addAll')

    @JOverride
    def retainAll(self, c):
        print('CoordinateSetWrapper: Implement retainAll')

    @JOverride
    def remove(self, o):
        print('CoordinateSetWrapper: Implement remove')
        
    @JOverride
    def removeAll(self, c):
        print('CoordinateSetWrapper: Implement removeAll')

    @JOverride
    def clear(self):
        print('CoordinateSetWrapper: Implement clear')
        
    @JOverride
    def contains(self, point):
        print('CoordinateSetWrapper: Implement contains')

    @JOverride
    def extend(self, point):
        print('CoordinateSetWrapper: Implement extend')
        
    @JOverride
    def equals(self, o):
        print('CoordinateSetWrapper: Implement equals')

    @JOverride
    def hashCode(self, o):
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

        