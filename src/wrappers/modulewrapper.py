from jpype import JImplements, JOverride  # type: ignore

from src.wrappers.workspacewrapper import WorkspaceWrapper


@JImplements("io.github.mianalysis.mia.module.ModuleI")
class ModuleWrapper:
    def __init__(self, module):
        self._module = module

    @JOverride
    def getCategory(self):
        raise NotImplementedError("ModuleWrapper: getCategory")

    @JOverride
    def getVersionNumber(self):
        raise NotImplementedError("ModuleWrapper: getVersionNumber")

    @JOverride
    def process(self, workspace: WorkspaceWrapper):
        raise NotImplementedError("ModuleWrapper: process")

    @JOverride
    def initialiseParameters(self):
        raise NotImplementedError("ModuleWrapper: initialiseParameters")

    @JOverride
    def updateAndGetParameters(self):
        raise NotImplementedError("ModuleWrapper: updateAndGetParameters")

    @JOverride
    def updateAndGetImageMeasurementRefs(self):
        raise NotImplementedError("ModuleWrapper: updateAndGetImageMeasurementRefs")

    @JOverride
    def updateAndGetObjectMeasurementRefs(self):
        raise NotImplementedError("ModuleWrapper: updateAndGetObjectMeasurementRefs")

    @JOverride
    def updateAndGetObjectMetadataRefs(self):
        raise NotImplementedError("ModuleWrapper: updateAndGetObjectMetadataRefs")

    @JOverride
    def updateAndGetMetadataReferences(self):
        raise NotImplementedError("ModuleWrapper: updateAndGetMetadataReferences")

    @JOverride
    def updateAndGetParentChildRefs(self):
        raise NotImplementedError("ModuleWrapper: updateAndGetParentChildRefs")

    @JOverride
    def updateAndGetPartnerRefs(self):
        raise NotImplementedError("ModuleWrapper: updateAndGetPartnerRefs")

    @JOverride
    def verify(self):
        raise NotImplementedError("ModuleWrapper: verify")

    @JOverride
    def execute(self, workspace: WorkspaceWrapper):
        raise NotImplementedError("ModuleWrapper: execute")

    @JOverride
    def addObjectMeasurementRef(self, ref):
        raise NotImplementedError("ModuleWrapper: addObjectMeasurementRef")

    @JOverride
    def addObjectMetadataRef(self, ref):
        raise NotImplementedError("ModuleWrapper: addObjectMetadataRef")

    @JOverride
    def getImageMeasurementRefs(self):
        raise NotImplementedError("ModuleWrapper: getImageMeasurementRefs")

    @JOverride
    def getImageMeasurementRef(self, name: str):
        raise NotImplementedError("ModuleWrapper: getImageMeasurementRef")

    @JOverride
    def addImageMeasurementRef(self, ref):
        raise NotImplementedError("ModuleWrapper: addImageMeasurementRef")

    @JOverride
    def getObjectMeasurementRefs(self):
        raise NotImplementedError("ModuleWrapper: getObjectMeasurementRefs")

    @JOverride
    def getObjectMeasurementRef(self, name: str):
        raise NotImplementedError("ModuleWrapper: getObjectMeasurementRef")

    @JOverride
    def getObjectMetadataRefs(self):
        raise NotImplementedError("ModuleWrapper: getObjectMetadataRefs")

    @JOverride
    def getObjectMetadataRef(self, name: str):
        raise NotImplementedError("ModuleWrapper: getObjectMetadataRef")

    @JOverride
    def getMetadataRefs(self):
        raise NotImplementedError("ModuleWrapper: getMetadataRefs")

    @JOverride
    def getMetadataRef(self, name: str):
        raise NotImplementedError("ModuleWrapper: getMetadataRef")

    @JOverride
    def addMetadataRef(self, ref):
        raise NotImplementedError("ModuleWrapper: addMetadataRef")

    @JOverride
    def getParentChildRefs(self):
        raise NotImplementedError("ModuleWrapper: getParentChildRefs")

    @JOverride
    def getParentChildRef(self, parent_name, child_name):
        raise NotImplementedError("ModuleWrapper: getParentChildRef")

    @JOverride
    def addParentChildRef(self, ref):
        raise NotImplementedError("ModuleWrapper: addParentChildRef")

    @JOverride
    def getPartnerRefs(self):
        raise NotImplementedError("ModuleWrapper: getPartnerRefs")

    @JOverride
    def addPartnerRef(self, ref):
        raise NotImplementedError("ModuleWrapper: addPartnerRef")

    @JOverride
    def getParameter(self, name: str):
        raise NotImplementedError("ModuleWrapper: getParameter")

    @JOverride
    def updateParameterValue(self, name, value):
        raise NotImplementedError("ModuleWrapper: updateParameterValue")

    @JOverride
    def getParameterValue(self, name, workspace: WorkspaceWrapper):
        raise NotImplementedError("ModuleWrapper: getParameterValue")

    @JOverride
    def setParameterVisibility(self, name, visible: bool):
        raise NotImplementedError("ModuleWrapper: setParameterVisibility")

    @JOverride
    def getAllParameters(self):
        raise NotImplementedError("ModuleWrapper: getAllParameters")

    @JOverride
    def invalidParameterIsVisible(self):
        raise NotImplementedError("ModuleWrapper: invalidParameterIsVisible")

    @JOverride
    def getParametersMatchingType(self, type):
        raise NotImplementedError("ModuleWrapper: getParametersMatchingType")

    @JOverride
    def addParameterGroupParameters(self, parameterGroup, type, parameters):
        raise NotImplementedError("ModuleWrapper: addParameterGroupParameters")

    @JOverride
    def getModules(self):
        raise NotImplementedError("ModuleWrapper: getModules")

    @JOverride
    def setModules(self, modules):
        raise NotImplementedError("ModuleWrapper: setModules")

    @JOverride
    def hasParameter(self, parameterName):
        raise NotImplementedError("ModuleWrapper: hasParameter")

    @JOverride
    def getModuleID(self):
        raise NotImplementedError("ModuleWrapper: getModuleID")

    @JOverride
    def setModuleID(self, moduleID):
        raise NotImplementedError("ModuleWrapper: setModuleID")

    @JOverride
    def getShortDescription(self):
        raise NotImplementedError("ModuleWrapper: getShortDescription")

    @JOverride
    def getNotes(self):
        raise NotImplementedError("ModuleWrapper: getNotes")

    @JOverride
    def setNotes(self, notes):
        raise NotImplementedError("ModuleWrapper: setNotes")

    @JOverride
    def isEnabled(self):
        raise NotImplementedError("ModuleWrapper: isEnabled")

    @JOverride
    def setEnabled(self, enabled):
        raise NotImplementedError("ModuleWrapper: setEnabled")

    @JOverride
    def canBeDisabled(self):
        raise NotImplementedError("ModuleWrapper: canBeDisabled")

    @JOverride
    def setCanBeDisabled(self, canBeDisabled):
        raise NotImplementedError("ModuleWrapper: setCanBeDisabled")

    @JOverride
    def canShowProcessingTitle(self):
        raise NotImplementedError("ModuleWrapper: canShowProcessingTitle")

    @JOverride
    def setShowProcessingViewTitle(self, showProcessingViewTitle):
        raise NotImplementedError("ModuleWrapper: setShowProcessingViewTitle")

    @JOverride
    def isVerbose(self):
        raise NotImplementedError("ModuleWrapper: isVerbose")

    @JOverride
    def setVerbose(self, verboseIn):
        raise NotImplementedError("ModuleWrapper: setVerbose")

    @JOverride
    def canShowOutput(self):
        raise NotImplementedError("ModuleWrapper: canShowOutput")

    @JOverride
    def setShowOutput(self, showOutput):
        raise NotImplementedError("ModuleWrapper: setShowOutput")

    @JOverride
    def isRunnable(self):
        raise NotImplementedError("ModuleWrapper: isRunnable")

    @JOverride
    def setRunnable(self, runnable):
        raise NotImplementedError("ModuleWrapper: setRunnable")

    @JOverride
    def isReachable(self):
        raise NotImplementedError("ModuleWrapper: isReachable")

    @JOverride
    def setReachable(self, reachable):
        raise NotImplementedError("ModuleWrapper: setReachable")

    @JOverride
    def isDeprecated(self):
        raise NotImplementedError("ModuleWrapper: isDeprecated")

    @JOverride
    def setDeprecated(self, deprecated):
        raise NotImplementedError("ModuleWrapper: setDeprecated")

    @JOverride
    def getIL2Support(self):
        raise NotImplementedError("ModuleWrapper: getIL2Support")

    @JOverride
    def getRedirectModuleID(self, workspace: WorkspaceWrapper):
        raise NotImplementedError("ModuleWrapper: getRedirectModuleID")

    @JOverride
    def setRedirectModuleID(self, redirectModuleID):
        raise NotImplementedError("ModuleWrapper: setRedirectModuleID")

    @JOverride
    def hasVisibleParameters(self):
        raise NotImplementedError("ModuleWrapper: hasVisibleParameters")

    @JOverride
    def duplicate(self, newModules, copyID):
        raise NotImplementedError("ModuleWrapper: duplicate")

    @JOverride
    def writeStatus(self, message):
        raise NotImplementedError("ModuleWrapper: writeStatus")

    @JOverride
    def writeProgressStatus(self, count, total, featureBeingProcessed):
        raise NotImplementedError("ModuleWrapper: writeProgressStatus")

    # From Ref

    @JOverride
    def getName(self) -> str:
        raise NotImplementedError("ModuleWrapper: getName")

    @JOverride
    def getDescription(self) -> str:
        raise NotImplementedError("ModuleWrapper: getDescription")

    @JOverride
    def setDescription(self, description: str):  # No return
        raise NotImplementedError("ModuleWrapper: setDescription")

    @JOverride
    def getNickname(self) -> str:
        raise NotImplementedError("ModuleWrapper: getNickname")

    @JOverride
    def setNickname(self, nickname: str):  # No return
        raise NotImplementedError("ModuleWrapper: setNickname")

    @JOverride
    def appendXMLAttributes(self, element):  # No return
        raise NotImplementedError("ModuleWrapper: appendXMLAttributes")

    @JOverride
    def setAttributesFromXML(self, node):  # No return
        raise NotImplementedError("ModuleWrapper: setAttributesFromXML")
