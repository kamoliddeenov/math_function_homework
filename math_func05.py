from math import cos, degrees
def main(a,b):
    c = a * cos(b)
    d = degrees(c)
    return round(d,2)

print(main(8,15))