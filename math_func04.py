from math import sin, degrees, radians
def main(a,b):
    c = a * sin(b)
    d = degrees(radians(c))
    return round(d,2)

print(main(30,60))