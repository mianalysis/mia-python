from __future__ import annotations
from typing import TYPE_CHECKING
from jpype import JImplements, JOverride # type: ignore

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

if TYPE_CHECKING:
    from src.objects.image import Image
    
@JImplements('io.github.mianalysis.mia.object.image.renderer.ImageRenderer') # type: ignore
class NotebookImageRenderer:         
    def __init__(self, ij):
        self._ij = ij
        
    @JOverride
    def render(self, image: Image, title: str, lut, normalise: bool, display_mode, overlay): # To do
        im = image.getRawImage()
        
        if isinstance(im, np.ndarray):
            da: xr.DataArray = xr.DataArray(im[:,:,0,0,0],dims=('row','col'),name=image.getName())
            
        else:
            self._ij.py.sync_image(im) # type: ignore
            da = self._ij.py.from_java(im) # type: ignore
        
        plt.imshow(da)
        
        