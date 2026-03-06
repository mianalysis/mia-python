from __future__ import annotations
from jpype import JImplements, JOverride # type: ignore
from scyjava import jimport # type: ignore
from typing import Any, Dict
from weakref import WeakKeyDictionary

from src.objects.metadata import Metadata
from src.types.JFileType import JFileType

JFile = jimport('java.io.File') # type: ignore

_wrapper_cache: WeakKeyDictionary[Metadata, MetadataWrapper] = WeakKeyDictionary()

@JImplements('io.github.mianalysis.mia.object.metadata.MetadataI')
class MetadataWrapper:
    def __init__(self):
        self._metadata: Metadata = Metadata()
        
    def getPythonMetadata(self) -> Metadata:
        return self._metadata
    
    def setPythonMetadata(self, metadata: Metadata):  # No return
        self._metadata = metadata
        
    @JOverride
    def getFilename(self) -> str:
        raise NotImplementedError('MetadataWrapper: getFilename')
    
    @JOverride
    def setFilename(self, filename: str):  # No return
        raise NotImplementedError('MetadataWrapper: setFilename')
    
    @JOverride
    def getFilepath(self) -> str:
        raise NotImplementedError('MetadataWrapper: getFilepath')
    
    @JOverride
    def setFilepath(self, filepath: str):  # No return
        raise NotImplementedError('MetadataWrapper: setFilepath')
    
    @JOverride
    def getExt(self) -> str:
        raise NotImplementedError('MetadataWrapper: getExt')
    
    @JOverride
    def setExt(self, ext: str):  # No return
        raise NotImplementedError('MetadataWrapper: setExt')
    
    @JOverride
    def getFile(self) -> JFileType:
        return JFile(self._metadata.getFile())
    
    @JOverride
    def setFile(self, file: JFileType):  # No return
        self._metadata.setFile(file.getPath())
    
    @JOverride
    def getHour(self) -> int:
        raise NotImplementedError('MetadataWrapper: getHour')
    
    @JOverride
    def setHour(self, hour: int):  # No return
        raise NotImplementedError('MetadataWrapper: setHour')
    
    @JOverride
    def getMin(self) -> int:
        raise NotImplementedError('MetadataWrapper: getMin')
    
    @JOverride
    def setMin(self, min: int):  # No return
        raise NotImplementedError('MetadataWrapper: setMin')
    
    @JOverride
    def getSec(self) -> int:
        raise NotImplementedError('MetadataWrapper: getSec')
    
    @JOverride
    def setSec(self, sec: int):  # No return
        raise NotImplementedError('MetadataWrapper: setSec')
    
    @JOverride
    def getWell(self) -> str:
        raise NotImplementedError('MetadataWrapper: getWell')
    
    @JOverride
    def setWell(self, well: str):  # No return
        raise NotImplementedError('MetadataWrapper: setWell')
    
    @JOverride
    def getRow(self) -> int:
        raise NotImplementedError('MetadataWrapper: getRow')
    
    @JOverride
    def setRow(self, row: int):  # No return
        raise NotImplementedError('MetadataWrapper: setRow')
    
    @JOverride
    def getCol(self) -> int:
        raise NotImplementedError('MetadataWrapper: getCol')
    
    @JOverride
    def setCol(self, col: int):  # No return
        raise NotImplementedError('MetadataWrapper: setCol')
    
    @JOverride
    def getField(self) -> int:
        raise NotImplementedError('MetadataWrapper: getField')
    
    @JOverride
    def setField(self, field: int):  # No return
        raise NotImplementedError('MetadataWrapper: setField')
    
    @JOverride
    def getTimepoint(self) -> int:
        raise NotImplementedError('MetadataWrapper: getTimepoint')
    
    @JOverride
    def setTimepoint(self, timepoint: int):  # No return
        raise NotImplementedError('MetadataWrapper: setTimepoint')
    
    @JOverride
    def getZ(self) -> int:
        raise NotImplementedError('MetadataWrapper: getZ')
    
    @JOverride
    def setZ(self, z: int):  # No return
        raise NotImplementedError('MetadataWrapper: setZ')
    
    @JOverride
    def getChannel(self) -> int:
        raise NotImplementedError('MetadataWrapper: getChannel')
    
    @JOverride
    def setChannel(self, channel: int):  # No return
        raise NotImplementedError('MetadataWrapper: setChannel')
    
    @JOverride
    def getCelltype(self) -> str:
        raise NotImplementedError('MetadataWrapper: getCelltype')
    
    @JOverride
    def setCelltype(self, celltype: str):  # No return
        raise NotImplementedError('MetadataWrapper: setCelltype')
    
    @JOverride
    def getMag(self) -> str:
        raise NotImplementedError('MetadataWrapper: getMag')
    
    @JOverride
    def setMag(self, mag: str):  # No return
        raise NotImplementedError('MetadataWrapper: setMag')
    
    @JOverride
    def getYear(self) -> int:
        raise NotImplementedError('MetadataWrapper: getYear')
    
    @JOverride
    def setYear(self, year: int):  # No return
        raise NotImplementedError('MetadataWrapper: setYear')
    
    @JOverride
    def getMonth(self) -> int:
        raise NotImplementedError('MetadataWrapper: getMonth')
    
    @JOverride
    def setMonth(self, month: int):  # No return
        raise NotImplementedError('MetadataWrapper: setMonth')
    
    @JOverride
    def getDay(self) -> int:
        raise NotImplementedError('MetadataWrapper: getDay')
    
    @JOverride
    def setDay(self, day: int):  # No return
        raise NotImplementedError('MetadataWrapper: setDay')
    
    @JOverride
    def getComment(self) -> str:
        raise NotImplementedError('MetadataWrapper: getComment')
    
    @JOverride
    def setComment(self, comment: str):  # No return
        raise NotImplementedError('MetadataWrapper: setComment')
    
    @JOverride
    def getKeyword(self) -> str:
        raise NotImplementedError('MetadataWrapper: getKeyword')
    
    @JOverride
    def putKeyword(self, keyword: str):  # No return
        raise NotImplementedError('MetadataWrapper: putKeyword')
    
    @JOverride
    def getSeriesNumber(self) -> int:
        return self._metadata.getSeriesNumber()
    
    @JOverride
    def setSeriesNumber(self, seriesNumber: int):  # No return
        self._metadata.setSeriesNumber(seriesNumber)
    
    @JOverride
    def getSeriesName(self) -> str:
        return self._metadata.getSeriesName()
    
    @JOverride
    def setSeriesName(self, seriesName: str):  # No return
        self._metadata.setSeriesName(seriesName)
    
    @JOverride
    def getUnits(self) -> str:
        raise NotImplementedError('MetadataWrapper: getUnits')
    
    @JOverride
    def setUnits(self, units: str):  # No return
        raise NotImplementedError('MetadataWrapper: setUnits')
    
    @JOverride
    def getPlateName(self) -> str:
        raise NotImplementedError('MetadataWrapper: getPlateName')
    
    @JOverride
    def setPlateName(self, plateName: str):  # No return
        raise NotImplementedError('MetadataWrapper: setPlateName')
    
    @JOverride
    def getPlateManufacturer(self) -> str:
        raise NotImplementedError('MetadataWrapper: getPlateManufacturer')
    
    @JOverride
    def setPlateManufacturer(self, plateManufacturer: str):  # No return
        raise NotImplementedError('MetadataWrapper: setPlateManufacturer')
    
    @JOverride
    def getPlateModel(self) -> str:
        raise NotImplementedError('MetadataWrapper: getPlateModel')
    
    @JOverride
    def setPlateModel(self, plateModel: str):  # No return
        raise NotImplementedError('MetadataWrapper: setPlateModel')
    
    @JOverride
    def getTimelineNumber(self) -> int:
        raise NotImplementedError('MetadataWrapper: getTimelineNumber')
    
    @JOverride
    def setTimelineNumber(self, timelineNumber: int):  # No return
        raise NotImplementedError('MetadataWrapper: setTimelineNumber')
    
    @JOverride
    def getActionNumber(self) -> int:
        raise NotImplementedError('MetadataWrapper: getActionNumber')
    
    @JOverride
    def setActionNumber(self, actionNumber: int):  # No return
        raise NotImplementedError('MetadataWrapper: setActionNumber')
    
    @JOverride
    def getAsString(self, property: str) -> str:
        raise NotImplementedError('MetadataWrapper: getAsString')
    
    @JOverride
    def printParameters(self):  # No return
        raise NotImplementedError('MetadataWrapper: raise NotImplementedErrorParameters')
    
    @JOverride
    def insertMetadataValues(self, genericFormat: str) -> str:
        raise NotImplementedError('MetadataWrapper: insertMetadataValues')

    @JOverride
    def hasKey(self, key: str) -> bool:
        raise NotImplementedError('MetadataWrapper: hasKey')
    
    @JOverride
    def keySet(self):  # To do
        raise NotImplementedError('MetadataWrapper: keySet')

    @JOverride
    def values(self):  # To do
        raise NotImplementedError('MetadataWrapper: values')

    @JOverride
    def clear(self):  # No return
        raise NotImplementedError('MetadataWrapper: clear')

    @JOverride
    def put(self, key: str, value: Any):
        raise NotImplementedError('MetadataWrapper: put')

    @JOverride
    def get(self, key: str) -> Any:
        raise NotImplementedError('MetadataWrapper: get')

    @JOverride
    def remove(self, key: str) -> Any:
        raise NotImplementedError('MetadataWrapper: remove')

    @JOverride
    def clone(self) -> MetadataWrapper:
        raise NotImplementedError('MetadataWrapper: clone')
        
def wrapMetadata(metadata: Metadata) -> MetadataWrapper:
    try:
        return _wrapper_cache[metadata]
    except:        
        metadata_wrapper: MetadataWrapper = MetadataWrapper()
        metadata_wrapper.setPythonMetadata(metadata)
        _wrapper_cache[metadata]  = metadata_wrapper
    
        return metadata_wrapper
