from scyjava import jimport
from typing import List

from src.objects.image import Image
from src.objects.volume import Volume
from src.utilities.store import Store

import numpy as np

JImageProcessor = jimport('ij.process.ImageProcessor')
JPrefs = jimport('ij.Prefs')
JRoi = jimport('ij.gui.Roi')
JThresholdToSelection = jimport('ij.plugin.filter.ThresholdToSelection')


# This is in a separate file so it can be accessed from both obj and volume wrappers
def getRoi(volume: Volume, slice: int):
    slice_volume: Volume = volume.getSlice(slice)
    
    slice_image: Image = slice_volume.getAsTightImage("Crop")
    slice_ipr = Store.ij.py.to_imageplus(slice_image.getRawImage()).getProcessor() # type: ignore
    slice_ipr.setThreshold(0, 0, JImageProcessor.NO_LUT_UPDATE)
    
    JPrefs.blackBackground = True
    
    roi = JThresholdToSelection().convert(slice_ipr)
    
    if roi is None:
        # If the cropped image is entire foreground, it seems to not be detected as a ROI
        if np.min(slice_image.getRawImage()):
            return JRoi(0, 0, slice_image.getWidth(), slice_image.getHeight())
        else:
            return None
    
    extents: List[List[float]] = slice_volume.getExtents(True, False)
    roi.translate(extents[0][0], extents[1][0])
    
    return roi
