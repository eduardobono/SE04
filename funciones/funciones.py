'''
        ##############################################
        ### Autor: Eduardo Bono Fecha: 11/03/2022  ###
        ### Funciones de los ejercicios propuestos ###
        ##############################################
'''
import math
#FUNCIONES


# Suma
def suma(a, b):
    c = a + b
    return c

# Resta
def resta(a, b):
    c = a - b
    return c

# Multiplicacion
def multiplicacion(a, b):
    c = a * b
    return c

# Division
def division(a, b):
    c = a / b
    return c

# Modulo
def modulo (a, b):
    c = a % b
    return c

# Doble
def doble(a):
    c = a * 2
    return c

# Area del circulo
def area(a):
    c = math.pi * (pow(int(a), 2))
    return c

# Calculo de un precio + IVA (21%)
def iva(a):
    c = a * 1.21
    return c

# Detectar si un dia es laborable
def laborable(dia):
    # variables
    laborable = ["lunes", "martes", "miercoles", "jueves", "viernes"]
    festivos = ["sabado", "domingo"]

    if (list(filter(lambda x: dia in x, laborable))):
        result = "es un dia laboral"
    elif (list(filter(lambda x: dia in x, festivos))):
        result = "es un dia festivo"
    else:
        result = "no es un dia valido"
    return result

# Detectar contraseña valida
def passwd(a):
    # variables
    password = "contrasenya"
    if (password == a):
        result = 1
    else:
        result = 0

    return result