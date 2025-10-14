from math import sqrt

a = int(input('a = '))
b = int(input('b = '))

perimeter = (a+b)*2
area = a * b
diagonal = sqrt(a**2 + b**2)

print(f"Perimeter: {perimeter}")
print(f"Area: {area}")
print(f"Diagonal: {diagonal}")