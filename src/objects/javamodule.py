from src.objects.module import Module

class JavaModule(Module):
    def __init__(self, java_module):
        self._java_module = java_module

    def getCategory(self):
        raise NotImplementedError("JavaModule: getCategory")

    def getVersionNumber(self):
        raise NotImplementedError("JavaModule: getVersionNumber")

    def process(self, workspace):
        raise NotImplementedError("JavaModule: process")

    def initialiseParameters(self):
        raise NotImplementedError("JavaModule: initialiseParameters")

    def updateAndGetParameters(self):
        raise NotImplementedError("JavaModule: updateAndGetParameters")

    def updateAndGetImageMeasurementRefs(self):
        raise NotImplementedError("JavaModule: updateAndGetImageMeasurementRefs")

    def updateAndGetObjectMeasurementRefs(self):
        raise NotImplementedError("JavaModule: updateAndGetObjectMeasurementRefs")

    def updateAndGetObjectMetadataRefs(self):
        raise NotImplementedError("JavaModule: updateAndGetObjectMetadataRefs")

    def updateAndGetMetadataReferences(self):
        raise NotImplementedError("JavaModule: updateAndGetMetadataReferences")

    def updateAndGetParentChildRefs(self):
        raise NotImplementedError("JavaModule: updateAndGetParentChildRefs")

    def updateAndGetPartnerRefs(self):
        raise NotImplementedError("JavaModule: updateAndGetPartnerRefs")

    def verify(self):
        raise NotImplementedError("JavaModule: verify")

    def execute(self, workspace):
        raise NotImplementedError("JavaModule: execute")

    def addObjectMeasurementRef(self, ref):
        raise NotImplementedError("JavaModule: addObjectMeasurementRef")

    def addObjectMetadataRef(self, ref):
        raise NotImplementedError("JavaModule: addObjectMetadataRef")

    def getImageMeasurementRef(self, name):
        raise NotImplementedError("JavaModule: getImageMeasurementRef")

    def addImageMeasurementRef(self, ref):
        raise NotImplementedError("JavaModule: addImageMeasurementRef")

    def getObjectMeasurementRef(self, name):
        raise NotImplementedError("JavaModule: getObjectMeasurementRef")

    def getObjectMetadataRef(self, name):
        raise NotImplementedError("JavaModule: getObjectMetadataRef")

    def getMetadataRef(self, name):
        raise NotImplementedError("JavaModule: getMetadataRef")

    def addMetadataRef(self, ref):
        raise NotImplementedError("JavaModule: addMetadataRef")

    def getParentChildRef(self, parentName, childName):
        raise NotImplementedError("JavaModule: getParentChildRef")

    def addParentChildRef(self, ref):
        raise NotImplementedError("JavaModule: addParentChildRef")

    def addPartnerRef(self, ref):
        raise NotImplementedError("JavaModule: addPartnerRef")

    def getParameter(self, name):
        raise NotImplementedError("JavaModule: getParameter")

    def updateParameterValue(self, name, value):
        self._java_module.updateParameterValue(name, value)

    def getParameterValue(self, name, workspace):
        raise NotImplementedError("JavaModule: getParameterValue")

    def setParameterVisibility(self, name, visible):
        raise NotImplementedError("JavaModule: setParameterVisibility")

    def getAllParameters(self):
        raise NotImplementedError("JavaModule: getAllParameters")

    def invalidParameterIsVisible(self):
        raise NotImplementedError("JavaModule: invalidParameterIsVisible")

    def getParametersMatchingType(self, type):
        raise NotImplementedError("JavaModule: getParametersMatchingType")

    def addParameterGroupParameters(self, parameterGroup, type, parameters):
        raise NotImplementedError("JavaModule: addParameterGroupParameters")

    def getModules(self):
        raise NotImplementedError("JavaModule: getModules")

    def setModules(self, modules):
        raise NotImplementedError("JavaModule: setModules")

    def hasParameter(self, parameterName):
        raise NotImplementedError("JavaModule: hasParameter")

    def getModuleID(self):
        raise NotImplementedError("JavaModule: getModuleID")

    def setModuleID(self, moduleID):
        raise NotImplementedError("JavaModule: setModuleID")

    def getShortDescription(self):
        raise NotImplementedError("JavaModule: getShortDescription")

    def getNotes(self):
        raise NotImplementedError("JavaModule: getNotes")

    def setNotes(self, notes):
        raise NotImplementedError("JavaModule: setNotes")

    def isEnabled(self):
        raise NotImplementedError("JavaModule: isEnabled")

    def setEnabled(self, enabled):
        raise NotImplementedError("JavaModule: setEnabled")

    def canBeDisabled(self):
        raise NotImplementedError("JavaModule: canBeDisabled")

    def setCanBeDisabled(self, canBeDisabled):
        raise NotImplementedError("JavaModule: setCanBeDisabled")

    def canShowProcessingTitle(self):
        raise NotImplementedError("JavaModule: canShowProcessingTitle")

    def setShowProcessingViewTitle(self, showProcessingViewTitle):
        raise NotImplementedError("JavaModule: setShowProcessingViewTitle")

    def isVerbose(self):
        raise NotImplementedError("JavaModule: isVerbose")

    def setVerbose(self, verboseIn):
        raise NotImplementedError("JavaModule: setVerbose")

    def canShowOutput(self):
        raise NotImplementedError("JavaModule: canShowOutput")

    def setShowOutput(self, showOutput):
        raise NotImplementedError("JavaModule: setShowOutput")

    def isRunnable(self):
        raise NotImplementedError("JavaModule: isRunnable")

    def setRunnable(self, runnable):
        raise NotImplementedError("JavaModule: setRunnable")

    def isReachable(self):
        raise NotImplementedError("JavaModule: isReachable")

    def setReachable(self, reachable):
        raise NotImplementedError("JavaModule: setReachable")

    def isDeprecated(self):
        raise NotImplementedError("JavaModule: isDeprecated")

    def setDeprecated(self, deprecated):
        raise NotImplementedError("JavaModule: setDeprecated")

    def getIL2Support(self):
        raise NotImplementedError("JavaModule: getIL2Support")

    def getRedirectModuleID(self, workspace):
        raise NotImplementedError("JavaModule: getRedirectModuleID")

    def setRedirectModuleID(self, redirectModuleID):
        raise NotImplementedError("JavaModule: setRedirectModuleID")

    def hasVisibleParameters(self):
        raise NotImplementedError("JavaModule: hasVisibleParameters")

    def duplicate(self, newModules, copyID):
        raise NotImplementedError("JavaModule: duplicate")

    def writeStatus(self, message):
        raise NotImplementedError("JavaModule: writeStatus")

    def writeProgressStatus(self, count, total, featureBeingProcessed):
        raise NotImplementedError("JavaModule: writeProgressStatus")
            
    
    # From Ref

    def getName(self) -> str:
        raise NotImplementedError("JavaModule: getName")
    
    def getDescription(self) -> str:
        raise NotImplementedError("JavaModule: getDescription")
    
    def setDescription(self, description: str):
        raise NotImplementedError("JavaModule: setDescription")
    
    def getNickname(self) -> str:
        raise NotImplementedError("JavaModule: getNickname")
    
    def setNickname(self, nickname: str):
        raise NotImplementedError("JavaModule: setNickname")
    
    def appendXMLAttributes(self, element):
        raise NotImplementedError("JavaModule: appendXMLAttributes")
    
    def setAttributesFromXML(self, node):
        raise NotImplementedError("JavaModule: setAttributesFromXML")
    