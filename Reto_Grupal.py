#Ejercicio #1 de Game of Progra
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
