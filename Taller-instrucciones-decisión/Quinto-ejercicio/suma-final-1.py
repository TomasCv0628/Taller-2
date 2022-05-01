"""Programa para saber si la suma de los dos últimos dígitos es 
igual a un número de 1 dígito"""

print("\n♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘")
print("♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘")
print("♘♘♘♘♘♘ La suma de ultimos dos ♘♘♘♘♘♘")
print("♘♘♘♘♘♘♘♘♘ dígitos igual a ♘♘♘♘♘♘♘♘♘♘")
print("♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘ uno ♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘")
print("♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘")
print("♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘♘\n")
# input


X = int(input("Inserte un número: "))

# processing

Z1 = X % 10
Z2 = (X % 100)//10
Z3 = Z1 + Z2

if 0 <= Z3 < 10:
    msj = (" es de 1 dígito ")
else:
    msj = (" no es de 1 dígito")
# output

print("\nLa suma de los dos ultimos dígitos de " + str(X) + msj )

