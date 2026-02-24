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
    
    def setPythonModules(self, modules: Modules):  # No return
        self._modules = modules
        
    @JOverride
    def getModules(self) -> List[ModuleWrapper]:
        raise NotImplementedError("ModulesWrapper: getModules")

    @JOverride
    def execute(self, workspace: WorkspaceWrapper, clear_memory_at_and: bool) -> bool: # To do
        raise NotImplementedError("ModulesWrapper: execute")

    @JOverride
    def removeAllModules(self): # No return
        raise NotImplementedError("ModulesWrapper: removeAllModules")

    @JOverride
    def getAnalysisFilename(self) -> str:
        raise NotImplementedError("ModulesWrapper: getAnalysisFilename")

    @JOverride
    def setAnalysisFilename(self, analysis_filename: str): # No return
        raise NotImplementedError("ModulesWrapper: setAnalysisFilename")

    @JOverride
    def getModuleByID(self, ID: str) -> ModuleWrapper:
        raise NotImplementedError("ModulesWrapper: getModuleByID")

    @JOverride
    def getImageSource(self, image_name: str, cut_off_module: ModuleWrapper): # To do
        raise NotImplementedError("ModulesWrapper: getImageSource")

    @JOverride
    def getObjectSource(self, object_name: str, cut_off_module: ModuleWrapper): 
        raise NotImplementedError("ModulesWrapper: getObjectSource")

    @JOverride
    def objectsExportMeasurements(self, object_name: str) -> bool:
        raise NotImplementedError("ModulesWrapper: objectsExportMeasurements")

    @JOverride
    def objectsExportMetadata(self, object_name: str) -> bool:
        raise NotImplementedError("ModulesWrapper: objectsExportMetadata")

    @JOverride
    def hasModuleMatchingType(self, clazz) -> bool: # To do
        raise NotImplementedError("ModulesWrapper: hasModuleMatchingType")

    @JOverride
    def getImageMeasurementRefs(self, image_name: str, cut_off_module: ModuleWrapper): # To do
        raise NotImplementedError("ModulesWrapper: getImageMeasurementRefs")

    @JOverride
    def getObjectMeasurementRefs(self, object_name: str, cut_off_module: ModuleWrapper): # To do
        raise NotImplementedError("ModulesWrapper: getObjectMeasurementRefs")

    @JOverride
    def getObjectMetadataRefs(self, object_name: str, cut_off_module: ModuleWrapper): # To do
        raise NotImplementedError("ModulesWrapper: getObjectMetadataRefs")

    @JOverride
    def getMetadataRefs(self, cut_off_module: ModuleWrapper): # To do
        raise NotImplementedError("ModulesWrapper: getMetadataRefs")

    @JOverride
    def getParentChildRefs(self, cut_off_module: ModuleWrapper): # To do
        raise NotImplementedError("ModulesWrapper: getParentChildRefs")

    @JOverride
    def getPartnerRefs(self, cut_off_module: ModuleWrapper): # To do
        raise NotImplementedError("ModulesWrapper: getPartnerRefs")

    @JOverride
    def getParametersMatchingType(self, type, cut_off_module: ModuleWrapper): # To do
        raise NotImplementedError("ModulesWrapper: getParametersMatchingType")

    @JOverride
    def getAvailableObjectsMatchingClass(self, cut_off_module: ModuleWrapper, object_class, ignore_removed: bool): # To do
        raise NotImplementedError("ModulesWrapper: getAvailableObjectsMatchingClass")

    @JOverride
    def getAvailableObjects(self, cut_off_module: ModuleWrapper, ignore_removed: bool): # To do
        raise NotImplementedError("ModulesWrapper: getAvailableObjects")

    @JOverride
    def getAvailableImages(self, cut_off_module: ModuleWrapper, ignore_removed: bool): # To do
        raise NotImplementedError("ModulesWrapper: getAvailableImages")

    @JOverride
    def hasVisibleParameters(self) -> bool:
        raise NotImplementedError("ModulesWrapper: hasVisibleParameters")

    @JOverride
    def getInputControl(self): # To do
        raise NotImplementedError("ModulesWrapper: getInputControl")

    @JOverride
    def setInputControl(self, input_control): # To do
        raise NotImplementedError("ModulesWrapper: setInputControl")

    @JOverride
    def getOutputControl(self): # To do
        raise NotImplementedError("ModulesWrapper: getOutputControl")

    @JOverride
    def setOutputControl(self, output_control): # To do
        raise NotImplementedError("ModulesWrapper: setOutputControl")

    @JOverride
    def reorder(self, from_indices: List[int], to_idx: int): # No return
        raise NotImplementedError("ModulesWrapper: reorder")

    @JOverride
    def insert(self, modules_to_insert: ModulesWrapper, to_idx: int): # No return
        raise NotImplementedError("ModulesWrapper: insert")

    @JOverride
    def duplicate(self, copy_ids: bool) -> ModulesWrapper:
        raise NotImplementedError("ModulesWrapper: duplicate")

    @JOverride
    def addAll(self, modules: ModulesWrapper) -> bool:
        raise NotImplementedError("ModulesWrapper: addAll")

    @JOverride
    def removeAll(self, modules: ModulesWrapper) -> bool:
        raise NotImplementedError("ModulesWrapper: removeAll")

    @JOverride
    def remove(self, module: ModuleWrapper) -> bool:
        raise NotImplementedError("ModulesWrapper: remove")

    @JOverride
    def size(self) -> int:
        raise NotImplementedError("ModulesWrapper: size")

    @JOverride
    def addAtIndex(self, idx: int, module: ModuleWrapper):  # No return
        raise NotImplementedError("ModulesWrapper: addAtIndex")

    @JOverride
    def getAtIndex(self, idx: int) -> ModuleWrapper:
        raise NotImplementedError("ModulesWrapper: getAtIndex")

    @JOverride
    def removeAtIndex(self, idx: int) -> ModuleWrapper:
        raise NotImplementedError("ModulesWrapper: removeAtIndex")

    @JOverride
    def clear(self): # No return
        raise NotImplementedError("ModulesWrapper: clear")

    @JOverride
    def indexOf(self, module: ModuleWrapper) -> int:
        raise NotImplementedError("ModulesWrapper: indexOf")
    
    
    # From Refs
    
    @JOverride
    def add(self, ref) -> bool:
        raise NotImplementedError("ModulesWrapper: add")
    
    @JOverride
    def values(self): # To do
        raise NotImplementedError("ModulesWrapper: values")
    
    
    # From Iterable
    
    @JOverride
    def iterator(self): # To do
        raise NotImplementedError("ModulesWrapper: iterator")
    
    
def wrapModules(modules: Modules) -> ModulesWrapper: # To do
    try:
        return _wrapper_cache[modules]
    except:        
        modules_wrapper: ModulesWrapper = ModulesWrapper()
        modules_wrapper.setPythonModules(modules)
        _wrapper_cache[modules]  = modules_wrapper
    
        return modules_wrapper