from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.objects.workspace import Workspace


class Workspaces:
    def __init__(self):
        pass

    def getNewWorkspace(self, current_file, series: int) -> Workspace:  # To do
        raise NotImplementedError("Workspaces: getNewWorkspace")

    def getWorkspace(self, ID: int) -> Workspace:
        raise NotImplementedError("Workspaces: getWorkspace")

    def getMetadataWorkspaces(self, metadata_ame: str):  # To do
        raise NotImplementedError("Workspaces: getMetadataWorkspaces")

    def resetProgress(self):  # No return
        raise NotImplementedError("Workspaces: resetProgress")

    def getOverallProgress(self) -> float:
        raise NotImplementedError("Workspaces: getOverallProgress")

    def add(self, workspace: Workspace) -> bool:
        raise NotImplementedError("Workspaces: add")

    def size(self) -> int:
        raise NotImplementedError("Workspaces: size")

    def contains(self, workspace: Workspace) -> bool:
        raise NotImplementedError("Workspaces: contains")

    def clear(self):  # No return
        raise NotImplementedError("Workspaces: clear")
