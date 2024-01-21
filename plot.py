import mat.s.geometry as _g
import numpy as _np
import matplotlib.pyplot as _plt

_ORIGIN = _np.array([[0, 0, 0],[0, 0, 0]]) # origin point

def plot(obj:_g.Vector|_g.Point, **kwargs):
    if isinstance(obj, _g.Vector):
        _plt.quiver(*_ORIGIN, [obj[0]], [obj[1]], **kwargs)
    if isinstance(obj, _g.Point):
        _plt.plot([obj[0]], [obj[1]], "o")


def show():
    _plt.show()

