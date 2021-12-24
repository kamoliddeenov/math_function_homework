from math import sin, degrees, pi, radians
def  main(a,b):
    return round(degrees(a*radians(sin(b))), 2)

print(main(60,90))