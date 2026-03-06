from __future__ import annotations
from jpype import JImplements, JOverride # type: ignore
from scyjava import jimport # type: ignore
from typing import TYPE_CHECKING
from weakref import WeakKeyDictionary

from src.objects.workspace import Workspace
from src.utilities.conversion import py_dict_to_java_map
from src.wrappers.imagewrapper import ImageWrapper, wrapImage
from src.wrappers.metadatawrapper import MetadataWrapper, wrapMetadata
from src.wrappers.objwrapper import ObjWrapper, wrapObj
from src.wrappers.objswrapper import ObjsWrapper, wrapObjs

import jpype
import os

if TYPE_CHECKING:
    from src.wrappers.workspaceswrapper import WorkspacesWrapper

_wrapper_cache: WeakKeyDictionary[Workspace, WorkspaceWrapper] = WeakKeyDictionary()

JFile = jimport('java.io.File') # type: ignore

@JImplements('io.github.mianalysis.mia.object.WorkspaceI')
class WorkspaceWrapper():
    def __init__(self, ID: int, file_path: str, series: int, workspaces: WorkspacesWrapper):
        if workspaces is not None:
            self._workspace: Workspace = Workspace(ID=ID, file_path=file_path, series=series, workspaces=workspaces.getPythonWorkspaces())
    
    def setPythonWorkspace(self, workspace: Workspace): # No return
        self._workspace = workspace
        
    @JOverride
    def addObjects(self, objs: ObjsWrapper): # No return
        self._workspace.addObjects(objs.getPythonObjs())

    @JOverride
    def removeObjects(self, name: str, retain_measurements: bool):
        raise NotImplementedError('WorkspaceWrapper: removeObjects')

    @JOverride
    def addImage(self, image: ImageWrapper): # No return
        self._workspace.addImage(image.getPythonImage())

    @JOverride
    def removeImage(self, name: str, retain_measurements: bool):
        raise NotImplementedError('WorkspaceWrapper: removeImage')

    @JOverride
    def clearAllImages(self,retain_measurements: bool):
        raise NotImplementedError('WorkspaceWrapper: clearAllImages')

    @JOverride
    def clearAllObjects(self,retain_measurements: bool):
        raise NotImplementedError('WorkspaceWrapper: clearAllObjects')

    @JOverride
    def clearMetadata(self):
        raise NotImplementedError('WorkspaceWrapper: clearMetadata')

    @JOverride
    def showMetadata(self,module=None): # To do
        raise NotImplementedError('WorkspaceWrapper: showMetadata')
    
    @JOverride
    def getImage(self, name: str) -> ImageWrapper:
        return wrapImage(self._workspace.getImage(name))

    @JOverride
    def getAllObjects(self):
        # return py_dict_to_java_map(self._objects,'LinkedHashMap')
        raise NotImplementedError('WorkspaceWrapper: getAllObjects')
        
    @JOverride
    def getObjects(self, name: str) -> ObjsWrapper:
        return wrapObjs(self._workspace.getObjects(name))

    @JOverride
    def getObjectSet(self,name: str):
        raise NotImplementedError('WorkspaceWrapper: getObjectSet')

    @JOverride
    def getSingleTimepointWorkspaces(self):
        raise NotImplementedError('WorkspaceWrapper: getSingleTimepointWorkspaces')

    @JOverride
    def setAllObjects(self,objects):
        raise NotImplementedError('WorkspaceWrapper: setAllObjects')

    @JOverride
    def getImages(self):
        # return jpype.java.util.LinkedHashMap(self._images)
        raise NotImplementedError('WorkspaceWrapper: getImages')

    @JOverride
    def setImages(self,images): # To do
        raise NotImplementedError('WorkspaceWrapper: setImages')

    @JOverride
    def getMetadata(self) -> MetadataWrapper:
        return wrapMetadata(self._workspace.getMetadata())

    @JOverride
    def setMetadata(self,metadata: MetadataWrapper):
        raise NotImplementedError('WorkspaceWrapper: setMetadata')

    @JOverride
    def getID(self) -> int:
        raise NotImplementedError('WorkspaceWrapper: getID')

    @JOverride
    def getProgress(self) -> float:
        raise NotImplementedError('WorkspaceWrapper: getProgress')

    @JOverride
    def setProgress(self,progress: float):
        raise NotImplementedError('WorkspaceWrapper: setProgress')

    @JOverride
    def getStatus(self):
        raise NotImplementedError('WorkspaceWrapper: getStatus')

    @JOverride
    def setStatus(self,status):
        raise NotImplementedError('WorkspaceWrapper: setStatus')

    @JOverride
    def exportWorkspace(self) -> bool:
        raise NotImplementedError('WorkspaceWrapper: exportWorkspace')
    
    @JOverride
    def setExportWorkspace(self,export_workspace):
        raise NotImplementedError('WorkspaceWrapper: setExportWorkspace')
    
    @JOverride
    def getWorkspaces(self):
        raise NotImplementedError('WorkspaceWrapper: getWorkspaces')
    
    @JOverride
    def setWorkspaces(self,workspaces):
        raise NotImplementedError('WorkspaceWrapper: setWorkspaces')
    
    
def wrapWorkspace(workspace: Workspace) -> WorkspaceWrapper:
    try:
        return _wrapper_cache[workspace]
    except:        
        workspace_wrapper: WorkspaceWrapper = WorkspaceWrapper(0, "", 0, None)
        workspace_wrapper.setPythonWorkspace(workspace)
        _wrapper_cache[workspace]  = workspace_wrapper
    
        return workspace_wrapper