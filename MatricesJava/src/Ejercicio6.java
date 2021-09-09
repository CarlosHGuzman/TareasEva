package paquete;

import java.util.Scanner;

public class Ejercicio6 {

    public static  void main(String[] args) {
        /*
        Hacer un programa que llene una m atriz de 10*10 y que almacene en la diagonal
        principal unos y en las demas posiciones ceros
         */
        var scanner = new Scanner(System.in);
        int cantidadFilas, cantidadColumnas;
        System.out.print("Ingrese la cantidad de filas: ");
        cantidadFilas = scanner.nextInt();
        System.out.print("Ingrese la cantidad de columnas: ");
        cantidadColumnas = scanner.nextInt();
        float matriz[][] = new float[cantidadFilas][cantidadColumnas];
        for (int i = 0; i < cantidadFilas; i++) {
            for (int j = 0; j < cantidadColumnas; j++) {
                if (i == j) {
                    matriz[i][j] = 1;
                } else {
                    matriz[i][j] = 0;
                }
            }
        }
        for (int i = 0; i < cantidadFilas; i++) {
            for (int j = 0; j < cantidadColumnas; j++) {
                System.out.print(matriz[i][j] + "-");
            }
            System.out.println("");
        }
    }
}
