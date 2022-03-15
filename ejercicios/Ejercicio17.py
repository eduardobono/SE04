'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 11/03/2022  ###
        ###               Ejercicio 17             ###
        ##############################################
'''

from funciones.funciones import *

# variables
intentos = 3

for i in range(1, intentos +1):
    password = input("Por favor introduce la contraseña: ")
    result = passwd(password)
    if result == 1:
        print("Contraseña correcta!!!")
        exit(0)
    else:
        print(" Contraseña incorrecta, por favor vuelva a introducirla")

print ("Ha introducido demasiadas veces la contraseña incorrecta, se informa al Administrador")