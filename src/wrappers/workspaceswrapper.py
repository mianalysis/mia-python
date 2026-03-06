from __future__ import annotations
from jpype import JImplements, JOverride # type: ignore
from weakref import WeakKeyDictionary

from src.objects.workspaces import Workspaces
from src.wrappers.workspacewrapper import WorkspaceWrapper

_wrapper_cache: WeakKeyDictionary[Workspaces, WorkspacesWrapper] = WeakKeyDictionary()


@JImplements('io.github.mianalysis.mia.object.metadata.MetadataI')
class WorkspacesWrapper:
    def __init__(self):
        self._workspaces: Workspaces = Workspaces()
        
    def getPythonWorkspaces(self) -> Workspaces:
        return self._workspaces
    
    def setPythonWorkspaces(self, workspaces: Workspaces):  # No return
        self._workspaces = workspaces
    
    @JOverride
    def getNewWorkspace(self, current_file, series: int) -> WorkspaceWrapper: # To do
        raise NotImplementedError('WorkspacesWrapper: getNewWorkspace')
    
    @JOverride    
    def getWorkspace(self, ID: int) -> WorkspaceWrapper:
        raise NotImplementedError('WorkspacesWrapper: getWorkspace')
    
    @JOverride
    def getMetadataWorkspaces(self, metadata_ame: str): # To do
        raise NotImplementedError('WorkspacesWrapper: getMetadataWorkspaces')
    
    @JOverride
    def resetProgress(self): # No return
        raise NotImplementedError('WorkspacesWrapper: resetProgress')
    
    @JOverride
    def getOverallProgress(self) -> float:
        raise NotImplementedError('WorkspacesWrapper: getOverallProgress')
    
    @JOverride
    def add(self, workspace: WorkspaceWrapper) -> bool:
        raise NotImplementedError('WorkspacesWrapper: add')
    
    @JOverride
    def size(self) -> int:
        raise NotImplementedError('WorkspacesWrapper: size')
    
    @JOverride
    def contains(self, workspace: WorkspaceWrapper) -> bool:
        raise NotImplementedError('WorkspacesWrapper: contains')
    
    @JOverride
    def clear(self): # No return
        raise NotImplementedError('WorkspacesWrapper: clear')
    
    
def wrapWorkspaces(workspaces: Workspaces) -> WorkspacesWrapper:
    try:
        return _wrapper_cache[workspaces]
    except:        
        workspaces_wrapper: WorkspacesWrapper = WorkspacesWrapper()
        workspaces_wrapper.setPythonWorkspaces(workspaces)
        _wrapper_cache[workspaces]  = workspaces_wrapper
    
        return workspaces_wrapper
