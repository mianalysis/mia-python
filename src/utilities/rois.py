from src.objects.image import Image
from src.objects.volume import Volume

def getRoi(volume: Volume, slice: int):
    slice_volume: Volume = volume.getSlice(slice)
    slice_image: Image = slice_volume.getAsTightImage("Crop")
    
    return None