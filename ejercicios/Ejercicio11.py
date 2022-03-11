'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 11/03/2022  ###
        ###               Ejercicio 11             ###
        ##############################################
'''

from funciones.funciones import *

precio = input("Introduce el precio bruto del producto: ")
print("El precio con IVA es: ", iva(float(precio)))