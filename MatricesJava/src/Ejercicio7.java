package paquete;

import java.util.Scanner;

public class Ejercicio7 {

    public static void main(String[] args) {
        var scanner = new Scanner(System.in);
        int cantidadFilas, cantidadColumnas, contador = 0;
        System.out.print("Ingrese la cantidad de filas: ");
        cantidadFilas = scanner.nextInt();
        System.out.print("Ingrese la cantidad de columnas: ");
        cantidadColumnas = scanner.nextInt();
        float matriz[][] = new float[cantidadFilas][cantidadColumnas];
        int tamanoVector = cantidadFilas * cantidadColumnas;
        float vector[] = new float[tamanoVector];
        for (int i = 0; i < cantidadFilas; i++) {
            for (int j = 0; j < cantidadColumnas; j++) {
                System.out.print("Ingrese un numero para la posicion: ("
                        + (i + 1) + "-" + (j + 1) + "): ");
                matriz[i][j] = scanner.nextInt();
                vector[contador++] = matriz[i][j];
            }
        }
        for (int i = 0; i < tamanoVector; i++) {
            System.out.println("Posicion : " + (i + 1) + " numero: " + vector[i]);
        }
    }
}