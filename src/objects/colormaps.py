from matplotlib.colors import ListedColormap

import numpy as np
from numpy.random import seed

def Random() -> ListedColormap:
    colors = np.random.default_rng(seed=230517).random((256, 3))
    colors[0] = [0, 0, 0]

    return ListedColormap(colors)
