from jpype import JImplements, JOverride, JPackage
from scyjava import jimport
from src.wrappers.metadatawrapper import MetadataWrapper
from src.utilities.conversion import py_dict_to_java_map

import jpype
import os

File = jimport('java.io.File')

@JImplements('io.github.mianalysis.mia.object.WorkspaceI')
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
        raise Exception('WorkspaceWrapper: Implement removeObjects')

    @JOverride
    def addImage(self, image):
        self._images[image.getName()] = image

    @JOverride
    def removeImage(self, name, retainMeasurements):
        raise Exception('WorkspaceWrapper: Implement removeImage')

    @JOverride
    def clearAllImages(self,retainMeasurements):
        raise Exception('WorkspaceWrapper: Implement clearAllImages')

    @JOverride
    def clearAllObjects(self,retainMeasurements):
        raise Exception('WorkspaceWrapper: Implement clearAllObjects')

    @JOverride
    def clearMetadata(self):
        raise Exception('WorkspaceWrapper: Implement clearMetadata')

    @JOverride
    def showMetadata(self,module=None):
        raise Exception('WorkspaceWrapper: Implement showMetadata')
    
    @JOverride
    def getImage(self,name):
        return self._images[name]

    @JOverride
    def getAllObjects(self):
        return py_dict_to_java_map(self._objects,'LinkedHashMap')
        
    @JOverride
    def getObjects(self, name):        
        return self._objects[name]

    @JOverride
    def getObjectSet(self,name):
        return self._objects[name]

    @JOverride
    def getSingleTimepointWorkspaces(self):
        raise Exception('WorkspaceWrapper: Implement getSingleTimepointWorkspaces')

    @JOverride
    def setAllObjects(self,objects):
        self._objects = objects

    @JOverride
    def getImages(self):
        return jpype.java.util.LinkedHashMap(self._images)

    @JOverride
    def setImages(self,images):
        raise Exception('WorkspaceWrapper: Implement setImages')

    @JOverride
    def getMetadata(self):
        return self._metadata

    @JOverride
    def setMetadata(self,metadata):
        raise Exception('WorkspaceWrapper: Implement setMetadata')

    @JOverride
    def getID(self):
        return self._ID

    @JOverride
    def getProgress(self):
        raise Exception('WorkspaceWrapper: Implement getProgress')

    @JOverride
    def setProgress(self,progress):
        raise Exception('WorkspaceWrapper: Implement setProgress')

    @JOverride
    def getStatus(self):
        raise Exception('WorkspaceWrapper: Implement getStatus')

    @JOverride
    def setStatus(self,status):
        raise Exception('WorkspaceWrapper: Implement setStatus')

    @JOverride
    def exportWorkspace(self):
        raise Exception('WorkspaceWrapper: Implement exportWorkspace')
    
    @JOverride
    def setExportWorkspace(self,exportWorkspace):
        raise Exception('WorkspaceWrapper: Implement setExportWorkspace')
    
    @JOverride
    def getWorkspaces(self):
        raise Exception('WorkspaceWrapper: Implement getWorkspaces')
    
    @JOverride
    def setWorkspaces(self,workspaces):
        raise Exception('WorkspaceWrapper: Implement setWorkspaces')