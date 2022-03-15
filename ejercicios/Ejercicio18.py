'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 11/03/2022  ###
        ###               Ejercicio 18             ###
        ##############################################
'''

from funciones.funciones import *

a = input("Introduce el primer opernado: ")
b = input("Introduce el segundo opernado: ")
c = 0

print("     Operadores      ")
print("+ - suma los dos operandos")
print("- - resta los operandos")
print("* - multiplica los operandos")
print("/ - divide los operandos, este debe dar un resultado con decimales float ")
print("^ - 1er operando como base y 2º como exponente")
print("% - módulo, resto de la división entre operando 1 y operando 2\n")

while c != 1:
    operador = input("Introduce el operador :")
    c = comprobacion(operador)
    if (c != 1):
        print("Operador no valido")
    else:
        result = operador(a, b, operador)

    print("El resultado de la operacion es: ", result)