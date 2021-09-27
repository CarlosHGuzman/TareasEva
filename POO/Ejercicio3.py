# Realizar un programa en el cual se declaren dos valores enteros por teclado
# utilizando el método __init__. Calcular después la suma, resta, multiplicación
# y division. Utilizar un método para cada una e imprimir los resultados
# obtenidos. LLamar a la clase Calculadora.

from os import system as lim


class Calculadora:
    def __init__(self, numero1: float = 0, numero2: float = 0):
        self.__numero1 = numero1
        self.__numero2 = numero2

    def calcular_suma(self):
        return self.__numero1 + self.__numero2

    def calcular_resta(self):
        return self.__numero1 - self.__numero2

    def calcular_division(self):
        return self.__numero1 / self.__numero2

    def calcular_multiplicacion(self):
        return self.__numero1 * self.__numero2


def menu():
    print("Bienvenido a nuestra Calculadora".center(50, '-'))
    opcion = int(input("""
    1. calcular suma
    2. calcular resta 
    3. calcular division
    4. calcular multiplicacion
    5. Salir
Ingrese la opcion: """))
    return opcion


def pedir_datos():
    numero1 = int(input("Por favor ingrese un numero: "))
    numero2 = int(input("Por favor ingrese un numero: "))
    calculadora = Calculadora(numero1, numero2)
    return calculadora


opcion = 0
while opcion != 5:
    opcion = menu()
    if opcion == 1:
        calculadora = pedir_datos()
        print("La suma es: ", calculadora.calcular_suma())
    elif opcion == 2:
        calculadora = pedir_datos()
        print(f'La resta es: {calculadora.calcular_resta()}')
    elif opcion == 3:
        calculadora = pedir_datos()
        print(f'La division es: {calculadora.calcular_division()}')
    elif opcion == 4:
        calculadora = pedir_datos()
        print(f"La multiplicacion es: {calculadora.calcular_multiplicacion()}")
    elif opcion == 5:
        print("Gracias por utilizar el programa")
    else:
        print("Opcion invalida vuelva a intentar")
    pause = input("Presione cualquier tecla para continuar: ")
    lim('cls')