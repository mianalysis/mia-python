import imagej
ij =imagej.init(['io.github.mianalysis:mia-plugin:2.0.0-SNAPSHOT'])

from jpype import JImplements, JOverride
from scyjava import jimport
from src.wrappers.imagerenderer import NotebookImageRenderer

import numpy as np
import PIL

@JImplements('io.github.mianalysis.mia.object.image.ImageI')
class ImageWrapper:
    def __init__(self, name, img):
        self._name = name
        self._np_img = img
        self._renderer = NotebookImageRenderer()
                
    @JOverride
    def getRenderer(self):
        if (ImageI.getUseGlobalImageRenderer()):
            return ImageI.getGlobalImageRenderer()
        else:
            return self._renderer
    
    @JOverride
    def clear(self):
        print('ImageWrapper: Implement clear')
    
    @JOverride
    def setRenderer(self, imageRenderer):
        self._renderer = imageRenderer
    
    @JOverride
    def getWidth(self):
        print('ImageWrapper: Implement getWidth')
    
    @JOverride
    def getHeight(self):
        print('ImageWrapper: Implement getHeight')
    
    @JOverride
    def getNChannels(self):
        print('ImageWrapper: Implement getNChannels')
    
    @JOverride
    def getNSlices(self):
        print('ImageWrapper: Implement getNSlices')
    
    @JOverride
    def getNFrames(self):
        print('ImageWrapper: Implement getNFrames')
    
    @JOverride
    def getImagePlus(self):
        return ij.py.to_imageplus(self._np_img)
    
    @JOverride
    def setImagePlus(self, imagePlus):        
        ij.py.sync_image(imagePlus)
        self._np_img = ij.py.from_java(imagePlus)
        print(self._np_img)
    
    @JOverride
    def getImgPlus(self):
        print('ImageWrapper: Implement getImgPlus')
    
    @JOverride
    def setImgPlus(self, img):
        print('ImageWrapper: Implement setImgPlus')

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
        print('ImageWrapper: Implement initialiseEmptyObjs')
    
    @JOverride
    def addObject(self, obj, hue):
        print('ImageWrapper: Implement addObject')
    
    @JOverride
    def addObjectCentroid(self, obj, hue):
        print('ImageWrapper: Implement addObjectCentroid')
    
    @JOverride
    def duplicate(self, outputImageName):
        print('ImageWrapper: Implement duplicate')
    
    @JOverride
    def getOverlay(self):
        print('ImageWrapper: Implement getOverlay')
    
    @JOverride
    def setOverlay(self, overlay):
        print('ImageWrapper: Implement setOverlay')
    
    @JOverride
    def convertImageToObjects(self, outputObjectsName):
        print('ImageWrapper: Implement convertImageToObjects with 1 parameter')
    
    @JOverride
    def convertImageToObjects(self, outputObjectsName, singleObject):
        print('ImageWrapper: Implement convertImageToObjects with 2 parameters')
    
    @JOverride
    def convertImageToObjects(self, volumeType, outputObjectsName):
        print('ImageWrapper: Implement convertImageToObjects with VolumeType and 2 parameters')

    @JOverride
    def convertImageToObjects(self, volumeType, outputObjectsName, singleObject):
        print('ImageWrapper: Implement convertImageToObjects with 3 parameters')
        
    @JOverride
    def convertImageToObjects(self, volumeType, outputObjectsName, singleObject):
        print('ImageWrapper: Implement convertImageToObjects with VolumeType and 3 parameters')

    @JOverride
    def convertImageToSingleObjects(self, volumeType, outputObjectsName, blackBackground):
        print('ImageWrapper: Implement convertImageToSingleObjects')
        
    @JOverride
    def addMeasurement(self, measurement):
        print('ImageWrapper: Implement addMeasurement')
    
    @JOverride
    def getMeasurement(self, name):
        print('ImageWrapper: Implement getMeasurement')
        
    @JOverride
    def removeMeasurement(self, name):
        print('ImageWrapper: Implement removeMeasurement')
    
    @JOverride
    def getName(self):
        return self._name
    
    @JOverride
    def getMeasurements(self):
        print('ImageWrapper: Implement getMeasurements')
    
    @JOverride
    def setMeasurements(self, measurements):
        print('ImageWrapper: Implement setMeasurements')

    @JOverride
    def show(self, title, lut, normalise, display_mode, overlay):
        self._renderer.render(self, title, lut, normalise, display_mode, overlay)

    @JOverride
    def showMeasurements(self, module):
        # ImageI.showMeasurements(module)
        print('ImageWrapper: Implement showMeasurements')
    
    @JOverride
    def showAllMeasurements(self):
        print('ImageWrapper: Implement showAllMeasurements')
        