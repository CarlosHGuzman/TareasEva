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