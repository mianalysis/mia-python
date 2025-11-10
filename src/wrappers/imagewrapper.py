import imagej
ij =imagej.init(['io.github.mianalysis:mia-plugin:2.0.0-SNAPSHOT'])

from jpype import JImplements, JOverride
from scyjava import jimport
from src.utilities.imagerenderer import NotebookImageRenderer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types.JPype import *

import numpy as np
import PIL

JImage = jimport('io.github.mianalysis.mia.object.image.ImageI')

@JImplements('io.github.mianalysis.mia.object.image.ImageI')
class ImageWrapper:
    def __init__(self, name, img):
        self._name = name
        self._np_img = img
        self._renderer = NotebookImageRenderer()
                
    @JOverride
    def getRenderer(self):
        if (JImage.getUseGlobalImageRenderer()):
            return JImage.getGlobalImageRenderer()
        else:
            return self._renderer
    
    @JOverride
    def clear(self):
        raise Exception('ImageWrapper: Implement clear')
    
    @JOverride
    def setRenderer(self, imageRenderer):
        self._renderer = imageRenderer
    
    @JOverride
    def getWidth(self):
        raise Exception('ImageWrapper: Implement getWidth')
    
    @JOverride
    def getHeight(self):
        raise Exception('ImageWrapper: Implement getHeight')
    
    @JOverride
    def getNChannels(self):
        raise Exception('ImageWrapper: Implement getNChannels')
    
    @JOverride
    def getNSlices(self):
        raise Exception('ImageWrapper: Implement getNSlices')
    
    @JOverride
    def getNFrames(self):
        raise Exception('ImageWrapper: Implement getNFrames')
    
    @JOverride
    def getImagePlus(self):
        return ij.py.to_imageplus(self._np_img) # type: ignore
    
    @JOverride
    def setImagePlus(self, imagePlus):        
        ij.py.sync_image(imagePlus) # type: ignore
        self._np_img = ij.py.from_java(imagePlus) # type: ignore
        raise Exception(self._np_img)
    
    @JOverride
    def getImgPlus(self):
        raise Exception('ImageWrapper: Implement getImgPlus')
    
    @JOverride
    def setImgPlus(self, img):
        raise Exception('ImageWrapper: Implement setImgPlus')

    @JOverride
    def getRawImage(self):
        return self._np_img
    
    @JOverride
    def setRawImage(self, image):
        if isinstance(self._np_img,np.ndarray):
            self._np_img = image
        else:
            raise TypeError("Error in ImageWrapper.setRawImage(image).  Image not instance of numpy.ndarray.")
    
    @JOverride
    def initialiseEmptyObjs(self, outputObjectsName):
        raise Exception('ImageWrapper: Implement initialiseEmptyObjs')
    
    @JOverride
    def addObject(self, obj, hue):
        raise Exception('ImageWrapper: Implement addObject')
    
    @JOverride
    def addObjectCentroid(self, obj, hue):
        raise Exception('ImageWrapper: Implement addObjectCentroid')
    
    @JOverride
    def duplicate(self, outputImageName):
        raise Exception('ImageWrapper: Implement duplicate')
    
    @JOverride
    def getOverlay(self):
        raise Exception('ImageWrapper: Implement getOverlay')
    
    @JOverride
    def setOverlay(self, overlay):
        raise Exception('ImageWrapper: Implement setOverlay')
        
    @JOverride
    def convertImageToObjects(self, coordinate_set_factory, output_objects_name, single_object):
        raise Exception('ImageWrapper: Implement convertImageToObjects')

    @JOverride
    def convertImageToSingleObjects(self, coordinate_set_factory, output_objects_name, blackBackground):
        raise Exception('ImageWrapper: Implement convertImageToSingleObjects')
        
    @JOverride
    def addMeasurement(self, measurement):
        raise Exception('ImageWrapper: Implement addMeasurement')
    
    @JOverride
    def getMeasurement(self, name):
        raise Exception('ImageWrapper: Implement getMeasurement')
        
    @JOverride
    def removeMeasurement(self, name):
        raise Exception('ImageWrapper: Implement removeMeasurement')
    
    @JOverride
    def getName(self):
        return self._name
    
    @JOverride
    def getMeasurements(self):
        raise Exception('ImageWrapper: Implement getMeasurements')
    
    @JOverride
    def setMeasurements(self, measurements):
        raise Exception('ImageWrapper: Implement setMeasurements')

    @JOverride
    def show(self, title, lut, normalise, display_mode, overlay):
        self._renderer.render(self, title, lut, normalise, display_mode, overlay)

    @JOverride
    def showMeasurements(self, module):
        # ImageI.showMeasurements(module)
        raise Exception('ImageWrapper: Implement showMeasurements')
    
    @JOverride
    def showAllMeasurements(self):
        raise Exception('ImageWrapper: Implement showAllMeasurements')
        