# Note: Can this extend Dict (e.g. class Objs(Dict[int, Obj])) and have the objswrapper just convert
# the methods?

from __future__ import annotations
import matplotlib
from matplotlib.colors import Colormap
from prettytable import PrettyTable
from typing import Dict, List, Tuple
from typing import TYPE_CHECKING

import math
import numpy as np
import src.objects.colormaps as cmaps

from src.objects.image import Image, createImage
from src.objects.measurement import Measurement
from src.objects.obj import Obj
from src.utilities.colourfactory import getIDHues

if TYPE_CHECKING:
    from src.objects.coordinateset import CoordinateSetFactory
    from src.types.types import Point


class Objs:
    def __init__(
        self,
        name: str,
        width: int,
        height: int,
        n_slices: int,
        dpp_xy: float,
        dpp_z: float,
        spatial_units: str,
        n_frames: int,
        frame_interval: float,
        temporal_units: str,
    ):
        self._objs: Dict[int, Obj] = {}
        self._max_ID: int = 0

        self._name: str = name
        self._width: int = width
        self._height: int = height
        self._n_slices: int = n_slices
        self._dpp_xy: float = dpp_xy
        self._dpp_z: float = dpp_z
        self._spatial_units: str = spatial_units

        self._n_frames: int = n_frames
        self._frame_interval: float = frame_interval
        self._temporal_units: str = temporal_units

    def createNewObjsFromThis(self, new_objs_name: str) -> Objs:
        return Objs(
            new_objs_name,
            width=self._width,
            height=self._height,
            n_slices=self._n_slices,
            dpp_xy=self._dpp_xy,
            dpp_z=self._dpp_z,
            spatial_units=self._spatial_units,
            n_frames=self._n_frames,
            frame_interval=self._frame_interval,
            temporal_units=self._temporal_units,
        )

    def createAndAddNewObject(
        self, coordinate_set_factory: CoordinateSetFactory
    ) -> Obj:
        obj: Obj = Obj(coordinate_set_factory, self, self.getAndIncrementID())
        self.add(obj)

        return obj

    def createAndAddNewObjectWithID(
        self, coordinate_set_factory: CoordinateSetFactory, ID: int
    ) -> Obj:
        obj: Obj = Obj(coordinate_set_factory, self, ID)
        self.add(obj)

        # Updating the max_ID if necessary
        self._max_ID = max(self._max_ID, ID)

        return obj

    def createAndAddNewObjectIfMissing(
        self, coordinate_set_factory: CoordinateSetFactory, ID: int
    ) -> Obj | None:
        if ID in self._objs.keys():
            return self._objs.get(ID)
        else:
            return self.createAndAddNewObjectWithID(coordinate_set_factory, ID)

    def getName(self) -> str:
        return self._name

    def add(self, object: Obj):  # No return
        self._max_ID = max(self._max_ID, object.getID())
        self._objs[object.getID()] = object

    def getAndIncrementID(self) -> int:
        self._max_ID = self._max_ID + 1
        return self._max_ID

    def resetCollection(self):  # No return
        raise NotImplementedError("Objs: resetCollection")

    def recalculateMaxID(self):  # No return
        raise NotImplementedError("Objs: recalculateMaxID")

    def getAsSingleObject(self) -> Obj:
        raise NotImplementedError("Objs: getAsSingleObject")

    def getObjectsInFrame(self, output_objects_name: str, frame: int) -> Objs:
        raise NotImplementedError("Objs: getObjectsInFrame")

    def getNFrames(self) -> int:
        return self._n_frames

    def setNFrames(self, n_frames: int):  # No return
        self._n_frames = n_frames

    def getFrameInterval(self) -> float:
        return self._frame_interval

    def setFrameInterval(self, frame_interval: float):  # No return
        self._frame_interval = frame_interval

    def getTemporalUnit(self) -> str:
        return self._temporal_units

    def setTemporalUnit(self, temporal_unit: str):
        self._temporal_units = temporal_unit

    def duplicate(
        self,
        new_objects_name: str,
        duplicate_relationships: bool,
        duplicate_measurement: bool,
        duplicate_metadata: bool,
        add_original_duplicate_relationship: bool,
    ) -> Objs:
        raise NotImplementedError("Objs: duplicate")

    # Default methods

    def getWidth(self) -> int:
        return self._width

    def setWidth(self, width: int):  # No return
        self._width = width

    def getHeight(self) -> int:
        return self._height

    def setHeight(self, height: int):  # No return
        self._height = height

    def getNSlices(self) -> int:
        return self._n_slices

    def setNSlices(self, n_slices: int):  # No return
        self._n_slices = n_slices

    def getDppXY(self) -> float:
        return self._dpp_xy

    def setDppXY(self, dpp_xy: float):  # No return
        self._dpp_xy = dpp_xy

    def getDppZ(self) -> float:
        return self._dpp_z

    def setDppZ(self, dpp_z: float):  # No return
        self._dpp_z = dpp_z

    def getSpatialUnits(self) -> str:
        return self._spatial_units

    def setSpatialUnits(self, spatial_units: str):  # No return
        self._spatial_units = spatial_units

    def getFirst(self) -> Obj:
        raise NotImplementedError("Objs: getFirst")

    def getSpatialExtents(self) -> List[List[int]]:
        raise NotImplementedError("Objs: getSpatialExtents")

    def getSpatialLimits(self) -> List[List[int]]:
        raise NotImplementedError("Objs: getSpatialLimits")

    def getTemporalLimits(self) -> List[int]:
        raise NotImplementedError("Objs: getTemporalLimits")

    def getLargestID(self) -> int:
        raise NotImplementedError("Objs: getLargestID")

    def convertToImage(
        self,
        output_name: str,
        hues: Dict[int, float],
        bit_depth: int,
        nanBackground: bool,
        verbose: bool,
    ) -> Image:
        im: Image = self.createImage(output_name, bit_depth)

        if nanBackground:
            np_img = im.getRawImage()
            np_img.fill(np.nan)

        object: Obj
        for object in self.values():
            hue: float | None = hues[object.getID()]
            if hue is None:
                continue

            object.addToImage(image=im, hue=hue)

        return im

    def convertToImageRandomColours(self) -> Image:
        raise NotImplementedError("Objs: convertToImageRandomColours")

    def convertToImageBinary(self, name: str) -> Image:
        raise NotImplementedError("Objs: convertToImageBinary")

    def convertToImageIDColours(self) -> Image:
        hues: Dict[int, float] = getIDHues(self, False)
        image: Image = self.convertToImage(self.getName(), hues, 32, False, False)
        image.setColormap(colormap=cmaps.Random())

        return image

    def convertCentroidsToImage(
        self,
        output_name: str,
        hues: Dict[int, float],
        bit_bepth: int,
        nan_background: bool,
    ) -> Image:
        raise NotImplementedError("Objs: convertCentroidsToImage")

    def applyCalibrationFromImage(self, image: Image):  # No return
        raise NotImplementedError("Objs: applyCalibrationFromImage")

    def createImage(self, output_name: str, bit_depth: int) -> Image:
        dtype: np.dtype
        if bit_depth == 8:
            dtype = np.uint8
        elif bit_depth == 16:
            dtype = np.uint16
        elif bit_depth == 32:
            dtype = np.float32
        else:
            raise NotImplementedError("Objs: Unsupported bit depth")

        return createImage(
            image_name=output_name,
            width=self._width,
            height=self._height,
            n_channels=1,
            n_slices=self._n_slices,
            n_frames=self._n_frames,
            d_type=dtype,
            dpp_xy=self._dpp_xy,
            dpp_z=self._dpp_z,
            spatial_units=self._spatial_units,
            frame_interval=self._frame_interval,
            temporal_units=self._temporal_units,
        )

    def setNaNBackground(self, ipl):  # To do
        raise NotImplementedError("Objs: setNaNBackground")

    def getByEqualsIgnoreNameAndID(self, reference_obj: Obj) -> Obj:
        raise NotImplementedError("Objs: getByEqualsIgnoreNameAndID")

    def showMeasurements(self, measurement_names: List[str]):
        table: PrettyTable = PrettyTable()

        # Adding fixed values
        ids_col: List[int] = []
        x_mean_col: List[float] = []
        y_mean_col: List[float] = []
        z_mean_col: List[float] = []
        timepoint_col: List[int] = []

        obj: Obj
        for obj in self.values():
            ids_col.append(obj.getID())
            x_mean_col.append(obj.getXMean(True))
            y_mean_col.append(obj.getYMean(True))
            z_mean_col.append(obj.getZMean(True, False))
            timepoint_col.append(obj.getT())

        table.add_column("OBJECT_ID", ids_col)
        table.add_column("X_CENTROID (PX)", x_mean_col)
        table.add_column("Y_CENTROID (PX)", y_mean_col)
        table.add_column("Z_CENTROID (SLICE)", z_mean_col)
        table.add_column("TIMEPOINT", timepoint_col)

        meas_col: List[float] = []
        for measurement_name in measurement_names:
            meas_col = []
            obj: Obj
            for obj in self.values():
                measurement: Measurement | None = obj.getMeasurement(measurement_name)
                meas_col.append(
                    math.nan if measurement is None else measurement.getValue()
                )

            table.add_column(measurement_name, meas_col)

        print(table)

    def showMetadata(self, module, modules):  # To do
        raise NotImplementedError("Objs: showMetadata")

    def showAllMetadata(self):  # No return
        raise NotImplementedError("Objs: showAllMetadata")

    def removeParents(self, parent_objects_name: str):  # No return
        raise NotImplementedError("Objs: removeParents")

    def removeChildren(self, child_objects_name: str):  # No return
        raise NotImplementedError("Objs: removeChildren")

    def removePartners(self, partner_objects_name: str):  # No return
        raise NotImplementedError("Objs: removePartners")

    def containsPoint(self, point: Point) -> bool:
        raise NotImplementedError("Objs: containsPoint")

    def containsCoord(self, x: int, y: int, z: int) -> bool:
        raise NotImplementedError("Objs: containsCoord")

    def getLargestObject(self, t: int) -> Obj:
        raise NotImplementedError("Objs: getLargestObject")

    def getSmallestObject(self, t: int) -> Obj:
        raise NotImplementedError("Objs: getSmallestObject")

    # From Map

    def size(self) -> int:
        return len(self._objs)

    def isEmpty(self) -> bool:
        raise NotImplementedError("Objs: isEmpty")

    def containsKey(self, key: int) -> bool:
        raise NotImplementedError("Objs: containsKey")

    def containsValue(self, value: Obj) -> bool:
        raise NotImplementedError("Objs: containsValue")

    def get(self, key: int) -> Obj | None:
        return self._objs.get(key)

    def put(self, key: int, value: Obj) -> Obj | None:
        prevObj: Obj | None = self._objs.get(key)
        self._objs[key] = value

        return prevObj

    def remove(self, key: int) -> Obj:
        return self._objs.pop(key)

    def putAll(self, m: Dict[int, Obj]):  # No return
        raise NotImplementedError("Objs: putAll")

    def clear(self):  # No return
        raise NotImplementedError("Objs: clear")

    def keySet(self) -> List[int]:
        raise NotImplementedError("Objs: keySet")

    def values(self) -> List[Obj]:
        return [obj for obj in self._objs.values()]

    def entrySet(self) -> List[Tuple[int, Obj]]:
        raise NotImplementedError("Objs: values")
        # entry_set: List[Tuple[int,Obj]] = []
        # for key, value in self._objs.items():
        #     entry_set.append((key, value))

        # return entry_set

    def equals(self, o: Objs) -> bool:
        raise NotImplementedError("Objs: equals")

    def hashCode(self) -> int:
        raise NotImplementedError("Objs: hashCode")

    def getOrDefault(self, key: int, defaultValue: Obj) -> Obj:
        raise NotImplementedError("Objs: getOrDefault")

    def forEach(self, action):  # To do
        raise NotImplementedError("Objs: forEach")

    def replaceAll(self, function):  # To do
        raise NotImplementedError("Objs: replaceAll")

    def putIfAbsent(self, key: int, value: Obj) -> Obj | None:
        if self._objs.get(key) is None:
            self._objs[key] = value
            return None
        else:
            return self._objs[key]

    def replace(self, key: int, value: Obj) -> Obj:
        raise NotImplementedError("Objs: replace (key, value)")

    def computeIfAbsent(self, key, mappingFunction):  # To do
        raise NotImplementedError("Objs: computeIfAbsent")

    def computeIfPresent(self, key, remappingFunction):  # To do
        raise NotImplementedError("Objs: computeIfPresent")

    def compute(self, key, remappingFunction):  # To do
        raise NotImplementedError("Objs: compute")

    def merge(self, key, value, remappingFunction):  # To do
        raise NotImplementedError("Objs: merge")

    # Note: May also need to implement the Entry interface:

    # # def getKey(self):
    #     raise NotImplementedError('EntryWrapper: getKey')

    # # def getValue(self):
    #     raise NotImplementedError('EntryWrapper: getValue')

    # # def setValue(self, value):
    #     raise NotImplementedError('EntryWrapper: setValue')

    # # def equals(self, o):
    #     raise NotImplementedError('EntryWrapper: equals')

    # # def hashCode(self):
    #     raise NotImplementedError('EntryWrapper: hashCode')

    # # Static comparator methods (if relevant to expose)

    # @staticmethod
    # def comparingByKey():
    #     raise NotImplementedError('EntryWrapper: comparingByKey')

    # @staticmethod
    # def comparingByValue():
    #     raise NotImplementedError('EntryWrapper: comparingByValue')

    # @staticmethod
    # def comparingByKeyWithComparator(cmp):
    #     raise NotImplementedError('EntryWrapper: comparingByKey with comparator')

    # @staticmethod
    # def comparingByValueWithComparator(cmp):
    #     raise NotImplementedError('EntryWrapper: comparingByValue with comparator')
