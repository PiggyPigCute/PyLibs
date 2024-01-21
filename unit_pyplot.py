
## NEEDS `unit_calc` lib

import numpy as _np
import matplotlib.pyplot as _plt


def _get_unit(X):
    x_unit = 1

    if isinstance(X, _u.unit):
        x_unit = X.dim
    elif type(X) in (list, tuple, _np.ndarray):
        x_unit = 1
        if isinstance(X[0], _u.unit):
            x_unit = X[0].dim
    
    return x_unit


def plot(X, Y, **kwargs):
    _plt.plot(X/_get_unit(X), Y/_get_unit(Y), **kwargs)

