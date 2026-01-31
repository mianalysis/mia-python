from __future__ import annotations
from typing import TYPE_CHECKING
from jpype import JImplements, JOverride # type: ignore

from src.utilities.store import Store

import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

if TYPE_CHECKING:
    from src.objects.image import Image
    
@JImplements('io.github.mianalysis.mia.object.image.renderer.ImageRenderer') # type: ignore
class NotebookImageRenderer:        
    @JOverride
    def render(self, image: Image, title: str, lut, normalise: bool, display_mode, overlay): # To do
        im = image.getRawImage()
        
        if isinstance(im, np.ndarray):
            da: xr.DataArray = xr.DataArray(im[:,:,0,0,0],dims=('row','col'),name=image.getName())
            
        else:
            Store.ij.py.sync_image(im) # type: ignore
            da = Store.ij.py.from_java(im) # type: ignore
        
        plt.imshow(da)
        
        