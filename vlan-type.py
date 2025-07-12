#Identificacion de tipo de VLAN

userInput = int(input("Ingresa el número de la VLAN: "))
if 1 <= userInput <= 1005:
    print("VLAN de Rango Normal")
elif 1006 <= userInput <= 4094:
    print("VLAN de Rango Extendido")
else:
    print("El número ingresado no corresponde a un número de VLAN valido")

