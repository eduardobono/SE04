'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 02/03/2022  ###
        ###               Ejercicio 2              ###
        ##############################################
'''

from funciones.funciones import *

def ejer02():

    # VARIABLES
    n = 4
    a = 3.2
    c = "4"

    print("la variable n tiene un valor de: ", n)
    print("la variable a tiene un valor de: ", a, "\n")
    print("La suma de las 2 variables es ", suma(a, n))
    print("La resta de las 2 variables es %.4f" % resta(a, n))
    print("El valor numérico de c es: ", int(c))
