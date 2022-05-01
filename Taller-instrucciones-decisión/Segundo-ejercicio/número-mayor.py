"""Programa para encontrar el numero mayor
de tres numeros"""

print("\n♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛")
print("♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛")
print("♛♛♛♛♛♛♛ NUMERO MAYOR DE TRES ♛♛♛♛♛♛♛♛")
print("♛♛♛♛♛♛♛♛♛♛♛♛♛♛ NUMEROS ♛♛♛♛♛♛♛♛♛♛♛♛♛♛")
print("♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛")
print("♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛\n")

# input

X = int(input("Inserte el primer numero:" ))
Y = int(input("Inserte el segundo numero: "))
Z = int(input("Inserte el tercer numero: "))

# processing

if X > Y and X > Z:
    msj = (" el primer numero es el mayor") 
elif X > Y and X < Z:
    msj = (" el tercer numero es el mayor ")
elif X < Y and Y > Z:
    msj = (" el segundo numero es el mayor")
elif X < Y and Y < Z:
    msj = (" el tercer numero es el mayor ")
else:
    msj =  (" los numeros son iguales ")

# output

print("\nDe los tres numeros " + msj)