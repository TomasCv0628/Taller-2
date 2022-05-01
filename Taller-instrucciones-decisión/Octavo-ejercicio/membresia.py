"""Programa para encontrar el valor de una compra segun los beneficios"""

import os
# input

from ast import While



X = int(input("Ingrese el valor de la compra:"))

# processing

while True:
    print("\nSeleccione su membresia\n\
Si es cliente general y va a pagar de contado presione G \n\
Si es cliente afiliado y va a pagar de contado presione A\n\
Si es cliente general y va a pagar a cuotas presione C\n\
Si es cliente afiliado y va a pagar a cuotas presione Q\n\
Presione X para salir")


    opcion = input()
    if opcion == 'G':
            print(f"S\nu compra tendria un valor de {X - X*15/100 } ")
    elif opcion == 'C':
            print(f"\nSu compra tendra un valor de {X + X*10/100 }")
    elif opcion == 'A':
            print(f"\nSu compra tendria un valor de {X - X*20/100 }")
    elif opcion == 'Q':
            print(f"\nSu compra tendria un valor de {X + X*5/100 }")
    elif opcion == 'X':
        break
    input()
 



