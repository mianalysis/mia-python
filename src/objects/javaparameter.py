from src.objects.parameter import Parameter


class JavaParameter(Parameter):
    def __init__(self, java_parameter) -> None:
        self._java_parameter = java_parameter

    def initialiseControl(self):
        raise NotImplementedError("JavaParameter: initialiseControl")

    def getValue(self, workspace):
        raise NotImplementedError("JavaParameter: getValue")

    def setValue(self, value) -> None:
        raise NotImplementedError("JavaParameter: setValue")

    def getRawStringValue(self) -> str:
        raise NotImplementedError("JavaParameter: getRawStringValue")

    def setValueFromString(self, string: str) -> None:
        self._java_parameter.setValueFromString(string)

    def verify(self) -> bool:
        raise NotImplementedError("JavaParameter: verify")

    def duplicate(self, new_module):
        raise NotImplementedError("JavaParameter: duplicate")

    def getNameAsString(self) -> str:
        raise NotImplementedError("JavaParameter: getNameAsString")

    def getAlternativeString(self) -> str:
        raise NotImplementedError("JavaParameter: getAlternativeString")

    def createNewInstance(self, name, module):
        raise NotImplementedError("JavaParameter: createNewInstance")

    def getModule(self):
        raise NotImplementedError("JavaParameter: getModule")

    def setModule(self, module):
        raise NotImplementedError("JavaParameter: setModule")

    def getControl(self):
        raise NotImplementedError("JavaParameter: getControl")

    def setControl(self, control) -> None:
        raise NotImplementedError("JavaParameter: setControl")

    def isVisible(self) -> bool:
        raise NotImplementedError("JavaParameter: isVisible")

    def setVisible(self, visible: bool) -> None:
        self._java_parameter.setVisible(visible)

    def isValid(self) -> bool:
        raise NotImplementedError("JavaParameter: isValid")

    def setValid(self, valid: bool) -> None:
        raise NotImplementedError("JavaParameter: setValid")

    def isExported(self) -> bool:
        raise NotImplementedError("JavaParameter: isExported")

    def setExported(self, exported: bool) -> None:
        raise NotImplementedError("JavaParameter: setExported")

    # From Ref

    def appendXMLAttributes(self, element):
        raise NotImplementedError("JavaParameter: appendXMLAttributes")

    def setAttributesFromXML(self, node):
        raise NotImplementedError("JavaParameter: setAttributesFromXML")
