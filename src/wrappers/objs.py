from jpype import JImplements, JOverride
from scyjava import jimport

import jpype

Objs = jimport('io.github.mianalysis.mia.object.ObjsI')

@JImplements('io.github.mianalysis.mia.object.ObjsI')
class PythonObjsWrapper(jpype._jcollection._JMap):      
    def __init__(self):
        self._objs = {}
        
    @JOverride
    def createAndAddNewObject(self, factory):
        print('ObjsWrapper: Implement createAndAddNewObject')
    
    @JOverride
    def createAndAddNewObjectWithID(self, factory, ID):
        print('ObjsWrapper: Implement createAndAddNewObjectWithID')
    
    @JOverride
    def values(self):
        print('ObjsWrapper: Implement values')
    
    @JOverride
    def size(self):
        print('ObjsWrapper: Implement size')
    
    @JOverride
    def getName(self):
        print('ObjsWrapper: Implement getName')
    
    @JOverride
    def add(self, object):
        print('ObjsWrapper: Implement add')
    
    @JOverride
    def getSpatialCalibration(self):
        print('ObjsWrapper: Implement getSpatialCalibration')
    
    @JOverride
    def setSpatialCalibration(self, spatCal, updateAllObjects):
        print('ObjsWrapper: Implement setSpatialCalibration')
    
    @JOverride
    def getAndIncrementID(self):
        print('ObjsWrapper: Implement getAndIncrementID')
    
    @JOverride
    def resetCollection(self):
        print('ObjsWrapper: Implement resetCollection')
    
    @JOverride
    def recalculateMaxID(self):
        print('ObjsWrapper: Implement recalculateMaxID')
    
    @JOverride
    def getAsSingleObject(self):
        print('ObjsWrapper: Implement getAsSingleObject')
    
    @JOverride
    def getObjectsInFrame(self, outputObjectsName, frame):
        print('ObjsWrapper: Implement getObjectsInFrame')
    
    @JOverride
    def getNFrames(self):
        print('ObjsWrapper: Implement getNFrames')
    
    @JOverride
    def getFrameInterval(self):
        print('ObjsWrapper: Implement getFrameInterval')
    
    @JOverride
    def getTemporalUnit(self):
        print('ObjsWrapper: Implement getTemporalUnit')
    
    @JOverride
    def setNFrames(self, nFrames):
        print('ObjsWrapper: Implement setNFrames')
    
    @JOverride
    def duplicate(self, newObjectsName, duplicateRelationships, duplicateMeasurement,
                  duplicateMetadata, addOriginalDuplicateRelationship):
        print('ObjsWrapper: Implement duplicate')


    # Default methods

    @JOverride
    def getWidth(self):
        print('ObjsWrapper: Implement getWidth')
    
    @JOverride
    def getHeight(self):
        print('ObjsWrapper: Implement getHeight')
    
    @JOverride
    def getNSlices(self):
        print('ObjsWrapper: Implement getNSlices')
    
    @JOverride
    def getDppXY(self):
        print('ObjsWrapper: Implement getDppXY')
    
    @JOverride
    def getDppZ(self):
        print('ObjsWrapper: Implement getDppZ')
    
    @JOverride
    def getSpatialUnits(self):
        print('ObjsWrapper: Implement getSpatialUnits')
    
    @JOverride
    def getFirst(self):
        print('ObjsWrapper: Implement getFirst')
    
    @JOverride
    def getSpatialExtents(self):
        print('ObjsWrapper: Implement getSpatialExtents')
    
    @JOverride
    def getSpatialLimits(self):
        print('ObjsWrapper: Implement getSpatialLimits')
    
    @JOverride
    def getTemporalLimits(self):
        print('ObjsWrapper: Implement getTemporalLimits')
    
    @JOverride
    def getLargestID(self):
        print('ObjsWrapper: Implement getLargestID')
        
    @JOverride
    def convertToImage(self, outputName, hues, bitDepth, nanBackground, verbose):
        print('ObjsWrapper: Implement convertToImage')
    
    @JOverride
    def convertToImageRandomColours(self):
        print('ObjsWrapper: Implement convertToImageRandomColours')
        
    @JOverride
    def convertToImageBinary(self, name):
        print('ObjsWrapper: Implement convertToImageBinary')
    
    @JOverride
    def convertToImageIDColours(self):
        print('ObjsWrapper: Implement convertToImageIDColours')
    
    @JOverride
    def convertCentroidsToImage(self, outputName, hues, bitDepth, nanBackground):
        print('ObjsWrapper: Implement convertCentroidsToImage')
    
    @JOverride
    def applyCalibration(self, image):
        print('ObjsWrapper: Implement applyCalibration')
    
    @JOverride
    def applyCalibrationFromImagePlus(self, ipl):
        print('ObjsWrapper: Implement applyCalibrationFromImagePlus')
    
    @JOverride
    def createImage(self, outputName, bitDepth):
        print('ObjsWrapper: Implement createImage')
    
    @JOverride
    def setNaNBackground(self, ipl):
        print('ObjsWrapper: Implement setNaNBackground')
    
    @JOverride
    def getByEqualsIgnoreNameAndID(self, referenceObj):
        print('ObjsWrapper: Implement getByEqualsIgnoreNameAndID')
    
    @JOverride
    def showMeasurements(self, module, modules):
        print('ObjsWrapper: Implement showMeasurements')
    
    @JOverride
    def showAllMeasurements(self):
        print('ObjsWrapper: Implement showAllMeasurements')
    
    @JOverride
    def showMetadata(self, module, modules):
        print('ObjsWrapper: Implement showMetadata')
    
    @JOverride
    def showAllMetadata(self):
        print('ObjsWrapper: Implement showAllMetadata')
    
    @JOverride
    def removeParents(self, parentObjectsName):
        print('ObjsWrapper: Implement removeParents')
    
    @JOverride
    def removeChildren(self, childObjectsName):
        print('ObjsWrapper: Implement removeChildren')
    
    @JOverride
    def removePartners(self, partnerObjectsName):
        print('ObjsWrapper: Implement removePartners')
    
    @JOverride
    def containsPoint(self, point):
        print('ObjsWrapper: Implement containsPoint')
    
    @JOverride
    def containsPoint(self, x, y, z):
        print('ObjsWrapper: Implement containsPoint')
    
    @JOverride
    def getLargestObject(self, t):
        print('ObjsWrapper: Implement getLargestObject')
    
    @JOverride
    def getSmallestObject(self, t):
        print('ObjsWrapper: Implement getSmallestObject')


    # From Map

    @JOverride
    def size(self):
        print('MapWrapper: Implement size')
    
    @JOverride
    def isEmpty(self):
        print('MapWrapper: Implement isEmpty')
    
    @JOverride
    def containsKey(self, key):
        print('MapWrapper: Implement containsKey')
    
    @JOverride
    def containsValue(self, value):
        print('MapWrapper: Implement containsValue')
    
    @JOverride
    def get(self, key):
        print('MapWrapper: Implement get')
    
    @JOverride
    def put(self, key, value):
        print('MapWrapper: Implement put')
    
    @JOverride
    def remove(self, key):
        print('MapWrapper: Implement remove')
    
    @JOverride
    def putAll(self, m):
        print('MapWrapper: Implement putAll')
    
    @JOverride
    def clear(self):
        print('MapWrapper: Implement clear')
    
    @JOverride
    def keySet(self):
        print('MapWrapper: Implement keySet')
    
    @JOverride
    def values(self):
        print('MapWrapper: Implement values')
    
    @JOverride
    def entrySet(self):
        print('MapWrapper: Implement entrySet')

    @JOverride
    def equals(self, o):
        print('MapWrapper: Implement equals')
    
    @JOverride
    def hashCode(self):
        print('MapWrapper: Implement hashCode')
    
    @JOverride
    def getOrDefault(self, key, defaultValue):
        print('MapWrapper: Implement getOrDefault')
    
    @JOverride
    def forEach(self, action):
        print('MapWrapper: Implement forEach')
    
    @JOverride
    def replaceAll(self, function):
        print('MapWrapper: Implement replaceAll')
    
    @JOverride
    def putIfAbsent(self, key, value):
        print('MapWrapper: Implement putIfAbsent')
    
    @JOverride
    def removeKeyValue(self, key, value):
        print('MapWrapper: Implement remove (key, value)')
    
    @JOverride
    def replaceKeyValue(self, key, oldValue, newValue):
        print('MapWrapper: Implement replace (key, oldValue, newValue)')
    
    @JOverride
    def replace(self, key, value):
        print('MapWrapper: Implement replace (key, value)')
    
    @JOverride
    def computeIfAbsent(self, key, mappingFunction):
        print('MapWrapper: Implement computeIfAbsent')
    
    @JOverride
    def computeIfPresent(self, key, remappingFunction):
        print('MapWrapper: Implement computeIfPresent')
    
    @JOverride
    def compute(self, key, remappingFunction):
        print('MapWrapper: Implement compute')
    
    @JOverride
    def merge(self, key, value, remappingFunction):
        print('MapWrapper: Implement merge')

    # Note: May also need to implement the Entry interface:

    # @JOverride
    # def getKey(self):
    #     print('EntryWrapper: Implement getKey')
    
    # @JOverride
    # def getValue(self):
    #     print('EntryWrapper: Implement getValue')
    
    # @JOverride
    # def setValue(self, value):
    #     print('EntryWrapper: Implement setValue')
    
    # @JOverride
    # def equals(self, o):
    #     print('EntryWrapper: Implement equals')
    
    # @JOverride
    # def hashCode(self):
    #     print('EntryWrapper: Implement hashCode')
    
    # # Static comparator methods (if relevant to expose)
    
    # @staticmethod
    # def comparingByKey():
    #     print('EntryWrapper: Implement comparingByKey')
    
    # @staticmethod
    # def comparingByValue():
    #     print('EntryWrapper: Implement comparingByValue')
    
    # @staticmethod
    # def comparingByKeyWithComparator(cmp):
    #     print('EntryWrapper: Implement comparingByKey with comparator')
    
    # @staticmethod
    # def comparingByValueWithComparator(cmp):
    #     print('EntryWrapper: Implement comparingByValue with comparator')



@JImplements('io.github.mianalysis.mia.object.ObjsFactoryI')
class PythonObjsFactory:
    
    @JOverride
    def getName(self):
        return "Python objects factory"
    
    @JOverride
    def createObjs(self, name, dppXY, dppZ, units, width, height, nSlices, nFrames, frameInterval, temporalUnit):
        print('PythonObjsFactory: Implement createObjs')
        return PythonObjsWrapper()
        # return PythonObjsWrapper(name, dppXY, dppZ, units, width, height, nSlices, nFrames, frameInterval, temporalUnit)

    @JOverride
    def createFromExampleObjs(self, name, example_objs):
        print('PythonObjsFactory: Implement createObjs')
        return PythonObjsWrapper()
        # return PythonObjsWrapper(name, name, imageForCalibration)

    @JOverride
    def createFromImage(self, name, imageForCalibration):
        print('PythonObjsFactory: Implement createObjs')
        return PythonObjsWrapper()
        # return PythonObjsWrapper(name, name, imageForCalibration)
        
    @JOverride
    def createFromSpatCal(self, name, spat_cal, nFrames, frameInterval, temporalUnit):
        print('PythonObjsFactory: Implement createObjs')
        return PythonObjsWrapper()
        # return PythonObjsWrapper(name, cal, nFrames, frameInterval, temporalUnit)
        
    @JOverride
    def duplicate(self):
        return PythonObjsFactory()
        