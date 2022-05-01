"""Programa que resuelva una ecuación de primer grado"""

print("\n✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧")
print("✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧")
print("✧✧✧✧✧✧ Ecuaciones de primer✧✧✧✧✧✧")
print("✧✧✧✧✧✧✧✧✧✧✧✧✧ grado ✧✧✧✧✧✧✧✧✧✧✧✧✧")
print("✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧")
print("✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧✧\n")

"aX + c = 0"
"X = -c/a"

# input
print("\nRecuerde  que es una ecuación de la forma aX+c=0\n")
X = int(input(" Inserte el valor de a: "))
Y = int(input(" Inserte el valor de c: "))

# processing

Z = (-Y/X)

if X != 0:
    msj = (str(Z))


# output

print("\nLa ecuación es igual " + msj )

