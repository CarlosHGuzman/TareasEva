# Escribir una clase en python llamada rectángulo que contenga una base y una altura, y que contenga
# un método que devuelva el área del rectángulo, agregar otro método que devuelva el perímetro del
# rectángulo. Agregar una clase circulo que contenga radio, y un método que devuelva el área del circulo
from math import pi


class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def calcular_area(self):
        return self.__base * self.__altura

    def calcular_perimetro(self):
        return self.__base * 2 + self.__altura * 2


class Circulo:
    def __init__(self, radio):
        self.__radio = radio

    def calcular_area(self):
        return pi * pow(self.__radio, 2)


def menu():
    print("Bienvenido".center(50, '-'))
    print("1. Rectangulo ")
    print("2. Circulo")
    print("3. Salir")
    opc = int(input("Ingrese la opcion: "))
    if opc == 1:
        print("1. Area")
        print("2. Perimetro")
        opc = int(input("Ingrese la opcion: "))
    elif opc == 2:
        print("Area: ")
        opc = 4
    else:
        print("Opcion equivocada")
    return opc
opc = 0
while opc != 3:
    opc = menu()
    if opc == 1:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        rectangulo = Rectangulo(base, altura)
        print(f"El area es: {rectangulo.calcular_area()}")
    elif opc == 2:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        rectangulo = Rectangulo(base, altura)
        print(f"El area es: {rectangulo.calcular_perimetro()}")
    elif opc == 3:
        print("Gracias por utilizar nuestro programa")
    elif opc == 4:
        radio = float(input("Ingrese el radio del circulo: "))
        circulo = Circulo(radio)
        print(f'El area es: {circulo.calcular_area()}')
    else:
        print("Opcion invalida")
    pause = input("Presione cualquier tecla para continuar: ")
