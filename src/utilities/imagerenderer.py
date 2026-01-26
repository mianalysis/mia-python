from __future__ import annotations
from typing import TYPE_CHECKING
from jpype import JImplements, JOverride # type: ignore

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
            print(f'max {np.max(im)}')
            self._ij.py.show(im[0,0,:,:,:])
        else:
            self._ij.py.show(im)