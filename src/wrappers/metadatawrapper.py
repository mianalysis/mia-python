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
        raise Exception('MetadataWrapper: Implement getHour')
    
    @JOverride
    def setHour(self, hour: int):  # No return
        raise Exception('MetadataWrapper: Implement setHour')
    
    @JOverride
    def getMin(self) -> int:
        raise Exception('MetadataWrapper: Implement getMin')
    
    @JOverride
    def setMin(self, min: int):  # No return
        raise Exception('MetadataWrapper: Implement setMin')
    
    @JOverride
    def getSec(self) -> int:
        raise Exception('MetadataWrapper: Implement getSec')
    
    @JOverride
    def setSec(self, sec: int):  # No return
        raise Exception('MetadataWrapper: Implement setSec')
    
    @JOverride
    def getWell(self) -> str:
        raise Exception('MetadataWrapper: Implement getWell')
    
    @JOverride
    def setWell(self, well: str):  # No return
        raise Exception('MetadataWrapper: Implement setWell')
    
    @JOverride
    def getRow(self) -> int:
        raise Exception('MetadataWrapper: Implement getRow')
    
    @JOverride
    def setRow(self, row: int):  # No return
        raise Exception('MetadataWrapper: Implement setRow')
    
    @JOverride
    def getCol(self) -> int:
        raise Exception('MetadataWrapper: Implement getCol')
    
    @JOverride
    def setCol(self, col: int):  # No return
        raise Exception('MetadataWrapper: Implement setCol')
    
    @JOverride
    def getField(self) -> int:
        raise Exception('MetadataWrapper: Implement getField')
    
    @JOverride
    def setField(self, field: int):  # No return
        raise Exception('MetadataWrapper: Implement setField')
    
    @JOverride
    def getTimepoint(self) -> int:
        raise Exception('MetadataWrapper: Implement getTimepoint')
    
    @JOverride
    def setTimepoint(self, timepoint: int):  # No return
        raise Exception('MetadataWrapper: Implement setTimepoint')
    
    @JOverride
    def getZ(self) -> int:
        raise Exception('MetadataWrapper: Implement getZ')
    
    @JOverride
    def setZ(self, z: int):  # No return
        raise Exception('MetadataWrapper: Implement setZ')
    
    @JOverride
    def getChannel(self) -> int:
        raise Exception('MetadataWrapper: Implement getChannel')
    
    @JOverride
    def setChannel(self, channel: int):  # No return
        raise Exception('MetadataWrapper: Implement setChannel')
    
    @JOverride
    def getCelltype(self) -> str:
        raise Exception('MetadataWrapper: Implement getCelltype')
    
    @JOverride
    def setCelltype(self, celltype: str):  # No return
        raise Exception('MetadataWrapper: Implement setCelltype')
    
    @JOverride
    def getMag(self) -> str:
        raise Exception('MetadataWrapper: Implement getMag')
    
    @JOverride
    def setMag(self, mag: str):  # No return
        raise Exception('MetadataWrapper: Implement setMag')
    
    @JOverride
    def getYear(self) -> int:
        raise Exception('MetadataWrapper: Implement getYear')
    
    @JOverride
    def setYear(self, year: int):  # No return
        raise Exception('MetadataWrapper: Implement setYear')
    
    @JOverride
    def getMonth(self) -> int:
        raise Exception('MetadataWrapper: Implement getMonth')
    
    @JOverride
    def setMonth(self, month: int):  # No return
        raise Exception('MetadataWrapper: Implement setMonth')
    
    @JOverride
    def getDay(self) -> int:
        raise Exception('MetadataWrapper: Implement getDay')
    
    @JOverride
    def setDay(self, day: int):  # No return
        raise Exception('MetadataWrapper: Implement setDay')
    
    @JOverride
    def getComment(self) -> str:
        raise Exception('MetadataWrapper: Implement getComment')
    
    @JOverride
    def setComment(self, comment: str):  # No return
        raise Exception('MetadataWrapper: Implement setComment')
    
    @JOverride
    def getKeyword(self) -> str:
        raise Exception('MetadataWrapper: Implement getKeyword')
    
    @JOverride
    def putKeyword(self, keyword: str):  # No return
        raise Exception('MetadataWrapper: Implement putKeyword')
    
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
        raise Exception('MetadataWrapper: Implement getSeriesName')
    
    @JOverride
    def setSeriesName(self, seriesName: str):  # No return
        raise Exception('MetadataWrapper: Implement setSeriesName')
    
    @JOverride
    def getUnits(self) -> str:
        raise Exception('MetadataWrapper: Implement getUnits')
    
    @JOverride
    def setUnits(self, units: str):  # No return
        raise Exception('MetadataWrapper: Implement setUnits')
    
    @JOverride
    def getPlateName(self) -> str:
        raise Exception('MetadataWrapper: Implement getPlateName')
    
    @JOverride
    def setPlateName(self, plateName: str):  # No return
        raise Exception('MetadataWrapper: Implement setPlateName')
    
    @JOverride
    def getPlateManufacturer(self) -> str:
        raise Exception('MetadataWrapper: Implement getPlateManufacturer')
    
    @JOverride
    def setPlateManufacturer(self, plateManufacturer: str):  # No return
        raise Exception('MetadataWrapper: Implement setPlateManufacturer')
    
    @JOverride
    def getPlateModel(self) -> str:
        raise Exception('MetadataWrapper: Implement getPlateModel')
    
    @JOverride
    def setPlateModel(self, plateModel: str):  # No return
        raise Exception('MetadataWrapper: Implement setPlateModel')
    
    @JOverride
    def getTimelineNumber(self) -> int:
        raise Exception('MetadataWrapper: Implement getTimelineNumber')
    
    @JOverride
    def setTimelineNumber(self, timelineNumber: int):  # No return
        raise Exception('MetadataWrapper: Implement setTimelineNumber')
    
    @JOverride
    def getActionNumber(self) -> int:
        raise Exception('MetadataWrapper: Implement getActionNumber')
    
    @JOverride
    def setActionNumber(self, actionNumber: int):  # No return
        raise Exception('MetadataWrapper: Implement setActionNumber')
    
    @JOverride
    def getAsString(self, property: str) -> str:
        raise Exception('MetadataWrapper: Implement getAsString')
    
    @JOverride
    def printParameters(self):  # No return
        raise Exception('MetadataWrapper: Implement raise ExceptionParameters')
    
    @JOverride
    def insertMetadataValues(self, genericFormat: str) -> str:
        raise Exception('MetadataWrapper: Implement insertMetadataValues')

    @JOverride
    def hasKey(self, key: str) -> bool:
        return key in self._store.keys()
    
    @JOverride
    def keySet(self):  # To do
        raise Exception('MetadataWrapper: Implement keySet')

    @JOverride
    def values(self):  # To do
        raise Exception('MetadataWrapper: Implement values')

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
        raise Exception('MetadataWrapper: Implement clone')
        
def wrapMetadataStore(store: Dict[str, Any]) -> MetadataWrapper:
    wrapper: MetadataWrapper = MetadataWrapper()
    wrapper.setPythonMetadataStore(store)
    
    return wrapper