from __future__ import annotations
from typing import Dict, TYPE_CHECKING

from src.objects.image import Image
from src.objects.metadata import Metadata
from src.objects.objs import Objs

if TYPE_CHECKING:
    from src.objects.workspaces import Workspaces

import os

class Workspace():
    def __init__(self, ID: int, file_path: str, series: int, workspaces: Workspaces): # To do
        self._ID: int = ID
        self._workspaces: Workspaces = workspaces
        self._images: Dict[str, Image] = {}
        self._objects: Dict[str, Objs] = {}

        self._metadata: Metadata = Metadata()
        self._metadata.setFile(file_path)
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
        
    def addObjects(self, objs: Objs):
        self._objects[objs.getName()] = objs

    def removeObjects(self, name: str, retain_measurements: bool):
        raise NotImplementedError('Workspace: removeObjects')

    def addImage(self, image: Image): # No return
        self._images[image.getName()] = image

    def removeImage(self, name: str, retain_measurements: bool):
        raise NotImplementedError('Workspace: removeImage')

    def clearAllImages(self,retain_measurements: bool):
        raise NotImplementedError('Workspace: clearAllImages')

    def clearAllObjects(self,retain_measurements: bool):
        raise NotImplementedError('Workspace: clearAllObjects')

    def clearMetadata(self):
        raise NotImplementedError('Workspace: clearMetadata')

    def showMetadata(self,module=None): # To do
        raise NotImplementedError('Workspace: showMetadata')
    
    def getImage(self,name: str):
        return self._images[name]

    def getAllObjects(self):
        raise NotImplementedError('Workspace: getAllObjects')
        
    def getObjects(self, name: str) -> Objs:
        return self._objects[name]

    def getObjectSet(self, name: str) -> Objs:
        return self.getObjects(name)

    def getSingleTimepointWorkspaces(self):
        raise NotImplementedError('Workspace: getSingleTimepointWorkspaces')

    def setAllObjects(self,objects):
        self._objects = objects

    def getImages(self):
        raise NotImplementedError('Workspace: getImages')

    def setImages(self,images): # To do
        raise NotImplementedError('Workspace: setImages')

    def getMetadata(self) -> Metadata:
        return self._metadata

    def setMetadata(self, metadata):
        raise NotImplementedError('Workspace: setMetadata')

    def getID(self) -> int:
        return self._ID

    def getProgress(self) -> float:
        raise NotImplementedError('Workspace: getProgress')

    def setProgress(self,progress: float):
        raise NotImplementedError('Workspace: setProgress')

    def getStatus(self):
        raise NotImplementedError('Workspace: getStatus')

    def setStatus(self,status):
        raise NotImplementedError('Workspace: setStatus')

    def exportWorkspace(self) -> bool:
        raise NotImplementedError('Workspace: exportWorkspace')
    
    def setExportWorkspace(self,exportWorkspace):
        raise NotImplementedError('Workspace: setExportWorkspace')
    
    def getWorkspaces(self):
        raise NotImplementedError('Workspace: getWorkspaces')
    
    def setWorkspaces(self,workspaces):
        raise NotImplementedError('Workspace: setWorkspaces')
