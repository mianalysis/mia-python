# To do: Convert WorkspaceWrapper to hold a Python Workspace object

from jpype import JImplements, JOverride # type: ignore
from scyjava import jimport # type: ignore
from src.wrappers.metadatawrapper import MetadataWrapper
from src.utilities.conversion import py_dict_to_java_map

from src.wrappers.imagewrapper import ImageWrapper
from src.wrappers.objwrapper import ObjWrapper
from src.wrappers.objswrapper import ObjsWrapper

import jpype
import os

JFile = jimport('java.io.File') # type: ignore

@JImplements('io.github.mianalysis.mia.object.WorkspaceI')
class WorkspaceWrapper():
    def __init__(self, ID: int, file_path: str, series: int, workspaces): # To do
        self._ID: int = ID
        self._workspaces = workspaces
        self._images = {}
        self._objects = {}

        self._metadata: MetadataWrapper = MetadataWrapper()
        self._metadata.setFile(JFile(file_path))
        self._metadata.setSeriesNumber(series)
        
        if file_path is None:
            self._metadata.setFilepath("")
            self._metadata.setFilename("")
            self._metadata.setExt("")
        else:
            (folder, filename) = os.path.split(file_path) 
            self._metadata.setFilepath(folder)
            self._metadata.setFilename(filename)
            self._metadata.setExt(os.path.splitext(file_path)[1])
        
    @JOverride
    def addObjects(self, obj: ObjWrapper):
        self._objects[obj.getName()] = obj

    @JOverride
    def removeObjects(self, name: str, retainMeasurements: bool):
        raise Exception('WorkspaceWrapper: Implement removeObjects')

    @JOverride
    def addImage(self, image: ImageWrapper):
        self._images[image.getName()] = image

    @JOverride
    def removeImage(self, name: str, retainMeasurements: bool):
        raise Exception('WorkspaceWrapper: Implement removeImage')

    @JOverride
    def clearAllImages(self,retainMeasurements: bool):
        raise Exception('WorkspaceWrapper: Implement clearAllImages')

    @JOverride
    def clearAllObjects(self,retainMeasurements: bool):
        raise Exception('WorkspaceWrapper: Implement clearAllObjects')

    @JOverride
    def clearMetadata(self):
        raise Exception('WorkspaceWrapper: Implement clearMetadata')

    @JOverride
    def showMetadata(self,module=None): # To do
        raise Exception('WorkspaceWrapper: Implement showMetadata')
    
    @JOverride
    def getImage(self,name: str):
        return self._images[name]

    @JOverride
    def getAllObjects(self):
        return py_dict_to_java_map(self._objects,'LinkedHashMap')
        
    @JOverride
    def getObjects(self, name: str) -> ObjsWrapper:
        return self._objects[name]

    @JOverride
    def getObjectSet(self,name: str):
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
    def setImages(self,images): # To do
        raise Exception('WorkspaceWrapper: Implement setImages')

    @JOverride
    def getMetadata(self) -> MetadataWrapper:
        return self._metadata

    @JOverride
    def setMetadata(self,metadata: MetadataWrapper):
        raise Exception('WorkspaceWrapper: Implement setMetadata')

    @JOverride
    def getID(self) -> int:
        return self._ID

    @JOverride
    def getProgress(self) -> float:
        raise Exception('WorkspaceWrapper: Implement getProgress')

    @JOverride
    def setProgress(self,progress: float):
        raise Exception('WorkspaceWrapper: Implement setProgress')

    @JOverride
    def getStatus(self):
        raise Exception('WorkspaceWrapper: Implement getStatus')

    @JOverride
    def setStatus(self,status):
        raise Exception('WorkspaceWrapper: Implement setStatus')

    @JOverride
    def exportWorkspace(self) -> bool:
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