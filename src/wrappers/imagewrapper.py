from __future__ import annotations

from jpype import JImplements, JOverride  # type: ignore
from scyjava import jimport  # type: ignore
from typing import TYPE_CHECKING
from weakref import WeakKeyDictionary
from xarray import DataArray

from src.objects.image import Image
from src.objects.measurement import Measurement
from src.objects.objs import Objs
from src.types.JLUT import JLUT
from src.utilities.imagerenderer import NotebookImageRenderer
from src.utilities.store import Store
from src.wrappers.coordinatesetwrapper import CoordinateSetFactoryWrapper
from src.wrappers.measurementwrapper import MeasurementWrapper, wrapMeasurement

if TYPE_CHECKING:
    from src.wrappers.objswrapper import ObjsWrapper

JDisplayModes = jimport('io.github.mianalysis.mia.object.image.ImageI.DisplayModes')
JImagePlus = jimport('ij.ImagePlus')
JImage = jimport('io.github.mianalysis.mia.object.image.ImageI')


_wrapper_cache: WeakKeyDictionary[Image, ImageWrapper] = WeakKeyDictionary()

@JImplements('io.github.mianalysis.mia.object.image.ImageI')
class ImageWrapper:
    def __init__(self, name: str, raw_image): # To do (raw_image could be ImagePlus, ImgPlus or DataArray)
        self._renderer = NotebookImageRenderer()
                
        # if raw_image isinstance 
        if isinstance(raw_image, JImagePlus):
            calibration = raw_image.getCalibration()
            Store.ij.py.sync_image(raw_image) # type: ignore
            da_img: DataArray = Store.ij.py.from_java(raw_image) # type: ignore
            self._image = Image(name=name, da_img=da_img, dpp_xy=calibration.pixelWidth, dpp_z=calibration.pixelDepth, spatial_units=calibration.getXUnit(), frame_interval=calibration.frameInterval, temporal_units=calibration.getTimeUnit())
        elif isinstance(raw_image, DataArray):
            print("ImageWrapper: Add calibration to new Image")
            self._image = Image(name, raw_image, dpp_xy=1, dpp_z=1, spatial_units="", frame_interval=1, temporal_units="")

    def getPythonImage(self) -> Image:
        return self._image
    
    def setPythonImage(self, img: Image):  # No return
        self._image = img
            
    @JOverride
    def clear(self):
        raise Exception('ImageWrapper: Implement clear')
    
    @JOverride
    def getRenderer(self):
        if (JImage.getUseGlobalImageRenderer()):
            return JImage.getGlobalImageRenderer()
        else:
            return self._image.getRenderer()
    
    @JOverride
    def setRenderer(self, imageRenderer):
        self._renderer = imageRenderer
    
    @JOverride
    def getWidth(self) -> int:
        return self._image.getWidth()
    
    @JOverride
    def getHeight(self) -> int:
        return self._image.getHeight()
    
    @JOverride
    def getNChannels(self) -> int:
        return self._image.getNChannels()
    
    @JOverride
    def getNSlices(self) -> int:
        return self._image.getNSlices()
    
    @JOverride
    def getNFrames(self) -> int:
        return self._image.getNFrames()
    
    @JOverride
    def getDppXY(self) -> float:
        return self._image.getDppXY()
    
    @JOverride
    def getDppZ(self) -> float:
        return self._image.getDppZ()
    
    @JOverride
    def getSpatialUnits(self): # To do
        return self._image.getSpatialUnits()
    
    @JOverride
    def getFrameInterval(self) -> float:
        return self._image.getFrameInterval()

    @JOverride
    def getTemporalUnit(self): # To do
        return self._image.getTemporalUnits()
    
    @JOverride
    def getImagePlus(self):
        return Store.ij.py.to_imageplus(self._image.getRawImage()) # type: ignore
    
    @JOverride
    def setImagePlus(self, imagePlus):        
        Store.ij.py.sync_image(imagePlus) # type: ignore
        self._image.setRawImage(Store.ij.py.from_java(imagePlus)) # type: ignore
        
    @JOverride
    def getImgPlus(self):
        raise Exception('ImageWrapper: Implement getImgPlus')
    
    @JOverride
    def setImgPlus(self, img):
        raise Exception('ImageWrapper: Implement setImgPlus')

    @JOverride
    def getRawImage(self):
        return self._image.getRawImage()
    
    @JOverride
    def setRawImage(self, image): # To do
        self._image.setRawImage(image)
    
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
    def convertImageToObjects(self, coordinate_set_factory: CoordinateSetFactoryWrapper, output_objects_name: str, single_object: bool) -> ObjsWrapper:
        # This import needs to be here to prevent circular imports
        from src.wrappers.objswrapper import wrapObjs
        
        objs: Objs = self._image.convertImageToObjects(coordinate_set_factory.getPythonCoordinateSetFactory(), output_objects_name, single_object)
        return wrapObjs(objs)
    
    @JOverride
    def convertImageToSingleObjects(self, coordinate_set_factory: CoordinateSetFactoryWrapper, output_objects_name: str, blackBackground: bool) -> ObjsWrapper:
        # This import needs to be here to prevent circular imports
        from src.wrappers.objswrapper import wrapObjs
        
        objs: Objs = self._image.convertImageToSingleObjects(coordinate_set_factory.getPythonCoordinateSetFactory(), output_objects_name, blackBackground)
        return wrapObjs(objs)

    @JOverride
    def addMeasurement(self, measurement: MeasurementWrapper): # No return
        self._image.addMeasurement(measurement.getPythonMeasurement())
    
    @JOverride
    def getMeasurement(self, name: str) -> MeasurementWrapper:
        measurement: Measurement | None = self._image.getMeasurement(name)
        return None if measurement is None else wrapMeasurement(measurement)
        
    @JOverride
    def removeMeasurement(self, name: str):
        raise Exception('ImageWrapper: Implement removeMeasurement')
    
    @JOverride
    def getName(self) -> str:
        return self._image.getName()
    
    @JOverride
    def getMeasurements(self):
        raise Exception('ImageWrapper: Implement getMeasurements')
    
    @JOverride
    def setMeasurements(self, measurements):
        raise Exception('ImageWrapper: Implement setMeasurements')

    @JOverride
    def show(self, title: str, lut: JLUT | None, normalise, display_mode, overlay):
        print("ImageWrapper: Implement LUT -> Colormap conversion in show.  For now, setting no LUT")
        self._image.show(title, None, normalise, display_mode, overlay)
        
    @JOverride
    def showWithTitle(self, title: str):
        self.show(title, None, True, JDisplayModes.COLOUR, None)

    @JOverride
    def showWithLUT(self, lut: JLUT): # To do
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


@JImplements('io.github.mianalysis.mia.object.image.ImageFactoryI')
class ImageFactoryWrapper:
    @JOverride
    def getName(self) -> str:
        return "Python image factory"
    
    @JOverride
    def duplicate(self) -> ImageFactoryWrapper:
        return ImageFactoryWrapper()

    @JOverride
    def create(self, name: str, raw_image) -> ImageWrapper: # To do (raw_image could be ImagePlus, ImgPlus or DataArray)
        return ImageWrapper(name, raw_image)

    
def wrapImage(img: Image) -> ImageWrapper: # To do
    try:
        return _wrapper_cache[img]
    except:        
        image_wrapper: ImageWrapper = ImageWrapper("", None)
        image_wrapper.setPythonImage(img)
        _wrapper_cache[img]  = image_wrapper
    
        return image_wrapper
    