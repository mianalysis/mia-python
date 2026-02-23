from __future__ import annotations

from jpype import JImplements, JOverride
from weakref import WeakKeyDictionary

from src.objects.modules import Modules

_wrapper_cache: WeakKeyDictionary[Modules, ModulesWrapper] = WeakKeyDictionary()

@JImplements("io.github.mianalysis.mia.module.ModulesI")
class ModulesWrapper:
    def __init__(self) -> None:
        self._modules: Modules = Modules()
    
    def getPythonModules(self) -> Modules:
        return self._modules
    
    def setPythonImage(self, modules: Modules):  # No return
        self._modules = modules

    @JOverride
    def execute(self, workspace, clear_memory_at_and):
        raise Exception("ModulesWrapper: Implement execute")

    @JOverride
    def removeAllModules(self):
        raise Exception("ModulesWrapper: Implement removeAllModules")

    @JOverride
    def getAnalysisFilename(self):
        raise Exception("ModulesWrapper: Implement getAnalysisFilename")

    @JOverride
    def setAnalysisFilename(self, analysis_filename):
        raise Exception("ModulesWrapper: Implement setAnalysisFilename")

    @JOverride
    def getModuleByID(self, ID):
        raise Exception("ModulesWrapper: Implement getModuleByID")

    @JOverride
    def getImageSource(self, image_name, cut_off_module):
        raise Exception("ModulesWrapper: Implement getImageSource")

    @JOverride
    def getObjectSource(self, object_name, cut_off_module):
        raise Exception("ModulesWrapper: Implement getObjectSource")

    @JOverride
    def objectsExportMeasurements(self, object_name):
        raise Exception("ModulesWrapper: Implement objectsExportMeasurements")

    @JOverride
    def objectsExportMetadata(self, object_name):
        raise Exception("ModulesWrapper: Implement objectsExportMetadata")

    @JOverride
    def hasModuleMatchingType(self, clazz):
        raise Exception("ModulesWrapper: Implement hasModuleMatchingType")

    @JOverride
    def getImageMeasurementRefs(self, image_name, cut_off_module):
        raise Exception("ModulesWrapper: Implement getImageMeasurementRefs")

    @JOverride
    def getObjectMeasurementRefs(self, object_name, cut_off_module):
        raise Exception("ModulesWrapper: Implement getObjectMeasurementRefs")

    @JOverride
    def getObjectMetadataRefs(self, object_name, cut_off_module):
        raise Exception("ModulesWrapper: Implement getObjectMetadataRefs")

    @JOverride
    def getMetadataRefs(self, cut_off_module):
        raise Exception("ModulesWrapper: Implement getMetadataRefs")

    @JOverride
    def getParentChildRefs(self, cut_off_module):
        raise Exception("ModulesWrapper: Implement getParentChildRefs")

    @JOverride
    def getPartnerRefs(self, cut_off_module):
        raise Exception("ModulesWrapper: Implement getPartnerRefs")

    @JOverride
    def getParametersMatchingType(self, type, cut_off_module):
        raise Exception("ModulesWrapper: Implement getParametersMatchingType")

    @JOverride
    def getAvailableObjectsMatchingClass(self, cut_off_module, object_class, ignore_removed):
        raise Exception("ModulesWrapper: Implement getAvailableObjectsMatchingClass")

    @JOverride
    def getAvailableObjects(self, cut_off_module, ignore_removed):
        raise Exception("ModulesWrapper: Implement getAvailableObjects")

    @JOverride
    def getAvailableImages(self, cut_off_module, ignore_removed):
        raise Exception("ModulesWrapper: Implement getAvailableImages")

    @JOverride
    def hasVisibleParameters(self):
        raise Exception("ModulesWrapper: Implement hasVisibleParameters")

    @JOverride
    def getInputControl(self):
        raise Exception("ModulesWrapper: Implement getInputControl")

    @JOverride
    def setInputControl(self, input_control):
        raise Exception("ModulesWrapper: Implement setInputControl")

    @JOverride
    def getOutputControl(self):
        raise Exception("ModulesWrapper: Implement getOutputControl")

    @JOverride
    def setOutputControl(self, output_control):
        raise Exception("ModulesWrapper: Implement setOutputControl")

    @JOverride
    def reorder(self, fromIndices, to_index):
        raise Exception("ModulesWrapper: Implement reorder")

    @JOverride
    def insert(self, modulesToInsert, to_index):
        raise Exception("ModulesWrapper: Implement insert")

    @JOverride
    def duplicate(self, copyIDs):
        raise Exception("ModulesWrapper: Implement duplicate")

    @JOverride
    def addAll(self, modules):
        raise Exception("ModulesWrapper: Implement addAll")

    @JOverride
    def removeAll(self, modules):
        raise Exception("ModulesWrapper: Implement removeAll")

    @JOverride
    def remove(self, module):
        raise Exception("ModulesWrapper: Implement remove")

    @JOverride
    def size(self):
        raise Exception("ModulesWrapper: Implement size")

    @JOverride
    def addAtIndex(self, index, module):
        raise Exception("ModulesWrapper: Implement addAtIndex")

    @JOverride
    def getAtIndex(self, idx):
        raise Exception("ModulesWrapper: Implement getAtIndex")

    @JOverride
    def removeAtIndex(self, idx):
        raise Exception("ModulesWrapper: Implement removeAtIndex")

    @JOverride
    def clear(self):
        raise Exception("ModulesWrapper: Implement clear")

    @JOverride
    def indexOf(self, module):
        raise Exception("ModulesWrapper: Implement indexOf")
    
def wrapImage(modules: Modules) -> ModulesWrapper: # To do
    try:
        return _wrapper_cache[modules]
    except:        
        modules_wrapper: ModulesWrapper = ModulesWrapper()
        modules_wrapper.setPythonImage(modules)
        _wrapper_cache[modules]  = modules_wrapper
    
        return modules_wrapper