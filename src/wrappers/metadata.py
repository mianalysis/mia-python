from jpype import JImplements, JOverride
from scyjava import jimport

MetadataI = jimport('io.github.mianalysis.mia.object.metadata.MetadataI')

@JImplements(MetadataI)
class MetadataWrapper:
    def __init__(self):
        self._store = {}
        
    @JOverride
    def getFilename(self):
        return self._store[MetadataI.FILENAME]

    @JOverride
    def setFilename(self, filename):
        self._store[MetadataI.FILENAME] = filename
    
    @JOverride
    def getFilepath(self):
        return self._store[MetadataI.FILEPATH]
    
    @JOverride
    def setFilepath(self, filepath):
        self._store[MetadataI.FILEPATH] = filepath
    
    @JOverride
    def getExt(self):
        return self._store[MetadataI.EXTENSION]
    
    @JOverride
    def setExt(self, ext):
        self._store[MetadataI.EXTENSION] = ext
    
    @JOverride
    def getFile(self):
        return self._store[MetadataI.FILE]
    
    @JOverride
    def setFile(self, file):
        self._store[MetadataI.FILE] = file
    
    @JOverride
    def getHour(self):
        print('MetadataWrapper: Implement getHour')
    
    @JOverride
    def setHour(self, hour):
        print('MetadataWrapper: Implement setHour')
    
    @JOverride
    def getMin(self):
        print('MetadataWrapper: Implement getMin')
    
    @JOverride
    def setMin(self, min):
        print('MetadataWrapper: Implement setMin')
    
    @JOverride
    def getSec(self):
        print('MetadataWrapper: Implement getSec')
    
    @JOverride
    def setSec(self, sec):
        print('MetadataWrapper: Implement setSec')
    
    @JOverride
    def getWell(self):
        print('MetadataWrapper: Implement getWell')
    
    @JOverride
    def setWell(self, well):
        print('MetadataWrapper: Implement setWell')
    
    @JOverride
    def getRow(self):
        print('MetadataWrapper: Implement getRow')
    
    @JOverride
    def setRow(self, row):
        print('MetadataWrapper: Implement setRow')
    
    @JOverride
    def getCol(self):
        print('MetadataWrapper: Implement getCol')
    
    @JOverride
    def setCol(self, col):
        print('MetadataWrapper: Implement setCol')
    
    @JOverride
    def getField(self):
        print('MetadataWrapper: Implement getField')
    
    @JOverride
    def setField(self, field):
        print('MetadataWrapper: Implement setField')
    
    @JOverride
    def getTimepoint(self):
        print('MetadataWrapper: Implement getTimepoint')
    
    @JOverride
    def setTimepoint(self, timepoint):
        print('MetadataWrapper: Implement setTimepoint')
    
    @JOverride
    def getZ(self):
        print('MetadataWrapper: Implement getZ')
    
    @JOverride
    def setZ(self, z):
        print('MetadataWrapper: Implement setZ')
    
    @JOverride
    def getChannel(self):
        print('MetadataWrapper: Implement getChannel')
    
    @JOverride
    def setChannel(self, channel):
        print('MetadataWrapper: Implement setChannel')
    
    @JOverride
    def getCelltype(self):
        print('MetadataWrapper: Implement getCelltype')
    
    @JOverride
    def setCelltype(self, celltype):
        print('MetadataWrapper: Implement setCelltype')
    
    @JOverride
    def getMag(self):
        print('MetadataWrapper: Implement getMag')
    
    @JOverride
    def setMag(self, mag):
        print('MetadataWrapper: Implement setMag')
    
    @JOverride
    def getYear(self):
        print('MetadataWrapper: Implement getYear')
    
    @JOverride
    def setYear(self, year):
        print('MetadataWrapper: Implement setYear')
    
    @JOverride
    def getMonth(self):
        print('MetadataWrapper: Implement getMonth')
    
    @JOverride
    def setMonth(self, month):
        print('MetadataWrapper: Implement setMonth')
    
    @JOverride
    def getDay(self):
        print('MetadataWrapper: Implement getDay')
    
    @JOverride
    def setDay(self, day):
        print('MetadataWrapper: Implement setDay')
    
    @JOverride
    def getComment(self):
        print('MetadataWrapper: Implement getComment')
    
    @JOverride
    def setComment(self, comment):
        print('MetadataWrapper: Implement setComment')
    
    @JOverride
    def getKeyword(self):
        print('MetadataWrapper: Implement getKeyword')
    
    @JOverride
    def putKeyword(self, keyword):
        print('MetadataWrapper: Implement putKeyword')
    
    @JOverride
    def getSeriesNumber(self):
        if self._store[MetadataI.SERIES_NUMBER] is None:
            return -1
        else:
            return self._store[MetadataI.SERIES_NUMBER]
    
    @JOverride
    def setSeriesNumber(self, seriesNumber):
        self._store[MetadataI.SERIES_NUMBER] = seriesNumber
    
    @JOverride
    def getSeriesName(self):
        print('MetadataWrapper: Implement getSeriesName')
    
    @JOverride
    def setSeriesName(self, seriesName):
        print('MetadataWrapper: Implement setSeriesName')
    
    @JOverride
    def getUnits(self):
        print('MetadataWrapper: Implement getUnits')
    
    @JOverride
    def setUnits(self, units):
        print('MetadataWrapper: Implement setUnits')
    
    @JOverride
    def getPlateName(self):
        print('MetadataWrapper: Implement getPlateName')
    
    @JOverride
    def setPlateName(self, plateName):
        print('MetadataWrapper: Implement setPlateName')
    
    @JOverride
    def getPlateManufacturer(self):
        print('MetadataWrapper: Implement getPlateManufacturer')
    
    @JOverride
    def setPlateManufacturer(self, plateManufacturer):
        print('MetadataWrapper: Implement setPlateManufacturer')
    
    @JOverride
    def getPlateModel(self):
        print('MetadataWrapper: Implement getPlateModel')
    
    @JOverride
    def setPlateModel(self, plateModel):
        print('MetadataWrapper: Implement setPlateModel')
    
    @JOverride
    def getTimelineNumber(self):
        print('MetadataWrapper: Implement getTimelineNumber')
    
    @JOverride
    def setTimelineNumber(self, timelineNumber):
        print('MetadataWrapper: Implement setTimelineNumber')
    
    @JOverride
    def getActionNumber(self):
        print('MetadataWrapper: Implement getActionNumber')
    
    @JOverride
    def setActionNumber(self, actionNumber):
        print('MetadataWrapper: Implement setActionNumber')
    
    @JOverride
    def getAsString(self, property):
        print('MetadataWrapper: Implement getAsString')
    
    @JOverride
    def printParameters(self):
        print('MetadataWrapper: Implement printParameters')
    
    @JOverride
    def insertMetadataValues(self, genericFormat):
        print('MetadataWrapper: Implement insertMetadataValues')

    @JOverride
    def hasKey(self, key):
        print('MetadataWrapper: Implement hasKey')
    
    @JOverride
    def keySet(self):
        print('MetadataWrapper: Implement keySet')

    @JOverride
    def values(self):
        print('MetadataWrapper: Implement values')

    @JOverride
    def clear(self):
        print('MetadataWrapper: Implement clear')

    @JOverride
    def put(self, key, value):
        print('MetadataWrapper: Implement put')

    @JOverride
    def get(self, key):
        print('MetadataWrapper: Implement get')

    @JOverride
    def clone(self):
        print('MetadataWrapper: Implement clone')
        