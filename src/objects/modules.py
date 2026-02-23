from __future__ import annotations


class Modules:
    def __init__(self):
        self._modules = []

    def execute(self, workspace, clear_memory_at_and):
        raise Exception("Modules: Implement execute")

    def removeAllModules(self):
        raise Exception("Modules: Implement removeAllModules")

    def getAnalysisFilename(self):
        raise Exception("Modules: Implement getAnalysisFilename")

    def setAnalysisFilename(self, analysis_filename):
        raise Exception("Modules: Implement setAnalysisFilename")

    def getModuleByID(self, ID):
        raise Exception("Modules: Implement getModuleByID")

    def getImageSource(self, image_name, cut_off_module):
        raise Exception("Modules: Implement getImageSource")

    def getObjectSource(self, object_name, cut_off_module):
        raise Exception("Modules: Implement getObjectSource")

    def objectsExportMeasurements(self, object_name):
        raise Exception("Modules: Implement objectsExportMeasurements")

    def objectsExportMetadata(self, object_name):
        raise Exception("Modules: Implement objectsExportMetadata")

    def hasModuleMatchingType(self, clazz):
        raise Exception("Modules: Implement hasModuleMatchingType")

    def getImageMeasurementRefs(self, image_name, cut_off_module):
        raise Exception("Modules: Implement getImageMeasurementRefs")

    def getObjectMeasurementRefs(self, object_name, cut_off_module):
        raise Exception("Modules: Implement getObjectMeasurementRefs")

    def getObjectMetadataRefs(self, object_name, cut_off_module):
        raise Exception("Modules: Implement getObjectMetadataRefs")

    def getMetadataRefs(self, cut_off_module):
        raise Exception("Modules: Implement getMetadataRefs")

    def getParentChildRefs(self, cut_off_module):
        raise Exception("Modules: Implement getParentChildRefs")

    def getPartnerRefs(self, cut_off_module):
        raise Exception("Modules: Implement getPartnerRefs")

    def getParametersMatchingType(self, type, cut_off_module):
        raise Exception("Modules: Implement getParametersMatchingType")

    def getAvailableObjectsMatchingClass(self, cut_off_module, object_class, ignore_removed):
        raise Exception("Modules: Implement getAvailableObjectsMatchingClass")

    def getAvailableObjects(self, cut_off_module, ignore_removed):
        raise Exception("Modules: Implement getAvailableObjects")

    def getAvailableImages(self, cut_off_module, ignore_removed):
        raise Exception("Modules: Implement getAvailableImages")

    def hasVisibleParameters(self):
        raise Exception("Modules: Implement hasVisibleParameters")

    def getInputControl(self):
        raise Exception("Modules: Implement getInputControl")

    def setInputControl(self, input_control):
        raise Exception("Modules: Implement setInputControl")

    def getOutputControl(self):
        raise Exception("Modules: Implement getOutputControl")

    def setOutputControl(self, output_control):
        raise Exception("Modules: Implement setOutputControl")

    def reorder(self, fromIndices, to_index):
        raise Exception("Modules: Implement reorder")

    def insert(self, modulesToInsert, to_index):
        raise Exception("Modules: Implement insert")

    def duplicate(self, copyIDs):
        raise Exception("Modules: Implement duplicate")

    def addAll(self, modules):
        raise Exception("Modules: Implement addAll")

    def removeAll(self, modules):
        raise Exception("Modules: Implement removeAll")

    def remove(self, module):
        raise Exception("Modules: Implement remove")

    def size(self):
        raise Exception("Modules: Implement size")

    def addAtIndex(self, index, module):
        raise Exception("Modules: Implement addAtIndex")

    def getAtIndex(self, idx):
        raise Exception("Modules: Implement getAtIndex")

    def removeAtIndex(self, idx):
        raise Exception("Modules: Implement removeAtIndex")

    def clear(self):
        raise Exception("Modules: Implement clear")

    def indexOf(self, module):
        raise Exception("Modules: Implement indexOf")
    