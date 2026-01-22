from jpype import JImplements, JOverride
from scyjava import jimport

from src.wrappers.volume import VolumeWrapper

Obj = jimport('io.github.mianalysis.mia.object.coordinates.ObjI')
ObjAdaptor = jimport('io.github.mianalysis.mia.python.ObjAdaptor')
VolumeAdaptor = jimport('io.github.mianalysis.mia.python.VolumeAdaptor')

@JImplements('io.github.mianalysis.mia.object.coordinates.ObjI')
class PythonObjWrapper(VolumeWrapper):
    # private LinkedHashMap<String, Obj> parents = new LinkedHashMap<>();
    # private LinkedHashMap<String, Objs> children = new LinkedHashMap<>();
    # private LinkedHashMap<String, Objs> partners = new LinkedHashMap<>();
    # private LinkedHashMap<String, Measurement> measurements = new LinkedHashMap<>();
    # private LinkedHashMap<String, ObjMetadata> metadata = new LinkedHashMap<>();
    # private HashMap<Integer, Roi> rois = new HashMap<>();
    
    def __init__(self, obj_collection, coordinate_set_factory, ID, spat_cal=None):
        if spat_cal is None:
            spat_cal = obj_collection.getSpatialCalibration()
            
        VolumeWrapper.__init__(self, coordinate_set_factory, spat_cal=spat_cal)
        self._ID = ID
        self._obj_collection = obj_collection
        self._T = 0

    @JOverride
    def getObjectCollection(self):
        return self._obj_collection

    @JOverride
    def setObjectCollection(self, obj_collection):
        self._obj_collection = obj_collection

    @JOverride
    def getName(self):
        return self._obj_collection.getName()

    @JOverride
    def getID(self):
        return self._ID

    @JOverride
    def setID(self, ID):
        self._ID = ID
        
        return self

    @JOverride
    def getT(self):
        return self._T

    @JOverride
    def setT(self, T):
        self._T = T
        
        return self

    @JOverride
    def getAllParents(self):
        print('ObjWrapper: Implement getAllParents')

    @JOverride
    def setAllParents(self, parents):
        print('ObjWrapper: Implement setAllParents')

    @JOverride
    def getAllChildren(self):
        print('ObjWrapper: Implement getAllChildren')

    @JOverride
    def setAllChildren(self, children):
        print('ObjWrapper: Implement setAllChildren')

    @JOverride
    def getAllPartners(self):
        print('ObjWrapper: Implement getAllPartners')

    @JOverride
    def setAllPartners(self, partners):
        print('ObjWrapper: Implement setAllPartners')

    @JOverride
    def removeRelationships(self):
        print('ObjWrapper: Implement removeRelationships')

    @JOverride
    def getMeasurements(self):
        print('ObjWrapper: Implement getMeasurements')

    @JOverride
    def setMeasurements(self, measurements):
        print('ObjWrapper: Implement setMeasurements')

    @JOverride
    def getMetadata(self):
        print('ObjWrapper: Implement getMetadata')

    @JOverride
    def setMetadata(self, metadata):
        print('ObjWrapper: Implement setMetadata')

    @JOverride
    def getRoi(self, z_slice):
        print('ObjWrapper: Implement getRoi')

    @JOverride
    def getRois(self):
        print('ObjWrapper: Implement getRois')

    @JOverride
    def clearROIs(self):
        print('ObjWrapper: Implement clearROIs')

    @JOverride
    def clearAllCoordinates(self):
        print('ObjWrapper: Implement clearAllCoordinates')

    @JOverride
    def duplicate(self, newCollection, duplicateRelationships, duplicateMeasurements, duplicateMetadata):
        print('ObjWrapper: Implement duplicate')

    @JOverride
    def hashCode(self):
        print('ObjWrapper: Implement hashCode')

    @JOverride
    def equals(self, obj):
        print('ObjWrapper: Implement equals')

    @JOverride
    def equalsIgnoreNameAndID(self, obj):
        print('ObjWrapper: Implement equalsIgnoreNameAndID')

    @JOverride
    def toString(self):
        return f"Object \"{self.getName()}\", ID = {self.getID()}, frame = {self.getT()}"


    ## Inherited from VolumeWrapper

    @JOverride
    def getFactory(self):
        return super().getFactory()

    @JOverride
    def getCoordinateSetFactory(self):
        return super().getCoordinateSetFactory()

    @JOverride
    def getSurface(self, ignoreEdgesXY, ignoreEdgesZ):
        return super().getSurface(ignoreEdgesXY, ignoreEdgesZ)

    @JOverride
    def hasCalculatedSurface(self):
        return super().hasCalculatedSurface()

    @JOverride
    def getProjected(self):
        return super().getProjected()

    @JOverride
    def hasCalculatedProjection(self):
        return super().hasCalculatedProjection()

    @JOverride
    def getMeanCentroid(self, pixelDistances, matchXY):
        return super().getMeanCentroid(pixelDistances, matchXY)

    @JOverride
    def hasCalculatedCentroid(self):
        return super().hasCalculatedCentroid()

    @JOverride
    def clearAllCoordinates(self):
        super().clearAllCoordinates()

    @JOverride
    def clearSurface(self):
        super().clearSurface()

    @JOverride
    def clearPoints(self):
        super().clearPoints()

    @JOverride
    def clearProjected(self):
        super().clearProjected()

    @JOverride
    def clearCentroid(self):
        super().clearCentroid()

    @JOverride
    def hashCode(self):
        super().hashCode()

    @JOverride
    def equals(self, obj):
        super().equals(obj)

    @JOverride
    def getSpatialCalibration(self):
        return super().getSpatialCalibration()

    @JOverride
    def setSpatialCalibration(self, spat_cal):
        super().setSpatialCalibration(spat_cal)

    @JOverride
    def getCoordinateSet(self):
        return super().getCoordinateSet()

    @JOverride
    def setCoordinateSet(self, coordinateSet):
        super().setCoordinateSet(coordinateSet)

    @JOverride
    def createNewVolume(self, factory, spatCal):
        return super().createNewVolume()

    @JOverride
    def getCalibratedIterator(self, pixelDistances, matchXY):
        return super().getCalibratedIterator(pixelDistances, matchXY)

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
    
    # Obj default methods
    def addToImage(self, image, hue):
        ObjAdaptor.addToImage(self, image, hue)


@JImplements('io.github.mianalysis.mia.object.coordinates.ObjFactoryI')
class PythonObjFactory:
    
    @JOverride
    def getName(self):
        return "Python object factory"
    
    @JOverride
    def createObj(self, obj_collection, factory, ID, spat_cal=None):
        return ObjWrapper(obj_collection, factory, ID, spat_cal)

    @JOverride
    def duplicate(self):
        return PythonObjFactory()