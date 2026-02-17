from __future__ import annotations

from matplotlib.colors import Colormap
from typing import Any, Dict, List, Tuple, TYPE_CHECKING
from xarray import DataArray

import numpy as np
import numpy.typing as npt

from src.objects.coordinateset import CoordinateSetFactory
from src.objects.measurement import Measurement
from src.utilities.imagerenderer import NotebookImageRenderer

if TYPE_CHECKING:
    from src.objects.obj import Obj
    from src.objects.objs import Objs

X: str = "col"
Y: str = "row"
C: str = "ch"
Z: str = "pln"
T: str = "t"
SPATIAL_UNITS = "spatial_units"
TEMPORAL_UNITS = "temporal_units"

class Image:
    def __init__(self, name: str, da_img: DataArray, dpp_xy: float, dpp_z: float, spatial_units: str, frame_interval: float, temporal_units: str):
        self._name: str = name
        self._da_img: DataArray = da_img
        self._dpp_xy: float = dpp_xy
        self._dpp_z: float = dpp_z
        self._spatial_units: str = spatial_units
        self._frame_interval: float = frame_interval
        self._temporal_units: str = temporal_units
        self._colormap: Colormap | str | None = None
        
        self._renderer = NotebookImageRenderer()
        
        self._measurements: Dict[str, Measurement] = {}
        
        self._x_idx: int = -1
        self._y_idx: int = -1
        self._c_idx: int = -1
        self._z_idx: int = -1
        self._t_idx: int = -1
        self._n_indices: int = 0
            
        if da_img is not None:    
            self.updateAxisIndices()
                
    def updateAxisIndices(self):
        dims = self._da_img.dims
        n_indices = 0
        
        if X in dims:
            self._x_idx = self._da_img.get_axis_num(X)
            n_indices = n_indices + 1
        
        if Y in dims:
            self._y_idx = self._da_img.get_axis_num(Y)
            n_indices = n_indices + 1
            
        if C in dims:
            self._c_idx = self._da_img.get_axis_num(C)
            n_indices = n_indices + 1
            
        if Z in dims:
            self._z_idx = self._da_img.get_axis_num(Z)
            n_indices = n_indices + 1
            
        if T in dims:
            self._t_idx = self._da_img.get_axis_num(T)
            n_indices = n_indices + 1
            
        self._n_indices = n_indices
        
    def clear(self):
        raise Exception('Image: Implement clear')
    
    def getRenderer(self):
        return self._renderer
    
    def setRenderer(self, image_renderer):
        self._renderer = image_renderer
    
    def getWidth(self) -> int:
        return self.getAxisLength(X)
    
    def getHeight(self) -> int:
        return self.getAxisLength(Y)
    
    def getNChannels(self) -> int:
        return self.getAxisLength(C)
    
    def getNSlices(self) -> int:
        return self.getAxisLength(Z)
    
    def getNFrames(self) -> int:
        return self.getAxisLength(T)
    
    def getAxisLength(self, axis_name: str) -> int:
        if axis_name not in self._da_img.dims:
            return 1
        
        axis_idx: int = self._da_img.get_axis_num(axis_name)
        return self._da_img.shape[axis_idx]
    
    def getDppXY(self) -> float:
        return self._dpp_xy
    
    def getDppZ(self) -> float:
        return self._dpp_z
    
    def getSpatialUnits(self): # To do
        return self._spatial_units
    
    def getFrameInterval(self) -> float:
        return self._frame_interval

    def getTemporalUnits(self) -> str:
        return self._temporal_units
    
    def getColormap(self) -> Colormap | str| None:
        return self._colormap
    
    def setColormap(self, colormap: Colormap | str | None):
        self._colormap = colormap
    
    def getSlice(self, x: int=-1,y: int=-1,c: int=-1,z: int=-1,t: int=-1):
        dims = self._da_img.dims
        indexers = {}
        if X in dims and x != -1:
            indexers[X] = x
        
        if Y in dims and y != -1:
            indexers[Y] = y
            
        if C in dims and c != -1:
            indexers[C] = c
            
        if Z in dims and z != -1:
            indexers[Z] = z
            
        if T in dims and t != -1:
            indexers[T] = t
                    
        return self._da_img.isel(indexers)
            
    # def getImagePlus(self):
    #     return Store.ij.py.to_imageplus(self._da_img) # type: ignore
    
    # def setImagePlus(self, imagePlus):        
    #     ij.py.sync_image(imagePlus) # type: ignore
    #     self._da_img = ij.py.from_java(imagePlus) # type: ignore
    
    def getImgPlus(self):
        raise Exception('Image: Implement getImgPlus')
    
    def setImgPlus(self, img):
        raise Exception('Image: Implement setImgPlus')
    
    def getRawImage(self) -> DataArray:
        return self._da_img
    
    def setRawImage(self, python_image: DataArray):
        self._da_img = python_image
        
        if self._da_img is not None:    
            self.updateAxisIndices()
    
    def putPixel(self, val: float, x: int, y: int, c: int=0, z: int=0, t: int=0):        
        indices: List[List[int]] = [[0]]*self._n_indices
        if self._x_idx != -1:
            indices[self._x_idx] = [x]
            
        if self._y_idx != -1:
            indices[self._y_idx] = [y]
        
        if self._c_idx != -1:
            indices[self._c_idx] = [c]
            
        if self._z_idx != -1:
            indices[self._z_idx] = [z]
            
        if self._t_idx != -1:
            indices[self._t_idx] = [t]
        
        self._da_img.data[tuple(indices)] = val

    def putAllPixels(self, vals: npt.NDArray[np.float32], x: npt.NDArray[np.int32], y: npt.NDArray[np.int32], c: npt.NDArray[np.int32] | None = None, z: npt.NDArray[np.int32] | None = None, t: npt.NDArray[np.int32] | None = None):
        indices = np.zeros((self._n_indices,len(x)),dtype=int)
        
        if self._x_idx != -1:
            indices[self._x_idx,:] = np.array(x)
            
        if self._y_idx != -1:
            indices[self._y_idx,:] = np.array(y)
            
        if self._c_idx != -1:
            indices[self._c_idx,:] = np.array(c)
            
        if self._z_idx != -1:
            indices[self._z_idx,:] = np.array(z)
            
        if self._t_idx != -1:
            indices[self._t_idx,:] = np.array(t)
        
        self._da_img.data[tuple(indices)] = vals
        
    def initialiseEmptyObjs(self, output_objects_name):
        raise Exception('Image: Implement initialiseEmptyObjs')
    
    def addObject(self, obj, hue):
        raise Exception('Image: Implement addObject')
    
    def addObjectCentroid(self, obj, hue):
        raise Exception('Image: Implement addObjectCentroid')
    
    def duplicate(self, output_image_name: str):
        raise Exception('Image: Implement duplicate')
    
    def getOverlay(self):
        raise Exception('Image: Implement getOverlay')
    
    def setOverlay(self, overlay):
        raise Exception('Image: Implement setOverlay')
        
    def convertImageToObjects(self, coordinate_set_factory: CoordinateSetFactory, output_objects_name: str, single_object: bool) -> Objs:
        return self.convertImageToObjectsGeneral(coordinate_set_factory, output_objects_name, single_object, True)

    def convertImageToSingleObjects(self, coordinate_set_factory: CoordinateSetFactory, output_objects_name: str, blackBackground: bool) -> Objs:
        return self.convertImageToObjectsGeneral(coordinate_set_factory, output_objects_name, True, blackBackground)
        
    def convertImageToObjectsGeneral(self, coordinate_set_factory: CoordinateSetFactory, output_objects_name: str, single_object: bool, black_background: bool) -> Objs:
        # This has to go here to prevent circular imports
        from src.objects.objs import Objs
        
        width: int = self.getWidth()
        height: int = self.getHeight()
        n_slices: int = self.getNSlices()
        dpp_xy: float = self.getDppXY()
        dpp_z: float = self.getDppZ()
        spatial_units: str = self.getSpatialUnits()
        n_frames: int = self.getNFrames()
        frame_interval: float = self.getFrameInterval()
        temporal_units: str = self.getTemporalUnits()
        n_channels: int = self.getNChannels()
        
        output_objs: Objs = Objs(output_objects_name, width, height, n_slices, dpp_xy, dpp_z, spatial_units, n_frames, frame_interval, temporal_units)
        
        c: int
        z: int
        t: int
        for c in range(n_channels):
            for t in range(n_frames):
                final_IDs: Dict[int, int] = {}
                
                for z in range(n_slices):
                    slice: np.ndarray = self.getSlice(c=c, z=z, t=t).data
                    
                    for x in range(width):
                        for y in range(height):
                            image_ID: int = slice[y,x] # This is indexed as row, col

                            if single_object:
                                image_ID = 1 if (black_background and image_ID != 0) or ( not black_background and image_ID == 0) else 0
                    
                            if single_object and image_ID != 0:
                                image_ID = 1
                                
                            if image_ID != 0:
                                if image_ID not in final_IDs:
                                    final_IDs[image_ID] = output_objs.getAndIncrementID()
                                
                                out_ID = final_IDs[image_ID]
                                output_objs.createAndAddNewObjectIfMissing(coordinate_set_factory, out_ID)
                                output_obj = output_objs.get(out_ID)
                                
                                if output_obj is not None:
                                    output_obj.addCoord(x,y,z)
                                                                         
                    obj: Obj                 
                    for obj in output_objs.values():
                        obj.finaliseSlice(z)
                        
        obj: Obj                 
        for obj in output_objs.values():
            obj.finalise()
                    
        return output_objs
    
    def addMeasurement(self, measurement: Measurement):
        self._measurements[measurement.getName()] = measurement
    
    def getMeasurement(self, name: str) -> Measurement | None:
        return self._measurements.get(name)
        
    def removeMeasurement(self, name: str):
        raise Exception('Image: Implement removeMeasurement')
    
    def getName(self) -> str:
        return self._name
    
    def getMeasurements(self):
        raise Exception('Image: Implement getMeasurements')
    
    def setMeasurements(self, measurements):
        raise Exception('Image: Implement setMeasurements')

    def show(self, title: str, colormap: Colormap | str | None, normalise: bool, display_mode: str, overlay):
        self._renderer.render(self, title, colormap, normalise, display_mode, overlay)

    def showMeasurements(self, module):
        raise Exception('Image: Implement showMeasurements')
    
    def showAllMeasurements(self):
        raise Exception('Image: Implement showAllMeasurements')

def createImage(image_name: str, width: int, height: int, n_channels: int, n_slices: int, n_frames: int, d_type: npt.DTypeLike, dpp_xy: float, dpp_z: float, spatial_units: str, frame_interval: float, temporal_units: str) -> Image:
    # Getting dimensions for array
    dim_lengths = [height, width]
    dim_names = [Y, X]
    coords = {X: np.arange(width)*dpp_xy, Y:np.arange(height)*dpp_xy}
    attrs = {SPATIAL_UNITS: spatial_units, TEMPORAL_UNITS: temporal_units}
    
    if n_channels > 1:
        dim_lengths.append(n_channels)
        dim_names.append(C)
        coords[C] = np.arange(n_channels)
        
    if n_slices > 1:
        dim_lengths.append(n_slices)
        dim_names.append(Z)
        coords[Z] = np.arange(n_slices)*dpp_z
        
    if n_frames > 1:
        dim_lengths.append(n_frames)
        dim_names.append(T)
        coords[T] = np.arange(n_frames)*frame_interval
    
    # Creating Numpy array
    np_arr = np.zeros(tuple(dim_lengths))
        
    return Image(image_name, DataArray(data=np_arr, coords=coords, dims=dim_names, name=image_name, attrs=attrs), dpp_xy=dpp_xy, dpp_z=dpp_z, spatial_units=spatial_units, frame_interval=frame_interval, temporal_units=temporal_units)
