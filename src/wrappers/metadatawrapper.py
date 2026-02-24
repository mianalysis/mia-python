from __future__ import annotations
from jpype import JImplements, JOverride # type: ignore
from scyjava import jimport # type: ignore
from typing import Any, Dict

from src.types.JFileType import JFileType

JMetadata = jimport('io.github.mianalysis.mia.object.metadata.MetadataI')

FILENAME: str = JMetadata.FILENAME
FILEPATH: str = JMetadata.FILEPATH
WELL: str = JMetadata.WELL
ROW: str = JMetadata.ROW
COL: str = JMetadata.COL
FIELD: str = JMetadata.FIELD
TIMEPOINT: str = JMetadata.TIMEPOINT
ZPOSITION: str = JMetadata.ZPOSITION
CHANNEL: str = JMetadata.CHANNEL
YEAR: str = JMetadata.YEAR
MONTH: str = JMetadata.MONTH
DAY: str = JMetadata.DAY
HOUR: str = JMetadata.HOUR
MINUTE: str = JMetadata.MINUTE
SECOND: str = JMetadata.SECOND
CELLTYPE: str = JMetadata.CELLTYPE
MAGNIFICATION: str = JMetadata.MAGNIFICATION
COMMENT: str = JMetadata.COMMENT
FILE: str = JMetadata.FILE
EXTENSION: str = JMetadata.EXTENSION
KEYWORD: str = JMetadata.KEYWORD
SERIES_NUMBER: str = JMetadata.SERIES_NUMBER
SERIES_NAME: str = JMetadata.SERIES_NAME
UNITS: str = JMetadata.UNITS
PLATE_NAME: str = JMetadata.PLATE_NAME
PLATE_MANUFACTURER: str = JMetadata.PLATE_MANUFACTURER
PLATE_MODEL: str = JMetadata.PLATE_MODEL
TIMELINE_NUMBER: str = JMetadata.TIMELINE_NUMBER
ACTION_NUMBER: str = JMetadata.ACTION_NUMBER
AREA_NAME: str = JMetadata.AREA_NAME

@JImplements('io.github.mianalysis.mia.object.metadata.MetadataI')
class MetadataWrapper:
    def __init__(self):
        self._store: Dict[str, Any] = {}
        
    def getPythonMetadataStore(self) -> Dict[str, Any]:
        return self._store
    
    def setPythonMetadataStore(self, store: Dict[str, Any]):  # No return
        self._store = store
        
    @JOverride
    def getFilename(self) -> str:
        return self._store[FILENAME]
    
    @JOverride
    def setFilename(self, filename: str):  # No return
        self._store[FILENAME] = filename
    
    @JOverride
    def getFilepath(self) -> str:
        return self._store[FILEPATH]
    
    @JOverride
    def setFilepath(self, filepath: str):  # No return
        self._store[FILEPATH] = filepath
    
    @JOverride
    def getExt(self) -> str:
        return self._store[EXTENSION]
    
    @JOverride
    def setExt(self, ext: str):  # No return
        self._store[EXTENSION] = ext
    
    @JOverride
    def getFile(self) -> JFileType:
        return self._store[FILE]
    
    @JOverride
    def setFile(self, file: JFileType):  # No return
        self._store[FILE] = file
    
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
        if self._store[SERIES_NUMBER] is None:
            return -1
        else:
            return self._store[SERIES_NUMBER]
    
    @JOverride
    def setSeriesNumber(self, seriesNumber: int):  # No return
        self._store[SERIES_NUMBER] = seriesNumber
    
    @JOverride
    def getSeriesName(self) -> str:
        raise NotImplementedError('MetadataWrapper: getSeriesName')
    
    @JOverride
    def setSeriesName(self, seriesName: str):  # No return
        raise NotImplementedError('MetadataWrapper: setSeriesName')
    
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
        return key in self._store.keys()
    
    @JOverride
    def keySet(self):  # To do
        raise NotImplementedError('MetadataWrapper: keySet')

    @JOverride
    def values(self):  # To do
        raise NotImplementedError('MetadataWrapper: values')

    @JOverride
    def clear(self):  # No return
        self._store = {}

    @JOverride
    def put(self, key: str, value: Any):
        self._store[key] = value

    @JOverride
    def get(self, key: str) -> Any:
        return self._store[key]

    @JOverride
    def remove(self, key: str) -> Any:
        item = self._store[key]
        self._store.pop(key)
        return item

    @JOverride
    def clone(self) -> MetadataWrapper:
        raise NotImplementedError('MetadataWrapper: clone')
        
def wrapMetadataStore(store: Dict[str, Any]) -> MetadataWrapper:
    print("MetadataWrapper: caching on wrapMetadataStore once separate Metadata class complete")
    wrapper: MetadataWrapper = MetadataWrapper()
    wrapper.setPythonMetadataStore(store)
    
    return wrapper