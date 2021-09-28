# Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los
# métodos para incializar los atributos,  impirmir el valor del lado con un tamaño mayor y el tipo
# triangulo que es(equilátero, isósceles o escaleno):
import math


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3
        self.__tipo = "No entra en ninguno de los tres tipos"

    def definir_tipo(self):
        if self.__lado1 == self.__lado2 == self.__lado3 :
            self.__tipo = "Triangulo Equilatero"
        elif self.__lado1 != self.__lado2 and self.__lado1 != self.__lado3 and self.__lado2 != self.__lado3:
            self.__tipo = "Triangulo Escaleno"
        else:
            self.__tipo = "Triangulo isosceles"
        return self.__tipo

def pedir_datos():
    lado1 = float(input("Ingrese el valor del primer lado: "))
    lado2 = float(input("Ingrese el valor del segundo lado: "))
    lado3 = float(input("Ingrese el valor del tercer lado: "))
    return lado1, lado2, lado3

opc = 'si'
while opc != 'no':
    lado1, lado2, lado3 = pedir_datos()
    triangulo = Triangulo(lado1, lado2, lado3)
    print(f"El tipo de triangulo es: {triangulo.definir_tipo()}")
    opc = input("Desea seguir si/no: ").lower()
    if opc == 'no':
        print("Gracias por utilizar nuestro programa")
        break
    while(opc != 'si'):
        opc = input("Desea seguir si/no: ").lower()