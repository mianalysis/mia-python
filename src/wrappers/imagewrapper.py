import imagej

ij = imagej.init(['io.github.mianalysis:mia-plugin:2.0.0-SNAPSHOT'])

from jpype import JImplements, JOverride  # type: ignore
from scyjava import jimport  # type: ignore

from src.objects.image import Image
from src.utilities.imagerenderer import NotebookImageRenderer

import numpy as np

JImage = jimport('io.github.mianalysis.mia.object.image.ImageI')
JDisplayModes = jimport('io.github.mianalysis.mia.object.image.ImageI.DisplayModes')

@JImplements('io.github.mianalysis.mia.object.image.ImageI')
class ImageWrapper:
    def __init__(self):
        self._renderer = NotebookImageRenderer(ij)

    def getPythonImage(self) -> Image:
        return self._img
    
    def setPythonImage(self, img: Image):  # No return
        self._img = img
            
    @JOverride
    def clear(self):
        raise Exception('ImageWrapper: Implement clear')
    
    @JOverride
    def getRenderer(self):
        if (JImage.getUseGlobalImageRenderer()):
            return JImage.getGlobalImageRenderer()
        else:
            return self._img.getRenderer()
    
    @JOverride
    def setRenderer(self, imageRenderer):
        self._renderer = imageRenderer
    
    @JOverride
    def getWidth(self) -> int:
        return self._img.getWidth()
    
    @JOverride
    def getHeight(self) -> int:
        return self._img.getHeight()
    
    @JOverride
    def getNChannels(self) -> int:
        return self._img.getNChannels()
    
    @JOverride
    def getNSlices(self) -> int:
        return self._img.getNSlices()
    
    @JOverride
    def getNFrames(self) -> int:
        return self._img.getNFrames()
    
    @JOverride
    def getDppXY(self) -> float:
        return self._img.getDppXY()
    
    @JOverride
    def getDppZ(self) -> float:
        return self._img.getDppZ()
    
    @JOverride
    def getSpatialUnits(self): # To do
        return self._img.getSpatialUnits()
    
    @JOverride
    def getFrameInterval(self) -> float:
        return self._img.getFrameInterval()

    @JOverride
    def getTemporalUnit(self): # To do
        raise Exception('ImageWrapper: Implement getTemporalUnit')
    
    @JOverride
    def getImagePlus(self):
        return ij.py.to_imageplus(self._img.getRawImage()) # type: ignore
    
    @JOverride
    def setImagePlus(self, imagePlus):        
        ij.py.sync_image(imagePlus) # type: ignore
        self._img.setRawImage(ij.py.from_java(imagePlus)) # type: ignore
        
    @JOverride
    def getImgPlus(self):
        raise Exception('ImageWrapper: Implement getImgPlus')
    
    @JOverride
    def setImgPlus(self, img):
        raise Exception('ImageWrapper: Implement setImgPlus')

    @JOverride
    def getRawImage(self):
        return self._img.getRawImage()
    
    @JOverride
    def setRawImage(self, image): # To do
        self._img.setRawImage(image)
    
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
    def duplicate(self, outputImageName: str):
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
    def getName(self) -> str:
        return self._img.getName()
    
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
    def showWithTitle(self, title: str):
        self.show(title, None, True, JDisplayModes.COLOUR, None)

    @JOverride
    def showWithLUT(self, lut): # To do
        self.show(self.getName(), lut, True, JDisplayModes.COLOUR, None)

    @JOverride
    def showAsIs(self):
        self.show(self.getName(), None, True, JDisplayModes.COLOUR, None)

    @JOverride
    def showWithOverlay(self, overlay): # To do
        self.show(self.getName(), None, True, JDisplayModes.COLOUR, overlay)

    @JOverride
    def showWithNormalisation(self, normalise: bool):
        self.show(self.getName(), None, normalise, JDisplayModes.COLOUR, None)

    @JOverride
    def showMeasurements(self, module):
        raise Exception('ImageWrapper: Implement showMeasurements')
    
    @JOverride
    def showAllMeasurements(self):
        raise Exception('ImageWrapper: Implement showAllMeasurements')

def wrapImage(img: Image) -> ImageWrapper:
    image_wrapper: ImageWrapper = ImageWrapper()
    image_wrapper.setPythonImage(img)
    
    return image_wrapper 