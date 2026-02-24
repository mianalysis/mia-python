from jpype import JClass

from src.objects.javamodule import JavaModule
from src.objects.module import Module
from src.objects.modules import Modules
from src.wrappers.moduleswrapper import wrapModules

import xml.etree.ElementTree as ET

CLASSNAME: str = "CLASSNAME"
DISABLEABLE: str = "DISABLEABLE"
ENABLED: str = "ENABLED"
ID: str = "ID"
NAME: str = "NAME"
NICKNAME: str = "NICKNAME"
NOTES: str = "NOTES"
SHOW_BASIC_TITLE: str = "SHOW_BASIC_TITLE"
SHOW_OUTPUT: str = "SHOW_OUTPUT"
VERSION: str = "VERSION"

def read(filepath: str, modules: Modules): # To do
    tree = ET.parse(filepath)
    root = tree.getroot()
    modules_nodes = root.findall("MODULES")
    
    for modules_node in modules_nodes:
        for module_node in modules_node:
            module: Module | None = initialiseModule(module_node, modules)
            print(module)
        
        
def initialiseModule(module_node: ET.Element, modules: Modules) -> Module | None:
    classname: str | None = module_node.get(CLASSNAME)
    
    if classname is None:
        return None
    
    # This is a Java module
    if "io.github.mianalysis.mia" in classname:
        return initialiseJavaModule(module_node, modules)
    else:
        return initialisePythonModule(module_node, modules)
    
def initialiseJavaModule(module_node: ET.Element, modules: Modules) -> JavaModule | None:
    classname: str | None = module_node.get(CLASSNAME)
    
    if classname is None:
        return None
    
    disableable: bool = bool(module_node.get(DISABLEABLE, True))
    enabled: bool = bool(module_node.get(ENABLED))
    id: str = module_node.get(ID, "")
    nickname: str = module_node.get(NICKNAME, "")
    notes: str = module_node.get(NOTES, "")
    show_basic_title: bool = bool(module_node.get(SHOW_BASIC_TITLE))
    show_output: bool = bool(module_node.get(SHOW_OUTPUT))
    
    module_class = JClass(classname)
    module = module_class(wrapModules(modules)) # Will need to provide Modules for normal usage
    
    module.setCanBeDisabled(disableable)
    module.setEnabled(enabled)
    module.setModuleID(id)
    module.setNickname(nickname)
    module.setNotes(notes)
    module.setShowProcessingViewTitle(show_basic_title)
    module.setShowOutput(show_output)
    
    return JavaModule(module)

def initialisePythonModule(module_node: ET.Element, modules: Modules) -> Module | None:
    raise NotImplementedError("AnalysisReader: initialisePythonModule")

        
        