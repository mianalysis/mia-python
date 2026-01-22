from jpype import JImplements, JOverride # type: ignore
    
@JImplements('io.github.mianalysis.mia.object.image.renderer.ImageRenderer') # type: ignore
class NotebookImageRenderer:     
    def __init__(self, ij):
        self._ij = ij
          
    @JOverride
    def render(self, image, title, lut, normalise, display_mode, overlay):
        self._ij.py.show(image.getRawImage())
        