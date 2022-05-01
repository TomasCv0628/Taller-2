"""Programa que encuentra el valor de una llamada telefonica"""

print("\n--------------------------------")
print("--------------------------------")
print("--------- Valor de una ---------")
print("----------- llamada ------------")
print("--------------------------------")
print("--------------------------------\n")


# input

X = int(input("Tiempo de la llamada: "))


# processing
  
if X <= 3:
    valor = 300
else:
    valor = 300 + 50 * (X-3)

print("\nEl costo es:" + str(valor))
