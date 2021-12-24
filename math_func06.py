from math import tan, degrees
def main(a,b):
    c = a * tan(b)
    d = degrees(c)
    return round(d,2)

print(main(18,8))