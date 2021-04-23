import math

def f(x,y):
    return math.e**(x*y) + (x-3)**2 + y**2

def f10(x,y):
    return y*math.e**(x*y) + 2*(x-3)

def f01(x,y):
    return x*math.e**(x*y) + 2*y

def f11(x,y):
    return math.e**(x*y) + y*x*math.e**(x*y)

def f20(x,y):
    return y*y*math.e**(x*y) + 2

def f02(x,y):
    return x*x*math.e**(x*y) + 2

def det(a, b, c, d):
    return 1/(a*d - b*c)

def f2(x,y):
    return math.sin(x+2*y)

def f2_10(x,y):
    return math.cos(x+2*y)

def f2_01(x,y):
    return 2*math.cos(x+2*y)


def NR(x0, y0):
    d = det(f20(x0, y0), f11(x0, y0), f11(x0, y0), f02(x0, y0))
    x = x0 - d * (f02(x0, y0) * f10(x0, y0) - f11(x0, y0) * f01(x0, y0))
    y = y0 - d * (f20(x0, y0) * f01(x0, y0) - f11(x0, y0) * f10(x0, y0))
    # if (x-x0)**2 + (y-y0)**2 < 0.000001:  # return condition quality
    #     return x,y
    # return NR(x, y)
    while (x-x0)**2 + (y-y0)**2 >= 0.000001:
        x0 = x
        y0 = y
        d = det(f20(x0, y0), f11(x0, y0), f11(x0, y0), f02(x0, y0))
        x = x0 - d * (f02(x0, y0) * f10(x0, y0) - f11(x0, y0) * f01(x0, y0))
        y = y0 - d * (f20(x0, y0) * f01(x0, y0) - f11(x0, y0) * f10(x0, y0))
    return x,y


def NR2(x0,y0):
    d = det(f10(x0, y0), f01(x0, y0), f2_10(x0, y0), f2_01(x0, y0))
    x = x0 - d*(f(x0, y0) * f2_01(x0, y0) - f2(x0, y0)*f01(x0, y0))
    y = y0 - d*(f2(x0, y0)*f10(x0, y0) - f(x0, y0)*f2_10(x0, y0))
    # if (x - x0) ** 2 + (y - y0) ** 2 < 0.000001:  # return condition quality
    #     return x, y
    # return NR2(x, y)
    while (x - x0) ** 2 + (y - y0) ** 2 >= 0.000001:
        x0 = x
        y0 = y
        d = det(f10(x0, y0), f01(x0, y0), f2_10(x0, y0), f2_01(x0, y0))
        x = x0 - d * (f(x0, y0) * f2_01(x0, y0) - f2(x0, y0) * f01(x0, y0))
        y = y0 - d * (f2(x0, y0) * f10(x0, y0) - f(x0, y0) * f2_10(x0, y0))
    return x,y


a,b = NR(1, 1)
print("x,y:", a, b)
print(f(a,b))
print(f2(a,b))

