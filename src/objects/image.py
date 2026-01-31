from typing import Dict
from xarray import DataArray

from src.objects.coordinateset import CoordinateSetFactory
from src.objects.measurement import Measurement
from src.objects.objs import Objs
from src.utilities.imagerenderer import NotebookImageRenderer

X: str = "col"
Y: str = "row"
C: str = "ch"
Z: str = "pln"
T: str = "t"

class Image:
    def __init__(self, name, da_img: DataArray):
        self._name = name
        self._da_img: DataArray = da_img
        self._renderer = NotebookImageRenderer()
        
        self._measurements: Dict[str, Measurement] = {}
            
    def clear(self):
        raise Exception('Image: Implement clear')
    
    def getRenderer(self):
        return self._renderer
    
    def setRenderer(self, image_renderer):
        self._renderer = image_renderer
    
    def getWidth(self) -> int:
        return self.getAxisLength(X)
    
    def getHeight(self) -> int:
        return self.getAxisLength(Y)
    
    def getNChannels(self) -> int:
        return self.getAxisLength(C)
    
    def getNSlices(self) -> int:
        return self.getAxisLength(Z)
    
    def getNFrames(self) -> int:
        return self.getAxisLength(T)
    
    def getAxisLength(self, axis_name: str) -> int:
        if axis_name not in self._da_img.dims:
            return 1
        
        axis_idx: int = self._da_img.get_axis_num(axis_name)
        return self._da_img.shape[axis_idx]
    
    def getDppXY(self) -> float:
        # Possibly use the following
        # return self._da_img.coords[X].diff(X).mean().item()
        print('Image: Implement getDppXY')
        return 1.0
    
    def getDppZ(self) -> float:
        print('Image: Implement getDppZ')
        return 1.0
    
    def getSpatialUnits(self): # To do
        print('Image: Implement getSpatialUnits')
        return "px"
    
    def getFrameInterval(self) -> float:
        print('Image: Implement getFrameInterval')
        return 1.0

    def getTemporalUnit(self): # To do
        print('Image: Implement getTemporalUnit')
        return "frames"
    
    def getImagePlus(self):
        return ij.py.to_imageplus(self._da_img) # type: ignore
    
    def setImagePlus(self, imagePlus):        
        ij.py.sync_image(imagePlus) # type: ignore
        self._da_img = ij.py.from_java(imagePlus) # type: ignore
    
    def getImgPlus(self):
        raise Exception('Image: Implement getImgPlus')
    
    def setImgPlus(self, img):
        raise Exception('Image: Implement setImgPlus')
    
    def getRawImage(self) -> DataArray:
        return self._da_img
    
    def setRawImage(self, python_image: DataArray):
        self._da_img = python_image
    
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
        
    def convertImageToObjects(self, coordinate_set_factory: CoordinateSetFactory, output_objects_name: str, single_object: bool) -> Objs:
        return self.convertImageToObjectsGeneral(coordinate_set_factory, output_objects_name, single_object, True)

    def convertImageToSingleObjects(self, coordinate_set_factory: CoordinateSetFactory, output_objects_name: str, blackBackground: bool) -> Objs:
        return self.convertImageToObjectsGeneral(coordinate_set_factory, output_objects_name, True, blackBackground)
        
    def convertImageToObjectsGeneral(self, coordinate_set_factory: CoordinateSetFactory, output_objects_name: str, single_object: bool, blackBackground: bool) -> Objs:
        raise Exception('ImageWrapper: Implement convertImageToObjects')
    
    def addMeasurement(self, measurement: Measurement):
        self._measurements[measurement.getName()] = measurement
    
    def getMeasurement(self, name: str) -> Measurement | None:
        return self._measurements.get(name)
        
    def removeMeasurement(self, name: str):
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
        