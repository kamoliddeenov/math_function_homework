from math import sin, degrees, pi
def  main(a,b):
    b = pi/2
    return round(degrees(a*sin(b)), 2)

print(main(4,3))