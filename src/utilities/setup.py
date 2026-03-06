# Imports
from scyjava import jimport # type: ignore
from src.utilities.imagerenderer import NotebookImageRenderer
from src.utilities.store import Store
from src.wrappers.coordinatesetwrapper import CoordinateSetFactoryWrapper
from src.wrappers.imagewrapper import ImageWrapper, ImageFactoryWrapper
from src.wrappers.measurementwrapper import MeasurementFactoryWrapper
from src.wrappers.objwrapper import ObjFactoryWrapper
from src.wrappers.objswrapper import ObjsFactoryWrapper
from src.wrappers.volumewrapper import VolumeFactoryWrapper

def setup(ij):
    # Main setup
    Store.ij = ij

    # Setting renderer
    ImageI = jimport('io.github.mianalysis.mia.object.image.ImageI')
    ImageI.setGlobalRenderer(NotebookImageRenderer())
    ImageI.setUseGlobalImageRenderer(True)

    # Setting image factory
    ImageFactories = jimport('io.github.mianalysis.mia.object.image.ImageFactories')
    image_factory = ImageFactoryWrapper()
    ImageFactories.addFactory(image_factory)
    ImageFactories.setDefaultFactory(image_factory)

    # Setting objects factory (both obj and objs factories must be enabled together)
    ObjsFactories = jimport('io.github.mianalysis.mia.object.ObjsFactories')
    objs_factory = ObjsFactoryWrapper()
    ObjsFactories.addFactory(objs_factory)
    ObjsFactories.setDefaultFactory(objs_factory)

    # Setting object factory (both obj and objs factories must be enabled together)
    ObjFactories = jimport('io.github.mianalysis.mia.object.coordinates.ObjFactories')
    obj_factory = ObjFactoryWrapper()
    ObjFactories.addFactory(obj_factory)
    ObjFactories.setDefaultFactory(obj_factory)

    # Setting volume factory
    VolumeFactories = jimport('io.github.mianalysis.mia.object.coordinates.volume.VolumeFactories')
    volume_factory = VolumeFactoryWrapper()
    VolumeFactories.addFactory(volume_factory)
    VolumeFactories.setDefaultFactory(volume_factory)

    # Setting coordinateset factory
    CoordinateSetFactories = jimport('io.github.mianalysis.mia.object.coordinates.volume.CoordinateSetFactories')
    coordinate_set_factory = CoordinateSetFactoryWrapper()
    CoordinateSetFactories.addFactory(coordinate_set_factory)
    CoordinateSetFactories.setDefaultFactory(coordinate_set_factory)

    # Setting measurement factory
    MeasurementFactories = jimport('io.github.mianalysis.mia.object.measurements.MeasurementFactories')
    measurement_factory = MeasurementFactoryWrapper()
    MeasurementFactories.addFactory(measurement_factory)
    MeasurementFactories.setDefaultFactory(measurement_factory)
    