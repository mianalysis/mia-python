from jpype import JImplements, JOverride
from scyjava import jimport
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types.JPype import *

JMetadata = jimport('io.github.mianalysis.mia.object.metadata.MetadataI')

@JImplements('io.github.mianalysis.mia.object.metadata.MetadataI')
class MetadataWrapper:
    def __init__(self):
        self._store = {}
        
    @JOverride
    def getFilename(self):
        return self._store[JMetadata.FILENAME]

    @JOverride
    def setFilename(self, filename):
        self._store[JMetadata.FILENAME] = filename
    
    @JOverride
    def getFilepath(self):
        return self._store[JMetadata.FILEPATH]
    
    @JOverride
    def setFilepath(self, filepath):
        self._store[JMetadata.FILEPATH] = filepath
    
    @JOverride
    def getExt(self):
        return self._store[JMetadata.EXTENSION]
    
    @JOverride
    def setExt(self, ext):
        self._store[JMetadata.EXTENSION] = ext
    
    @JOverride
    def getFile(self):
        return self._store[JMetadata.FILE]
    
    @JOverride
    def setFile(self, file):
        self._store[JMetadata.FILE] = file
    
    @JOverride
    def getHour(self):
        raise Exception('MetadataWrapper: Implement getHour')
    
    @JOverride
    def setHour(self, hour):
        raise Exception('MetadataWrapper: Implement setHour')
    
    @JOverride
    def getMin(self):
        raise Exception('MetadataWrapper: Implement getMin')
    
    @JOverride
    def setMin(self, min):
        raise Exception('MetadataWrapper: Implement setMin')
    
    @JOverride
    def getSec(self):
        raise Exception('MetadataWrapper: Implement getSec')
    
    @JOverride
    def setSec(self, sec):
        raise Exception('MetadataWrapper: Implement setSec')
    
    @JOverride
    def getWell(self):
        raise Exception('MetadataWrapper: Implement getWell')
    
    @JOverride
    def setWell(self, well):
        raise Exception('MetadataWrapper: Implement setWell')
    
    @JOverride
    def getRow(self):
        raise Exception('MetadataWrapper: Implement getRow')
    
    @JOverride
    def setRow(self, row):
        raise Exception('MetadataWrapper: Implement setRow')
    
    @JOverride
    def getCol(self):
        raise Exception('MetadataWrapper: Implement getCol')
    
    @JOverride
    def setCol(self, col):
        raise Exception('MetadataWrapper: Implement setCol')
    
    @JOverride
    def getField(self):
        raise Exception('MetadataWrapper: Implement getField')
    
    @JOverride
    def setField(self, field):
        raise Exception('MetadataWrapper: Implement setField')
    
    @JOverride
    def getTimepoint(self):
        raise Exception('MetadataWrapper: Implement getTimepoint')
    
    @JOverride
    def setTimepoint(self, timepoint):
        raise Exception('MetadataWrapper: Implement setTimepoint')
    
    @JOverride
    def getZ(self):
        raise Exception('MetadataWrapper: Implement getZ')
    
    @JOverride
    def setZ(self, z):
        raise Exception('MetadataWrapper: Implement setZ')
    
    @JOverride
    def getChannel(self):
        raise Exception('MetadataWrapper: Implement getChannel')
    
    @JOverride
    def setChannel(self, channel):
        raise Exception('MetadataWrapper: Implement setChannel')
    
    @JOverride
    def getCelltype(self):
        raise Exception('MetadataWrapper: Implement getCelltype')
    
    @JOverride
    def setCelltype(self, celltype):
        raise Exception('MetadataWrapper: Implement setCelltype')
    
    @JOverride
    def getMag(self):
        raise Exception('MetadataWrapper: Implement getMag')
    
    @JOverride
    def setMag(self, mag):
        raise Exception('MetadataWrapper: Implement setMag')
    
    @JOverride
    def getYear(self):
        raise Exception('MetadataWrapper: Implement getYear')
    
    @JOverride
    def setYear(self, year):
        raise Exception('MetadataWrapper: Implement setYear')
    
    @JOverride
    def getMonth(self):
        raise Exception('MetadataWrapper: Implement getMonth')
    
    @JOverride
    def setMonth(self, month):
        raise Exception('MetadataWrapper: Implement setMonth')
    
    @JOverride
    def getDay(self):
        raise Exception('MetadataWrapper: Implement getDay')
    
    @JOverride
    def setDay(self, day):
        raise Exception('MetadataWrapper: Implement setDay')
    
    @JOverride
    def getComment(self):
        raise Exception('MetadataWrapper: Implement getComment')
    
    @JOverride
    def setComment(self, comment):
        raise Exception('MetadataWrapper: Implement setComment')
    
    @JOverride
    def getKeyword(self):
        raise Exception('MetadataWrapper: Implement getKeyword')
    
    @JOverride
    def putKeyword(self, keyword):
        raise Exception('MetadataWrapper: Implement putKeyword')
    
    @JOverride
    def getSeriesNumber(self):
        if self._store[JMetadata.SERIES_NUMBER] is None:
            return -1
        else:
            return self._store[JMetadata.SERIES_NUMBER]
    
    @JOverride
    def setSeriesNumber(self, seriesNumber):
        self._store[JMetadata.SERIES_NUMBER] = seriesNumber
    
    @JOverride
    def getSeriesName(self):
        raise Exception('MetadataWrapper: Implement getSeriesName')
    
    @JOverride
    def setSeriesName(self, seriesName):
        raise Exception('MetadataWrapper: Implement setSeriesName')
    
    @JOverride
    def getUnits(self):
        raise Exception('MetadataWrapper: Implement getUnits')
    
    @JOverride
    def setUnits(self, units):
        raise Exception('MetadataWrapper: Implement setUnits')
    
    @JOverride
    def getPlateName(self):
        raise Exception('MetadataWrapper: Implement getPlateName')
    
    @JOverride
    def setPlateName(self, plateName):
        raise Exception('MetadataWrapper: Implement setPlateName')
    
    @JOverride
    def getPlateManufacturer(self):
        raise Exception('MetadataWrapper: Implement getPlateManufacturer')
    
    @JOverride
    def setPlateManufacturer(self, plateManufacturer):
        raise Exception('MetadataWrapper: Implement setPlateManufacturer')
    
    @JOverride
    def getPlateModel(self):
        raise Exception('MetadataWrapper: Implement getPlateModel')
    
    @JOverride
    def setPlateModel(self, plateModel):
        raise Exception('MetadataWrapper: Implement setPlateModel')
    
    @JOverride
    def getTimelineNumber(self):
        raise Exception('MetadataWrapper: Implement getTimelineNumber')
    
    @JOverride
    def setTimelineNumber(self, timelineNumber):
        raise Exception('MetadataWrapper: Implement setTimelineNumber')
    
    @JOverride
    def getActionNumber(self):
        raise Exception('MetadataWrapper: Implement getActionNumber')
    
    @JOverride
    def setActionNumber(self, actionNumber):
        raise Exception('MetadataWrapper: Implement setActionNumber')
    
    @JOverride
    def getAsString(self, property):
        raise Exception('MetadataWrapper: Implement getAsString')
    
    @JOverride
    def printParameters(self):
        raise Exception('MetadataWrapper: Implement raise ExceptionParameters')
    
    @JOverride
    def insertMetadataValues(self, genericFormat):
        raise Exception('MetadataWrapper: Implement insertMetadataValues')

    @JOverride
    def hasKey(self, key):
        return key in self._store.keys()
    
    @JOverride
    def keySet(self):
        raise Exception('MetadataWrapper: Implement keySet')

    @JOverride
    def values(self):
        raise Exception('MetadataWrapper: Implement values')

    @JOverride
    def clear(self):
        self._store = {}

    @JOverride
    def put(self, key, value):
        self._store[key] = value

    @JOverride
    def get(self, key):
        return self._store[key]

    @JOverride
    def remove(self, key):
        item = self._store[key]
        self._store.pop(key)
        return item

    @JOverride
    def clone(self):
        raise Exception('MetadataWrapper: Implement clone')
        