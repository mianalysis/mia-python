from src.utilities.imagerenderer import NotebookImageRenderer

import imagej
import numpy as np

ij = imagej.init(['io.github.mianalysis:mia-plugin:2.0.0-SNAPSHOT'])

class Image:
    def __init__(self, name, np_img: np.ndarray):
        self._name = name
        self._np_img: np.ndarray = np_img
        self._renderer = NotebookImageRenderer(ij)
            
    def clear(self):
        raise Exception('Image: Implement clear')
    
    def getRenderer(self):
        return self._renderer
    
    def setRenderer(self, image_renderer):
        self._renderer = image_renderer
    
    def getWidth(self) -> int:
        raise Exception('Image: Implement getWidth')
    
    def getHeight(self) -> int:
        raise Exception('Image: Implement getHeight')
    
    def getNChannels(self) -> int:
        raise Exception('Image: Implement getNChannels')
    
    def getNSlices(self) -> int:
        raise Exception('Image: Implement getNSlices')
    
    def getNFrames(self) -> int:
        raise Exception('Image: Implement getNFrames')
    
    def getDppXY(self) -> float:
        raise Exception('Image: Implement getDppXY')
    
    def getDppZ(self) -> float:
        raise Exception('Image: Implement getDppZ')
    
    def getSpatialUnits(self): # To do
        raise Exception('Image: Implement getSpatialUnits')
    
    def getFrameInterval(self) -> float:
        raise Exception('Image: Implement getFrameInterval')

    def getTemporalUnit(self): # To do
        raise Exception('Image: Implement getTemporalUnit')
    
    def getImagePlus(self):
        return ij.py.to_imageplus(self._np_img) # type: ignore
    
    def setImagePlus(self, imagePlus):        
        ij.py.sync_image(imagePlus) # type: ignore
        self._np_img = ij.py.from_java(imagePlus) # type: ignore
        raise Exception(self._np_img)
    
    def getImgPlus(self):
        raise Exception('Image: Implement getImgPlus')
    
    def setImgPlus(self, img):
        raise Exception('Image: Implement setImgPlus')
    
    def getRawImage(self) -> np.ndarray:
        return self._np_img
    
    def setRawImage(self, python_image: np.ndarray):
        self._np_img = python_image
    
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
        
    def convertImageToObjects(self, coordinate_set_factory, output_objects_name, single_object):
        raise Exception('Image: Implement convertImageToObjects')

    def convertImageToSingleObjects(self, coordinate_set_factory, output_objects_name, blackBackground):
        raise Exception('Image: Implement convertImageToSingleObjects')
        
    def addMeasurement(self, measurement):
        raise Exception('Image: Implement addMeasurement')
    
    def getMeasurement(self, name):
        raise Exception('Image: Implement getMeasurement')
        
    def removeMeasurement(self, name):
        raise Exception('Image: Implement removeMeasurement')
    
    def getName(self) -> str:
        return self._name
    
    def getMeasurements(self):
        raise Exception('Image: Implement getMeasurements')
    
    def setMeasurements(self, measurements):
        raise Exception('Image: Implement setMeasurements')

    def show(self, title: str, lut, normalise: bool, display_mode: str, overlay):
        self._renderer.render(self, title, lut, normalise, display_mode, overlay)
        
    def showWithTitle(self, title: str):
        self.show(title, None, True, 'COLOUR', None)

    def showWithLUT(self, lut): # To do
        self.show(self.getName(), lut, True, 'COLOUR', None)

    def showAsIs(self):
        self.show(self.getName(), None, True, 'COLOUR', None)

    def showWithOverlay(self, overlay): # To do
        self.show(self.getName(), None, True, 'COLOUR', overlay)

    def showWithNormalisation(self, normalise: bool):
        self.show(self.getName(), None, normalise, 'COLOUR', None)

    def showMeasurements(self, module):
        raise Exception('Image: Implement showMeasurements')
    
    def showAllMeasurements(self):
        raise Exception('Image: Implement showAllMeasurements')
        