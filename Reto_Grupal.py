#Ejercicio #1 de Game of Progra
#Menu
#Variables
conteoPersonas = 1
estadisticaEdades = 2
salir = 0
#Obciones del menu
menuPrincipal = int(input("Menu Principal: \n 1-Ingresar una edad. \n 2-Ver la estadistica. \n 0-Salir.\n"))
while menuPrincipal !=0:
    if menuPrincipal == 1:
        #Conteo de personas.
        #Variables
        edad = 0
        menor = 0 
        adulto = 0
        mayor = 0
        ingreseOtra = "si"
        #conteo de las personas 
        while ingreseOtra == "si" or ingreseOtra == "s":
          edad = int(input("Ingrese su edad: "))
          if edad < 18:
            menor += 1
            ingreseOtra = input("Desea agregar otra edad (si o no):\n")
          elif edad in range(17,66):
            adulto += 1
            ingreseOtra = input("Desea agregar otra edad (si o no):\n")
          else:
            mayor += 1
            ingreseOtra = input("Desea agregar otra edad (si o no):\n")
    elif menuPrincipal == 2:
        #aqui va el codigo de la estadistica
    else: 
        print ("Digita una opcion correcta.")
    menuPrincipal = int(input("Menu Principal: \n 1-Ingresar una edad. \n 2-Ver la estadistica. \n 0-Salir.\n"))
