from __future__ import annotations

from jpype import JImplements, JOverride # type: ignore
from typing import List
from weakref import WeakKeyDictionary

from src.objects.modules import Modules
from src.wrappers.modulewrapper import ModuleWrapper
from src.wrappers.workspacewrapper import WorkspaceWrapper

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
    def execute(self, workspace: WorkspaceWrapper, clear_memory_at_and: bool) -> bool: # To do
        raise Exception("ModulesWrapper: Implement execute")

    @JOverride
    def removeAllModules(self): # No return
        raise Exception("ModulesWrapper: Implement removeAllModules")

    @JOverride
    def getAnalysisFilename(self) -> str:
        raise Exception("ModulesWrapper: Implement getAnalysisFilename")

    @JOverride
    def setAnalysisFilename(self, analysis_filename: str): # No return
        raise Exception("ModulesWrapper: Implement setAnalysisFilename")

    @JOverride
    def getModuleByID(self, ID: str) -> ModuleWrapper:
        raise Exception("ModulesWrapper: Implement getModuleByID")

    @JOverride
    def getImageSource(self, image_name: str, cut_off_module: ModuleWrapper): # To do
        raise Exception("ModulesWrapper: Implement getImageSource")

    @JOverride
    def getObjectSource(self, object_name: str, cut_off_module: ModuleWrapper): 
        raise Exception("ModulesWrapper: Implement getObjectSource")

    @JOverride
    def objectsExportMeasurements(self, object_name: str) -> bool:
        raise Exception("ModulesWrapper: Implement objectsExportMeasurements")

    @JOverride
    def objectsExportMetadata(self, object_name: str) -> bool:
        raise Exception("ModulesWrapper: Implement objectsExportMetadata")

    @JOverride
    def hasModuleMatchingType(self, clazz) -> bool: # To do
        raise Exception("ModulesWrapper: Implement hasModuleMatchingType")

    @JOverride
    def getImageMeasurementRefs(self, image_name: str, cut_off_module: ModuleWrapper): # To do
        raise Exception("ModulesWrapper: Implement getImageMeasurementRefs")

    @JOverride
    def getObjectMeasurementRefs(self, object_name: str, cut_off_module: ModuleWrapper): # To do
        raise Exception("ModulesWrapper: Implement getObjectMeasurementRefs")

    @JOverride
    def getObjectMetadataRefs(self, object_name: str, cut_off_module: ModuleWrapper): # To do
        raise Exception("ModulesWrapper: Implement getObjectMetadataRefs")

    @JOverride
    def getMetadataRefs(self, cut_off_module: ModuleWrapper): # To do
        raise Exception("ModulesWrapper: Implement getMetadataRefs")

    @JOverride
    def getParentChildRefs(self, cut_off_module: ModuleWrapper): # To do
        raise Exception("ModulesWrapper: Implement getParentChildRefs")

    @JOverride
    def getPartnerRefs(self, cut_off_module: ModuleWrapper): # To do
        raise Exception("ModulesWrapper: Implement getPartnerRefs")

    @JOverride
    def getParametersMatchingType(self, type, cut_off_module: ModuleWrapper): # To do
        raise Exception("ModulesWrapper: Implement getParametersMatchingType")

    @JOverride
    def getAvailableObjectsMatchingClass(self, cut_off_module: ModuleWrapper, object_class, ignore_removed: bool): # To do
        raise Exception("ModulesWrapper: Implement getAvailableObjectsMatchingClass")

    @JOverride
    def getAvailableObjects(self, cut_off_module: ModuleWrapper, ignore_removed: bool): # To do
        raise Exception("ModulesWrapper: Implement getAvailableObjects")

    @JOverride
    def getAvailableImages(self, cut_off_module: ModuleWrapper, ignore_removed: bool): # To do
        raise Exception("ModulesWrapper: Implement getAvailableImages")

    @JOverride
    def hasVisibleParameters(self) -> bool:
        raise Exception("ModulesWrapper: Implement hasVisibleParameters")

    @JOverride
    def getInputControl(self): # To do
        raise Exception("ModulesWrapper: Implement getInputControl")

    @JOverride
    def setInputControl(self, input_control): # To do
        raise Exception("ModulesWrapper: Implement setInputControl")

    @JOverride
    def getOutputControl(self): # To do
        raise Exception("ModulesWrapper: Implement getOutputControl")

    @JOverride
    def setOutputControl(self, output_control): # To do
        raise Exception("ModulesWrapper: Implement setOutputControl")

    @JOverride
    def reorder(self, from_indices: List[int], to_idx: int): # No return
        raise Exception("ModulesWrapper: Implement reorder")

    @JOverride
    def insert(self, modules_to_insert: ModulesWrapper, to_idx: int): # No return
        raise Exception("ModulesWrapper: Implement insert")

    @JOverride
    def duplicate(self, copy_ids: bool) -> ModulesWrapper:
        raise Exception("ModulesWrapper: Implement duplicate")

    @JOverride
    def addAll(self, modules: ModulesWrapper) -> bool:
        raise Exception("ModulesWrapper: Implement addAll")

    @JOverride
    def removeAll(self, modules: ModulesWrapper) -> bool:
        raise Exception("ModulesWrapper: Implement removeAll")

    @JOverride
    def remove(self, module: ModuleWrapper) -> bool:
        raise Exception("ModulesWrapper: Implement remove")

    @JOverride
    def size(self) -> int:
        raise Exception("ModulesWrapper: Implement size")

    @JOverride
    def addAtIndex(self, idx: int, module: ModuleWrapper):  # No return
        raise Exception("ModulesWrapper: Implement addAtIndex")

    @JOverride
    def getAtIndex(self, idx: int) -> ModuleWrapper:
        raise Exception("ModulesWrapper: Implement getAtIndex")

    @JOverride
    def removeAtIndex(self, idx: int) -> ModuleWrapper:
        raise Exception("ModulesWrapper: Implement removeAtIndex")

    @JOverride
    def clear(self): # No return
        raise Exception("ModulesWrapper: Implement clear")

    @JOverride
    def indexOf(self, module: ModuleWrapper) -> int:
        raise Exception("ModulesWrapper: Implement indexOf")
    
def wrapImage(modules: Modules) -> ModulesWrapper: # To do
    try:
        return _wrapper_cache[modules]
    except:        
        modules_wrapper: ModulesWrapper = ModulesWrapper()
        modules_wrapper.setPythonImage(modules)
        _wrapper_cache[modules]  = modules_wrapper
    
        return modules_wrapper