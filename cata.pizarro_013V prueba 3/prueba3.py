import time
import os
sw = True
Tipo2='Buscar Datos'
Tipo1='Grabar Datos'
lista1=[]
while sw:
    os.system("cls")
    print ("1. Opción Grabar Datos")
    print ("2. Opción Buscar Datos")
    print ("3. Opción Listar Datos")
    print ("4. Salir")

    try:
        op = int(input("Ingrese su opción\n"))
        if(op > 0 and op < 5):
            if (op == 1):
                print("Selecciono opcion 1")
                tipo1='Grabar Datos'
                tipo_auto=input("ingrese tipo de auto: ")
                lista1.insert(0,tipo_auto)
                patente1=input("ingrese su patente: ")
                lista1.insert(1,patente1)
                marca=input("ingrese marca: ")
                lista1.insert(2,marca)
                precio=input("ingrese precio: ")
                lista1.insert(3,precio)
                print(lista1)
                resp=input("Desea volver al menu principal? 1.si 2.no: ")
                if resp == "si":
                    continue
                else:
                    continuar = False
            elif(op == 2):
                print("Buscar Datos")
                tipo2 = 'Buscar Datos'
                buscar=input("ingrese su rut: ")
                lista1.index(buscar)
                if buscar == patente1:
                    print([lista1])
            elif(op == 3):
                print("Adulto Mayor")
                tipo3='Adultomayor'
                cant3=int(input("ingrese la cantidad de entradas"))
                cant_entradas3= 0
                Valor3=1000
                Valor_final3= cant3 * Valor3
            elif(op == 4):
                print("Adios")
            sw = False
        else:
            print("Tipo de dato no permitido, vuelva a intentarlo")
            time.sleep (2)
    except:
        print ("Ha ingresado una opción inválida")
        time.sleep(2)
