"""Programa para ordenar de manera ascendente tres numeros"""

print("\n♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜")
print("♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜")
print("♜♜♜♜♜♜ Ordenar números de manera ♜♜♜♜♜♜")
print("♜♜♜♜♜♜♜♜♜♜♜♜♜ ascendente ♜♜♜♜♜♜♜♜♜♜♜♜♜♜")
print("♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜")
print("♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜♜\n")


X = int(input("Ingrese el primer numero: "))
Y = int(input("Ingrese el segundo numero: "))
Z = int(input("Ingrese el tercer numero: "))

if Y < X > Z:
    if Y > Z:
        print("\nEl orden ascendente es:" + str(Z) + "-" + str (Y)+ "-" + str(X))
    if Z > Y:
        print("\nEl orden ascendente es:" + str(Y)+ "-" + str(Z)+ "-" + str(X))
elif X < Y > Z:
    if X > Z:
        print("\nEl orden ascendente es:" + str(Z)+ "-" + str(X)+ "-" + str(Y))
    if Z > X:
        print("\nEl orden ascendente es:" + str(X)+ "-" + str(Z)+ "-" + str(Y))
elif Y < Z > X:
    if Y > X:
        print("\nEl orden ascendente es:" + str(X)+ "-" + str(Y)+ "-" + str(Z))
    if X > Y:
        print("\nEl orden ascendente es:" + str(Y)+ "-" + str(X)+ "-" + str(Z))
else:
    print("\nLos numeros son iguales")

        

