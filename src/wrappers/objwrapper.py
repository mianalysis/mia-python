from jpype import JImplements, JOverride
from scyjava import jimport

from src.objects.obj import Obj
from src.wrappers.volumewrapper import VolumeWrapper

Obj = jimport('io.github.mianalysis.mia.object.coordinates.ObjI')
ObjAdaptor = jimport('io.github.mianalysis.mia.python.ObjAdaptor')
VolumeAdaptor = jimport('io.github.mianalysis.mia.python.VolumeAdaptor')

@JImplements('io.github.mianalysis.mia.object.coordinates.ObjI')
class ObjWrapper(VolumeWrapper):
    
    def __init__(self, obj_collection, coordinate_set_factory_wrapper, ID, spat_cal=None):
        self._obj = Obj(obj_collection, coordinate_set_factory_wrapper.getPythonCoordinateSetFactory(), ID, spat_cal)

    def getPythonObj(self):
        return self._obj
    
    @JOverride
    def getFactory(self):
        return ObjFactoryWrapper()
    
    @JOverride
    def getObjectCollection(self):
        self._obj.getObjectCollection()

    @JOverride
    def setObjectCollection(self, obj_collection):
        self._obj.setObjectCollection(obj_collection)

    @JOverride
    def getName(self):
        return self._obj.getName()

    @JOverride
    def getID(self):
        return self._obj.getID()

    @JOverride
    def setID(self, ID):
        return self._obj.setID(ID)

    @JOverride
    def getT(self):
        return self._obj.getT()

    @JOverride
    def setT(self, T):
        return self._obj.setT(T)

    @JOverride
    def getAllParents(self):
        raise Exception('ObjWrapper: Implement getAllParents')

    @JOverride
    def setAllParents(self, parents):
        raise Exception('ObjWrapper: Implement setAllParents')

    @JOverride
    def getAllChildren(self):
        raise Exception('ObjWrapper: Implement getAllChildren')

    @JOverride
    def setAllChildren(self, children):
        raise Exception('ObjWrapper: Implement setAllChildren')

    @JOverride
    def getAllPartners(self):
        raise Exception('ObjWrapper: Implement getAllPartners')

    @JOverride
    def setAllPartners(self, partners):
        raise Exception('ObjWrapper: Implement setAllPartners')

    @JOverride
    def removeRelationships(self):
        raise Exception('ObjWrapper: Implement removeRelationships')

    @JOverride
    def getMeasurements(self):
        raise Exception('ObjWrapper: Implement getMeasurements')

    @JOverride
    def setMeasurements(self, measurements):
        raise Exception('ObjWrapper: Implement setMeasurements')

    @JOverride
    def getMetadata(self):
        raise Exception('ObjWrapper: Implement getMetadata')

    @JOverride
    def setMetadata(self, metadata):
        raise Exception('ObjWrapper: Implement setMetadata')

    @JOverride
    def getRoi(self, z_slice):
        raise Exception('ObjWrapper: Implement getRoi')

    @JOverride
    def getRois(self):
        raise Exception('ObjWrapper: Implement getRois')

    @JOverride
    def clearROIs(self):
        raise Exception('ObjWrapper: Implement clearROIs')

    @JOverride
    def duplicate(self, newCollection, duplicateRelationships, duplicateMeasurements, duplicateMetadata):
        raise Exception('ObjWrapper: Implement duplicate')

    @JOverride
    def equalsIgnoreNameAndID(self, obj):
        raise Exception('ObjWrapper: Implement equalsIgnoreNameAndID')

    @JOverride
    def toString(self):
        return self._obj.toString()


    ## Inherited from VolumeWrapper

    @JOverride
    def getCoordinateSetFactory(self):
        return self._obj.getCoordinateSetFactory()

    @JOverride
    def getSurface(self, ignoreEdgesXY, ignoreEdgesZ):
        return self._obj.getSurface(ignoreEdgesXY, ignoreEdgesZ)

    @JOverride
    def hasCalculatedSurface(self):
        return self._obj.hasCalculatedSurface()

    @JOverride
    def getProjected(self):
        return self._obj.getProjected()

    @JOverride
    def hasCalculatedProjection(self):
        return self._obj.hasCalculatedProjection()

    @JOverride
    def getMeanCentroid(self, pixelDistances, matchXY):
        return self._obj.getMeanCentroid(pixelDistances, matchXY)

    @JOverride
    def hasCalculatedCentroid(self):
        return self._obj.hasCalculatedCentroid()

    @JOverride
    def clearAllCoordinates(self):
        self._obj.clearAllCoordinates()

    @JOverride
    def clearSurface(self):
        self._obj.clearSurface()

    @JOverride
    def clearPoints(self):
        self._obj.clearPoints()

    @JOverride
    def clearProjected(self):
        self._obj.clearProjected()

    @JOverride
    def clearCentroid(self):
        self._obj.clearCentroid()

    @JOverride
    def hashCode(self):
        self._obj.hashCode()

    @JOverride
    def equals(self, obj):
        self._obj.equals(obj)

    @JOverride
    def getSpatialCalibration(self):
        return self._obj.getSpatialCalibration()

    @JOverride
    def setSpatialCalibration(self, spat_cal):
        self._obj.setSpatialCalibration(spat_cal)

    @JOverride
    def getCoordinateSet(self):
        return self._obj.getCoordinateSet()

    @JOverride
    def setCoordinateSet(self, coordinate_set):
        self._obj.setCoordinateSet(coordinate_set)

    @JOverride
    def createNewVolume(self, factory, spat_cal):
        return self._obj.createNewVolume(factory, spat_cal)

    @JOverride
    def getCalibratedIterator(self, pixelDistances, matchXY):
        return self._obj.getCalibratedIterator(pixelDistances, matchXY)
    
    # Obj default methods
    def addToImage(self, image, hue):
        self._obj.addToImage(image, hue)


@JImplements('io.github.mianalysis.mia.object.coordinates.ObjFactoryI')
class ObjFactoryWrapper:
    
    @JOverride
    def getName(self):
        return "Python object factory"
    
    @JOverride
    def createObj(self, obj_collection, factory, ID, spat_cal=None):
        return ObjWrapper(obj_collection, factory, ID, spat_cal)

    @JOverride
    def duplicate(self):
        return ObjFactoryWrapper()