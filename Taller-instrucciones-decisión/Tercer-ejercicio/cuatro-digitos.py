"""Programa para saber si un numero
posee únicamente cuatro digitos"""

print("\n✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥")
print("✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥")
print("✥✥✥✥✥✥✥✥✥ CUATRO DIGITOS ✥✥✥✥✥✥✥✥")
print("✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥")
print("✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥✥\n")

# input

X = int(input("Ingrese un número entero: "))

# processing

if 999 < X < 10000:
    msj = (" es de cuatro dígitos")
else:
    msj = (" no posee cuatro digitos")
# output

print("\nEl numero " + str(X) + msj)
