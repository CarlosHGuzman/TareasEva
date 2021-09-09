package paquete;

import java.util.Scanner;

public class Ejercicio4 {
    static public void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int cantidadFilas, cantidadColumnas, columnaMayor = 0; 
        System.out.print("Ingrese la cantidad de filas: "); cantidadFilas = scanner.nextInt();
        System.out.print("Ingrese la cantidad de columnas: "); cantidadColumnas = scanner.nextInt();
        float matriz[][] = new float[cantidadFilas][cantidadColumnas]; float sumaColumna = 0, columnaConSumaMayor = 0, primeraSuma = 0;
        
        for (int i = 0; i < cantidadFilas; i++) {
            for (int j = 0; j < cantidadColumnas; j++) {
                System.out.print("Ingrese un numero para la posicion: (" +
                        (i+1) + "-" + (j+1) + "): "); matriz[i][j] = scanner.nextInt();
            }
        }
        for (int i = 0; i < cantidadColumnas; i++) {
            sumaColumna = 0;
            for (int j = 0; j < cantidadFilas; j++) {
                sumaColumna += matriz[j][i];
            }
            primeraSuma = 0;
            if(sumaColumna >= columnaConSumaMayor){
                columnaConSumaMayor = sumaColumna;
                columnaMayor = i;
            }
        }
        System.out.println("La columna mayor es: " + columnaMayor);
        System.out.println("Suma Columna: " + columnaConSumaMayor);
    }
}
