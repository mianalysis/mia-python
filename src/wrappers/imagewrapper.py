import imagej  # type: ignore
ij =imagej.init(['io.github.mianalysis:mia-plugin:2.0.0-SNAPSHOT'])

from jpype import JImplements, JOverride  # type: ignore
from scyjava import jimport  # type: ignore
from src.utilities.imagerenderer import NotebookImageRenderer

import numpy as np

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
    def getWidth(self) -> int:
        raise Exception('ImageWrapper: Implement getWidth')
    
    @JOverride
    def getHeight(self) -> int:
        raise Exception('ImageWrapper: Implement getHeight')
    
    @JOverride
    def getNChannels(self) -> int:
        raise Exception('ImageWrapper: Implement getNChannels')
    
    @JOverride
    def getNSlices(self) -> int:
        raise Exception('ImageWrapper: Implement getNSlices')
    
    @JOverride
    def getNFrames(self) -> int:
        raise Exception('ImageWrapper: Implement getNFrames')
    
    @JOverride
    def getDppXY(self) -> float:
        raise Exception('ImageWrapper: Implement getDppXY')
    
    @JOverride
    def getDppZ(self) -> float:
        raise Exception('ImageWrapper: Implement getDppZ')
    
    @JOverride
    def getSpatialUnits(self): # To do
        raise Exception('ImageWrapper: Implement getSpatialUnits')
    
    @JOverride
    def getFrameInterval(self) -> float:
        raise Exception('ImageWrapper: Implement getFrameInterval')

    @JOverride
    def getTemporalUnit(self): # To do
        raise Exception('ImageWrapper: Implement getTemporalUnit')
    
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
    def showWithTitle(self, title: str):
        self.show(title, None, True, jimport('io.github.mianalysis.mia.object.image.DisplayModes').COLOUR, None)

    @JOverride
    def showWithLUT(self, lut): # To do
        self.show(self.getName(), lut, True, jimport('io.github.mianalysis.mia.object.image.DisplayModes').COLOUR, None)

    @JOverride
    def showAsIs(self):
        self.show(self.getName(), None, True, jimport('io.github.mianalysis.mia.object.image.DisplayModes').COLOUR, None)

    @JOverride
    def showWithOverlay(self, overlay): # To do
        self.show(self.getName(), None, True, jimport('io.github.mianalysis.mia.object.image.DisplayModes').COLOUR, overlay)

    @JOverride
    def showWithNormalisation(self, normalise: bool):
        self.show(self.getName(), None, normalise, jimport('io.github.mianalysis.mia.object.image.DisplayModes').COLOUR, None)

    @JOverride
    def showMeasurements(self, module):
        raise Exception('ImageWrapper: Implement showMeasurements')
    
    @JOverride
    def showAllMeasurements(self):
        raise Exception('ImageWrapper: Implement showAllMeasurements')
        