"""Programa para descubrir las raices de una ecuaciรณn de segundo grado"""
print("\n๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐")
print("๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐")
print("๐๐๐๐๐๐ RAICES DE UNA ECUACIรN ๐๐๐๐๐๐")
print("๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐ DE ๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐")
print("๐๐๐๐๐๐๐๐๐๐๐ SEGUNDO GRADO ๐๐๐๐๐๐๐๐๐๐")
print("๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐๐\n1")

import math
print("\nRecuerde que es una ecuaciรณn de la forma aX^2+bX+c=0\n")
a = input("Inserte el valor de a: ")
a = float(a)
b = input("Inserte el valor de b: ")
b = float(b)
c = input("Inserte el valor de c: ")
c = float(c)
d = float((b*b)-(4*(a)*(c)))

if d <  0:
    print("La ecuaciรณn tiene solucion en los complejos")
elif d > 0:
    if a != 0:
        if b != 0:
             x1 = (-(b) + math.sqrt((b*b)-(4*(a)*(c)))) / (2*(a))
             x1 = float(x1)
             x2 = (-(b) - math.sqrt((b*b)-(4*(a)*(c)))) / (2*(a))
             x2 = float(x2)
             print("\nX1 = "+str(x1))
             print("X2 = "+str(x2))
        else:
            print("La ecuaciรณn tiene solucion en los complejos")
    else:
        print("La ecuaciรณn tiene solucion en los complejos")
else:
    print("La ecuaciรณn tiene solucion en los complejos")