from jpype import JImplements, JOverride
from src.objects.objs import Objs

@JImplements('io.github.mianalysis.mia.object.ObjsI')
class ObjsWrapper():      
    def __init__(self):
        self._objs = Objs()
        
    @JOverride
    def createAndAddNewObject(self, factory):
        raise Exception('ObjsWrapper: Implement createAndAddNewObject')
    
    @JOverride
    def createAndAddNewObjectWithID(self, factory, ID):
        raise Exception('ObjsWrapper: Implement createAndAddNewObjectWithID')
        
    @JOverride
    def getName(self):
        raise Exception('ObjsWrapper: Implement getName')
    
    @JOverride
    def add(self, object):
        raise Exception('ObjsWrapper: Implement add')
    
    @JOverride
    def getSpatialCalibration(self):
        raise Exception('ObjsWrapper: Implement getSpatialCalibration')
    
    @JOverride
    def setSpatialCalibration(self, spatCal, updateAllObjects):
        raise Exception('ObjsWrapper: Implement setSpatialCalibration')
    
    @JOverride
    def getAndIncrementID(self):
        raise Exception('ObjsWrapper: Implement getAndIncrementID')
    
    @JOverride
    def resetCollection(self):
        raise Exception('ObjsWrapper: Implement resetCollection')
    
    @JOverride
    def recalculateMaxID(self):
        raise Exception('ObjsWrapper: Implement recalculateMaxID')
    
    @JOverride
    def getAsSingleObject(self):
        raise Exception('ObjsWrapper: Implement getAsSingleObject')
    
    @JOverride
    def getObjectsInFrame(self, outputObjectsName, frame):
        raise Exception('ObjsWrapper: Implement getObjectsInFrame')
    
    @JOverride
    def getNFrames(self):
        raise Exception('ObjsWrapper: Implement getNFrames')
    
    @JOverride
    def getFrameInterval(self):
        raise Exception('ObjsWrapper: Implement getFrameInterval')
    
    @JOverride
    def getTemporalUnit(self):
        raise Exception('ObjsWrapper: Implement getTemporalUnit')
    
    @JOverride
    def setNFrames(self, nFrames):
        raise Exception('ObjsWrapper: Implement setNFrames')
    
    @JOverride
    def duplicate(self, newObjectsName, duplicateRelationships, duplicateMeasurement,
                  duplicateMetadata, addOriginalDuplicateRelationship):
        raise Exception('ObjsWrapper: Implement duplicate')


    # Default methods

    @JOverride
    def getWidth(self):
        raise Exception('ObjsWrapper: Implement getWidth')
    
    @JOverride
    def getHeight(self):
        raise Exception('ObjsWrapper: Implement getHeight')
    
    @JOverride
    def getNSlices(self):
        raise Exception('ObjsWrapper: Implement getNSlices')
    
    @JOverride
    def getDppXY(self):
        raise Exception('ObjsWrapper: Implement getDppXY')
    
    @JOverride
    def getDppZ(self):
        raise Exception('ObjsWrapper: Implement getDppZ')
    
    @JOverride
    def getSpatialUnits(self):
        raise Exception('ObjsWrapper: Implement getSpatialUnits')
    
    @JOverride
    def getFirst(self):
        raise Exception('ObjsWrapper: Implement getFirst')
    
    @JOverride
    def getSpatialExtents(self):
        raise Exception('ObjsWrapper: Implement getSpatialExtents')
    
    @JOverride
    def getSpatialLimits(self):
        raise Exception('ObjsWrapper: Implement getSpatialLimits')
    
    @JOverride
    def getTemporalLimits(self):
        raise Exception('ObjsWrapper: Implement getTemporalLimits')
    
    @JOverride
    def getLargestID(self):
        raise Exception('ObjsWrapper: Implement getLargestID')
        
    @JOverride
    def convertToImage(self, outputName, hues, bitDepth, nanBackground, verbose):
        raise Exception('ObjsWrapper: Implement convertToImage')
    
    @JOverride
    def convertToImageRandomColours(self):
        raise Exception('ObjsWrapper: Implement convertToImageRandomColours')
        
    @JOverride
    def convertToImageBinary(self, name):
        raise Exception('ObjsWrapper: Implement convertToImageBinary')
    
    @JOverride
    def convertToImageIDColours(self):
        raise Exception('ObjsWrapper: Implement convertToImageIDColours')
    
    @JOverride
    def convertCentroidsToImage(self, outputName, hues, bitDepth, nanBackground):
        raise Exception('ObjsWrapper: Implement convertCentroidsToImage')
    
    @JOverride
    def applyCalibration(self, image):
        raise Exception('ObjsWrapper: Implement applyCalibration')
    
    @JOverride
    def applyCalibrationFromImagePlus(self, ipl):
        raise Exception('ObjsWrapper: Implement applyCalibrationFromImagePlus')
    
    @JOverride
    def createImage(self, outputName, bitDepth):
        raise Exception('ObjsWrapper: Implement createImage')
    
    @JOverride
    def setNaNBackground(self, ipl):
        raise Exception('ObjsWrapper: Implement setNaNBackground')
    
    @JOverride
    def getByEqualsIgnoreNameAndID(self, referenceObj):
        raise Exception('ObjsWrapper: Implement getByEqualsIgnoreNameAndID')
    
    @JOverride
    def showMeasurements(self, module, modules):
        raise Exception('ObjsWrapper: Implement showMeasurements')
    
    @JOverride
    def showAllMeasurements(self):
        raise Exception('ObjsWrapper: Implement showAllMeasurements')
    
    @JOverride
    def showMetadata(self, module, modules):
        raise Exception('ObjsWrapper: Implement showMetadata')
    
    @JOverride
    def showAllMetadata(self):
        raise Exception('ObjsWrapper: Implement showAllMetadata')
    
    @JOverride
    def removeParents(self, parentObjectsName):
        raise Exception('ObjsWrapper: Implement removeParents')
    
    @JOverride
    def removeChildren(self, childObjectsName):
        raise Exception('ObjsWrapper: Implement removeChildren')
    
    @JOverride
    def removePartners(self, partnerObjectsName):
        raise Exception('ObjsWrapper: Implement removePartners')
    
    @JOverride
    def containsPoint(self, point):
        raise Exception('ObjsWrapper: Implement containsPoint')
    
    @JOverride
    def containsCoord(self, x, y, z):
        raise Exception('ObjsWrapper: Implement containsCoord')
    
    @JOverride
    def getLargestObject(self, t):
        raise Exception('ObjsWrapper: Implement getLargestObject')
    
    @JOverride
    def getSmallestObject(self, t):
        raise Exception('ObjsWrapper: Implement getSmallestObject')


    # From Map

    @JOverride
    def get(self, object):
        raise Exception('MapWrapper: Implement size')
    
    @JOverride
    def size(self):
        raise Exception('MapWrapper: Implement size')
    
    @JOverride
    def isEmpty(self):
        raise Exception('MapWrapper: Implement isEmpty')
    
    @JOverride
    def containsKey(self, key):
        raise Exception('MapWrapper: Implement containsKey')
    
    @JOverride
    def containsValue(self, value):
        raise Exception('MapWrapper: Implement containsValue')
        
    @JOverride
    def put(self, key, value):
        raise Exception('MapWrapper: Implement put')
    
    @JOverride
    def remove(self, key):
        raise Exception('MapWrapper: Implement remove')
    
    @JOverride
    def putAll(self, m):
        raise Exception('MapWrapper: Implement putAll')
    
    @JOverride
    def clear(self):
        raise Exception('MapWrapper: Implement clear')
    
    @JOverride
    def keySet(self):
        raise Exception('MapWrapper: Implement keySet')
    
    @JOverride
    def values(self):
        raise Exception('MapWrapper: Implement values')
    
    @JOverride
    def entrySet(self):
        raise Exception('MapWrapper: Implement entrySet')

    @JOverride
    def equals(self, o):
        raise Exception('MapWrapper: Implement equals')
    
    @JOverride
    def hashCode(self):
        raise Exception('MapWrapper: Implement hashCode')
    
    @JOverride
    def getOrDefault(self, key, defaultValue):
        raise Exception('MapWrapper: Implement getOrDefault')
    
    @JOverride
    def forEach(self, action):
        raise Exception('MapWrapper: Implement forEach')
    
    @JOverride
    def replaceAll(self, function):
        raise Exception('MapWrapper: Implement replaceAll')
    
    @JOverride
    def putIfAbsent(self, key, value):
        raise Exception('MapWrapper: Implement putIfAbsent')
    
    @JOverride
    def removeKeyValue(self, key, value):
        raise Exception('MapWrapper: Implement remove (key, value)')
    
    @JOverride
    def replaceKeyValue(self, key, oldValue, newValue):
        raise Exception('MapWrapper: Implement replace (key, oldValue, newValue)')
    
    @JOverride
    def replace(self, key, value):
        raise Exception('MapWrapper: Implement replace (key, value)')
    
    @JOverride
    def computeIfAbsent(self, key, mappingFunction):
        raise Exception('MapWrapper: Implement computeIfAbsent')
    
    @JOverride
    def computeIfPresent(self, key, remappingFunction):
        raise Exception('MapWrapper: Implement computeIfPresent')
    
    @JOverride
    def compute(self, key, remappingFunction):
        raise Exception('MapWrapper: Implement compute')
    
    @JOverride
    def merge(self, key, value, remappingFunction):
        raise Exception('MapWrapper: Implement merge')

    # Note: May also need to implement the Entry interface:

    # @JOverride
    # def getKey(self):
    #     raise Exception('EntryWrapper: Implement getKey')
    
    # @JOverride
    # def getValue(self):
    #     raise Exception('EntryWrapper: Implement getValue')
    
    # @JOverride
    # def setValue(self, value):
    #     raise Exception('EntryWrapper: Implement setValue')
    
    # @JOverride
    # def equals(self, o):
    #     raise Exception('EntryWrapper: Implement equals')
    
    # @JOverride
    # def hashCode(self):
    #     raise Exception('EntryWrapper: Implement hashCode')
    
    # # Static comparator methods (if relevant to expose)
    
    # @staticmethod
    # def comparingByKey():
    #     raise Exception('EntryWrapper: Implement comparingByKey')
    
    # @staticmethod
    # def comparingByValue():
    #     raise Exception('EntryWrapper: Implement comparingByValue')
    
    # @staticmethod
    # def comparingByKeyWithComparator(cmp):
    #     raise Exception('EntryWrapper: Implement comparingByKey with comparator')
    
    # @staticmethod
    # def comparingByValueWithComparator(cmp):
    #     raise Exception('EntryWrapper: Implement comparingByValue with comparator')



@JImplements('io.github.mianalysis.mia.object.ObjsFactoryI')
class ObjsFactoryWrapper:
    
    @JOverride
    def getName(self):
        return "Python objects factory"
    
    @JOverride
    def createObjs(self, name, dppXY, dppZ, units, width, height, nSlices, nFrames, frameInterval, temporalUnit):
        raise Exception('ObjsFactoryWrapper: Implement createObjs 1')
        return ObjsWrapper()
        # return ObjsWrapper(name, dppXY, dppZ, units, width, height, nSlices, nFrames, frameInterval, temporalUnit)

    @JOverride
    def createFromExampleObjs(self, name, example_objs):
        raise Exception('ObjsFactoryWrapper: Implement createObjs 2')
        return ObjsWrapper()
        # return ObjsWrapper(name, name, imageForCalibration)

    @JOverride
    def createFromImage(self, name, imageForCalibration):
        raise Exception('ObjsFactoryWrapper: Implement createObjs 3')
        return ObjsWrapper()
        # return ObjsWrapper(name, name, imageForCalibration)
        
    @JOverride
    def createFromSpatCal(self, name, spat_cal, nFrames, frameInterval, temporalUnit):
        # raise Exception('ObjsFactoryWrapper: Implement createObjs 4')
        return ObjsWrapper()
        # return ObjsWrapper(name, cal, nFrames, frameInterval, temporalUnit)
        
    @JOverride
    def duplicate(self):
        return ObjsFactoryWrapper()
        