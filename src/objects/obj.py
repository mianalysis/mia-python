from src.objects.volume import Volume

class Obj(Volume):
    # private LinkedHashMap<String, Obj> parents = new LinkedHashMap<>();
    # private LinkedHashMap<String, Objs> children = new LinkedHashMap<>();
    # private LinkedHashMap<String, Objs> partners = new LinkedHashMap<>();
    # private LinkedHashMap<String, Measurement> measurements = new LinkedHashMap<>();
    # private LinkedHashMap<String, ObjMetadata> metadata = new LinkedHashMap<>();
    # private HashMap<Integer, Roi> rois = new HashMap<>();
    
    def __init__(self, obj_collection, coordinate_set_factory, ID, spat_cal=None):        
        if spat_cal is None:
            spat_cal = obj_collection.getSpatialCalibration()
            
        super().__init__(coordinate_set_factory, spat_cal=spat_cal)
        
        self._ID = ID
        self._obj_collection = obj_collection
        self._T = 0

    def getObjectCollection(self):
        return self._obj_collection

    def setObjectCollection(self, obj_collection):
        self._obj_collection = obj_collection

    def getName(self):
        return self._obj_collection.getName()

    def getID(self):
        return self._ID

    def setID(self, ID):
        self._ID = ID
        
        return self

    def getT(self):
        return self._T

    def setT(self, T):
        self._T = T
        
        return self

    def getAllParents(self):
        print('ObjWrapper: Implement getAllParents')

    def setAllParents(self, parents):
        print('ObjWrapper: Implement setAllParents')

    def getAllChildren(self):
        print('ObjWrapper: Implement getAllChildren')

    def setAllChildren(self, children):
        print('ObjWrapper: Implement setAllChildren')

    def getAllPartners(self):
        print('ObjWrapper: Implement getAllPartners')

    def setAllPartners(self, partners):
        print('ObjWrapper: Implement setAllPartners')

    def removeRelationships(self):
        print('ObjWrapper: Implement removeRelationships')

    def getMeasurements(self):
        print('ObjWrapper: Implement getMeasurements')

    def setMeasurements(self, measurements):
        print('ObjWrapper: Implement setMeasurements')

    def getMetadata(self):
        print('ObjWrapper: Implement getMetadata')

    def setMetadata(self, metadata):
        print('ObjWrapper: Implement setMetadata')

    def getRoi(self, z_slice):
        print('ObjWrapper: Implement getRoi')

    def getRois(self):
        print('ObjWrapper: Implement getRois')

    def clearROIs(self):
        print('ObjWrapper: Implement clearROIs')

    def duplicate(self, newCollection, duplicateRelationships, duplicateMeasurements, duplicateMetadata):
        print('ObjWrapper: Implement duplicate')

    def equalsIgnoreNameAndID(self, obj):
        print('ObjWrapper: Implement equalsIgnoreNameAndID')

    def toString(self):
        return f"Object \"{self.getName()}\", ID = {self.getID()}, frame = {self.getT()}"
    
    # Obj default methods
    def addToImage(self, image, hue):
        print('ObjWrapper: Implement addToImage')
        