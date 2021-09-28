# Escribir una clase en python llamada temperatura utilizando un constructor _init_
# que contenga un arreglo de 31 posiciones donde se encuentran almacenados
# los valores correspondientes a las temperaturas promedio diario del mes de agosto del corriente año.
# Se pide mostrar:
# -	El día de mayor temperatura (método diamayor)
# -	El día de menor temperatura (método diamenor)
# -	La mayor temperatura (método tempmayor)
# -	El promedio mensual de temperaturas (método promedio)
# Se deberá mostrar por pantalla los resultados.
class Temperatura:
    suma_temperatura = 0
    def __init__(self, temperaturas):
        self.__temperaturas = temperaturas

    @property
    def temperaturas(self):
        return self.__temperaturas

    def diamenor(self):
        valor_menor = min(self.__temperaturas)
        encontrar = self.__temperaturas.index(valor_menor)
        return encontrar + 1

    def diamayor(self):
        valor_mayor = max(self.__temperaturas)
        encontrar = self.__temperaturas.index(valor_mayor)
        return encontrar + 1

    def temperaturaMayor(self):
        valor_mayor = max(self.__temperaturas)
        encontrar = self.__temperaturas.index(valor_mayor)
        return self.__temperaturas[encontrar]

    def promedio(self):
        return sum(self.__temperaturas) / 31





temperaturas =  ['nulo']*31

for i in range(1, 32, 1):
    pedir_temperatura = float(input(f"Ingrese una temperatura (dia: {i}): "))
    temperaturas[i-1] = pedir_temperatura

temperatura = Temperatura(temperaturas)
print(f'El dia de la temperatura menor es: {temperatura.diamenor()}')
print(f'El dia de la temperatura mayor es: {temperatura.diamayor()}')
print(f'La temperatura mayor es: {temperatura.temperaturaMayor()}')
print(f'El promedio de las temperaturas es:  {temperatura.promedio()}')

for temp in temperatura.temperaturas:
    print(f"Temperatura: {temp}")