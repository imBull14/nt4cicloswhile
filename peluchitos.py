peluches=["roshi","conejito","aguacatico"]

#estructura del while en phyton

opcion=0

print("Pelucheria PELUCHITOS")
print("......................")
print("1: Agregar producto a la bodega")
print("2. Ver productos en bodega")
print("3. Obtener valor del inventario")
print("4. Ver productos más vendidos")
print("5. SALIR")

while(opcion!=5):
    opcion=int(input("Digita un número: "))

    if(opcion==1):
        print("Usted está en la opción 1")
    elif(opcion==2):
        print("Usted está en la opción 2")
    elif(opcion==3):
        print("Usted está en la opción 3")
    elif(opcion==4):
        print("Usted está en la opción 4")
    else:
        print("La opcion digitada es incorrecta")

print("Sali del ciclo")