from __future__ import annotations
from typing import Any, Dict


FILENAME: str = "Filename"
FILEPATH: str = "Filepath"
WELL: str = "Well"
ROW: str = "Row"
COL: str = "Col"
FIELD: str = "Field"
TIMEPOINT: str = "Timepoint"
ZPOSITION: str = "Z-position"
CHANNEL: str = "Channel"
YEAR: str = "Year"
MONTH: str = "Month"
DAY: str = "Day"
HOUR: str = "Hour"
MINUTE: str = "Minute"
SECOND: str = "Second"
CELLTYPE: str = "CellType"
MAGNIFICATION: str = "Magnification"
COMMENT: str = "Comment"
FILE: str = "File"
EXTENSION: str = "Extension"
KEYWORD: str = "Keyword"
SERIES_NUMBER: str = "Series number"
SERIES_NAME: str = "Series name"
UNITS: str = "Units"
PLATE_NAME: str = "Plate name"
PLATE_MANUFACTURER: str = "Plate manufacturer"
PLATE_MODEL: str = "Plate model"
TIMELINE_NUMBER: str = "Timeline number"
ACTION_NUMBER: str = "Action number"
AREA_NAME: str = "Area name"


class Metadata:
    def __init__(self):
        self._store: Dict[str, Any] = {}

    def getPythonMetadataStore(self) -> Dict[str, Any]:
        return self._store

    def setPythonMetadataStore(self, store: Dict[str, Any]):  # No return
        self._store = store

    def getFilename(self) -> str:
        return self._store[FILENAME]

    def setFilename(self, filename: str):  # No return
        self._store[FILENAME] = filename

    def getFilepath(self) -> str:
        return self._store[FILEPATH]

    def setFilepath(self, filepath: str):  # No return
        self._store[FILEPATH] = filepath

    def getExt(self) -> str:
        return self._store[EXTENSION]

    def setExt(self, ext: str):  # No return
        self._store[EXTENSION] = ext

    def getFile(self) -> str:
        if FILE not in self._store:
            return ""

        return self._store[FILE]

    def setFile(self, file):  # To do
        self._store[FILE] = file

    def getHour(self) -> int:
        raise NotImplementedError("Metadata: getHour")

    def setHour(self, hour: int):  # No return
        raise NotImplementedError("Metadata: setHour")

    def getMin(self) -> int:
        raise NotImplementedError("Metadata: getMin")

    def setMin(self, min: int):  # No return
        raise NotImplementedError("Metadata: setMin")

    def getSec(self) -> int:
        raise NotImplementedError("Metadata: getSec")

    def setSec(self, sec: int):  # No return
        raise NotImplementedError("Metadata: setSec")

    def getWell(self) -> str:
        raise NotImplementedError("Metadata: getWell")

    def setWell(self, well: str):  # No return
        raise NotImplementedError("Metadata: setWell")

    def getRow(self) -> int:
        raise NotImplementedError("Metadata: getRow")

    def setRow(self, row: int):  # No return
        raise NotImplementedError("Metadata: setRow")

    def getCol(self) -> int:
        raise NotImplementedError("Metadata: getCol")

    def setCol(self, col: int):  # No return
        raise NotImplementedError("Metadata: setCol")

    def getField(self) -> int:
        raise NotImplementedError("Metadata: getField")

    def setField(self, field: int):  # No return
        raise NotImplementedError("Metadata: setField")

    def getTimepoint(self) -> int:
        raise NotImplementedError("Metadata: getTimepoint")

    def setTimepoint(self, timepoint: int):  # No return
        raise NotImplementedError("Metadata: setTimepoint")

    def getZ(self) -> int:
        raise NotImplementedError("Metadata: getZ")

    def setZ(self, z: int):  # No return
        raise NotImplementedError("Metadata: setZ")

    def getChannel(self) -> int:
        raise NotImplementedError("Metadata: getChannel")

    def setChannel(self, channel: int):  # No return
        raise NotImplementedError("Metadata: setChannel")

    def getCelltype(self) -> str:
        raise NotImplementedError("Metadata: getCelltype")

    def setCelltype(self, celltype: str):  # No return
        raise NotImplementedError("Metadata: setCelltype")

    def getMag(self) -> str:
        raise NotImplementedError("Metadata: getMag")

    def setMag(self, mag: str):  # No return
        raise NotImplementedError("Metadata: setMag")

    def getYear(self) -> int:
        raise NotImplementedError("Metadata: getYear")

    def setYear(self, year: int):  # No return
        raise NotImplementedError("Metadata: setYear")

    def getMonth(self) -> int:
        raise NotImplementedError("Metadata: getMonth")

    def setMonth(self, month: int):  # No return
        raise NotImplementedError("Metadata: setMonth")

    def getDay(self) -> int:
        raise NotImplementedError("Metadata: getDay")

    def setDay(self, day: int):  # No return
        raise NotImplementedError("Metadata: setDay")

    def getComment(self) -> str:
        raise NotImplementedError("Metadata: getComment")

    def setComment(self, comment: str):  # No return
        raise NotImplementedError("Metadata: setComment")

    def getKeyword(self) -> str:
        raise NotImplementedError("Metadata: getKeyword")

    def putKeyword(self, keyword: str):  # No return
        raise NotImplementedError("Metadata: putKeyword")

    def getSeriesNumber(self) -> int:
        if SERIES_NUMBER not in self._store:
            return -1

        if self._store[SERIES_NUMBER] is None:
            return -1
        else:
            return self._store[SERIES_NUMBER]

    def setSeriesNumber(self, seriesNumber: int):  # No return
        self._store[SERIES_NUMBER] = seriesNumber

    def getSeriesName(self) -> str:
        raise NotImplementedError("Metadata: getSeriesName")

    def setSeriesName(self, seriesName: str):  # No return
        raise NotImplementedError("Metadata: setSeriesName")

    def getUnits(self) -> str:
        raise NotImplementedError("Metadata: getUnits")

    def setUnits(self, units: str):  # No return
        raise NotImplementedError("Metadata: setUnits")

    def getPlateName(self) -> str:
        raise NotImplementedError("Metadata: getPlateName")

    def setPlateName(self, plateName: str):  # No return
        raise NotImplementedError("Metadata: setPlateName")

    def getPlateManufacturer(self) -> str:
        raise NotImplementedError("Metadata: getPlateManufacturer")

    def setPlateManufacturer(self, plateManufacturer: str):  # No return
        raise NotImplementedError("Metadata: setPlateManufacturer")

    def getPlateModel(self) -> str:
        raise NotImplementedError("Metadata: getPlateModel")

    def setPlateModel(self, plateModel: str):  # No return
        raise NotImplementedError("Metadata: setPlateModel")

    def getTimelineNumber(self) -> int:
        raise NotImplementedError("Metadata: getTimelineNumber")

    def setTimelineNumber(self, timelineNumber: int):  # No return
        raise NotImplementedError("Metadata: setTimelineNumber")

    def getActionNumber(self) -> int:
        raise NotImplementedError("Metadata: getActionNumber")

    def setActionNumber(self, actionNumber: int):  # No return
        raise NotImplementedError("Metadata: setActionNumber")

    def getAsString(self, property: str) -> str:
        raise NotImplementedError("Metadata: getAsString")

    def printParameters(self):  # No return
        raise NotImplementedError("Metadata: raise NotImplementedErrorParameters")

    def insertMetadataValues(self, genericFormat: str) -> str:
        raise NotImplementedError("Metadata: insertMetadataValues")

    def hasKey(self, key: str) -> bool:
        return key in self._store.keys()

    def keySet(self):  # To do
        raise NotImplementedError("Metadata: keySet")

    def values(self):  # To do
        raise NotImplementedError("Metadata: values")

    def clear(self):  # No return
        self._store = {}

    def put(self, key: str, value: Any):
        self._store[key] = value

    def get(self, key: str) -> Any:
        return self._store[key]

    def remove(self, key: str) -> Any:
        item = self._store[key]
        self._store.pop(key)

        return item

    def clone(self) -> Metadata:
        raise NotImplementedError("Metadata: clone")
