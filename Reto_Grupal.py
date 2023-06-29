# Ejercicio #1 de Game of Progra

# Variables
personas = 0
edad = 0
menor = 0
adulto = 0
mayor = 0
porcentajeMenor = 0
porcentajeAdulto = 0
porcentajeMayor = 0

# Opciones del menú
try:
    menuPrincipal = int(input("Menu Principal: \n 1-Ingresar una edad. \n 2-Ver la estadistica. \n 0-Salir.\n"))
except:
    menuPrincipal = -1
    print("Digita una opción correcta.")

while menuPrincipal != 0:

    if menuPrincipal == 1:
        # Conteo de personas.

        ingreseOtra = "si"
        # conteo de las personas
        while ingreseOtra == "si" or ingreseOtra == "s":
            edad = int(input("Ingrese su edad: "))
            if edad < 18:
                personas += 1
                menor += 1
                ingreseOtra = input("Desea agregar otra edad (si o no):\n")
            elif edad in range(17, 66):
                adulto += 1
                personas += 1
                ingreseOtra = input("Desea agregar otra edad (si o no):\n")
            else:
                mayor += 1
                personas += 1
                ingreseOtra = input("Desea agregar otra edad (si o no):\n")
    elif menuPrincipal == 2:
        # Estadísticas

        porcentajeMenor = (int(menor) * 100) / int(personas)
        porcentajeAdulto = (int(adulto) * 100) / int(personas)
        porcentajeMayor = (int(mayor) * 100) / int(personas)

        print("A continuación se observa las estadísticas de las personas: \n")
        print("Cantidad de personas menores a 18 años: ", menor, " ", str(porcentajeMenor)+"%")
        print("Cantidad de personas entre 18 años a 65 años: ", adulto, " ", str(porcentajeAdulto)+"%")
        print("Cantidad de personas mayor a 65 años: ", mayor, " ", str(porcentajeMayor)+"%")
        break
    else:
        print("Digita una opción correcta.")

    try:
        menuPrincipal = int(input("Menu Principal: \n 1-Ingresar una edad. \n 2-Ver la estadistica. \n 0-Salir.\n"))
    except:
        menuPrincipal = -1
        print("Digita una opción correcta.")
