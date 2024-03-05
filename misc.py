import random as rd

def cut(dec:float, digits:int=3) -> float:
    return round(dec*10**digits)/10**digits

def jcut(jdec:complex, digits:int=3) -> complex|float:
    if round(jdec.imag*10**digits) == 0:
        return cut(jdec.real, digits)
    return cut(jdec.real, digits) + 1j*cut(jdec.imag, digits)

def flist(iterable, f, *args, **kwargs) -> list:
    return [f(i, *args, **kwargs) for i in iterable]

def fmat(matrix, f, *args, **kwargs) -> list[list]:
    return [flist(i, f, *args, **kwargs) for i in matrix]

def rfloat(inf,sup):
    return rd.random()*(sup-inf)+inf

def rdigit():
    return rd.randint(0,9)

def ri():
    return rd.randint(-9,9)

def rf():
    return rfloat(-10,10)

def rj():
    return rf() + 1j*rf()

π = 3.14159265358979323
