'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 11/03/2022  ###
        ###               Ejercicio 10             ###
        ##############################################
'''

from funciones.funciones import *

numero = input("Por favor introduce un numero: ")
if (modulo(int(numero), 2)) == 0:
    print("el numero es par")
else:
    print("el numero es impar")