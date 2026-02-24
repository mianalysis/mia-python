from __future__ import annotations
from typing import List
from src.objects.module import Module

class Modules:
    def __init__(self):
        self._modules: List[Module] = []

    def execute(self, workspace, clear_memory_at_and):
        raise NotImplementedError("Modules: execute")

    def removeAllModules(self):
        raise NotImplementedError("Modules: removeAllModules")

    def getAnalysisFilename(self):
        raise NotImplementedError("Modules: getAnalysisFilename")

    def setAnalysisFilename(self, analysis_filename):
        raise NotImplementedError("Modules: setAnalysisFilename")

    def getModuleByID(self, ID):
        raise NotImplementedError("Modules: getModuleByID")

    def getImageSource(self, image_name, cut_off_module):
        raise NotImplementedError("Modules: getImageSource")

    def getObjectSource(self, object_name, cut_off_module):
        raise NotImplementedError("Modules: getObjectSource")

    def objectsExportMeasurements(self, object_name):
        raise NotImplementedError("Modules: objectsExportMeasurements")

    def objectsExportMetadata(self, object_name):
        raise NotImplementedError("Modules: objectsExportMetadata")

    def hasModuleMatchingType(self, clazz):
        raise NotImplementedError("Modules: hasModuleMatchingType")

    def getImageMeasurementRefs(self, image_name, cut_off_module):
        raise NotImplementedError("Modules: getImageMeasurementRefs")

    def getObjectMeasurementRefs(self, object_name, cut_off_module):
        raise NotImplementedError("Modules: getObjectMeasurementRefs")

    def getObjectMetadataRefs(self, object_name, cut_off_module):
        raise NotImplementedError("Modules: getObjectMetadataRefs")

    def getMetadataRefs(self, cut_off_module):
        raise NotImplementedError("Modules: getMetadataRefs")

    def getParentChildRefs(self, cut_off_module):
        raise NotImplementedError("Modules: getParentChildRefs")

    def getPartnerRefs(self, cut_off_module):
        raise NotImplementedError("Modules: getPartnerRefs")

    def getParametersMatchingType(self, type, cut_off_module):
        raise NotImplementedError("Modules: getParametersMatchingType")

    def getAvailableObjectsMatchingClass(self, cut_off_module, object_class, ignore_removed):
        raise NotImplementedError("Modules: getAvailableObjectsMatchingClass")

    def getAvailableObjects(self, cut_off_module, ignore_removed):
        raise NotImplementedError("Modules: getAvailableObjects")

    def getAvailableImages(self, cut_off_module, ignore_removed):
        raise NotImplementedError("Modules: getAvailableImages")

    def hasVisibleParameters(self):
        raise NotImplementedError("Modules: hasVisibleParameters")

    def getInputControl(self):
        raise NotImplementedError("Modules: getInputControl")

    def setInputControl(self, input_control):
        raise NotImplementedError("Modules: setInputControl")

    def getOutputControl(self):
        raise NotImplementedError("Modules: getOutputControl")

    def setOutputControl(self, output_control):
        raise NotImplementedError("Modules: setOutputControl")

    def reorder(self, fromIndices, to_index):
        raise NotImplementedError("Modules: reorder")

    def insert(self, modulesToInsert, to_index):
        raise NotImplementedError("Modules: insert")

    def duplicate(self, copyIDs):
        raise NotImplementedError("Modules: duplicate")

    def addAll(self, modules):
        raise NotImplementedError("Modules: addAll")

    def removeAll(self, modules):
        raise NotImplementedError("Modules: removeAll")

    def remove(self, module):
        raise NotImplementedError("Modules: remove")

    def size(self):
        raise NotImplementedError("Modules: size")

    def addAtIndex(self, index, module):
        raise NotImplementedError("Modules: addAtIndex")

    def getAtIndex(self, idx):
        raise NotImplementedError("Modules: getAtIndex")

    def removeAtIndex(self, idx):
        raise NotImplementedError("Modules: removeAtIndex")

    def clear(self):
        raise NotImplementedError("Modules: clear")

    def indexOf(self, module):
        raise NotImplementedError("Modules: indexOf")
    