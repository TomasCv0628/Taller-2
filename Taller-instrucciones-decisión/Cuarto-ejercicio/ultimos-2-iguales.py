"""Programa para daber si los ultimos dos dígitos de un numero son iguales"""

print("\n❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅")
print("❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅")
print("❅❅❅❅❅❅ Los últimos dígitos ❅❅❅❅❅❅")
print("❅❅❅❅❅❅❅❅❅❅❅❅ iguales ❅❅❅❅❅❅❅❅❅❅❅❅")
print("❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅")
print("❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅❅\n")
# input

X = int(input("Inserte un número entero: "))

# processing

Z1 = X % 10
Z2 = (X % 100)//10

if Z1 == Z2:
    msj = (" son iguales")
else:
    msj = (" no son iguales")

# output

print("\nLos ultimos dos dígitos del número" + "-" + str(X) + msj)
