import xml.etree.ElementTree as ET

class AnalysisReader():
    def read(self, filepath: str): # To do
        tree = ET.parse(filepath)
        root = tree.getroot()
        
        for child in root:
            for childchild in child:
                print(childchild.tag, childchild.attrib)
        
        