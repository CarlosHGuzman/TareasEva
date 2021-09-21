class Espectador():
    def __init__(self, sector, costo):
        self.costo = costo
        self.sector = sector

    def agregarCosto(self):
        for sector in self.sector:
            if sector == 1:
                self.costo.append(30)
            elif sector == 2:
                self.costo.append(50)
            elif sector == 3:
                self.costo.append(80)
            elif sector == 4:
                self.costo.append(150)
            elif sector == 5:
                self.costo.append(200)
    def calcularCosto(self):
        valorTotalTickets = 0
        for costos in self.costo:
            valorTotalTickets += costos
        return valorTotalTickets

def menu():
    print("""
    Sector               |  Costo de la entrada(miles de pesos)
    ________________________________________________________________
    1. Sol general       |   30
    ________________________________________________________________
    2. Sol preferente    |   50
    ________________________________________________________________
    3. Sombra            |   80
    ________________________________________________________________
    4. Tribuna           |   150
    ________________________________________________________________
    5. Platea            |   200
    ________________________________________________________________
    """)

agregar = 'si'
lista = []
menu()
while agregar == 'si':
    sector = int(input("Por favor ingrese el sector: "))
    agregar = str(input("Desea agregar otro ticket a su compra: ")).strip().lower()
    lista.append(sector)
lista1 = []
espectadores = Espectador(lista, lista1)
espectadores.agregarCosto()
print(f"El valor a pagar es: {espectadores.calcularCosto()}")