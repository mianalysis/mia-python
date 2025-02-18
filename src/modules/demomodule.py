
from jpype import JImplements, JOverride
from scyjava import jimport

ModuleI = jimport('io.github.mianalysis.mia.module.ModuleI')


@JImplements(ModuleI)
class ModuleDemo:
    @JOverride
    def getCategory(self):
        print('ModuleWrapper: Implement getCategory')
    
    @JOverride
    def getVersionNumber(self):
        print('ModuleWrapper: Implement getVersionNumber')
    
    @JOverride
    def process(self, workspace):
        print('ModuleWrapper: Implement process')
    
    @JOverride
    def initialiseParameters(self):
        print('ModuleWrapper: Implement initialiseParameters')
    
    @JOverride
    def updateAndGetParameters(self):
        print('ModuleWrapper: Implement updateAndGetParameters')
    
    @JOverride
    def updateAndGetImageMeasurementRefs(self):
        print('ModuleWrapper: Implement updateAndGetImageMeasurementRefs')
    
    @JOverride
    def updateAndGetObjectMeasurementRefs(self):
        print('ModuleWrapper: Implement updateAndGetObjectMeasurementRefs')
    
    @JOverride
    def updateAndGetObjectMetadataRefs(self):
        print('ModuleWrapper: Implement updateAndGetObjectMetadataRefs')
    
    @JOverride
    def updateAndGetMetadataReferences(self):
        print('ModuleWrapper: Implement updateAndGetMetadataReferences')
    
    @JOverride
    def updateAndGetParentChildRefs(self):
        print('ModuleWrapper: Implement updateAndGetParentChildRefs')
    
    @JOverride
    def updateAndGetPartnerRefs(self):
        print('ModuleWrapper: Implement updateAndGetPartnerRefs')
    
    @JOverride
    def verify(self):
        print('ModuleWrapper: Implement verify')
    
    @JOverride
    def execute(self, workspace):
        print('ModuleWrapper: Implement execute')
    
    @JOverride
    def addObjectMeasurementRef(self, ref):
        print('ModuleWrapper: Implement addObjectMeasurementRef')
    
    @JOverride
    def addObjectMetadataRef(self, ref):
        print('ModuleWrapper: Implement addObjectMetadataRef')
    
    @JOverride
    def getImageMeasurementRef(self, name):
        print('ModuleWrapper: Implement getImageMeasurementRef')
    
    @JOverride
    def addImageMeasurementRef(self, ref):
        print('ModuleWrapper: Implement addImageMeasurementRef')
    
    @JOverride
    def getObjectMeasurementRef(self, name):
        print('ModuleWrapper: Implement getObjectMeasurementRef')
    
    @JOverride
    def getObjectMetadataRef(self, name):
        print('ModuleWrapper: Implement getObjectMetadataRef')
    
    @JOverride
    def getMetadataRef(self, name):
        print('ModuleWrapper: Implement getMetadataRef')
    
    @JOverride
    def addMetadataRef(self, ref):
        print('ModuleWrapper: Implement addMetadataRef')
    
    @JOverride
    def getParentChildRef(self, parentName, childName):
        print('ModuleWrapper: Implement getParentChildRef')
    
    @JOverride
    def addParentChildRef(self, ref):
        print('ModuleWrapper: Implement addParentChildRef')
    
    @JOverride
    def addPartnerRef(self, ref):
        print('ModuleWrapper: Implement addPartnerRef')
    
    @JOverride
    def getParameter(self, name):
        print('ModuleWrapper: Implement getParameter')
    
    @JOverride
    def updateParameterValue(self, name, value):
        print('ModuleWrapper: Implement updateParameterValue')
    
    @JOverride
    def getParameterValue(self, name, workspace):
        print('ModuleWrapper: Implement getParameterValue')
    
    @JOverride
    def setParameterVisibility(self, name, visible):
        print('ModuleWrapper: Implement setParameterVisibility')
    
    @JOverride
    def getAllParameters(self):
        print('ModuleWrapper: Implement getAllParameters')
    
    @JOverride
    def invalidParameterIsVisible(self):
        print('ModuleWrapper: Implement invalidParameterIsVisible')
    
    @JOverride
    def getParametersMatchingType(self, type):
        print('ModuleWrapper: Implement getParametersMatchingType')
    
    @JOverride
    def addParameterGroupParameters(self, parameterGroup, type, parameters):
        print('ModuleWrapper: Implement addParameterGroupParameters')
    
    @JOverride
    def getModules(self):
        print('ModuleWrapper: Implement getModules')
    
    @JOverride
    def setModules(self, modules):
        print('ModuleWrapper: Implement setModules')
    
    @JOverride
    def hasParameter(self, parameterName):
        print('ModuleWrapper: Implement hasParameter')
    
    @JOverride
    def getModuleID(self):
        print('ModuleWrapper: Implement getModuleID')
    
    @JOverride
    def setModuleID(self, moduleID):
        print('ModuleWrapper: Implement setModuleID')
    
    @JOverride
    def getShortDescription(self):
        print('ModuleWrapper: Implement getShortDescription')
    
    @JOverride
    def getNotes(self):
        print('ModuleWrapper: Implement getNotes')
    
    @JOverride
    def setNotes(self, notes):
        print('ModuleWrapper: Implement setNotes')
    
    @JOverride
    def isEnabled(self):
        print('ModuleWrapper: Implement isEnabled')
    
    @JOverride
    def setEnabled(self, enabled):
        print('ModuleWrapper: Implement setEnabled')
    
    @JOverride
    def canBeDisabled(self):
        print('ModuleWrapper: Implement canBeDisabled')
    
    @JOverride
    def setCanBeDisabled(self, canBeDisabled):
        print('ModuleWrapper: Implement setCanBeDisabled')
    
    @JOverride
    def canShowProcessingTitle(self):
        print('ModuleWrapper: Implement canShowProcessingTitle')
    
    @JOverride
    def setShowProcessingViewTitle(self, showProcessingViewTitle):
        print('ModuleWrapper: Implement setShowProcessingViewTitle')
    
    @JOverride
    def isVerbose(self):
        print('ModuleWrapper: Implement isVerbose')
    
    @JOverride
    def setVerbose(self, verboseIn):
        print('ModuleWrapper: Implement setVerbose')
    
    @JOverride
    def canShowOutput(self):
        print('ModuleWrapper: Implement canShowOutput')
    
    @JOverride
    def setShowOutput(self, showOutput):
        print('ModuleWrapper: Implement setShowOutput')
    
    @JOverride
    def isRunnable(self):
        print('ModuleWrapper: Implement isRunnable')
    
    @JOverride
    def setRunnable(self, runnable):
        print('ModuleWrapper: Implement setRunnable')
    
    @JOverride
    def isReachable(self):
        print('ModuleWrapper: Implement isReachable')
    
    @JOverride
    def setReachable(self, reachable):
        print('ModuleWrapper: Implement setReachable')
    
    @JOverride
    def isDeprecated(self):
        print('ModuleWrapper: Implement isDeprecated')
    
    @JOverride
    def setDeprecated(self, deprecated):
        print('ModuleWrapper: Implement setDeprecated')
    
    @JOverride
    def getIL2Support(self):
        print('ModuleWrapper: Implement getIL2Support')
    
    @JOverride
    def getRedirectModuleID(self, workspace):
        print('ModuleWrapper: Implement getRedirectModuleID')
    
    @JOverride
    def setRedirectModuleID(self, redirectModuleID):
        print('ModuleWrapper: Implement setRedirectModuleID')
    
    @JOverride
    def hasVisibleParameters(self):
        print('ModuleWrapper: Implement hasVisibleParameters')
    
    @JOverride
    def duplicate(self, newModules, copyID):
        print('ModuleWrapper: Implement duplicate')
    
    @JOverride
    def writeStatus(self, message):
        print('ModuleWrapper: Implement writeStatus')
    
    @JOverride
    def writeProgressStatus(self, count, total, featureBeingProcessed):
        print('ModuleWrapper: Implement writeProgressStatus')