from jpype import JImplements, JOverride
from scyjava import jimport

ObjI = jimport('io.github.mianalysis.mia.object.coordinates.Obj')

@JImplements(ObjI)
class ObjWrapper:
    def __init__(self):
        print('Implement constructor')
     