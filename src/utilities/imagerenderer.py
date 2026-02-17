from __future__ import annotations
from typing import TYPE_CHECKING
from jpype import JImplements, JOverride # type: ignore
from matplotlib.widgets import Slider
from pandas.core import base
from xarray import DataArray

from src.utilities.store import Store

import matplotlib.pyplot as plt
import numpy as np

if TYPE_CHECKING:
    from src.objects.image import Image

X: str = "col"
Y: str = "row"
C: str = "ch"
Z: str = "pln"
T: str = "t"

@JImplements('io.github.mianalysis.mia.object.image.renderer.ImageRenderer') # type: ignore
class NotebookImageRenderer:       
    @JOverride
    def render(self, image: Image, title: str, lut, normalise: bool, display_mode, overlay): # To do
        self._c = 0
        self._z = 0
        self._t = 0
        self._n_channels = image.getNChannels()
        self._n_slices = image.getNSlices()
        self._n_frames = image.getNFrames()
    
        # Getting image
        self._da: DataArray = getDataArray(image)
        
        self.fig, self.ax = plt.subplots(num='  ')
        self.ax.set_axis_off()
        self.fig.tight_layout()        
                   
        # Determining positions        
        base_pos: float = 0
        base_pos = base_pos + 0.05 if image.getNChannels() > 1 else base_pos
        base_pos = base_pos + 0.05 if image.getNSlices() > 1 else base_pos
        base_pos = base_pos + 0.05 if image.getNFrames() > 1 else base_pos
        
        # Doing initial render
        da_slice: DataArray = getSlice(self._da, c=self._c, z=self._z, t=self._t)
        self._im_ax = self.fig.add_axes((0.05,base_pos+0.1,0.9,0.8-base_pos))
        self._canvas = self._im_ax.imshow(da_slice, aspect='equal')
        self._im_ax.set_axis_off()
        self._im_ax.set_title(title)        
                
        if image.getNChannels() > 1:
            self.c_slider_axes = self.fig.add_axes((0.15, base_pos, 0.7, 0.03))
            self._c_slider = Slider(
                ax=self.c_slider_axes,
                label="C",
                valmin=0,
                valmax=self._n_channels-1,
                valinit=self._c,
                valstep=np.linspace(0, self._n_channels-1, self._n_channels)
            )
            self._c_slider.on_changed(self.updateC)
            base_pos -= 0.05
        
        if image.getNSlices() > 1:
            self.z_slider_axes = self.fig.add_axes((0.15, base_pos, 0.7, 0.03))
            self._z_slider = Slider(
                ax=self.z_slider_axes,
                label="Z",
                valmin=0,
                valmax=self._n_slices-1,
                valinit=self._z,
                valstep=np.linspace(0, self._n_slices-1, self._n_slices)
            )
            self._z_slider.on_changed(self.updateZ)
            base_pos -= 0.05
        
        if image.getNFrames() > 1:
            self.t_slider_axes = self.fig.add_axes((0.15, base_pos, 0.7, 0.03))
            self._t_slider = Slider(
                ax=self.t_slider_axes,
                label="T",
                valmin=0,
                valmax=self._n_frames-1,
                valinit=self._t,
                valstep=np.linspace(0, self._n_frames-1, self._n_frames)
            )
            self._t_slider.on_changed(self.updateT)
            
        return None
    
    def updateC(self, val):
        self._c = int(val)
        self.update()
        
    def updateZ(self, val):
        self._z = int(val)
        self.update()
        
    def updateT(self, val):
        self._t = int(val)
        self.update()
        
    def update(self):
        da_slice: DataArray = getSlice(self._da, c=self._c, z=self._z, t=self._t)
        self._canvas.set_data(da_slice)
        self.fig.canvas.draw_idle()
        
def getDataArray(image: Image) -> DataArray:
    raw_image = image.getRawImage()
    
    if isinstance(raw_image, DataArray):
         return raw_image
        
    elif isinstance(raw_image, np.ndarray):
        return DataArray(raw_image[:,:,0,0,0],dims=('row','col'),name=image.getName())
        
    else:
        Store.ij.py.sync_image(raw_image) # type: ignore
        return Store.ij.py.from_java(raw_image) # type: ignore
            
def getSlice(da: DataArray, x: int=-1,y: int=-1,c: int=-1,z: int=-1,t: int=-1):
    dims = da.dims
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
                
    return da.isel(indexers)
