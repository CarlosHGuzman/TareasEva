# Realizar una clase que administre el grupo de estudiantes de programación I. Se debe almacenar
# para cada contacto el código, nombre, nota. Debera mostrar un men+u con las siguientes opciones:
# a. Añadir
# b. Lista de estudiantes
# c. Salir

class Estudiante:
    def __init__(self, codigo, nombre, nota):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__nota = nota

    def __str__(self):
        return f'{self.__codigo}\t {self.__nombre}\t {self.__nota}'


def ingresar_datos():
    codigo = int(input("Ingrese el codigo del estudiante: "))
    nombre = str(input("Ingrese el nombre del estudiante: ")).title()
    nota = float(input("Ingrese la nota del estudiante: "))
    return codigo, nombre, nota


listaEstudiantes = []


def menu():
    opc = 0
    bandera = False
    while opc != 3:
        print("Bienvenido".center(70, '='))
        opc = int(input("""
        1. Añadir estudiante
        2. Lista de estudiantes
        3. Salir
Ingrese una opcion: """))
        if opc == 1:
            codigo, nombre, nota = ingresar_datos()
            bandera = True
            estudiante = Estudiante(codigo, nombre, nota)
            listaEstudiantes.append(estudiante)
        elif opc == 2 :
            if bandera:
                for estudiante in listaEstudiantes:
                    print(estudiante)
            else:
                print("No ha ingresado estudiantes, por favor ingrese la opcion 1")
        elif opc == 3:
            print("Gracias por utilizar nuestro programa")
        else:
            print("No ingreso una opcion valida")
    pause = input("Presion cualquier teclas para continuar: ")


menu()