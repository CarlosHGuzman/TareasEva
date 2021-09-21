# class Semaforo():
#     def __init__(self, precionVolcan):
#         self.precionVolcan = precionVolcan
#
#     def SemaforoVerde(self):
#         if self.precionVolcan >= 0.1 and self.precionVolcan <=0.4:
#             print("SEMAFORO VERDE: Se encuentra en estado normal")
#
#     def SemaforoNaranja(self):
#         if self.precionVolcan >= 0.5 and self.precionVolcan <= 0.9:
#             print("SEMAFORO NARANJA: Se encuentra ante posible erupcion ")
#
#     def SemaforoRojo(self):
#         if self.precionVolcan >= 1.0 and self.precionVolcan <= 2.0:
#             print("SEMAFORO ROJO: Existe una erupcion inminente ")
#
#     def SemaforoBlanco(self):
#         if self.precionVolcan == 0:
#             print("SEMAFORO BLANCO: Se puede regresar a la vivienda")
#
#
# # Principal
# opc = 'si'
# while(opc == 'si'):
#     precionVolcan = float(input("ingrese la precion de el volcan: "))
#     semaforo1 = Semaforo(precionVolcan)
#     semaforo1.SemaforoVerde()
#     semaforo1.SemaforoNaranja()
#     semaforo1.SemaforoRojo()
#     semaforo1.SemaforoBlanco()
#     opc = input("Dsea seguir? (si/no): ")

class Empleado():
    sumaEstaturaHombres = 0
    contadorHombres = 0
    cantidadEmpleados = 0
    def __init__(self, genero, estatura):
        self.genero = genero
        self.estatura = estatura
        Empleado.cantidadEmpleados += 1
        if(genero == "masculino"):
            Empleado.sumaEstaturaHombres += self.estatura
            Empleado.contadorHombres += 1

    def promedioEstaturaHombre(self):
        return Empleado.sumaEstaturaHombres / Empleado.contadorHombres

    def porcentajeEmpleadas(self):
        return (Empleado.cantidadEmpleados - Empleado.contadorHombres)/Empleado.cantidadEmpleados * 100
try:
    cantidadEncuestados = int(input("Ingrese la cantidad de personas que desea encuestar: "))
    listaEncuestados = []
    for i in range(0,cantidadEncuestados,1):
        print("--------------Empleado-----------------")
        genero = input("Ingrese su genero (masculino/femenino): ").strip()
        estatura = int(input("Ingrese la estatura en centimetros: "))
        empleados = Empleado(genero, estatura)
        listaEncuestados.append(empleados)

    promedioEstaturaHombres = empleados.promedioEstaturaHombre()
    print(f"El promedio de estatura de los hombres es: {promedioEstaturaHombres}")

    porcentajeEmpleadas = empleados.porcentajeEmpleadas()
    print(f"El porcentaje de mujeres empleadas es: {porcentajeEmpleadas}")
except Exception:
    print("Error")
