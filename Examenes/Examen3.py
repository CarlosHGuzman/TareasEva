class Arreglo():
    def __init__(self, numeros, numeros2, sumaNumeros):
        self.numeros = numeros
        self.numeros2 = numeros2
        self.sumaNumeros = sumaNumeros

    def suma(self):
        for i in range(0, 10, 1):
            self.sumaNumeros.append(self.numeros[i] + self.numeros2[i])
        return self.sumaNumeros
    def imprimir(self):
        print("---------------------Arreglo#1 Impresion-----------------")
        for elemento in self.numeros:
            print(f"Elemento: {elemento}")
        print("---------------------Arreglo#2 Impresion-----------------")
        for elemento in self.numeros2:
            print(f"Elemento: {elemento}")
        print("---------------------Arreglo#3 Impresion-----------------")
        for elemento in self.sumaNumeros:
            print(f"Elemento: {elemento}")


listaNumeros1 = []
listaNumeros2 = []
listaSumaLista1_2 = []

Arreglos = Arreglo(listaNumeros1, listaNumeros2, listaSumaLista1_2)

for i in range(0, 10, 1):
    numero = float(input(f"Ingrese el elemento {i+1} para la primera lista: ",))
    listaNumeros1.append(numero)
    numero = float(input(f"Ingrese el elemento {i+1} para la segunda lista: "))
    listaNumeros2.append(numero)
    print("")

Arreglos = Arreglo(listaNumeros1, listaNumeros2, listaSumaLista1_2)
Arreglos.suma()
Arreglos.imprimir()

