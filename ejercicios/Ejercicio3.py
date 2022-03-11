'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 11/03/2022  ###
        ###               Ejercicio 3              ###
        ##############################################
'''

from funciones.funciones import *

def ejer03():
    # VARIABLES
    x = 4
    y = 5
    n = 2.4
    m = 4.8

    print("La suma de x e y es: ", suma(x, y))
    print("La diferencia entre y e x es: ", resta(y, x))
    print("El producto de x e y es: ", suma(x, y))
    print("La cociente de x entre y es: ", division(x, y))
    print("El resto de x e y es: ", modulo(x, y))
    print("La suma de n y m es: %.4f" % suma(n, m))
    print("La diferrencia entre n y m es: %.4f" % resta(n, m))
    print("El producto de n y m es: %.4f" % multiplicacion(n, m))
    print("El cociente de n entre m es: %.4f" % division(n, m))
    print("El resto de n entre m es: %.4f" % modulo(n, m))
    print("La suma de x y n es:  %.4f" % suma(x, n))
    print("El cociente de y entre m es: %.4f" % division(y, m))
    print("El resto de y entre m es: %.4f" % modulo(y, m))
    print("El doble de las variables es: x = ", doble(x), ", y = ", doble(y), ", n = %.4f" % doble(n), ", m = %.4f" % doble(m))
    print("La suma de todas las variables es: %.4f" % (x + y + n + m))
    print("El producto de todas las variables es: %.4f" % (x * y * n * m))
