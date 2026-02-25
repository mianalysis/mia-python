from jpype import JClass
from typing import List

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
VALUE: str = "VALUE"
VERSION: str = "VERSION"
VISIBLE: str = "VISIBLE"

def read(filepath: str): # To do
    tree = ET.parse(filepath)
    root: ET.Element = tree.getroot()
    modules_nodes: List[ET.Element] = root.findall("MODULES")
    
    modules: Modules = Modules()
    module_node: ET.Element
    for modules_node in modules_nodes:
        for module_node in modules_node:
            module: Module = initialiseModule(module_node, modules)
            print(module)
        
        
def initialiseModule(module_node: ET.Element, modules: Modules) -> Module:
    classname: str | None = module_node.get(CLASSNAME)
    
    if classname is None:
        raise Exception(f'AnalysisReader: Classname {classname} not found')
    
    # This is a Java module
    module: Module
    if "io.github.mianalysis.mia" in classname:
        module = initialiseJavaModule(module_node, modules)
    else:
        module = initialisePythonModule(module_node, modules)
    
    # Populate parameters
    parameters_node: ET.Element | None = module_node.find("PARAMETERS")
    if parameters_node is None:
        raise Exception(f'AnalysisReader: Can\'t find parameters')
    
    populateParameters(parameters_node, module)
    
    return module
    
def initialiseJavaModule(module_node: ET.Element, modules: Modules) -> JavaModule:
    classname: str | None = module_node.get(CLASSNAME)
    
    if classname is None:
        raise Exception(f'AnalysisReader: Classname {classname} not found')
    
    disableable: bool = bool(module_node.get(DISABLEABLE, True))
    enabled: bool = bool(module_node.get(ENABLED))
    id: str = module_node.get(ID, "")
    nickname: str = module_node.get(NICKNAME, "")
    notes: str = module_node.get(NOTES, "")
    show_basic_title: bool = bool(module_node.get(SHOW_BASIC_TITLE))
    show_output: bool = bool(module_node.get(SHOW_OUTPUT))
    
    module_class = JClass(classname)
    module: Module = module_class(wrapModules(modules)) # Will need to provide Modules for normal usage
    
    module.setCanBeDisabled(disableable)
    module.setEnabled(enabled)
    module.setModuleID(id)
    module.setNickname(nickname)
    module.setNotes(notes)
    module.setShowProcessingViewTitle(show_basic_title)
    module.setShowOutput(show_output)
    
    return JavaModule(module)

def initialisePythonModule(module_node: ET.Element, modules: Modules) -> Module:
    raise NotImplementedError("AnalysisReader: initialisePythonModule")

def populateParameters(parameters_node: ET.Element, module: Module):
    parameter_nodes: List[ET.Element] = parameters_node.findall("PARAMETER")
    parameter_node: ET.Element
    for parameter_node in parameter_nodes:
        name: str = parameter_node.get(NAME, "")
        nickname: str = parameter_node.get(NICKNAME, "")
        value: str = parameter_node.get(VALUE, "")
        visible: bool = bool(parameter_node.get(VISIBLE, False))
        
        module.updateParameterValue(name, value)
        
        parameter = module.getParameter(name)
        if parameter is None:
            raise Exception(f'AnalysisReader: Parameter "{name}" in module "{module.getName()}" not found')
        
        parameter.setNickname(nickname)
        parameter.setVisible(visible)
