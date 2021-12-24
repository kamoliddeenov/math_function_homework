from math import sin, degrees
def  main(a,b):
    c = sin(a) * sin(b)
    d = degrees(c)
    return round(d, 2)

print(main(4,3))