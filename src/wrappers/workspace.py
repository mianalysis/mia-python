from jpype import JImplements, JOverride, JPackage
from scyjava import jimport
from src.wrappers.metadata import MetadataWrapper

import jpype
import os   
pac = JPackage('io.github.mianalysis.mia.object')
# 
File = jimport('java.io.File')

@JImplements(pac.WorkspaceI)
class WorkspaceWrapper(object):
    def __init__(self, ID, file_path, series, workspaces):
        self._ID = ID
        self._workspaces = workspaces
        self._images = {}
        self._objects = {}

        self._metadata = MetadataWrapper()
        self._metadata.setFile(File(file_path))
        self._metadata.setSeriesNumber(series)
        
        if file_path is None:
            self._metadata.setFilepath("")
            self._metadata.setFilename("")
            self._metadata.setExt("")
        else:
            folder, filename = os.path.split(file_path)
            self._metadata.setFilepath(folder)
            self._metadata.setFilename(filename)
            self._metadata.setExt(os.path.splitext(file_path)[1])
        
    @JOverride
    def addObjects(self, obj):
        self._objects[obj.getName()] = obj

    @JOverride
    def removeObjects(self, name, retainMeasurements):
        print('WorkspaceWrapper: Implement removeObjects')

    @JOverride
    def addImage(self, image):
        self._images[image.getName()] = image

    @JOverride
    def removeImage(self, name, retainMeasurements):
        print('WorkspaceWrapper: Implement removeImage')

    @JOverride
    def clearAllImages(self,retainMeasurements):
        print('WorkspaceWrapper: Implement clearAllImages')

    @JOverride
    def clearAllObjects(self,retainMeasurements):
        print('WorkspaceWrapper: Implement clearAllObjects')

    @JOverride
    def clearMetadata(self):
        print('WorkspaceWrapper: Implement clearMetadata')

    @JOverride
    def showMetadata(self,module):
        print('WorkspaceWrapper: Implement showMetadata')

    @JOverride
    def showMetadata(self):
        print('WorkspaceWrapper: Implement showMetadata')

    # Deactivating this for now as it's a default method and this is 
    # something I'm testing using jpype1 1.5.1
    
    # @JOverride
    # def getImage(self,name):
    #     return super().getImage(name)
        # return self._images[name]

    @JOverride
    def getObjects(self,name=None):
        if not name:
            return self._objects
        
        return self._objects[name]

    @JOverride
    def getObjectSet(self,name):
        return self._objects[name]

    @JOverride
    def getSingleTimepointWorkspaces(self):
        print('WorkspaceWrapper: Implement getSingleTimepointWorkspaces')

    @JOverride
    def setObjects(self,objects):
        self._objects = objects

    @JOverride
    def getImages(self):
        return jpype.java.util.LinkedHashMap(self._images)

    @JOverride
    def setImages(self,images):
        print('WorkspaceWrapper: Implement setImages')

    @JOverride
    def getMetadata(self):
        return self._metadata

    @JOverride
    def setMetadata(self,metadata):
        print('WorkspaceWrapper: Implement setMetadata')

    @JOverride
    def getID(self):
        return self._ID

    @JOverride
    def getProgress(self):
        print('WorkspaceWrapper: Implement getProgress')

    @JOverride
    def setProgress(self,progress):
        print('WorkspaceWrapper: Implement setProgress')

    @JOverride
    def getStatus(self):
        print('WorkspaceWrapper: Implement getStatus')

    @JOverride
    def setStatus(self,status):
        print('WorkspaceWrapper: Implement setStatus')

    @JOverride
    def exportWorkspace(self):
        print('WorkspaceWrapper: Implement exportWorkspace')
    
    @JOverride
    def setExportWorkspace(self,exportWorkspace):
        print('WorkspaceWrapper: Implement setExportWorkspace')
    
    @JOverride
    def getWorkspaces(self):
        print('WorkspaceWrapper: Implement getWorkspaces')
    
    @JOverride
    def setWorkspaces(self,workspaces):
        print('WorkspaceWrapper: Implement setWorkspaces')